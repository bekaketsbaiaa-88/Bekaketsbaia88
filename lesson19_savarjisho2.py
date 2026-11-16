class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def reverse_text(text):
    stack = Stack()
    for letter in text:
        stack.push(letter)

    result = ""
    while not stack.is_empty():
        result = result + stack.pop()
    return result


def is_palindrome(text):
    clean_text = text.replace(" ", "").lower()
    return clean_text == reverse_text(clean_text)


print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))
print(is_palindrome("Never odd or even"))
print(is_palindrome("აი ია"))
print(is_palindrome("Python"))
