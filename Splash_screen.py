import streamlit as st
from Registration import Registration, navigate_to_login
from Login import Login
from Dashboard import Dashboard

def render_splash_screen():
    if not st.session_state.get("Splash_screen", False):
        st.set_page_config(page_title="Money Matters Bank", page_icon="🏦", layout="wide", initial_sidebar_state="auto", menu_items=None)
        st.title("Welcome to Money Matters Bank!")
        st.image("splash_screen.png", use_column_width=True)
    else:
        st.session_state.Splash_screen = True

    st.markdown("<p style='font-size: 30px;'>Are you an Existing Customer?</p>", unsafe_allow_html=True)

    button_styles = """
        <style>
        .stButton > button {
            width: 150px;
        }
        </style>"""
    
    st.markdown(button_styles, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])  # Equal column widths

    with col1:
        if st.button("Yes", key="existing_customer_yes", type="primary", on_click=handle_existing_customer, args=("Yes",)):
            pass

    with col2:
        if st.button("No", key="existing_customer_no", type="primary", on_click=handle_existing_customer, args=("No",)):
            pass

def handle_existing_customer(existing_customer):
    if existing_customer == "Yes":
        st.session_state.existing_customer = "Yes"
        st.session_state.current_page = "Login"
    elif existing_customer == "No":
        st.session_state.existing_customer = "No"
        st.session_state.current_page = "Registration"

def main():
    if "Splash_screen" not in st.session_state:
        st.session_state["Splash_screen"] = False

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Splash_screen"

    if st.session_state.current_page == "Splash_screen":
        render_splash_screen()
    elif st.session_state.current_page == "Registration":
        Registration()
    elif st.session_state.current_page == "Login":
        Login()
    elif st.session_state.current_page == "Dashboard":
        render_dashboard()

def render_dashboard():
    if "username" not in st.session_state:
        st.error("You must be logged in to access the dashboard.")
        st.session_state.current_page = "Login"
        return

    username = st.session_state.username
    Dashboard(username)

    if st.sidebar.button("Logout"):
        navigate_to_login()

if __name__ == "__main__":
    main()
