fig = px.violin(
    df,
    x="outcome",
    y="market_size_billion",
    color="outcome"
)

st.plotly_chart(fig)
