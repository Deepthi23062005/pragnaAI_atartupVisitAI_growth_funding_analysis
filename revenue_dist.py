fig = px.histogram(
    df,
    x="revenue_million",
    nbins=50,
    color="outcome"
)

st.plotly_chart(fig)
