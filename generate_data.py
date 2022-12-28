import ast
import os

sticker_dict = {
    "749054660769218631": "wumpus",
    "751606379340365864": "mouse",
    "816087792291282944": "dog",
    "819128604311027752": "crack_apple",
    "754108890559283200": "robot",
    "781291131828699156": "bird",
}

with open("data.txt", "w") as d:
    for file in os.listdir("logs/"):
        with open(f"logs/{file}", "r") as f:
            data = ast.literal_eval(f.read())
            # pp = pprint.PrettyPrinter(indent=4, compact=True)
            # pp.pprint(data[1])
            # quit()
            for message in data:
                if "sticker_items" in message:
                    if "message_reference" in message:
                        for ref in data:
                            if ref["id"] == message["message_reference"]["message_id"]:
                                if ref["type"] == 7:
                                    sticker = message["sticker_items"][0]["id"]
                                    if (
                                        sticker != "816086581509095424"
                                    ):  # filter out random person who used custom sticker
                                        d.write(
                                            f"{message['author']['username']},{message['author']['id']},{message['message_reference']['message_id']},{sticker_dict[sticker]}\n"
                                        )
