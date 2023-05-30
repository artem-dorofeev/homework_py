lorem = "text\n ne pro \nchto ne o chem"

split_data = lorem.split("\n")
split_data_clear = [i.strip() for i in lorem.split("\n")]

# print(lorem.split())
print(split_data)
print(split_data_clear)

print(":".join(split_data_clear[:1]))
