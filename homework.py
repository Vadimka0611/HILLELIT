numbers1 = [1, 2, 3, 4, 5, 6]
numbers2 = [1, 2, 3]
numbers3 = [1, 2, 3, 4, 5]
numbers4 = [1]
numbers5 = []
#Задал переменные
first_part1 = numbers1 [:len(numbers1) // 2]
second_part1 = numbers1 [len(numbers1) // 2:]
result1 = [first_part1, second_part1]
print(result1)
#Выявил первую половину, вторую, сложил через переменную "result" и вывел вв консоль
first_part2 = numbers2 [:len(numbers2) // -3]
second_part2 = numbers2 [len(numbers2) // -3:]
result2 = [first_part2, second_part2]
print(result2)

first_part3 = numbers3 [:len(numbers3) // -3]
second_part3 = numbers3 [len(numbers3) // -4:]
result3 = [first_part3, second_part3]
print(result3)

first_part4 = numbers4 [:len(numbers4) // 1]
second_part4 = numbers4 [len(numbers4) // 1:]
result4 = [first_part4, second_part4]
print(result4)

first_part5 = numbers5 [:len(numbers5) // 1]
second_part5 = numbers5 [len(numbers5) // 1:]
result5 = [first_part5, second_part5]
print(result5)
