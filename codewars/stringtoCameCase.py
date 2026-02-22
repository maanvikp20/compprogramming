# 6 kyu - Covert String to Camel Case

def to_camel_case(text):
    words = text.replace("-", " ").replace("_", " ").split()
    if not words:
        return ""
    return words[0] + "".join(word.capitalize() for word in words[1:])

print(to_camel_case("The_stealth_warrior"))