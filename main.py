import ast
import logging

import discord

# change these to your liking
TOKEN = "OTI0NDQyMTA2MDgzMzExNjE2.Yce5sw.Sgtz0bhGW4qmGrmm1D7cRnNmKVI"
MESSAGE_LIMIT = 100000
OUTPUT_NAME = "data.txt"
CHANNELS = [
    903390307494805554,
    401255675264761868,
]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        dummy = []
        for channel in CHANNELS:
            channel = self.get_channel(channel)
            async for message in channel.history(limit=MESSAGE_LIMIT):
                dummy.append([message.author, message.created_at])
        print("done scraping")
        await self.close()


def generate_data(path):
    sticker_dict = {
        "749054660769218631": "wumpus",
        "751606379340365864": "mouse",
        "816087792291282944": "dog",
        "819128604311027752": "crack_apple",
        "754108890559283200": "robot",
        "781291131828699156": "bird",
    }
    with open(path, "w") as d:
        with open("discord.log", "r") as logs:
            lines = logs.readlines()
            for i in range(len(lines)):
                if "has received [" in lines[i]:
                    start = lines[i].index("[")
                    data = ast.literal_eval(lines[i][start:])
                    # pp = pprint.PrettyPrinter(indent=4, compact=True)
                    # pp.pprint(data[1])
                    # quit()
                    for message in data:
                        if (
                            "sticker_items" in message
                            and "message_reference" in message
                        ):
                            for ref in data:
                                if (
                                    ref["id"]
                                    == message["message_reference"]["message_id"]
                                    and ref["type"] == 7
                                ):
                                    sticker = message["sticker_items"][0]["id"]
                                    if (
                                        sticker != "816086581509095424"
                                    ):  # filter out random person who used custom sticker
                                        d.write(
                                            "{},{},{},{},{},{}\n".format(
                                                message["author"]["username"],
                                                message["author"]["id"],
                                                message["message_reference"][
                                                    "message_id"
                                                ],
                                                sticker_dict[sticker],
                                                message["author"]["discriminator"],
                                                message["timestamp"],
                                            )
                                        )


def main():
    logger = logging.getLogger("discord")
    logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)

    client = MyClient()
    client.run(TOKEN, bot=False)

    generate_data(OUTPUT_NAME)


if __name__ == "__main__":
    main()
