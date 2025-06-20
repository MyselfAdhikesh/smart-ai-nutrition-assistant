import pandas as pd
from backend.diet_templates import diet_templates

# Load food data
df = pd.read_csv("data/food_dataset.csv")

# -------------------------------
# Calorie Calculator with Goal
# -------------------------------
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
    calorie_adjust = diet_templates.get(goal, {}).get("calorie_adjustment", 0)

    return round(tdee + calorie_adjust)

# -------------------------------
# Macro-Based Meal Plan
# -------------------------------
def generate_meal_plan(target_calories, goal="Balanced", diet_type="Normal"):
    macro_split = diet_templates.get(goal, diet_templates["Balanced"])["macro_split"]

    # Target grams of each macro (based on kcal/g: 4 for carbs & protein, 9 for fat)
    target_carbs = (macro_split["carbs"] / 100) * target_calories / 4
    target_protein = (macro_split["protein"] / 100) * target_calories / 4
    target_fat = (macro_split["fat"] / 100) * target_calories / 9

    filtered_df = df.copy()

    # Optional: filter by diet type
    if "Type" in df.columns and diet_type.lower() != "normal":
        filtered_df = filtered_df[filtered_df["Type"].str.lower() == diet_type.lower()]

    selected = []
    total_cals = total_protein = total_carbs = total_fat = 0

    for _, row in filtered_df.sample(frac=1).iterrows():  # randomize
        if total_cals + row["Calories"] > target_calories:
            continue

        selected.append(row)
        total_cals += row["Calories"]
        total_protein += row["Protein"]
        total_carbs += row["Carbs"]
        total_fat += row["Fat"]

        if total_cals >= target_calories * 0.95:
            break

    return pd.DataFrame(selected)

# -------------------------------
# Format Food Display
# -------------------------------
def format_food_info(df_meals):
    return df_meals[["Name", "Calories", "Protein", "Carbs", "Fat"]].rename(columns={
        "Name": "Food Item",
        "Calories": "kcal",
        "Protein": "Protein (g)",
        "Carbs": "Carbs (g)",
        "Fat": "Fat (g)"
    })
