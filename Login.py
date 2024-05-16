import streamlit as st
import re
from Registration import validate_email
from Dashboard import Dashboard

def validate_password(password):
    # Custom password validation logic
    # Example: Minimum length of 8 characters, at least one uppercase letter, one lowercase letter, and one number
    return len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password)

def Login():
    if not st.session_state.get("logged_in", False):
        st.title("Sign In")
        st.header("Login using your Email Id and Password.")

        # Load registration data from .Text file
        with open("registration_data.txt", "r") as file:
            registration_data = file.readlines()

        # Login form fields Username, Password and Login button
        email_id = st.text_input("Email ID", placeholder="Enter your registered email id.", max_chars=51)
        password = st.text_input("Password", placeholder="Enter your password", type="password")

        login_button = st.button("Login", on_click=validate_login, args=(email_id, password, registration_data))

    else:
        Dashboard(st.session_state["username"])
       

def validate_login(email_id, password, registration_data):
    # Validate email and password fields
    if not email_id:
        st.error("Please enter your email address.")
    elif not password:
        st.error("Please enter your password.")
    else:
        # Validate email and password
        for data in registration_data:
            fields = data.strip().split(",")
            if len(fields) >= 6:
                registered_email, registered_password, username, initial_balance = fields[2], fields[5], fields[0], fields[4]
                if email_id == registered_email and password == registered_password:
                    # Process the Login functionality
                    #st.success("Login successful!")
                    
                    st.session_state["logged_in"] = True
                    # Store the username in session state
                    st.session_state["username"] = username
                    st.session_state["initial_balance"] = float(initial_balance)
                    st.session_state["account_number"] = fields[6].strip()
                    
                    break
        else:
            st.error("Invalid email or password. Please enter a valid email and password.")


def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    Login()

if __name__ == "__main__":
    main()