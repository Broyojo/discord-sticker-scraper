import discord
import logging


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel_id = 401255675264761868
        channel = self.get_channel(channel_id)
        with open(f"{channel.name}.txt", "w") as f:
            async for message in channel.history(limit=2500):
                f.writelines([
                    f"author: {message.author}\n",
                    f"time: {message.created_at}\n",
                ])
                f.write("\n")
        print("done")

    # async def on_message(self, message):
    #     print('Message from {0.author}: {0.content}'.format(message))


def main():
    logger = logging.getLogger('discord')
    logging.basicConfig(level=logging.DEBUG)
    handler = logging.FileHandler(
        filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

    token = "OTI0NDQyMTA2MDgzMzExNjE2.Yce5sw.Sgtz0bhGW4qmGrmm1D7cRnNmKVI"
    client = MyClient()
    client.run(token, bot=False)


if __name__ == "__main__":
    main()
