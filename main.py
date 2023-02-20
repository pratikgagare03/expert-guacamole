Assumptions: 
1. The file consists of tweets in text format 
2. The racial slurs are provided in a separate file

Python code: 

# Load the racial slurs from the file into a set
slurs = set()
with open('slurs.txt', 'rb') as f:
    for line in f:
        slurs.add(line.strip())

# Count the number of slurs in each tweet
profanity_score = {}
with open('tweets.txt', 'rb') as f:
    for line in f:
        words = line.lower().split()
        profanity_score[line] = 0
        for word in words:
            if word in slurs:
                profanity_score[line] += 1

# Print the profanity score for each tweet
for line, score in profanity_score.items():
    print('Tweet: ' + line + '\nProfanity score: ' + str(score) + '\n')
