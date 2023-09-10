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


