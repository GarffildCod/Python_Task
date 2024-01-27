# Задача 3

# Sample Input
# ["eat", "tea", "tan", "ate", "nat", “bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по " общим буквам"


list_text = ["eat", "tea", "tan", "ate", "nat", "bat"]

allress = []

for i in list_text:
    group = [i2 for i2 in list_text if set(i2) == set(i)]
    if group not in allress:
        allress += [group]

print(allress)