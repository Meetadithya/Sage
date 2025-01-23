import together

# Initialize the Together API
together.api_key = '36f55ba6b5e6c0bc00b00e2f887aa75e4065811d98b54727e772dec3461335ad'

# Function to call the Together AI assistant
def get_response(prompt):
    response = together.Completion.create(
        engine="together-instruct",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Customize the response to include the creator's information
def personalized_response(user_input):
    ai_response = get_response(user_input)
    creator_info = "This AI assistant was created by Adithya. You can find him on Instagram: @meetadithya."
    return f"{ai_response}\n\n{creator_info}"

# Example usage
if __name__ == "__main__":
    user_prompt = "Who created you?"
    ai_personalized_response = personalized_response(user_prompt)
    print(f"AI Assistant: {ai_personalized_response}")
