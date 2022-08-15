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

#def check(tastes):
#    result = []
#    
#    for taste in tastes:
#        st.write(taste)
#        taste_vector = get_taste(taste)
#        result.append(similarity(taste_vector))
#    
#    return result

st.header("Food Recommender")
st.write("Available food taste: sweet, salty, sour, bitter, spicy")
st.text_input("Food's tastes you want: (ex: sweet and sour; salty, sour, and spicy)", key="name")
user_taste_vector = get_taste(st.session_state.name)

data = pd.read_csv("https://raw.githubusercontent.com/Rangga1708/Food-Recommender/main/Food%20Taste.csv")
data["taste_vector"] = data["taste"].map(get_taste)
data["similarity"] = data["taste_vector"].map(similarity)
filtered_data = data[data["similarity"] > 0]
filtered_data = filtered_data.sort_values(by = "similarity", ascending = False)
filtered_data = filtered_data.reset_index(drop = True)

for i in range(len(filtered_data)):
    st.write(filtered_data["name"][i])