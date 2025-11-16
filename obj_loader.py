from vec import *

coins = []
arrettes = []

def load_obj(name):
    global coins
    global arrettes
    ALen = len(coins)
    with open("objects/"+name) as file:
        for j in file:
            line = j
            if "v" in line.split():
                v = line.split(" ")
                coins.append(vec3(float(v[1]),float(v[2]),float(v[3])))
            if "f" in line.split():
                f = line.split("/")
                f[0] = f[0].split("f")
                f[2] = f[2].split(" ")
                f[4] = f[4].split(" ")
                arrettes.append(vec3(int(f[0][1])+ALen,int(f[2][1])+ALen,int(f[4][1])+ALen))
