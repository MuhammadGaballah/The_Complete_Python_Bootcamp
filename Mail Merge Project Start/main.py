# TODO: Create a letter using starting_letter.txt


# for each name in invited_names.txt

with open("Input/Names/invited_names.txt") as file:
    initial_list = file.readlines()
    names_list = []

    for name in initial_list:
        names_list.append(name.strip('\n'))

with open("Input/Letters/starting_letter.txt") as starting_file:
    invitation_template = starting_file.read()

for name in names_list:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter:
        final_letter.write(invitation_template.replace("[name]", name))


# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
