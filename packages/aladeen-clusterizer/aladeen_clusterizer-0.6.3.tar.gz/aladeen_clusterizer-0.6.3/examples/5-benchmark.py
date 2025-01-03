
from benchmark_util import evaluate, create_dummy_data
import pandas as pd
from aladeen_clusterizer.ClusteringPipeline import ClusteringPipeline
from aladeen_clusterizer.outlier_detectors.ZScoreOutlierDetector import ZScoreOutlierDetector
from aladeen_clusterizer.cluster_scorers.CosineSimililarityClusterScorer import (
    CosineSimililarityClusterScorer,
)


hdb_config = {
    "min_cluster_size": 2,
    "min_samples": 6,
    "metric": "euclidean",
    "cluster_selection_epsilon": 0.15,
    "cluster_selection_method": "leaf",
}


gold_csv_path = "csvs/golden_300.csv"
gold = pd.read_csv(gold_csv_path)
labels = gold["label"]
df = gold.drop(columns=["label"])



def run_benchmark(items, expected_labels):
    outlier_scorer = CosineSimililarityClusterScorer()
    outlier_detector = ZScoreOutlierDetector(outlier_scorer, 0.8, 0.6)
    pipeline = ClusteringPipeline(
        hdb_config,
        outlier_scorer=outlier_scorer,
        outlier_detector=outlier_detector,
        model_name="BAAI/bge-m3",
        uuid_col="uuid",
        title_col="title",
        description_col="description",
        content_col="content",
        datetime_col="created_at",
        verbose=False,
    )

    uuids = items["uuid"]
    predicted_labels = pipeline.run(items)
    # save embeddings
    embeddings = pipeline.processed_embeddings
    # save embeddings as file
    
    return evaluate(uuids, predicted_labels, expected_labels)



benchmark_results = run_benchmark(df, labels)
print(benchmark_results)

# create dummy data
# uuids, predicted_labels, expected_labels = create_dummy_data()

# # print the data
# print("UUIDs:", uuids)
# print("Predicted Labels:", predicted_labels)
# print("Expected Labels:", expected_labels)

# # run evaluation
# results = evaluate(uuids, predicted_labels, expected_labels)


# # print the results
# print("\nEvaluation Results:")
# for metric, value in results.items():
#     print(f"{metric}: {value:.4f}")