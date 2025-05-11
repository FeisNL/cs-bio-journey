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


# problem 2
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
s = 'azcbobobegghakl'

current_substr = [0]
longest_substr = [0]


for i in range(1, len(g)):
    if g[i] > g[i-1]:
        current_substr += [i]
    else:
        current_substr = [i]
    
    if len(current_substr) > len(longest_substr):
        current_substr = longest_substr