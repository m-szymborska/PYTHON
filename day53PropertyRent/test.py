original_string = ['$2,895+/mo', '$2,895/mo']

# Find the index of the last character you want to keep (in this case, the '+' sign)
end_index = original_string.find('+')

# Slice the string to keep only the characters up to 'end_index'
sliced_string = original_string[:end_index]

print(sliced_string)