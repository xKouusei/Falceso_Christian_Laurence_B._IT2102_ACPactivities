input_chars = input("Enter two space-separated characters: ")
char1, char2 = input_chars.split()
if len(char1) != 1 or len(char2) != 1:
    print("Please enter exactly two characters.")
    print("------------------------------------")
else:
    ascii_char1 = ord(char1)
    ascii_char2 = ord(char2)

    if ascii_char1 > ascii_char2:
        greater_char = char1
    else:
        greater_char = char2
    print("------------------------------------")
    print(f"The character with greater value is: {greater_char}")
    print("------------------------------------")
    print("This part is optional to include.")
    print("Showing ASCII Values:")
    print(f"{char1}: {ascii_char1}")
    print(f"{char2}: {ascii_char2}")
