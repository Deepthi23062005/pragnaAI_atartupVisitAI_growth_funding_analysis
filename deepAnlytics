sector_outcome = pd.crosstab(
    df["sector"],
    df["outcome"]
)

fig = px.imshow(
    sector_outcome,
    text_auto=True,
    title="Sector vs Outcome Heatmap"
)

st.plotly_chart(fig)
