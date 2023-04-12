months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
months.insert(0,0)
print(months[int(input())])


my_list = [1] * 77
print(my_list)


my_list1 = ['q', 'w', 't'] * 15
print(my_list1)



my_list3 = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244, -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381, 109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275, 619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254, 307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598, -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
print(min(my_list3),max(my_list3))


my_list4 = list(map(int, input().split()))
print(777 in my_list4)


list_numbers = list(map(int, input().split()))
print(sum(list_numbers))


mas = list(map(int, input().split()))
print(min(mas), max(mas))

list_numbers1 = list(map(int, input().split()))
a = sum(list_numbers1)
b = float(a/ len(list_numbers1))
print(b)


