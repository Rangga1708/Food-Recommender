import streamlit as st
import pandas as pd
import numpy as np

def get_taste(x):
    tastes = ["sweet", "salty", "sour", "bitter", "spicy"]
    taste_result = []
    
    for taste in tastes:
        if taste in x:
            taste_result.append(1)
        else:
            taste_result.append(0)
    
    return taste_result

def similarity(x):
    taste = np.array(x)
    user_taste = np.array(user_taste_vector)
    
    return np.dot(taste, user_taste)

def check(tastes):
    result = []
    
    for taste in tastes:
        taste_vector = get_taste(taste)
        result.append(similarity(taste_vector, user_taste_vector))
    
    return result

st.header("Food Recommender")
st.text_input("Food's tastes you want: ", key="name")
user_taste_vector = get_taste(st.session_state.name)

data = pd.read_csv("https://raw.githubusercontent.com/Rangga1708/Food-Recommender/main/Food%20Taste.csv")
data["check"] = check(data["taste_name"])
filtered_data = data[data["check"] > 0]
filtered_data = filtered_data.sort_values(by = "check", ascending = False)
filtered_data = filtered_data.reset_index(drop = True)

for i in range(len(filtered_data)):
    st.write(filtered_data["name"][i])