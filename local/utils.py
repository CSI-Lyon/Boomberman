decoding = {
    0 : "GRASS",
    1 : "PLAYER_1",
    2 : "PLAYER_2",
    3 : "PLAYER_3",
    4 : "PLAYER_4",
    5 : "STONE"
}

def decode(ID):
    return decoding[ID]

def encode(name):
    for key, value in decoding.items():
        if value == name:
            return key
            break
