print("=" * 55) # the print() displays text, variables, or data onto the output screen (terminal or console)
print("PART 1 - VARIABLES")
print("=" * 55)

score = 55 # think of it like a container, (its a variable) where you can store stuff
print(score)
score = 90 # as you can see there is 2 scores, it will initially first read score = 55, but then it gets replaced and rewritten as score
# = 90. Only the last value is the one that's kept in there, in this case the latest value is score = 90

print("score is", score)

student_name = "Maya" # This is a string, just a bunch of characters on it, its JUST text, you can
attempts = 3 # This is an integer, whole numbers like 1,2,3
average = 78.5 # This is a float, basically a number with a decimal
is_enrolled = True #This is a boolean, true or false

print(f"{student_name}'s attempts:", attempts) # use an f-string instead of the original one

score +=5 # the better way than score = score +5
print("after the bonus, score is", score)

print("the type of average is", float(attempts))


print()
print("=" * 55)
print("part 3 - CONTROL FLOAT (if / elif / else")
print("=" * 55)

def letter_grade(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    else:
        return "needs work"

score = [88, 74, 91, 40, 83]

print("all score:", score)
print("how many:", len(score))
print("the first one:", score[0])
print("the first two:", score[2])


score.append(67)
print("after append:", score)


