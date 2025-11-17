
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("paf_matrix.tsv", sep="\t", names=["gene", "genome", "identity"])

matrix = df.pivot_table(index="gene", columns="genome", values="identity", fill_value=0)

# Plot heatmap
plt.figure(figsize=(10,8))
sns.heatmap(matrix, cmap="YlOrRd", linewidths=0.5)
plt.title("Gene–Genome Similarity Heatmap (% identity)")
plt.show()
plt.savefig("paf_heatmap.png", dpi=300, bbox_inches='tight')
