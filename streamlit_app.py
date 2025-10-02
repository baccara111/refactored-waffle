# streamlit_app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Refactored Waffle", layout="wide")
st.title("Refactored Waffle")

uploaded = st.file_uploader("Upload a CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success(f"Rows: {len(df):,}")
    st.dataframe(df.head())
    st.line_chart(df.select_dtypes('number'))
else:
    st.info("Upload a CSV to get started.")
