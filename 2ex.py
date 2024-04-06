input_string = input("Введите строку: ")
output_string = ""
for i in range(0, len(input_string), 2):
    output_string += input_string[i]

print(output_string)