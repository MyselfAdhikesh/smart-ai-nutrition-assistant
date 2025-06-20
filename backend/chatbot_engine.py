from .nlp_model import predict_answer

def keyword_chatbot(user_input):
    try:
        return predict_answer(user_input)
    except Exception as e:
        return "Sorry, I couldn't understand that. Please rephrase your question."
