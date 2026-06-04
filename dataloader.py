import streamlit as st
import pandas as pd

df = pd.read_csv("data/startup_success_dataset.csv")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Startups",
    len(df)
)

c2.metric(
    "IPO %",
    round(
        (df["outcome"]=="IPO").mean()*100,
        2
    )
)

c3.metric(
    "Acquisition %",
    round(
        (df["outcome"]=="Acquisition").mean()*100,
        2
    )
)

c4.metric(
    "Failure %",
    round(
        (df["outcome"]=="Failure").mean()*100,
        2
    )
)
