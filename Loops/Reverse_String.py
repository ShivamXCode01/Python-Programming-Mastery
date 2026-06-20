get_input=input("Enter your String=")
reversed_char=""
#print(get_input[::-1])

for char in get_input:
    reversed_char = char +reversed_char


print(reversed_char)
# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str  

# print(reversed_str)