import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sari_scored_news.csv")

# Count risk levels
risk_counts = df["risk_level"].value_counts()

# Global font settings
plt.rcParams.update({
    "font.size": 14,
    "axes.titlesize": 20,
    "axes.labelsize": 16,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14
})

# Create figure
plt.figure(figsize=(10, 8))

# Pie chart
wedges, texts, autotexts = plt.pie(
    risk_counts,
    labels=risk_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=[0.03, 0.05, 0.08],
    textprops={"fontsize": 15}
)

# Make percentage labels bigger
for autotext in autotexts:
    autotext.set_fontsize(15)
    autotext.set_fontweight("bold")

# Title
plt.title(
    "Distribution of Risk Levels",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.tight_layout()

# Save image
plt.savefig(
    "visualization/risk_distribution.pdf",
    bbox_inches="tight"
)

plt.show()