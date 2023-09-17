import re

def get_response(user_input):
    user_input = user_input.lower()

    # Define patterns and respective responses
    patterns_responses = {
        r'\b(hi|hello|hey)\b': "Hello! How can I assist you today?",
        r'\b(how are you)\b': "I'm just a computer program, but I'm here to help you!",
        r'\b(good morning)\b': "Good morning! How can I assist you today?",
        r'\b(good afternoon)\b': "Good afternoon! How can I assist you today?",
        r'\b(good evening)\b': "Good evening! How can I assist you today?",
        r'\b(bye|goodbye)\b': "Goodbye! Have a great day!",
        r'\b(messi)\b': "Lionel Messi is a legendary football player known for his skills and talent.",
        r'\b(ronaldo)\b': "Cristiano Ronaldo is one of the greatest footballers of all time.",
        r'\b(barcelona)\b': "FC Barcelona is a prominent football club based in Barcelona, Spain.",
        r'\b(cricket|sports)\b': "Cricket is one of the most famous sports in the world with amazing fanbase.",
        r'\b(cricketer|babar azam)\b': "Babar Azam is a top-class cricketer and the captain of the Pakistan national cricket team.",
        r'\b(cricketer|imran khan)\b': "Imran Khan is a cricket legend and ex Prime Minister of Pakistan.",
        r'\b(create)\b': "Hello! I'm a chatbot created by Abdullah Mashhadi. How can I assist you today?"
    }

    # Check patterns and provide responses
    for pattern, response in patterns_responses.items():
        if re.search(pattern, user_input):
            return response

    return "Sorry, I don't understand. Can you please rephrase or ask a different question?"

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye! Have a great day!")
        break

    response = get_response(user_input)
    print("Bot:", response)
