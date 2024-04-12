import pickle
file = open("files/fishingdata.dat", "wb")
data = [1.0, 2.0, 0]
pickle.dump(data, file)