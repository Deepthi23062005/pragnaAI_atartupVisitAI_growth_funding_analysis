fig = px.scatter(
    df.sample(5000),
    x="burn_rate_million",
    y="revenue_million",
    color="outcome",
    size="team_size",
    hover_data=["sector"]
)

st.plotly_chart(
    fig,
    use_container_width=True
)
