print("enter any words : ")
# word = input('')
word = 'inzaghi'

word_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#inzaghi
input_arr = word
index_arr = []
final_arr = {}
arr_range = range(0, 27)
word_count = 0

for word_w in word_arr:
    for input_w in input_arr:
        if input_w == word_w:

            print(input_w, word_w)
            print(word_arr.index(input_w))
            index_arr.append(word_arr.index(input_w))

print(index_arr)

# finding max number in list
max = index_arr[0]
for index_r in index_arr:
    if index_r > max:
        max = index_r
print(max)









