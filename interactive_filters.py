sector = st.sidebar.multiselect(
    "Sector",
    df["sector"].unique()
)

investor = st.sidebar.multiselect(
    "Investor Type",
    df["investor_type"].unique()
)

filtered = df.copy()

if sector:
    filtered = filtered[
        filtered["sector"].isin(sector)
    ]

if investor:
    filtered = filtered[
        filtered["investor_type"].isin(investor)
    ]
