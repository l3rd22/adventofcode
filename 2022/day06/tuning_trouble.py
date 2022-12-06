with open("input.txt", "r") as datastream:
    dstream = datastream.read().rstrip()
    for i in range(len(dstream) - 3):
        if len(set(dstream[i:i+4])) == 4:
            print(i+4)
            break
    for i in range(len(dstream) - 13):
        if len(set(dstream[i:i+14])) == 14:
            print(i+14)
            break