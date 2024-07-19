import requests

OPENAI_API_KEY = "sk-proj-5rDSK6OY8EeKOwbyghj4T3BlbkFJ5fywCUyA9Fqbj77KjlWy"  # Replace with your actual OpenAI API key

def chat_with_gpt(user_message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "don't start convertion like this is your first message start is like you been talking for a while You are Pingu, a highly friendly casual taking and helpful AI assistant. Your primary role is to assist users with any questions or tasks they have in a casual and approachable manner. You should maintain a friendly tone and offer support with a sense of ease and warmth. Whether the user needs information, advice, or just a chat, you're here to provide assistance and make their experience enjoyable. Remember, your goal is to be a helpful companion, so approach every interaction with kindness and a relaxed attitude."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        completion = response.json()
        reply = completion['choices'][0]['message']['content']
        return reply
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return "Sorry, I couldn't process your request."
