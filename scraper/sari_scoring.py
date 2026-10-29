import pandas as pd

df = pd.read_csv("data/processed_news.csv")

# Risk score function
def calculate_score(row):

    score = 0

    incident = str(row["incident_type"])

    if incident == "Poisoning":
        score += 10

    elif incident == "Killing":
        score += 9

    elif incident == "Abuse":
        score += 8

    elif incident == "Disease":
        score += 6

    elif incident == "Rescue":
        score += 2

    else:
        score += 3

    return score


# Apply score
df["risk_score"] = df.apply(calculate_score, axis=1)


# Risk level
def risk_level(score):

    if score >= 8:
        return "High"

    elif score >= 5:
        return "Medium"

    return "Low"


df["risk_level"] = df["risk_score"].apply(risk_level)

# Save file
df.to_csv("data/sari_scored_news.csv", index=False)

print(df[["title", "incident_type", "risk_score", "risk_level"]].head())

print("\nDone!")