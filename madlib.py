with open("txt", "r") as f:
    txt = f.read()

words = set()
target_start = "<"
target_end = ">"

for i, char in enumerate(txt):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = txt[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1



answers = {"<name>": "Diana"}

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer


for word in words:
    txt = txt.replace(word, answers[words])

print(txt)
