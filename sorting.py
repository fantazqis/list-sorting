def sorting(listing):
    i = 0
    print(listing)
    biggest_num = listing[0]
    while i < len(listing):
        if biggest_num < listing[i]:
            biggest_num = listing[i]

        # elif biggest_num > listing[i]:
        #     break

        i = i + 1
    return biggest_num


num_list = [1, 4, 6, 3, 2, 7, 3, 5, 6, 3, 3, 5, 6, 7, 2, 10, 20, 23]
sorting_num_list = []
# num_list.sort()
# sorted(num_list, reverse=True)
for i in range(0, len(num_list)):
    num_to_append = sorting(num_list)
    sorting_num_list.append(num_to_append)
    num_list.remove(num_to_append)

print(sorting_num_list)
#print(f"terbesar: {num_list.index(5)}")
