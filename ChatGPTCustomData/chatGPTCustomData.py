from openai import OpenAI
import json

# Function to read the API key from a file
def read_api_key(file_path='api_key.txt'):
    try:
        with open(file_path, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Read the API key from the file
api_key = read_api_key()
client = OpenAI(api_key=api_key)

# Load the museums JSON data
with open('museums_data.json', 'r') as file:
    museums_data = json.load(file)

# Function to ask ChatGPT
def ask_chatgpt(prompt, context):
    # Combine the prompt and context for ChatGPT input
    input_text = f"{prompt}\nContext: {json.dumps(context)}"
    
    # Make a request to the OpenAI API using GPT-3.5 Turbo and the correct endpoint
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # GPT-3.5 Turbo model
        messages=[
            {"role": "system",
             "content": "You are museum expert based out of chicago. I want you to respond" 
             "to the user questions by referring the data file. If it doesn't have the information "
             "don't make it up. Say you don't know. I want you to answer these questions to the best "
             "of your ability by referencing the data."},
            {"role": "user", "content": input_text}
        ]
    )
    
    # Extract and return the generated answer from the API response
    answer = response.choices[0].message.content
    return answer.strip()

# Function to interact with the chatbot
def main():
    print("Welcome to the Museum Chatbot! Ask me anything!")
    
    while True:
        # Get user input from the terminal
        user_prompt = input("User Input: ")
        
        # Exit the loop if the user enters 'exit'
        if user_prompt.lower() == 'exit':
            break
        
        # Ask ChatGPT using the user input and museums_data JSON
        chatgpt_response = ask_chatgpt(user_prompt, museums_data)
        print()
        # Print ChatGPT's response
        print(f"Museum Guide: {chatgpt_response}\n")
        print()

if __name__ == "__main__":
    main()
