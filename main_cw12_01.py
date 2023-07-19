import pickle

data = {"a": [1,2,3,4], "b": "Hello"}

byte_str = pickle.dumps(data)

print(byte_str)

unpacked_data = pickle.loads(byte_str)

print(unpacked_data)

with open("data.bin", "wb") as f:
    pickle.dump(data, f)

with open("data.bin", "rb") as f:
    some_data = pickle.load(f)

print(some_data)