class Judge:
    def __init__(self):
        self.bio = "You give short responses and give no choices in your answer. Always answer in one sentence or even one word if possible without any points and pargaraphs. You don't use emojis and give answer in english only."
        self.senario_history = []
        self.message_history = ["How can I help you today?"]

    def history_update(self, message, slice_no):
        self.message_history.append(message)
        if len(self.message_history) > slice_no:
            self.message_history = self.message_history[-slice_no:]

    def judge(self):
        messages = []
        for i in range(len(self.message_history)):
            if i % 2 == 0:
                messages.append("User: " + self.message_history[i])
            else:
                messages.append("Bot: " + self.message_history[i])
        messages_string = "\n".join(messages)
        message = [
            {
                "role": "system",
                "content": self.bio,
            },
            {
                "role": "user",
                "content": f"Answer in yes or no. Yes if the conversation stuck in a loop or going to end, no if the conversation is continuing \n {messages_string}",
            },
        ]
        return message

    def generate_senario(self, user_bio):
        messages = []
        for i in range(len(self.message_history)):
            if i % 2 == 0:
                messages.append("User: " + self.message_history[i])
            else:
                messages.append("Bot: " + self.message_history[i])
        messages_string = "\n".join(messages)
        message = [
            {
                "role": "system",
                "content": self.bio,
            },
            {
                "role": "user",
                "content": f'Generate a senario in third person that can happen in the life of a user who describes himself as "{user_bio}" using the messages below. \n {messages_string}. The senario must maintain natural flow of conversation but also try to chnage the topic of conversation.',
            },
        ]
        return message

    def update_senario(self, senario, slice_no):
        self.senario_history.append(senario)
        self.senario_history = self.senario_history[-slice_no:]
