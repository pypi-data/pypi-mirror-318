import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from pprint import pprint


from aladeen_clusterizer.ClusteringPipeline import ClusteringPipeline
from aladeen_clusterizer.cluster_scorers.CosineSimililarityClusterScorer import (
    CosineSimililarityClusterScorer,
)
from aladeen_clusterizer.outlier_detectors.ZScoreOutlierDetector import ZScoreOutlierDetector


engine = create_engine(
    "postgresql://readonly_aladeen:readonly_password@localhost:5555/aladeen"
)

query = """
SELECT
    i.uuid, i.title, i.created_at,
    e.title_embed
FROM items i
LEFT JOIN item_embeddings e ON
    i.uuid = e.item_uuid
WHERE
    e.title_embed IS NOT NULL
ORDER BY
    i.created_at DESC
LIMIT 300
"""

df = pd.read_sql(query, engine)

# must convert the string to a numpy array of floats (!!!!!!)
df["title_embed"] = df["title_embed"].apply(lambda x: np.array(eval(x), dtype=float))
# –----------------


# CLUSTERING STUFF ----------------
hdb_config = {
    "min_cluster_size": 2,
    "min_samples": 1,
    "cluster_selection_epsilon": 0.15,
    # 'max_df': 0.5,
    "core_dist_n_jobs": -1,
    "cluster_selection_method": "leaf",
    "metric": "euclidean",
    # 'p': 2,
}

outlier_scorer = CosineSimililarityClusterScorer()
threshold_range = (0, 4.0)
step = 0.1
outlier_detector = ZScoreOutlierDetector(outlier_scorer, 1, 0.75)

pipeline = ClusteringPipeline(
    hdb_config,
    model_name="BAAI/bge-m3",
    uuid_col="uuid",  # !!!!!!!!!!!!!! make sure to specify this correctly
    title_col="title",
    content_col=None,
    datetime_col="created_at",
    outlier_detector=outlier_detector,
    outlier_scorer=outlier_scorer,
)

labels = pipeline.run_embeddings_only(df)
# tadaaa
print(labels)  # these are the cluster labels <<-------------
# ----------------

cluster_scores = pipeline.cluster_scores


# PRINTING ----------------
def print_clusters(cluster_scores):
    for cluster_label, score in cluster_scores.items():
        print(f"Cluster {cluster_label} / Score: {round(score, 3)}")
        labels = pipeline.labels
        for i, label in enumerate(labels):
            if label == cluster_label:
                title = df.iloc[i]["title"].replace("\n", "")
                print("X.", title)
        print("")


print("-------------------")
print("-------------------")
pprint(pipeline.get_clusters(labels))
print("-------------------")
print("-------------------")
print_clusters(cluster_scores)
