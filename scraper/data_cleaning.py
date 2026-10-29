import pandas as pd

# Load dataset
df = pd.read_csv("data/raw_news.csv")

print("Original Rows:", len(df))

# Remove duplicate news
df = df.drop_duplicates(subset=["title"])

# Remove missing titles
df = df.dropna(subset=["title"])

# Convert title to lowercase for filtering
df["title_lower"] = df["title"].str.lower()

# Relevant keywords
keywords = [
    "dog",
    "dogs",
    "cat",
    "cats",
    "animal",
    "stray",
    "rabies",
    "poison",
    "abuse",
    "rescue"
]

# Keep only relevant titles
df = df[
    df["title_lower"].apply(
        lambda x: any(word in x for word in keywords)
    )
]

print("After Filtering:", len(df))

# Detect Animal Type
def detect_animal(title):
    title = title.lower()

    if "dog" in title:
        return "Dog"

    elif "cat" in title:
        return "Cat"

    return "Unknown"

# Detect Incident Type
def detect_incident(title):
    title = title.lower()

    if "poison" in title or "toxic" in title:
        return "Poisoning"

    elif "kill" in title or "killed" in title or "dead" in title or "death" in title:
        return "Killing"

    elif "abuse" in title or "cruelty" in title or "torture" in title or "beaten" in title:
        return "Abuse"

    elif "rescue" in title or "rescued" in title or "saved" in title:
        return "Rescue"

    elif "rabies" in title or "vaccination" in title or "vaccine" in title or "disease" in title:
        return "Disease"

    elif "relocate" in title or "relocation" in title or "protest" in title or "rights" in title or "conflict" in title:
        return "Conflict"

    elif "bite" in title or "attack" in title or "aggressive" in title:
        return "Human-Animal Conflict"

    return "Other"
# Apply functions
df["animal_type"] = df["title"].apply(detect_animal)
df["incident_type"] = df["title"].apply(detect_incident)

# Remove helper column
df = df.drop(columns=["title_lower"])

# Save processed data
df.to_csv("data/processed_news.csv", index=False)

print("\nProcessed dataset saved!")
print(df.head())
print("\nFinal Rows:", len(df))