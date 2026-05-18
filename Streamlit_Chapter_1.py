import streamlit as st 

st.header("Welcome To language Picker")
st.subheader("You can choose any language that are present in the list")
language_user = st.selectbox("Choose Your Favourite Language", ["Python", "JS", "R", "C","C++", "Other"])
st.write(f"Thats Great {language_user}. Excellent Choise")

#st.write(f"Thats Great {language_user}. Excellent Choice")