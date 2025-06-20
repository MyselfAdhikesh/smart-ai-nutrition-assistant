import streamlit as st
from backend.meal_planner import calculate_calories, generate_meal_plan, format_food_info
from backend.chatbot_engine import keyword_chatbot

# -------- SIDEBAR NAVIGATION --------
st.sidebar.title("🍱 Smart AI Nutrition Assistant")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📝 User Input", "📊 Results", "🤖 Chatbot"])

# -------- PAGE: HOME --------
if page == "🏠 Home":
    st.title("Welcome to Smart AI Nutrition Assistant")
    st.markdown("""
    🔹 Personalized diet plans  
    🔹 Daily calorie estimation  
    🔹 Chatbot support for nutrition questions  
    """)

# -------- PAGE: USER INPUT --------
elif page == "📝 User Input":
    st.title("Enter Your Details")

    with st.form("user_form"):
        age = st.number_input("Age", 10, 100, 25)
        gender = st.selectbox("Gender", ["Male", "Female"])
        height = st.number_input("Height (cm)", 100, 250, 170)
        weight = st.number_input("Weight (kg)", 30, 200, 65)
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
        goal = st.selectbox("Goal", ["Balanced", "Weight Loss", "Protein Gain"])
        diet_type = st.selectbox("Diet Type", ["Normal", "Vegetarian", "Vegan"])
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.session_state.user = {
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight,
            "activity_level": activity_level,
            "goal": goal,
            "diet_type": diet_type
        }
        st.success("✅ Input saved! Go to 📊 Results tab.")

# -------- PAGE: RESULTS --------
elif page == "📊 Results":
    st.title("Your Personalized Meal Plan")

    if "user" not in st.session_state:
        st.warning("Please fill in your details first.")
    else:
        user = st.session_state.user
        calories = calculate_calories(
            user["age"], user["gender"], user["weight"],
            user["height"], user["activity_level"], user["goal"]
        )
        st.info(f"🎯 Your Daily Calorie Goal: **{calories} kcal**")

        meal_df = generate_meal_plan(calories, user["goal"], user["diet_type"])
        st.dataframe(format_food_info(meal_df))

# -------- PAGE: CHATBOT --------
elif page == "🤖 Chatbot":
    st.title("Ask NutritionBot 🤖")

    user_question = st.text_input("Type your question here:")
    if st.button("Ask"):
        if user_question:
            response = keyword_chatbot(user_question)
            st.success(f"Bot: {response}")
        else:
            st.warning("Please enter a question.")
