import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Stray Animal Abuse Dashboard",
    page_icon="🐶",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #111827);
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
    border-right: 1px solid #334155;
}

.metric-card {
    background: #111827;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #334155;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
}

.metric-title {
    font-size: 15px;
    color: #cbd5e1;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #38bdf8;
}

.chart-card {
    background: #111827;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #334155;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
}

h1, h2, h3 {
    color: #f8fafc;
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Load Data ----------
df = pd.read_csv("data/sari_scored_news.csv")

# ---------- Sidebar ----------
st.sidebar.title("🔎 Filters")

risk_filter = st.sidebar.multiselect(
    "Select Risk Level",
    options=df["risk_level"].unique(),
    default=df["risk_level"].unique()
)

animal_filter = st.sidebar.multiselect(
    "Select Animal Type",
    options=df["animal_type"].unique(),
    default=df["animal_type"].unique()
)

incident_filter = st.sidebar.multiselect(
    "Select Incident Type",
    options=df["incident_type"].unique(),
    default=df["incident_type"].unique()
)

filtered_df = df[
    (df["risk_level"].isin(risk_filter)) &
    (df["animal_type"].isin(animal_filter)) &
    (df["incident_type"].isin(incident_filter))
]

st.sidebar.markdown("---")
st.sidebar.info("""
**Project Tools**
- Python
- Pandas
- Plotly
- Streamlit
- SARI Risk Scoring
""")

# ---------- Header ----------
st.title("🐶 Stray Animal Abuse Detection Dashboard")
st.markdown("### Data-Driven Risk Assessment Framework for Bangladesh")
st.markdown("---")

# ---------- Metrics ----------
total_articles = len(filtered_df)
dog_count = (filtered_df["animal_type"] == "Dog").sum()
cat_count = (filtered_df["animal_type"] == "Cat").sum()
high_risk_count = (filtered_df["risk_level"] == "High").sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📄 Total Articles</div>
        <div class="metric-value">{total_articles}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🐕 Dog Incidents</div>
        <div class="metric-value">{dog_count}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🐈 Cat Incidents</div>
        <div class="metric-value">{cat_count}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">⚠️ High Risk Cases</div>
        <div class="metric-value">{high_risk_count}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------- Charts ----------
st.header("📊 Interactive Visual Analytics")

col1, col2 = st.columns(2)

with col1:
    incident_counts = filtered_df["incident_type"].value_counts().reset_index()
    incident_counts.columns = ["Incident Type", "Count"]

    fig_incident = px.bar(
        incident_counts,
        x="Count",
        y="Incident Type",
        orientation="h",
        text="Count",
        title="Incident Type Distribution",
        color="Count",
        color_continuous_scale="Blues"
    )
    fig_incident.update_layout(
        template="plotly_dark",
        yaxis={"categoryorder": "total descending"},
        height=450
    )
    st.plotly_chart(fig_incident, width="stretch")

with col2:
    risk_counts = filtered_df["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["Risk Level", "Count"]

    fig_risk = px.pie(
        risk_counts,
        names="Risk Level",
        values="Count",
        hole=0.50,
        title="SARI Risk Level Distribution",
        color="Risk Level",
        color_discrete_map={
            "Low": "#22c55e",
            "Medium": "#f59e0b",
            "High": "#ef4444"
        }
    )
    fig_risk.update_traces(
        pull=[0.02, 0.05, 0.09],
        textinfo="label+percent",
        hovertemplate="<b>%{label}</b><br>Articles: %{value}<br>Percentage: %{percent}<extra></extra>"
    )
    fig_risk.update_layout(template="plotly_dark", height=450)
    st.plotly_chart(fig_risk, width="stretch")

col3, col4 = st.columns(2)

with col3:
    animal_counts = filtered_df["animal_type"].value_counts().reset_index()
    animal_counts.columns = ["Animal Type", "Count"]

    fig_animal = px.pie(
        animal_counts,
        names="Animal Type",
        values="Count",
        hole=0.50,
        title="Animal Type Distribution",
        color="Animal Type",
        color_discrete_map={
            "Dog": "#3b82f6",
            "Cat": "#a855f7",
            "Unknown": "#64748b"
        }
    )
    fig_animal.update_traces(
        pull=[0.03, 0.05, 0.07],
        textinfo="label+percent",
        hovertemplate="<b>%{label}</b><br>Articles: %{value}<br>Percentage: %{percent}<extra></extra>"
    )
    fig_animal.update_layout(template="plotly_dark", height=450)
    st.plotly_chart(fig_animal, width="stretch")

with col4:
    source_counts = filtered_df["source"].value_counts().head(10).reset_index()
    source_counts.columns = ["Source", "Count"]

    fig_source = px.bar(
        source_counts,
        x="Count",
        y="Source",
        orientation="h",
        text="Count",
        title="Top 10 News Sources",
        color="Count",
        color_continuous_scale="Teal"
    )
    fig_source.update_layout(
        template="plotly_dark",
        yaxis={"categoryorder": "total ascending"},
        height=450
    )
    st.plotly_chart(fig_source, width="stretch")

st.markdown("---")

# ---------- High Risk Preview ----------
st.header("🔥 High Risk Incident Preview")

high_risk_df = filtered_df[filtered_df["risk_level"] == "High"]

st.dataframe(
    high_risk_df[["title", "source", "date", "animal_type", "incident_type", "risk_score", "risk_level"]].head(15),
    width="stretch"
)

# ---------- Full Dataset ----------
st.header("📄 Full Dataset Preview")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_sari_dataset.csv",
    mime="text/csv"
)

st.dataframe(filtered_df, width="stretch")

st.success("Dashboard successfully visualizes cleaned, classified, and SARI-scored stray animal incident data.")