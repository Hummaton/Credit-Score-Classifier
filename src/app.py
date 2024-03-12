# Harjot Gill 
import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import subprocess

#streamlit run app.py --server.runOnSave true

# Include CSS files
def include_css(filename):
    with open(filename, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def learn_more():
    with st.sidebar:
        st.markdown("<center><h1> What could effect my credit score? </h1></center>", unsafe_allow_html=True)
        st.write("1. Age: The older you are, the more credit history you have. \
                 This means you have more data for the credit bureaus to use to calculate your credit score.")
        st.write("2. Annual Income: A higher income can help you get approved for more credit. \
                 This is because you have more money to pay back potential loans.")
        st.write("3. Monthly Inhand Salary: This is the amount of money you have left after taxes and other deductions. \
                 The more money you have left over, the greater your ability to pay back loans.")
        st.write("4. Number of Bank Accounts: The more bank accounts you have, the more credit history/activity you have generally speaking. \
                 While this is not as important as other factors, it can still have an impact on your credit score.")
        
        ### Add more factors here
        """"
        Age                          True
        Annual_Income                True
        Monthly_Inhand_Salary        True
        Num_Bank_Accounts            True
        Num_Credit_Card              True
        Interest_Rate                True
        Num_of_Loan                  True
        Type_of_Loan                False
        Num_of_Delayed_Payment       True
        Num_Credit_Inquiries         True
        Outstanding_Debt             True
        Credit_Utilization_Ratio     True
        Credit_History_Age           True
        Total_EMI_per_month          True
        Payment_Behaviour           False
        Monthly_Balance              True
        Credit_Score                False  """

def credit_score_input(df, index):
    #User Input with button 
    input = None
    submit_button = None
    invalid = False

    if df is None:
        df = []  # Initialize df as an empty list if None

    with st.form(key='my_form'):
        st.write("Question " + str(index) + "/16")

        if index == 1:
            input = st.number_input("What is your age?")
            submit_button = st.form_submit_button(label='Submit')
            invalid = input < 16 or input > 100
            errorMsg = "Please enter a valid age between 16 and 100"

        if submit_button:
            if invalid:
                st.error(errorMsg)
            else:
                df.append({'Age': input})
                return df

        


            


def main():
    if 'data' not in st.session_state:
        st.session_state.data = []
        st.session_state.input_index = 1

    # Include page styling and header removal  CSS files
    include_css('../src/.style/header_remove.css')
        # ******Main body of the page*****

    # Title of the page
    title = "Credit Score Form"
    st.markdown(f"<center><h1>{title}</h1></center>", unsafe_allow_html=True)
    st.write("\n")

    st.subheader("Get an estimation on your credit score easily!") 

    # Creating two columns layout
    col1, col2 = st.columns([2.8, 1])  

    # Text in the left column
    with col1:
        st.write("Understanding your credit score is a vital part of your financial well-being")

    # Button in the right column
    with col2:
        if st.button("Learn more"):
            learn_more()

    st.session_state.data = credit_score_input(st.session_state.data, st.session_state.input_index)

    #Updating the dataframe
    dataframe = pd.DataFrame(st.session_state.data)

    #Displaying the current dataframe 
    if not dataframe.empty:
        st.write(dataframe)

    

if __name__ == "__main__":
    main()
    

