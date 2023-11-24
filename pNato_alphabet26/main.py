import pandas
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def play():

    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

    my_word = input("Enter a word:").upper()
    second_faze = [letters for letters in my_word]

    answer = [code_dict[let] for let in second_faze]

    print(answer)
play()
play2 = input("Again? Y/N?:").upper()
while play2 == "Y":
    play()