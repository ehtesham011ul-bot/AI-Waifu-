import openai

class AIEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

# Example usage:
if __name__ == '__main__':
    api_key = 'YOUR_OPENAI_API_KEY'
    ai_engine = AIEngine(api_key)
    user_input = 'Hello, how are you?'
    response = ai_engine.generate_response(user_input)
    print(response)
