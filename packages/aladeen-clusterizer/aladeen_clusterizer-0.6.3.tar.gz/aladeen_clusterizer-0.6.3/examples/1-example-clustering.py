import pandas as pd
from sqlalchemy import create_engine

from aladeen_clusterizer.ClusteringPipeline import ClusteringPipeline
from aladeen_clusterizer.outlier_detectors.ZScoreOutlierDetector import ZScoreOutlierDetector
from aladeen_clusterizer.cluster_scorers.CosineSimililarityClusterScorer import (
    CosineSimililarityClusterScorer,
)


engine = create_engine(
    "postgresql://readonly_aladeen:readonly_password@localhost:5555/aladeen"
)

df = pd.read_sql_query(
    """
        SELECT uuid,
            source,
            title,
            created_at
        FROM items
        ORDER BY created_at DESC
        LIMIT 800
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

    model_name="bge-m3",

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
clusters = pipeline.get_clusters(threshold=0.5, include_outliers=True)
print("done")


for cluster in clusters:
    print(f"CLUSTER {cluster['label']} - SCORE: {cluster['score']} - ITEMS: {len(cluster['items'])}")
    for item_dict in cluster['items']:
        uuid = item_dict['uuid']
        item = df[df['uuid'] == uuid]
        title = item['title'].values[0].replace("\n", " ")
        source = item['source'].values[0]
        score = round(item_dict['score'], 3)
        print(f"--[{score}] {title} - {source}")
    print()






# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# csv = pd.DataFrame(clusters)


# #     cluster_label     score                                              items
# # 0       0  1.000000  [67d5f354-5f81-4ede-925f-de8202850a76, 59d79f4...

# # convert to:
# #      item_id          title                     cluster
# # 0  67d5f354-5f81-4ede-925f-de8202850a76  title of the item 1

# transformed_data = []

# # Iterate through each cluster
# for _, row in csv.iterrows():
#     cluster_label = row['label']
    
#     # Iterate through each item in the cluster
#     for item_id in row['items']:
#         # Find the corresponding item in the original DataFrame
#         item = df[df['uuid'] == item_id]
        
#         # Extract the title
#         title = item['title'].values[0] if not item.empty else "Title not found"
        
#         # Append the transformed data
#         transformed_data.append({
#             'item_id': item_id,
#             'title': title,
#             'cluster': cluster_label
#         })

# # Create a new DataFrame from the transformed data
# new_csv = pd.DataFrame(transformed_data)
# new_csv.to_csv('csvs/clustered_data.csv', index=False)

# # Display the first 20 rows of the new DataFrame
# print(new_csv.head(20))



# print()
# print()
# # print(csv.head(20))