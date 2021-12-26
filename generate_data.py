import os
import ast
import pprint

with open("data.txt", "w") as d:
    for file in os.listdir("logs/"):
        with open(f"logs/{file}", "r") as f:
            data = ast.literal_eval(f.read())
            # pp = pprint.PrettyPrinter(indent=4, compact=True)
            for message in data:
                if 'sticker_items' in message:
                    d.write(
                        f"{message['author']['discriminator']} {message['sticker_items'][0]['name']}\n")
