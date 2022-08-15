import streamlit as st
import SessionState
import pandas as pd
import numpy as np

def get_taste(x):
    # Convert string of tastes to vector
    tastes = ["sweet", "salty", "sour", "bitter", "spicy"]
    taste_result = []
    
    for taste in tastes:
        if taste in x:
            taste_result.append(1)
        else:
            taste_result.append(0)
    
    return taste_result

def similarity(x):
    # Calculate similarity of user's taste vector and food's taste vector on database
    taste = np.array(x)
    user_taste = np.array(user_taste_vector)
    
    return np.dot(taste, user_taste)

st.header("Food Recommender Based on Taste")
st.write("Available food taste: sweet, salty, sour, bitter, spicy")
st.text_input("What food's tastes do you want? (ex: sweet and sour; salty, sour, and spicy)", key="name")
user_taste_vector = get_taste(st.session_state.name)

data = pd.read_csv("https://raw.githubusercontent.com/Rangga1708/Food-Recommender/main/Food%20Taste.csv")
data["taste_vector"] = data["taste"].map(get_taste)
data["similarity"] = data["taste_vector"].map(similarity)
filtered_data = data[data["similarity"] > 0]
filtered_data = filtered_data.sort_values(by = "similarity", ascending = False)
filtered_data = filtered_data.reset_index(drop = True)

#for i in range(len(filtered_data)):
#    st.write(filtered_data["name"][i])
    
# Number of entries per screen
N = 10

# A variable to keep track of which product we are currently displaying
current_page = SessionState.get(page_number = 0)
last_page = len(filtered_data) // N

# Add a next button and a previous button
prev, _ ,next = st.beta_columns([1, 10, 1])

if next.button("Next"):

    if current_page.page_number + 1 > last_page:
        current_page.page_number = 0
    else:
        current_page.page_number += 1

if prev.button("Previous"):

    if current_page.page_number - 1 < 0:
        current_page.page_number = last_page
    else:
        current_page.page_number -= 1

# Get start and end indices of the next page of the dataframe
start_idx = current_page.page_number * N 
end_idx = (1 + current_page.page_number) * N

# Index into the sub dataframe
sub_df = filtered_data.iloc[start_idx:end_idx]
st.write(sub_df)