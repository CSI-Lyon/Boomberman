decoding = {
    0 : "GRASS",
    1 : "PLAYER_1"
}

def decode(ID):
    return decoding[ID]

def encode(name):
    for key, value in decoding.items():
        if value == name:
            return key
            break
