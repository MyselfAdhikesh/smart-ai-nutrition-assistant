import streamlit as st

# Page Configuration
st.set_page_config(page_title="Smart AI Nutrition Assistant", layout="centered")

# Header
st.title("🥗 Smart AI Nutrition Assistant")
st.subheader("Your AI-powered guide to a healthier lifestyle")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Chatbot", "Meal Planner", "About"])

# Page Views
if page == "Home":
    st.header("🏠 Home")
    st.write("Welcome! Enter your basic details to get started.")
    st.text_input("Name")
    st.number_input("Age", min_value=1, max_value=120)
    st.selectbox("Gender", ["Male", "Female", "Other"])
    st.selectbox("Goal", ["Lose Weight", "Maintain Weight", "Gain Muscle"])
    st.selectbox("Diet Type", ["Normal", "Vegetarian", "Vegan", "Keto", "Other"])
    st.button("Submit")

elif page == "Chatbot":
    st.header("💬 AI Nutrition Chatbot")
    st.write("Ask any question related to food, calories, diet plans, or health.")
    user_input = st.text_input("Type your question here")
    if st.button("Ask"):
        st.write("🤖 Bot reply: [This will show your ML model output]")

elif page == "Meal Planner":
    st.header("📅 Weekly Meal Planner")
    st.write("Based on your goals, we’ll suggest a full day’s meal.")
    st.write("[This section will generate or show meal plans]")

elif page == "About":
    st.header("ℹ️ About")
    st.write("This assistant helps you understand and improve your diet using AI.")
    st.write("Team: Adhikesh, Ajin, Nihal, Sreerag, Akhil")


