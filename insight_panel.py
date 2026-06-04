top_sector = (
    df.groupby("sector")
    ["revenue_million"]
    .mean()
    .idxmax()
)

st.success(
f"""
Highest revenue sector:
{top_sector}
"""
)

top_investor = (
    df.groupby("investor_type")
    ["revenue_million"]
    .mean()
    .idxmax()
)

st.info(
f"""
Best performing investor:
{top_investor}
"""
)
