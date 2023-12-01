# Read the content of the file input.txt
input_file = open("input_1.txt", "r")
file_content = input_file.read()

# Cut the content of the file into a list of lines
lines = file_content.split("\n")

total_sum = 0
first_int = None # 5
last_int = None # 2
for line in lines:
    # Parcourir chaque caractère de la ligne
    for char in line:
        if char.isdigit():
            if first_int == None:
                first_int = int(char)
            else:
                last_int = int(char)
    # Put the two digits next to each other
    if last_int == None:
        last_int = first_int
    if first_int != None and last_int != None:
            total_sum += first_int * 10 + last_int
            first_int = None
            last_int = None

print(total_sum)