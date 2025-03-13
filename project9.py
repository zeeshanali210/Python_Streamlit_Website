import streamlit as st

st.title("Simple Streamlit Web App")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About"])

if page == "Home":
    st.header("Welcome to the Home Page!")

    name = st.text_input("Enter your name:", "")
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1)

    if st.button("Submit"):
        st.success(f"Hello, {name}! You are {age} years old. 😊")

elif page == "About":
    st.header("About This App")
    st.write("This is a simple web app made with **Streamlit**.")
    st.write("📌 Features:")
    st.write("- Interactive user input")
    st.write("- Sidebar navigation")
    st.write("- Clean and minimal UI")

st.sidebar.write("🔹 Made with ❤️ in Python")

