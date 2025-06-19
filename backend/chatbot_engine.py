# backend/chatbot_engine.py

def keyword_chatbot(user_input):
    user_input = user_input.lower()

    if "calorie" in user_input:
        return "Most adults need 2000–2500 kcal daily, depending on activity."

    elif "protein" in user_input:
        return "You need around 1g of protein per kg of body weight daily."

    elif "breakfast" in user_input and "weight loss" in user_input:
        return "A healthy weight loss breakfast: oats, fruit, boiled egg."

    elif "meal plan" in user_input:
        return "Use the meal planner tab to get a personalized diet based on your goal."

    elif "fats" in user_input:
        return "Healthy fats include nuts, seeds, olive oil, and avocado."

    elif "carbs" in user_input:
        return "Complex carbs like brown rice, oats, and quinoa are healthy options."

    else:
        return "Sorry, I didn't get that. Try asking about calories, protein, or meals."
