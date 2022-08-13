import streamlit as st
import pandas as pd

#data = pd.read_csv("https://raw.githubusercontent.com/Rangga1708/Food-Recommender/main/Food%20Taste.csv")

st.header("Food Recommender")
st.text_input("Food's tastes you want: ", key="name")

st.write(f"You want {st.session_state.name}")