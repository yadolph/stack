

class Stack:
    def __init__(self):
        self.contents = []

    def is_empty(self):
        if self.contents == 0:
            return True
        else:
            return False

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        popped_item = self.contents.pop(-1)
        return popped_item

    def peek(self):
        last_item = self.contents[-1]
        return last_item

    def size(self):
        size = len(self.contents)
        return size


def check_bracket_balance(brackets):
    checker = Stack()
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    brackets_list = list(brackets)

    if len(brackets_list) % 2 != 0:
        return 'несбалансировано'
    elif len(brackets_list) == 0:
        return 'пустая строка'
    else:
        for bracket in brackets_list:
            if bracket in open_brackets:
                checker.push(bracket)
            elif bracket in close_brackets:
                idx = close_brackets.index(bracket)
                if checker.peek() == open_brackets[idx]:
                    checker.pop()
            else:
                return 'Похоже, тут что-то кроме скобок'
    if checker.size() == 0:
        return 'сбалансировано'
    else:
        return 'несбалансировано'


a = '((([{}]{}[]{[]})))'
b = '{{[(])]}}'

print(check_bracket_balance(a))
print(check_bracket_balance(b))