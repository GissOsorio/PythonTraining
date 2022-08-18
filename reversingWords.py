def reverse(text):
    words = []
    reversed = ""
    words = text.split()     
    words.reverse()
    for word in words:
        reversed += word + " "

    return reversed.strip()