import streamlit as st
import pandas as pd
import plotly.express as px
import temps

temps.update()
df = pd.read_csv('temps.csv')
df

figure = px.line(
            x=df.date,
            y=df.temperature,
            labels={'x': 'date', 'y': 'temp'}
)

st.plotly_chart(figure, use_container_width=True)
