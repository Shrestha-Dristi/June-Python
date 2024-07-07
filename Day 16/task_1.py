# Vowel Check


def is_vowel(l):
    if l.lower() in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False


x = input("Enter a letter")
str = is_vowel(x)
print(str)



data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

result = map(lambda element: element in ['a', 'e', 'i', 'o', 'u'], data)
print(list(result))

