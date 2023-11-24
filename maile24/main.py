PLACEHOLDER = "[name]"
with open("Input\\Names\\invited_names.txt") as name_list:
    mylist = name_list.read().splitlines()

with open("Input\\Letters\\starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in mylist:
        new_letter = letter_content.replace(PLACEHOLDER, name)

        with open(f"Output\\ReadyToSend\\letter_for{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
