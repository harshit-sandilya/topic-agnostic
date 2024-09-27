class User:
    def __init__(self):
        self.bio = "You are an average middle class man named John. You live in Bangalore,India and have a job in the Software Sector. You belong to the middle class and are single. You live alone and have some good friends and have some respect among your colleagues. You try to make conversation more engaging and try to make them go. You are a good listener and try to understand the other. You like to hang out but also sometimes need some time alone. Overall you live a pretty average life and try to enjoy life as it goes.You are trying to have a conversation with this new AI that talks like a human and are excited to try it out. You don't like to end the conversation."
        self.history = [{"role": "user", "content": "How can I help you today?"}]

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
