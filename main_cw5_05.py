text = "   Hello Word from Python!   "

word_list = text.strip().replace("Python", "GoIT").split(" ")

print(word_list)

list_of_words = ["We", "learn", "Python!"]
result = ". ".join(list_of_words)
print(result)


result2 = ". ".join(list_of_words[:2])
print(result2)
