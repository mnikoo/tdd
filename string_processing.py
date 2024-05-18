def reverse_string(input):
    if input is None:
        return None
    
    result = ""
    for i in range(0, len(input)):
        result = result + input[len(input) - i - 1]
    return result

def reverse_sentence(input):
    if input is None:
        return None
    result = ""
    words = input.split(" ")
    for i in range(0, len(words)):
        result = result + words[-i - 1] + " "

    return result[:-1]