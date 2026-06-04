import plotly.figure_factory as ff

num_df = df.select_dtypes(
    include="number"
)

corr = num_df.corr()

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.columns)
)

st.plotly_chart(fig)
