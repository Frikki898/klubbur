book = "Hello Hello Hello I am a book look at my I am a dumb book"
book = book.split(' ')
print(book)

dictionary = {}

for word in book:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
        
print(dictionary)


arr = []
for elem in dictionary:
    arr.append([elem, dictionary[elem]])

arr.sort(key=lambda x: -x[1])

print(arr)
