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

def credit_score_input(index):
    #User Input with button 
    submit_button = None
    invalid = False

    with st.form(key='my_form'):
        st.write("Please enter the following information:")
        st.write("Age: ")
        age = st.number_input("Enter your age", min_value=0, max_value=100, value=None)
        
        st.write("\n")
        st.write("Annual Income: ")
        annual_income = st.number_input("Enter your annual income", min_value=0, max_value=1000000, value=None)
        
        st.write("\n")
        st.write("Monthly Inhand Salary: ")
        monthly_inhand_salary = st.number_input("Enter your monthly inhand salary", min_value=0, max_value=100000, value=None)
        
        st.write("\n")
        st.write("Number of Bank Accounts: ")
        num_BA = st.number_input("Enter the number of bank accounts you have", min_value=0, max_value=15, value=None)

        st.write("\n")
        st.write("Number of Credit Cards: ")
        num_CC = st.number_input("Enter the number of credit cards you have", min_value=0, max_value=10, value=None)
        
        st.write("\n")
        st.write("Interest Rate: ") 
        interest_rate = st.number_input("Enter your average interest rate", min_value=0, max_value=100, value=None)
        
        st.write("\n")
        st.write("Number of Loans: ")
        num_loans = st.number_input("Enter the number of loans you have", min_value=0, max_value=10, value=None)
        
        st.write("\n")
        st.write("Type of Loan: ")
        options = 'Choose an Option', 'Student Loan', 'Equity Loan', 'Payday Loan', 'Personal Loan', 'Consolidation Loan', 'Mortgage Loan', 'Auto Loan', 'Builder Loan'
        loan_types = st.multiselect("Select the type of loan you have, if applicable", options)

        st.write("\n")
        st.write("Number of Delayed Payments: ")
        num_delayed_payments = st.number_input("Enter the number of delayed payments", min_value=0, max_value=10, value=None)
        
        st.write("\n")
        st.write("Number of Credit Inquiries: ")
        num_cred_inquires = st.number_input("Enter the number of credit inquiries", min_value=0, max_value=10, value=None)
        
        st.write("\n")
        st.write("Outstanding Debt: ")
        debt = st.number_input("Enter the outstanding debt", min_value=0, max_value=1000000, value=None)
        
        st.write("\n")
        st.write("Credit Utilization Ratio: ")
        cred_util = st.number_input("Enter the credit utilization ratio. For example, for 30% enter 30", min_value=0, max_value=100, value=None)
        
        st.write("\n")
        st.write("Credit History Age: ")
        cred_age = st.number_input("Enter the credit history age", min_value=0, max_value=100, value=None)
        
        st.write("\n")
        st.write("Total EMI per month: ")
        emi = st.number_input("Enter the total EMI per month", min_value=0, max_value=100000, value=None)
        
        st.write("\n")
        st.write("Payment Behaviour: ")

        payment_behavior = st.selectbox("Enter the payment behaviour that best fits you", ('High Spending and Large Value Payments', 'High Spending and Medium Value Payments', 
                'High Spending and Small Value Payments', 'Low Spending and Large Value Payments', 'Low Spending and Medium Value Payments', 'Low Spending and Small Value Payments'))
        
        st.write("\n")
        st.write("Monthly Balance: ")
        monthly_balance = st.number_input("Enter the monthly balance", min_value=0, max_value=100000, value=None)
        
        st.write("\n")
        st.write("\n")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button: 
        st.session_state.data[0] = {'Age': age, 'Annual_Income': annual_income, 'Monthly_Inhand_Salary': monthly_inhand_salary, 'Num_Bank_Accounts': num_BA, 
                          'Num_Credit_Card': num_CC, 'Interest_Rate': interest_rate, 'Num_of_Loan': num_loans, 'Type_of_Loan': loan_types, 
                          'Num_of_Delayed_Payment': num_delayed_payments, 'Num_Credit_Inquiries': num_cred_inquires, 'Outstanding_Debt': debt, 
                          'Credit_Utilization_Ratio': cred_util, 'Credit_History_Age': cred_age, 'Total_EMI_per_month': emi, 
                          'Payment_Behaviour': payment_behavior, 'Monthly_Balance': monthly_balance}
        
def main():
    if 'data' not in st.session_state:
        st.session_state.data = [{'Age': 0, 'Annual_Income': 0, 'Monthly_Inhand_Salary': 0, 'Num_Bank_Accounts': 0, 
                                  'Num_Credit_Card': 0, 'Interest_Rate': 0, 'Num_of_Loan': 0, 'Type_of_Loan': 0, 
                                 'Num_of_Delayed_Payment': 0, 'Num_Credit_Inquiries': 0, 'Outstanding_Debt': 0, 
                                 'Credit_Utilization_Ratio': 0, 'Credit_History_Age': 0, 'Total_EMI_per_month': 0, 
                                 'Payment_Behaviour': 0, 'Monthly_Balance': 0}]
    

    if 'input_index' not in st.session_state:
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

    credit_score_input(st.session_state.input_index)    

    #Updating the dataframe
    dataframe = pd.DataFrame(st.session_state.data)

    #Displaying the current dataframe 
    if not dataframe.empty:
        st.write(dataframe)

    

if __name__ == "__main__":
    main()
    

