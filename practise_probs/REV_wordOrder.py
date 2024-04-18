def rev(text):
    text = text.split(" ")
    text = text[::-1]
    result = " ".join(text)
    return result
print(rev("My name is Michele"))