import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sari_scored_news.csv")

# Top 10 sources
source_counts = df["source"].value_counts().head(10).sort_values()

# Global font settings
plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 20,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14
})

# Create figure
plt.figure(figsize=(14, 7))

# Horizontal bar chart
bars = plt.barh(
    source_counts.index,
    source_counts.values,
    color="steelblue"
)

# Title
plt.title(
    "Top News Sources Distribution",
    fontsize=20,
    fontweight="bold",
    pad=15
)

# Axis labels
plt.xlabel(
    "Number of Articles",
    fontsize=16,
    fontweight="bold"
)

plt.ylabel(
    "News Source",
    fontsize=16,
    fontweight="bold"
)

# Grid
plt.grid(axis="x", linestyle="--", alpha=0.4)

# Value labels (bigger and bold)
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va="center",
        fontsize=14,
        fontweight="bold"
    )

plt.tight_layout()

# Save high-quality image
plt.savefig("visualization/source_distribution.pdf", bbox_inches="tight")

plt.show()