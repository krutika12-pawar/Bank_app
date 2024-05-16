import streamlit as st
import random



class Bank:
    def __init__(self, username, initial_balance, account_number):
        self.username = username
        self.initial_balance = initial_balance
        self.account_number = account_number
        


    def display_initial_balance(self):
        st.header("Initial Balance")
        initial_balance = self.initial_balance
        st.write(f"Your initial balance is: £{initial_balance}")
        
            
    def deposit(self):
        st.header("Deposit Money")
        st.write("Want to deposit money into your account? Proceed with entering amount.")
        account_number = st.text_input("Your account number:", value=self.account_number, disabled=True)
        amount = st.number_input("Enter the amount to deposit:", min_value=0.0)

        if st.button("Deposit Money", type="primary"):
            if amount > 0:
                if account_number == self.account_number:
                    self.initial_balance += amount
                    # Update the initial balance in the session state
                    st.session_state["initial_balance"] = self.initial_balance 
                     # Update the initial balance in the text file
                    self.update_initial_balance_in_file(account_number, self.initial_balance)
                    st.success(f"£{amount} deposited into your account. Your new balance is: £{self.initial_balance}")
                else:
                    st.error("Invalid account number.")
            else:
                st.warning("Please enter a valid amount to deposit.")
    
    def update_initial_balance_in_file(self, account_number, new_balance):
        file_path = "/Users/aniket/Desktop/UCB/OOPS Lectures/Bank_appilcation_new/registration_data.txt"
        updated_lines = []

        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            fields = line.strip().split(",")
            if len(fields) >= 7 and fields[6] == account_number:
                 # Update the initial balance field
                fields[4] = str(new_balance) 
            updated_lines.append(",".join(fields))

        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))

        print(f"Initial balance updated in the file for account number {account_number}")

        
    def withdraw(self):
        st.header("Withdraw Money")
        st.write("Want to withdraw money from your account? Proceed with amount you want to withdraw.")
        account_number = st.text_input("Your account number:", value=self.account_number, disabled=True)
        amount = st.number_input("Enter the amount to withdraw:", min_value=0.0)

        if st.button("Withdraw Money", type="primary"):
            if amount > 0:
                if account_number == self.account_number:
                    if self.initial_balance >= amount:
                        self.initial_balance -= amount
                        st.session_state["initial_balance"] = self.initial_balance
                        self.update_initial_balance_in_file(account_number, self.initial_balance)
                        st.success(f"£{amount} withdrawn from your account. Your new balance is: £{self.initial_balance}")
                    else:
                        st.error("Insufficient balance.")
                else:
                    st.error("Invalid account number.")
            else:
                st.warning("Please enter a valid amount to withdraw.")
            

   