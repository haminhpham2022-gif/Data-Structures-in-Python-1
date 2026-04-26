empty = [] # empty list
words = ['apple', 'elephant', 'lion', 'laugh'] # str
num = [1, 4, 0.7] # int and float
boolean = [True, False] # boolean
mixed = ['hello', 99, False, 4.5] # mixed

# display
print(words)
print("===next===")
# using a loop
print("===next===")
for word in words:
    print(word)
# accessing one element
print("===next===")
print(words[3])
# adding an element
print("===next===")
empty.append('new')
print(empty)
# remove
print("===next===")
words.remove('elephant')
print(words)
# pop
print("===next===")
empty.pop(0)
print(empty)
