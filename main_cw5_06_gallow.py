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

result = ""
for i in gallows:
    result += "".join(i) + "\n"

print(result)
