with open("data.txt", "r") as f:
    lines = f.readlines()
    messages = []
    for line in lines:
        _, id, _ = line.split()
        if id not in messages:
            messages.append(id)
    print("messages:", len(messages))
    buckets = [[] for i in range(len(messages))]
    for line in lines:
        tag, id, sticker = line.split()
        buckets[messages.index(id)].append((tag, sticker))

    for bucket in buckets:
        print(bucket)
