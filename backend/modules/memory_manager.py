class MemoryManager:
    def __init__(self):
        self.conversation_history = []

    def add_message(self, user_message, bot_response):
        self.conversation_history.append({
            'user': user_message,
            'bot': bot_response
        })

    def get_history(self):
        return self.conversation_history

    def clear_history(self):
        self.conversation_history = []
        return 'Conversation history cleared.'

# Example usage:
if __name__ == '__main__':
    memory = MemoryManager()
    memory.add_message('Hello', 'Hi there!')
    memory.add_message('How are you?', 'I am just a program, but thanks for asking!')
    print(memory.get_history())
