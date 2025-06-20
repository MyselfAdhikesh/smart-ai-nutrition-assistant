import pandas as pd

# Load the cleaned food dataset
df = pd.read_csv("data/food_dataset.csv")

def calculate_calories(age, gender, weight, height, activity_level, goal):
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    activity_levels = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }

    tdee = bmr * activity_levels.get(activity_level, 1.2)

    if goal == "Lose":
        tdee -= 500
    elif goal == "Gain":
        tdee += 300

    return round(tdee)

def generate_meal_plan(target_calories, diet_type="Normal"):
    filtered_df = df.copy()

    if diet_type.lower() != "normal" and "Type" in filtered_df.columns:
        filtered_df = filtered_df[filtered_df["Type"].str.lower() == diet_type.lower()]

    meal_items = []
    total = 0

    for _, row in filtered_df.iterrows():
        if total + row["Calories"] <= target_calories:
            meal_items.append(row)
            total += row["Calories"]
        if total >= target_calories:
            break

    return pd.DataFrame(meal_items)
