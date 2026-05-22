import streamlit as st

#strealit run Streamlit_Chapter_2.py

st.title("Chai Maker App")

cups = st.number_input("Kitane Cup laagaoo : ", min_value =1 , max_value = 10 )
st.write("Ho Gaya Aab Aage :", cups)
if st.button("Aaoo Chai Banaye"):

    tea_type = st.selectbox("Kya Kya Dalana hai:" ,["Doodh" ,"Paani", "Baash Ka Doodh" , "Recomnded if Dimag Kam jor Hai - Badamm", "Keser" , "Extra MAsala"])
    st.write("Select Jo Bhi chiaye: ", tea_type)

elif st.button("or kuch"):
    Flavour = st.selectbox("Le li JI Ye : ", ["Haldhi" , "Adhrak" , "Tulsi ", "Extra Keser"])
    st.write("Le ne ho to lijiye: ", Flavour,"Ka Swadh")

shakker = st.slider("Shakker Kitani chaamach dalu per cup : ", 0,10)

#if st.button("Bana duu Chai Pakka Ya or Kuch"):
        #st.button("Ha Bana Dooooo") 
       # st.success("Baan Rahi hai Time La Ge Ga")

name = st.text_input("Aapaka Subh Nam: ")
if name:
    st.write("Swagat hai", name,"!")
    #st.write("Chai Raste Mai hai ban Rahi hai.")

dob = st.date_input("Aaj ki Tarik")
if dob:
    st.write("Tarik", dob)


if st.button("Bana duu Chai Pakka Ya or Kuch"):
        st.button("Ha Bana Dooooo") 
        st.success("Baan Rahi hai Time La Ge Ga")




