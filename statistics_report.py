import pandas as pd

df = pd.read_csv("data/sari_scored_news.csv")

print("\n===== DATASET SUMMARY =====")
print("Total Records:", len(df))

print("\n===== ANIMAL TYPE =====")
print(df["animal_type"].value_counts())

print("\n===== INCIDENT TYPE =====")
print(df["incident_type"].value_counts())

print("\n===== RISK LEVEL =====")
print(df["risk_level"].value_counts())

print("\n===== TOP SOURCES =====")
print(df["source"].value_counts().head(10))