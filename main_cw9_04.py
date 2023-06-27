def get_letter(word):
    for i in word:
        yield i


gen_letter = get_letter("python")

print(next(gen_letter))
print(next(gen_letter))
print(next(gen_letter))
