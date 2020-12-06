from collections import Counter

## PART 1
# Read data from input file
with open("input") as f:
    compliant_pass = 0  # Initialize counter for compliant passwords
    for line in f:
        # separate fields in each line and read data
        policy, letter, password = line.split()
        min_, max_ = policy.split('-')  # separate policy data 
        min_ = int(min_)  # Convert to number/int
        max_ = int(max_)
        # remove colon from letter
        letter = letter[0]
        # Counter object with password
        password_counter = Counter(password)
        # Check if password complies with policy
        count = password_counter[letter]  # get count for letter
        if ( min_ <= count ) and ( count <= max_ ):
            compliant_pass += 1

print("PART 1 - Number of valid passwords is {}".format(compliant_pass))


### PART 2
# Read data from input file
with open("input") as f:
    compliant_pass = 0  # Initialize counter for compliant passwords
    for line in f:
        # separate fields in each line and read data
        policy, letter, password = line.split()
        pos1, pos2 = policy.split('-')  # separate policy data 
        pos1 = int(pos1)  # Convert to number/int
        pos2 = int(pos2)
        # remove colon from letter
        letter = letter[0]
        # get letters in position and count (remove 1 for python 0-based)
        letter_counter = Counter(password[pos1-1] + password[pos2-1])
        # Check if password complies with policy
        count = letter_counter[letter]  # get count for letter
        if count==1:
            compliant_pass += 1

print("PART 2 - Number of valid passwords is {}".format(compliant_pass))