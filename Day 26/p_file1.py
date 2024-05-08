# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)
# list_of_strings = input("Enter numbers").split(',')
# list_of_numbers = [int(string_a) for string_a in list_of_strings]
# result = [num for num in list_of_numbers if num%2 == 0]
# print(result)
with open("file1.txt") as f:
    lst_1 = f.readlines()
with open("file2.txt") as v:
    lst_2 = v.readlines()
lst1 = [string_a.strip("\n") for string_a in lst_1]
lst2 = [string_b.strip("\n") for string_b in lst_2]
result = [int(string_a) for string_a in lst1 if string_a in lst1 and string_a in lst2]
print(result)