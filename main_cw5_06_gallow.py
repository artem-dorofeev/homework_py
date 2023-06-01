# import re

word = ["banana", "borsch", "milk", "apple", "pine", "salo", "sushi"]

"""
------
  | |
  | 
 / \\

"""

gallows = [["-", "-", "-", "-", "-", "-"],
           [" ", "|", " ", " ", "|", " "],
           [" ", "|", " ", " ", " ", " "],
           [" ", "|", " ", " ", " ", " "],
           [" ", "|", " ", " ", " ", " "],
           ["/", " ", "\\", " ", " ", " "],]


def draw_gallows(step=None):
    if step:
        if step >= 1:
            gallows[2][4] = "O"
        if step >= 2:
            gallows[3][3] = "/"
        if step >= 3:
            gallows[3][4] = "|"
        if step >= 4:
            gallows[3][5] = "\\"
        if step >= 5:
            gallows[4][3] = "/"
        if step >= 6:
            gallows[4][5] = "\\"

    result = ""
    for i in gallows:
        result += "".join(i) + "\n"

    return result


def main():
    # for i in range(0, 6+1):
    step = 0

    print(draw_gallows())

    word = "hello"
    answer_word = ["_" for _ in range(len(word))]

    print((len("Hello") * " _ ").strip())

    while True:
        user_input = input("Give yuor letter >>>")
        if user_input == "":
            break

        if user_input not in word:
            step += 1
            print(draw_gallows(step + 1))
        else:
            # indexes_letter = re.findall(user_input, word)

            answer_word[index_letter] = user_input

        print(" ".join(answer_word))


if __name__ == "__main__":
    main()

# gallows[2][4] = "O"
# gallows[3][3] = "/"
# gallows[3][4] = "|"
# gallows[3][5] = "\\"

# result = ""
# for i in gallows:
#     result += "".join(i) + "\n"

# print(result)
