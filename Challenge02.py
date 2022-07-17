
#challange 02

# string input from the user
input_string = input("Enter the string: ")
# converting the string to the lower case
lower_string = input_string.lower()
# getting the unique characters from the strings
unique_characters = set(lower_string)
unique_characters = list(unique_characters)
# list to store the count of the characters
counts = []
for character in unique_characters:
    count = 0
    for char in lower_string:
        if character == char:
            count += 1
    counts.append(count)

# variable to store the highest count index
highest = counts[0]
highest_index = 0
# getting the index of the highest count
for index in range(len(counts)):
    if counts[index] > highest:
        highest = counts[index]
        highest_index = index

# list to store the characters with highest count
highest_count_characters = []
for index in range(len(counts)):
    if highest == counts[index]:
        highest_count_characters.append(unique_characters[index])

# checking the index of highest count characters
highest_indexes = []
for character in highest_count_characters:
    for index in range(len(lower_string)):
        if lower_string[index] == character:
            highest_indexes.append(index)
            break

min_value = min(highest_indexes)

# printing the character with highest count
print("Character with highest count", highest, "is:", lower_string[min_value])
