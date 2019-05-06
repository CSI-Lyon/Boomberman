decoding = {
    0 : "GRASS",
    1 : "stone",
    2 : "bedrock",
    10 : "GRASS+PLAYER_1",
    50 : "GHOST"
}

def decode(ID):
    return decoding[ID]

def encode(name):
    for key, value in decoding.items():
        if value == name:
            return key
            break
