import streamlit as st
import re
import Registration as reg
from BankClass import Bank
from AccountClass import Account


  
def Dashboard(username):
    st.title("Dashboard")
    username = username.upper()
    st.header(f"Hello {username}, Welcome to your personal Banking!")

    # Retrieve the initial balance from the session state
    initial_balance = st.session_state.get("initial_balance", 0)
    # Retrieve the account number from the session state
    account_number = st.session_state.get("account_number", "")
    # Create an instance of the Bank class
    bank_instance = Bank(username, initial_balance, account_number)
    account_instance = Account(username, initial_balance, account_number)
    # Create separate menu items in the sidebar
    st.sidebar.header("Menu")
    menu_option = st.sidebar.radio("Select an option", ["Initial Balance", "Deposit Money", "Withdraw Money", "Check Balance", "Transaction History", "Logout"])

    # Display the selected menu option
    if menu_option == "Initial Balance":
        bank_instance.display_initial_balance()
    elif menu_option == "Deposit Money":
        bank_instance.deposit()
    elif menu_option == "Withdraw Money":
        bank_instance.withdraw()
    elif menu_option == "Check Balance":
        account_instance.current_balance()
    elif menu_option == "Transaction History":
        display_transaction_history()
    elif menu_option == "Logout":
        reg.navigate_to_login(username)
        
def check_balance():
    # Code to display the user's balance
    st.header("Check Balance")
    if st.button("Check Balance", type="primary"):
        if account_number == self.account_number:
            st.write(f"Your current balance is: £{current_balance()}")
        else:
            st.error("Invalid account number.")
    else:
        st.warning("Please enter a valid account number to check balance.")
    
def display_transaction_history():
    # Code to display the user's transaction history
    st.header("Transaction History")
    transactions = st.session_state.transactions
    for transaction in transactions:
        st.write(transaction)

