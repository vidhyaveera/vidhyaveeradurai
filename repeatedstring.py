def most_repeated_letters(word_1):
    lettersCount = {}
    for ch in word_1:
        if ch not in lettersCount:
            lettersCount[ch] = 1
        else:
            lettersCount[ch] += 1

    return max(lettersCount, key=lettersCount.get)

n=input()
print(most_repeated_letters(n))


