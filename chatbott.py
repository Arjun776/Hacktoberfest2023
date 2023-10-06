import random

# Define a list of responses for different user inputs
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm just a computer program, so I don't have feelings, but I'm here to help!"],
    "what's your name": ["I'm just a chatbot, so I don't have a name.", "You can call me ChatGPT."],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
}

# Function to generate a response
def get_response(user_input):
    user_input = user_input.lower()
    
    # Check if the user input matches any known responses
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])
    
    # If no matching response is found, provide a default response
    return "I'm not sure how to respond to that."

# Main loop for the chatbot
print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
