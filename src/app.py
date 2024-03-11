# Harjot Gill 
import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import subprocess


# Include CSS files
def include_css(filename):
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def learn_more():
    with st.sidebar:
        st.markdown("<center><h1> What could effect my credit score? </h1></center>", unsafe_allow_html=True)

def main():
    if 'data' not in st.session_state:
        st.session_state.data = []

    # Include page styling and header removal  CSS files
    include_css('.style/header_remove.css')
        # ******Main body of the page*****

    #Display the background image
    include_css('.style/page_style.css')

    # Title of the page
    title = "Credit Score Form"
    st.markdown(f"<center><h1 style='color: white;'>{title}</h1></center>", unsafe_allow_html=True)
    st.write("\n")

    st.subheader("Get an estimation on your credit score easily!") 

        # Creating two columns layout
    col1, col2 = st.columns([2.8, 1])  # Adjust the ratio as needed

    # Text in the first column
    with col1:
        st.write("Understanding your credit score is a vital part of your financial well-being")

    # Button in the second column
    with col2:
        if st.button("Learn more"):
            learn_more()


    #User Input with button 
    with st.form(key='my_form'):
        col1, col2 = st.columns(2)
        first_name = col1.text_input("First Name")
        last_name = col2.text_input("Last Name") 
        fav_animal = st.selectbox("Pick your favorite animal", options=["Select an animal", "dog", "cat", "bird", "fish", "rabbit"])
        submit_button = st.form_submit_button(label='Submit')

    #Validation of the input
    if submit_button:
        if fav_animal == "Select an animal" or first_name == "" or last_name == "":   #<-- If parameters not are filled 
            st.write("Invalid input")
        else:
            st.session_state.data.append({'First Name': first_name, 'Last Name': last_name, 'Favorite Animal': fav_animal})

    #Updating the dataframe
    dataframe = pd.DataFrame(st.session_state.data)

    if not dataframe.empty:
        st.write(dataframe)

    

if __name__ == "__main__":
    main()
    

