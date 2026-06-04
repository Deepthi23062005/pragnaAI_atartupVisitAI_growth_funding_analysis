fig = px.pie(
    df,
    names="outcome",
    title="Startup Outcomes"
)

st.plotly_chart(fig)
