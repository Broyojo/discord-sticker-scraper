with open("test.json", "r") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if "has received" in lines[i]:
            s = "926:DEBUG:discord.http: GET https: //discord.com/api/v7/channels/903390307494805554/messages has received "
            with open(f"logs/{i}.json", "w") as o:
                o.write(lines[i][len(s):])
