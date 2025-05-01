# Problem set 1 

# problem 1
# Given string
s = 'azcbobobegghakl'

count=  0

for letter in s:
    if letter in "aeiou":
        count += 1
print(count)

# problem 2
# Given string

# solution 1
s = 'azcbobobegghakl'

count = 0

for x in range(len(s)-2)):
    if len[i:i+3] == "bob":
        count += 1
# using , adds an additional space to the concatenation
print("Number of times bob occurs is:", count)


# solution 2
count = 0 
s = 'azcbobobegghakl'

# use sliding window to check every 3 charachter substring, 
# using index n stopping at len(s)-2 to avoid out of bound errors for last slice "akl"
for i in range(len(s)-2):
    if s[i:i+3] == "bob":
        count += 1
# + concatenates everything without any spaces, pure concatenation
print("Number of times bob occurs is: " + str(count))
    

# problem 3
# Given string
s = 'azcbobobegghakl'

# Initialize variables to track the longest substring
longest = s[0]  # Start with the first character as the longest substring
current = s[0]  # Current substring being tracked

# Iterate through the string from the second character onwards, including the last character because we used len(s)
for i in range(1, len(s)):
    # Check if the current character is in alphabetical order with the previous one
    if s[i] >= s[i - 1]:
        current += s[i]  # If yes, add the character to the current substring
    else:
        # If not, check if the current substring is the longest
        if len(current) > len(longest):
            longest = current  # Update the longest substring
        current = s[i]  # Start a new substring with the current character

# After the loop, check once more if the current substring is the longest
if len(current) > len(longest):
    longest = current

# Print the result
print("Longest substring in alphabetical order is:", longest)