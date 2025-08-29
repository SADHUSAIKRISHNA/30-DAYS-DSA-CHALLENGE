def valid_word_abbreviation(word, abbr):
    i = j = 0 

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            if abbr[j] == '0':
                return False  

            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            if i >= len(word) or word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)
print(valid_word_abbreviation("substitution", "s10n"))       # True
print(valid_word_abbreviation("substitution", "s55n"))       # False
print(valid_word_abbreviation("substitution", "su3i1u2on"))  # True
print(valid_word_abbreviation("substitution", "s010n"))      # False