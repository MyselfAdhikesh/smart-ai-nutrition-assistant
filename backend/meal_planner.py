import pandas as pd

# Load the food dataset (adjust path as needed)
df = pd.read_csv("data/food_dataset.csv")

# --------------------------
# 1. Calorie Calculation
# --------------------------
def calculate_calories(age, gender, weight, height, activity_level, goal):
    # BMR calculation using Mifflin-St Jeor
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

# --------------------------
# 2. Meal Plan Generator
# --------------------------
def generate_meal_plan(target_calories, diet_type="Normal"):
    # Filter based on diet type (if available in dataset)
    filtered_df = df.copy()
    if "Type" in df.columns and diet_type.lower() != "normal":
        filtered_df = filtered_df[filtered_df["Type"].str.lower() == diet_type.lower()]

    # Select foods that add up to the target_calories
    meal_items = []
    total = 0

    for _, row in filtered_df.iterrows():
        if total + row["Calories"] <= target_calories:
            meal_items.append(row)
            total += row["Calories"]
        if total >= target_calories:
            break

    return pd.DataFrame(meal_items)

# --------------------------
# 3. Show Food Info (optional UI helper)
# --------------------------
def format_food_info(df_meals):
    df_meals = df_meals[["Name", "Calories", "Protein", "Carbs", "Fat"]]
    df_meals = df_meals.rename(columns={
        "Name": "Food Item",
        "Calories": "kcal",
        "Protein": "Protein (g)",
        "Carbs": "Carbs (g)",
        "Fat": "Fat (g)"
    })
    return df_meals
