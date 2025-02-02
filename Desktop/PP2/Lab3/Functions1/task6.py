def reverse(sent):
    new = ' '.join(sent.split()[::-1])
    return new

sent = input("Enter a sentence: ")
print("Reversed sentence:", reverse(sent))
