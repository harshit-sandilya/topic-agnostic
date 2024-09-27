import csv
import ollama
import random

from user import User
from bot import Bot

user = User()
bot = Bot()

c_no = 1
slice_no = 8
min_tokens = 32
max_tokens = 256


with open("./data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["User", "Bot", "Senario", "Judge", "User Tokens"])
    print("Initiated")
    while True:
        user_tokens = random.randint(min_tokens, max_tokens)
        res1 = ollama.chat(
            model="llama3",
            messages=user.get_message(),
            keep_alive=0,
            options={"num_predict": user_tokens},
        )
        res1 = res1["message"]["content"].replace("\n", " ").replace(",", "")
        user.update_self(res1, slice_no)
        bot.update_user(res1, slice_no)

        res2 = ollama.chat(
            model="llama3",
            messages=bot.get_message(),
            keep_alive=0,
        )
        res2 = res2["message"]["content"].replace("\n", " ").replace(",", "")
        bot.update_self(res2, slice_no)
        user.update_user(res2, slice_no)

        writer.writerow([res1, res2, user_tokens])
        print("..|", c_no, "|..")
