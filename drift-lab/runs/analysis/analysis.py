import json
import glob
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------
# LOAD ALL RUN FILES
# ---------------------------
def load_runs():
    files = glob.glob("drift-lab/runs/*.json")
    all_rows = []
    for f in files:
        with open(f, "r", encoding="utf-8") as infile:
            data = json.load(infile)
            if isinstance(data, list):
                all_rows.extend(data)
    return all_rows

rows = load_runs()

print(f"Loaded {len(rows)} responses across {len(set([r['run_id'] for r in rows]))} runs.")

# ---------------------------
# BASIC STATS
# ---------------------------
def compute_basic_stats(rows):
    lengths = [len(r["response"].split()) for r in rows]
    avg_length = sum(lengths) / len(lengths)
    print(f"Average response length: {avg_length:.2f} words")

compute_basic_stats(rows)

# ---------------------------
# SEMANTIC DRIFT ANALYSIS
# ---------------------------
def compute_semantic_drift(rows):
    texts = [r["response"] for r in rows]
    ids = [r["run_id"] for r in rows]

    tfidf = TfidfVectorizer().fit_transform(texts)
    sims = cosine_similarity(tfidf)

    # drift = 1 - similarity
    drift_matrix = 1 - sims

    return drift_matrix, ids

drift_matrix, ids = compute_semantic_drift(rows)

# ---------------------------
# PLOT DRIFT SCATTER
# ---------------------------
def plot_drift(drift_matrix):
    plt.figure(figsize=(8, 6))
    flat = drift_matrix[np.triu_indices(len(drift_matrix), k=1)]
    plt.scatter(range(len(flat)), flat, s=8)
    plt.title("Semantic Drift Across All Responses")
    plt.xlabel("Pair index")
    plt.ylabel("Drift (1 - cosine similarity)")
    plt.tight_layout()
    plt.savefig("drift-lab/drift_scatter.png")
    print("Saved drift-lab/drift_scatter.png")

plot_drift(drift_matrix)

# ---------------------------
# OUTPUT SUMMARY TO MARKDOWN
# ---------------------------
def save_summary(rows, drift_matrix):
    summary_file = "drift-lab/summary.md"

    avg_drift = float(np.mean(drift_matrix[np.triu_indices(len(drift_matrix), k=1)]))

    run_ids = sorted(list(set(r["run_id"] for r in rows)))

    with open(summary_file, "w", encoding="utf-8") as out:
        out.write("# Drift-Lab Summary\n\n")
        out.write(f"Total responses: **{len(rows)}**\n\n")
        out.write(f"Runs detected: **{len(run_ids)}**\n\n")
        out.write(f"Average semantic drift: **{avg_drift:.4f}**\n\n")
        out.write("## Run IDs:\n")
        for rid in run_ids:
            out.write(f"- {rid}\n")

    print("Saved summary to drift-lab/summary.md")

save_summary(rows, drift_matrix)
