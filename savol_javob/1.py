string_example = "hello"
tuple_example = (1, 2, 3)
int_example = 10

list_example = [1, 2, 3]
dict_example = {'a': 1, 'b': 2}


def modify_immutable(data):
    data += " world"
    print("Modified inside function:", data)


print("Original:", string_example)
modify_immutable(string_example)
print("After function call:", string_example)


def modify_mutable(data):
    data.append(4)
    print("Modified inside function:", data)


print("Original:", list_example)
modify_mutable(list_example)
print("After function call:", list_example)