
with open("../data/story.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()

words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Word Count Result:")
print(word_counts)
