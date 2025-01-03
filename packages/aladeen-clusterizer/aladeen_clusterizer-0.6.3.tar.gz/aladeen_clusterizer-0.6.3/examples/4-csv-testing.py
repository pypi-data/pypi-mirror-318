import pandas as pd
from sqlalchemy import create_engine

from aladeen_clusterizer.ClusteringPipeline import ClusteringPipeline
from aladeen_clusterizer.outlier_detectors.ZScoreOutlierDetector import ZScoreOutlierDetector
from aladeen_clusterizer.cluster_scorers.CosineSimililarityClusterScorer import (
    CosineSimililarityClusterScorer,
)


engine = create_engine(
    "postgresql://readonly_aladeen:readonly_password@localhost:5432/aladeen"
)

df = pd.read_sql_query(
    """
        SELECT uuid,
            source,
            title,
            description,
            content,
            created_at
        FROM items
        ORDER BY created_at DESC
        LIMIT 1000
    """,
    con=engine
)

print("Length of df", len(df))
# remove newlines from titles
df['title'] = df['title'].str.replace("\n", " ")

# BEST PARAMETERS  ---------------------------
hdb_config ={
    'min_samples': 6,
    'min_cluster_size': 2,
    'metric': 'euclidean',
    'cluster_selection_method':'eom', 
    'cluster_selection_epsilon': 0.1,
    'alpha': 0.6,
    'algorithm': 'prims_kdtree'
    }

outlier_scorer = CosineSimililarityClusterScorer()
outlier_detector = ZScoreOutlierDetector(outlier_scorer, 0.8, 0.6) # dont forget these
# --------------------------------------------

pipeline = ClusteringPipeline(
    hdb_config,

    outlier_scorer=outlier_scorer,
    outlier_detector=outlier_detector,

    model_name="BAAI/bge-m3",

    uuid_col="uuid",

    title_col="title",
    description_col="description",
    content_col="content",

    # FIXME: change to published_at after we normalize that column
    datetime_col="created_at",

    verbose=True,
)
print("Running pipeline")
labels = pipeline.run(df)
print("Length of labels", len(labels))
clusters = pipeline.get_clusters(threshold=False, include_outliers=True)
print("done")

# ---------------------------
# SAVE TO CSV
df['label'] = labels
# scores_by_cluster = pipeline.item_scores # (variable) item_scores: dict[int, list[float]]
uuid_to_score = {}
for cluster, scores in pipeline.item_scores.items():
    for uuid, score in zip(df[df['label'] == cluster]['uuid'], scores):
        uuid_to_score[uuid] = score

df['score'] = df['uuid'].map(uuid_to_score)
df.sort_values(by=['score'], inplace=True, ascending=False)
df['label'] = df.groupby('label').ngroup() + 1

df.sort_values(by=['label'], inplace=True)


df = df.drop(columns=['description', 'content', 'created_at'])
# get today's date
from datetime import date
today = date.today()
today = today.strftime("%Y-%m-%d")
df.to_csv(f'csvs/clustered_n1000_{today}.csv', index=False)
