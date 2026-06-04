fig = px.box(
    df,
    x="outcome",
    y="founder_experience_years",
    color="outcome",
    title="Founder Experience Impact"
)

st.plotly_chart(fig)
Insight
