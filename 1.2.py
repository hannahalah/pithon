def count_vowels_and_consonants(text):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    vowel_count = 0
    consonant_count = 0
    consonant_list = []
    words = text.split()

    for word in words:
        ове
        for letter in word:
            if letter in vowels:
                vowel_count += 1
            elif letter in consonants:
                consonant_count += 1
                consonant_list.append(letter)


return vowel_count, consonant_count, consonant_list
text = input("Введите текст: ")
vowel_count, consonant_count, consonant_list = count_vowels_and_consonants(text)

print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")

if vowel_count == consonant_count:
    print("Согласные буквы в тексте:", ''.join(consonant_list))

words = text.split()
word_count = len(words)
print(f"Количество слов в тексте: {word_count}