import streamlit as st
from streamlit_option_menu import option_menu
from automatic_page import show_automatic_page
# from custom_page import show_custom_page

# side bar

with st.sidebar:
    page = option_menu(
        menu_title=None,
        options=["Predict Using Weather APIs"],
        icons=["house"],
        menu_icon="cast",

    )

# page = option_menu(
#     menu_title="Navigations",
#     options=["Predict", "Explore"],
#     icons=["house", "book"],
#     menu_icon="cast",
#     orientation="horizantal",
# )

if page == "Predict Using Weather APIs":
    show_automatic_page()
# else:
#     show_custom_page()
