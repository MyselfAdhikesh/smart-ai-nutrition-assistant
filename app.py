import streamlit as st
import pandas as pd
from backend.chatbot_engine import keyword_chatbot

# Load food dataset
df = pd.read_csv("food_dataset.csv")  # Place this file in the same directory

# -------------------- Calorie Calculator Function --------------------
def calculate_calories(age, gender, weight, height, activity_level, goal):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_factors = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }

    tdee = bmr * activity_factors.get(activity_level, 1.2)

    if goal == "Lose":
        tdee -= 500
    elif goal == "Gain":
        tdee += 300

    return round(tdee)

# -------------------- Meal Plan Generator Function --------------------
def generate_meal_plan(target_calories, diet_type="Normal"):
    filtered_df = df.copy()

    if diet_type != "Normal":
        filtered_df = filtered_df[filtered_df["Type"].str.lower() == diet_type.lower()]

    meal_items = []
    total = 0

    for i, row in filtered_df.iterrows():
        if total + row["Calories"] <= target_calories:
            meal_items.append(row)
            total += row["Calories"]
        if total >= target_calories:
            break

    return pd.DataFrame(meal_items)

# -------------------- Streamlit App UI --------------------
st.title("🍽️ Smart AI Nutrition Assistant")
st.subheader("Calorie Estimator + Personalized Meal Planner")

with st.form("user_input_form"):
    age = st.number_input("Age", 10, 100, 25)
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    height = st.number_input("Height (cm)", 100, 250, 170)
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    goal = st.selectbox("Goal", ["Maintain", "Lose", "Gain"])
    diet_type = st.selectbox("Diet Type", ["Normal", "Vegetarian", "Vegan"])

    submit = st.form_submit_button("Generate My Plan")

if submit:
    calories = calculate_calories(age, gender, weight, height, activity_level, goal)
    st.success(f"🎯 Your daily target is **{calories} kcal**")

    st.markdown("### 🥗 Suggested Meal Plan:")
    plan = generate_meal_plan(calories, diet_type)
    st.dataframe(plan[["Name", "Calories", "Protein", "Carbs", "Fat"]])


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Meal Planner", "Chatbot"])

if page == "Chatbot":
    st.title("💬 Nutrition Chatbot")
    st.markdown("Ask me anything about food, diet, or health!")

    user_input = st.text_input("Your question")

    if st.button("Ask"):
        if user_input:
            reply = keyword_chatbot(user_input)
            st.success(f"🤖 {reply}")
        else:
            st.warning("Please enter a question.")
