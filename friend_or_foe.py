"""
Codewars: Friend or Foe
https://www.codewars.com/kata/55b42574ff091733d900002f

Description:
Make a program that filters a list of names and returns only your friends.
Your friends have exactly 4 letters in their name.
"""

def friend(x):
    return [name for name in x if len(name) == 4]


if __name__ == "__main__":
    print(friend(["Ryan", "Kieran", "Mark", "John"]))
