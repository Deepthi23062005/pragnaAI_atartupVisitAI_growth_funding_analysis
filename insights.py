fig = px.box(
    df,
    x="outcome",
    y="founder_experience_years",
    color="outcome",
    title="Founder Experience Impact"
)

st.plotly_chart(fig)

best = (
    df.groupby("outcome")
    ["founder_experience_years"]
    .mean()
)

st.success(
f"""
IPO founders average
{best['IPO']:.1f} years experience.
"""
)
