import streamlit as st
import re
import os
import random
import string

def validate_phone_number(phone_number):
    # Check if the phone number field is empty
    if not phone_number:
        st.error("Please enter your phone number.")
        return ''

    # Regular expression pattern to match numeric values
    pattern = r'^[0-9]+$'
    if not re.match(pattern, phone_number):
        st.error("Please enter only numeric values in the phone number field.")
        return ''

    # Check if the phone number has at least 10 digits
    if len(phone_number) < 10:
        st.error("Phone number must be at least 10 digits long.")
        return ''

    return phone_number
        
def validate_email(email):
    # Regular expression pattern for email validation
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(email_pattern, email):
        return email
    else:
        st.error("Please enter a valid email address.")
        return ''
    
def validate_password(password, confirm_password):
    # Expression for password validation
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password)
    has_lowercase = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special_char = re.search(r'[!@#$%*_.?~]', password)
    
    if len(password) < min_length:
        st.error(f"Password must be at least {min_length} characters long.")
        return False
    elif not has_uppercase:
        st.error("Password must contain at least one uppercase letter.")
        return False
    elif not has_lowercase:
        st.error("Password must contain at least one lowercase letter.")
        return False
    elif not has_digit:
        st.error("Password must contain at least one digit.")
        return False
    elif not has_special_char:
        st.error("Password must contain at least one special character.")
        return False
    elif password != confirm_password:
        st.error("Passwords do not match.")
        return False
    else:
        return True
    
def validate_initial_balance(initial_balance):
    if not initial_balance:
        st.error("Please enter your initial balance.")
        return False
    elif not initial_balance.isdigit():
        st.error("Initial balance should be a numeric value.")
        return False
    else:
        return initial_balance
    
def generate_account_number():
    # Generate a 10-digit random account number
    account_number = ''.join(random.choices(string.digits, k=10))

    # Check if the account number is unique
    while account_number in st.session_state.issued_account_numbers:
        account_number = ''.join(random.choices(string.digits, k=10))

    # Add the new account number to the set of issued account numbers
    st.session_state.issued_account_numbers.add(account_number)
    return account_number
   
        
        
def Registration():
    st.title("Registration")
    st.header("Create your account")
    
     # Initialize the set of issued account numbers if it doesn't exist
    if "issued_account_numbers" not in st.session_state:
        st.session_state.issued_account_numbers = set()
        
    # Add your registration form or content here
    with st.form("registration_form"):
        first_name = st.text_input("First Name", placeholder="Enter your first name.", max_chars=20)
        last_name = st.text_input("Last Name", placeholder="Enter your last name.", max_chars=20)
        email_id = st.text_input("Email ID", placeholder="Enter your email id.", max_chars=51)
        phone_number = st.text_input("Mobile Number", placeholder="Enter your mobile number.", max_chars=11)
        initial_balance = st.text_input("Initial Balance", placeholder="Enter your initial balance.", max_chars=11)
        password = st.text_input("Create Password", placeholder="Enter new password", type="password")
        confirm_password = st.text_input("Confirm Password", placeholder="Enter confirm password", type="password")
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            if not first_name:
                st.error("Please enter your first name.")
            elif not last_name:
                st.error("Please enter your last name.")
            else:
                validated_email = validate_email(email_id)
                if not validated_email:
                    return

                validated_phone_number = validate_phone_number(phone_number)
                if not validated_phone_number:
                    return

                is_valid_initial_balance = validate_initial_balance(initial_balance)
                if not is_valid_initial_balance:
                    return
                
                is_valid_password = validate_password(password, confirm_password)
                if not is_valid_password:
                    return

                account_number = generate_account_number()                
                store_registration_data(first_name, last_name, email_id, phone_number, initial_balance, password, account_number)
                st.success("Registration successful!")
                #st.session_state.current_page = "Splash_screen"
                st.experimental_rerun()

def store_registration_data(first_name, last_name, email_id, phone_number, initial_balance, password, account_number):
    # Define the file path to store the registration data
    file_path = "/Users/aniket/Desktop/UCB/OOPS Lectures/Bank_appilcation_new/registration_data.txt"

    # Construct the registration data string
    registration_data = f"{first_name},{last_name},{email_id},{phone_number},{initial_balance},{password},{account_number}\n"

    try:
        # Check if the file exists, if not, create a new file
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write(registration_data)
        else:
            # Append the new registration data to the existing file
            with open(file_path, "a") as file:
                file.write(registration_data)

        print("Registration data stored successfully.")
        
         # Navigate to the login page
        navigate_to_login()
        
    except Exception as e:
        print(f"Error storing registration data: {e}")

"""def navigate_to_login(username):
    # Reset the session state
    st.session_state.clear()
    
    # Set the current page to the login page
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Registration"
    elif "current_page" in st.session_state:
        st.session_state.current_page = "Login"

    # Clear the form fields
    clear_form_fields()

    # Display a success message
    st.success("Registration successful! Navigating to the login page.")

    # Rerun the application to update the page
    st.experimental_rerun()"""

def navigate_to_login(username=None):
    # Reset the session state
    st.session_state.clear()

    # Set the current page to the login page
    st.session_state.current_page = "Login"

    # Clear the form fields
    clear_form_fields()

    # Display a success message
    if username:
        st.success(f"{username}, you have been logged out successfully!")
    else:
        st.success("You have been logged out successfully!")

    # Rerun the application to update the page
    st.experimental_rerun()


def clear_form_fields():
    # Clear the form fields
    st.session_state.first_name = ""
    st.session_state.last_name = ""
    st.session_state.email_id = ""
    st.session_state.phone_number = ""
    st.session_state.password = ""
    st.session_state.confirm_password = ""
    st.session_state.initial_balance = ""
    

