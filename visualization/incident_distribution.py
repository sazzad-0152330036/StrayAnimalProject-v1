import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sari_scored_news.csv")

# Count incident types
incident_counts = df["incident_type"].value_counts()

# Global font settings
plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 20,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14
})

# Create figure
plt.figure(figsize=(12, 7))

# Horizontal bar chart
bars = plt.barh(
    incident_counts.index,
    incident_counts.values,
    color="steelblue"
)

# Title and labels
plt.title(
    "Distribution of Stray Animal Incident Types",
    fontsize=20,
    fontweight="bold",
    pad=15
)

plt.xlabel(
    "Number of Articles",
    fontsize=16,
    fontweight="bold"
)

plt.ylabel(
    "Incident Type",
    fontsize=16,
    fontweight="bold"
)

# Grid
plt.grid(axis="x", linestyle="--", alpha=0.4)

# Add values on bars (BIGGER)
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 3,
        bar.get_y() + bar.get_height()/2,
        str(int(width)),
        va="center",
        fontsize=14,
        fontweight="bold"
    )

# Adjust layout
plt.tight_layout()

# Save high-quality image
plt.savefig("visualization/incident_distribution.pdf", bbox_inches="tight")

# Show chart
plt.show()