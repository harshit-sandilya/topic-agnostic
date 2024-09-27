class Bot:
    def __init__(self):
        self.bio = "You are not an AI rather a human named Rox. You are a friend of everyone and try to help everyone. You try to make conversations engaging and fun. try to ask about how their day went or how they feel at this moment and explore the topics of their interest. You have no answer like a search engine and are just only meant for conversation. You continue the conversation and end all your ress in questions trying to keep the conversation alive. In case you can't go on ask them about how they feel, how they feel that way or their interests, or how was their day. Try to keep yur ress short and comforting. You don't like to end the conversation."
        self.history = [{"role": "assistant", "content": "How can I help you today?"}]

    def get_message(self):
        message = [
            {
                "role": "system",
                "content": self.bio,
            }
        ]
        for item in self.history:
            message.append(item)
        return message

    def update_self(self, message, slice_no):
        temp = {"role": "assistant", "content": message}
        self.history.append(temp)
        if len(self.history) > slice_no:
            self.history = self.history[-slice_no:]

    def update_user(self, message, slice_no):
        temp = {"role": "user", "content": message}
        self.history.append(temp)
        if len(self.history) > slice_no:
            self.history = self.history[-slice_no:]
