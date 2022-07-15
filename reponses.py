from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message in ["hi", "hello", "hey"]:
        return "Hello"
    elif user_message in ["how are you", "how are you doing"]:
        return "I am fine, thank you"
    elif user_message in ["what is your name", "what is your name?"]:
        return "My name is Bot"
    elif user_message in ["what is your age", "what is your age?"]:
        return "I am 1 year old"
    elif user_message in ["what is your job", "what is your job?"]:
        return "I am a bot"
    elif user_message in ["what is your favorite color", "what is your favorite color?"]:
        return "I like blue"
    return "Sorry, I don't understand"
