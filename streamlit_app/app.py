import datetime
import streamlit as st
st.title("Form for the Users")
st.write("Here, you can answer to some questions in this form.")
user_id = st.text_input("ID", value="Your ID", max_chars=7)
info = st.text_area("Share somw information about you", "Put information here", help = 'You can write about your hobbies or family')
age = st.number_input("Age", min_value=18, max_value=100, step=1)
birth_date = st.date_input("Date of Birth", min_value=datetime.date(1921, 1, 1), max_value=datetime.date(2003, 12, 31))
smoke = st.checkbox("Do you smoke?")
genre = st.radio("Which movie genre do you like?", options=["horror", 'adventure', 'comedy', 'romance'])
weight = st.slider("Chosse your weight(lbs)", min_value=30., max_value=180., step=0.1)
physical_form = st.selectbox("Select your physical condition", options=["Bad", "Normal","Good"])
colors = st.multiselect("What are your favourite colors?", options=['Green', 'Blue', 'Black', 'Indigo', 'Yellow', 'Red'])
image = st.file_uploader("Upload your photo here", type=['jpg', 'png'])
submit = st.button("Submit")
if submit :
    st.write("You've submitted the form")

sidebar = st.sidebar.button('Contact me')
if sidebar:
    st.sidebar.write("You'll be lead to a respective page")

col1, col2 = st.columns(2)
with col1 :
    st.image("https://static.streamlit.io/examples/cat.jpg", width=300)
    st.button("Like cats")
with col2 :
    st.image("https://static.streamlit.io/examples/dog.jpg", width=355)
    st.button("Like dogs")