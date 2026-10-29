import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sari_scored_news.csv")

# Count animal types
animal_counts = df["animal_type"].value_counts()

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
    animal_counts,
    labels=animal_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=[0.04, 0.02, 0.06],
    textprops={"fontsize": 14}
)

# Make percentage text bigger
for autotext in autotexts:
    autotext.set_fontsize(14)
    autotext.set_fontweight("bold")

# Title
plt.title(
    "Distribution of Animal Types",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.tight_layout()

# Save image
plt.savefig("visualization/animal_distribution.pdf", bbox_inches="tight")

plt.show()