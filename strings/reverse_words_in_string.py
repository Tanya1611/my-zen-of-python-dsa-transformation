'''Reverse Words in a String in Python

Given a string, the task is to reverse the words in it without changing the words themselves.

'''

s = input("Enter a string: ")
words = s.split()
res = ""

for word in reversed(words):
    res += word + " "

res = res.strip()
print(f"Result is {res}")

# Output:
# Enter a string: Coding is Fun
# Result is Fun is Coding