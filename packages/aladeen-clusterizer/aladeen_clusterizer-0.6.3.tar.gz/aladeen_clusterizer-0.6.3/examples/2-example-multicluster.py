# import pandas as pd
# from sqlalchemy import create_engine


# from clusterizer.ClusteringPipeline import MultiSentClusteringPipeline


# engine = create_engine(
#     "postgresql://readonly_aladeen:readonly_password@localhost:5555/aladeen"
# )
# df = pd.read_sql_query(
#     "SELECT * FROM items ORDER BY published_at DESC LIMIT 1000", con=engine
# )
# print("Data loaded from server")
# print(len(df))

# # {'min_samples': 4, 'min_cluster_size': 8,
# #  'metric': 'manhattan', 'cluster_selection_method': 'eom'}

# hdb_config = {
#     "min_cluster_size": 2,
#     "min_samples": 1,
#     "cluster_selection_epsilon": 0.15,
#     # 'max_df': 0.5,
#     "cluster_selection_method": "leaf",
#     "metric": "manhattan",
#     # 'p': 2,
# }

# n_sentences = 1  # Specify the number of sentences to include from the content

# df["first_n_sentences_of_content"] = df["content"].apply(
#     lambda x: x.split(".")[:n_sentences]
# )
# df["title_and_content"] = df.apply(
#     lambda row: [row["title"]] + row["first_n_sentences_of_content"], axis=1
# )
# data = df["title_and_content"].tolist()
# data = [[d.strip() for d in item if len(d.strip()) > 5] for item in data]
# print("length:", [len(item) for item in data])
# data = [d for d in data if len(d) == n_sentences + 1]
# print("total data:", len(data))

# # ----------------- multi-sentence clustering -----------------
# pipeline = MultiSentClusteringPipeline(hdb_config, model_name="BAAI/bge-m3")
# clusters = pipeline.run(data=data)

# pipeline.print_clusters()
