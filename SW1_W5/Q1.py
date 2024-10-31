import time

# abc
# with open('simpleText.txt', 'w') as f:
#     f.write('Hello World \nTest test \ntest')


# d
# with open('simpleText.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)
#         time.sleep(2)

# 2
def count_occurrence():
    with open('simpleFile.txt', 'r') as f:
        text = f.read().lower().replace('\n', '').split(' ')
        unique_words = {}
        vowel_count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word in text:
            count = text.count(word)
            if word in unique_words:
                unique_words[word] += 1
            else:
                unique_words[word] = 1
            for letter in word:
                if letter in vowels:
                    vowel_count += 1

        print(f"There are {vowel_count} vowels in the text file")
        print(f"The occurrence of each word in the file is: {unique_words}")


count_occurrence()


