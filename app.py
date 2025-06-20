import streamlit as st
import pandas as pd
from backend.chatbot_engine import keyword_chatbot
from backend.meal_planner import calculate_calories, generate_meal_plan

# Load data
df = pd.read_csv("data/food_dataset.csv")

# Sidebar Navigation
st.sidebar.title("🍱 Smart AI Nutrition Assistant")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📝 User Input", "🤖 Chatbot", "📊 Results"])

# ---------- HOME ----------
if page == "🏠 Home":
    st.title("🥗 Welcome to Smart AI Nutrition Assistant")
    st.markdown("""
    This assistant helps you:
    - 🧮 Calculate your daily calorie needs
    - 🥘 Generate personalized meal plans
    - 🤖 Ask questions about food & nutrition

    ---  

    **Team Members:**
    - Adhikesh R S  
    - Ajin K J  
    - Muhammed Nihal  
    - Sreerag  
    - Akhil Das  
    """)

# ---------- USER INPUT ----------
elif page == "📝 User Input":
    st.title("📝 Enter Your Details")

    with st.form("user_input_form"):
        age = st.number_input("Age", 10, 100, 25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.number_input("Height (cm)", 100, 250, 170)
        weight = st.number_input("Weight (kg)", 30, 200, 65)
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
        goal = st.selectbox("Goal", ["Maintain", "Lose", "Gain"])
        diet_type = st.selectbox("Diet Type", ["Normal", "Vegetarian", "Vegan"])

        submit = st.form_submit_button("Submit")

    if submit:
        st.session_state['user_data'] = {
            'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'activity_level': activity_level,
            'goal': goal,
            'diet_type': diet_type
        }
        st.success("✅ Input saved! Go to '📊 Results' tab.")

# ---------- CHATBOT ----------
elif page == "🤖 Chatbot":
    st.title("💬 Nutrition Chatbot")
    st.markdown("Ask me anything about nutrition, calories, protein, or meals!")

    user_input = st.text_input("Your Question")
    if st.button("Ask"):
        if user_input:
            reply = keyword_chatbot(user_input)
            st.success(f"🤖 {reply}")
        else:
            st.warning("Please type something.")

# ---------- RESULTS ----------
elif page == "📊 Results":
    st.title("📊 Your Personalized Meal Plan")

    if 'user_data' not in st.session_state:
        st.warning("⚠️ Please fill out the form in '📝 User Input' tab first.")
    else:
        u = st.session_state['user_data']
        calories = calculate_calories(u['age'], u['gender'], u['weight'], u['height'], u['activity_level'], u['goal'])
        st.info(f"🎯 Estimated Daily Calories: **{calories} kcal**")

        meal_df = generate_meal_plan(calories, u['diet_type'])

        st.subheader("🥘 Suggested Meal Plan")
        st.dataframe(meal_df[["Name", "Calories", "Protein", "Carbs", "Fat"]])
