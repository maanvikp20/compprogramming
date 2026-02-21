# 5 kyu - Readability is King

def flesch_kincaid(text):
    for ender in "!?":
        text = text.replace(ender, ".")
    
    for punc in "-—'()…":
        text = text.replace(punc, "")
    
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    words = [sentence.split() for sentence in sentences]

    syllables = 0

    for sentence in words:
        for word in sentence:
            word = word.lower()
            for char in range(len(word)):
                if word[char] in "aeiou":
                    if char == 0 or word[char - 1] not in "aeiou":
                        syllables += 1
    
    
    avg_words_per_sentence = sum(len(sentence) for sentence in words) / len(words)
    avg_syllables_per_word = syllables / sum(len(sentence) for sentence in words)

    return round((0.39 * avg_words_per_sentence) + (11.8 * avg_syllables_per_word) - 15.59, 2)

    

print(flesch_kincaid("Purrs food food food? Sweet."))
