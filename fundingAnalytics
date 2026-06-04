import plotly.express as px

sector_funding = (
    df.groupby("sector")
    ["revenue_million"]
    .mean()
    .sort_values(ascending=False)
)

fig = px.bar(
    sector_funding,
    title="Average Revenue by Sector"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
