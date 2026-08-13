"""
Lesson 1 - Section 3  (10:30 - 12:00)
Python refresher.

How we use this file:
  1. We RUN it once with no explanation. You watch the output.
  2. Then we read it together, top to bottom, and you tell me what each part did.
  3. The notes are at the BOTTOM of the file. Do not scroll down yet.

Nothing here is new. The point is to wake it back up, and to make sure everyone
can run Python inside PyCharm before we get to machine learning this afternoon.

Run it:  right-click in the editor -> Run '01_refresher'
"""

print("=" * 55)
print("PART 1  -  VARIABLES")
print("=" * 55)

score = 72
score = 91

print("score is", score)

student_name = "Maya"
attempts = 3
average = 78.5
is_enrolled = True

print("name:", student_name, "| attempts:", attempts,
      "| average:", average, "| enrolled:", is_enrolled)

score = score + 5
print("after the bonus, score is", score)

print("the type of average is", type(average))


print()
print("=" * 55)
print("PART 2  -  FUNCTIONS")
print("=" * 55)


def show_result(name, number):
    print(f"  {name} scored {number}")


def average_of(a, b):
    total = a + b
    return total / 2


show_result("Maya", 88)
show_result("Liam", 74)
show_result("Noor", 91)

result = average_of(88, 74)
print("the average of 88 and 74 is", result)


print()
print("=" * 55)
print("PART 3  -  CONTROL FLOW  (if / elif / else)")
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


print("95 ->", letter_grade(95))
print("83 ->", letter_grade(83))
print("71 ->", letter_grade(71))
print("40 ->", letter_grade(40))


print()
print("=" * 55)
print("PART 4  -  LISTS AND LOOPS")
print("=" * 55)

scores = [88, 74, 91, 40, 83]

print("all scores:", scores)
print("how many:", len(scores))
print("the first one:", scores[0])
print("the last one:", scores[-1])

scores.append(67)
print("after append:", scores)

print("looping over the list:")
for one_score in scores:
    print("  ", one_score, "->", letter_grade(one_score))

print("range(3) gives:")
for i in range(3):
    print("   i =", i)

total = 0
for one_score in scores:
    total = total + one_score
print("total:", total, "| class average:", round(total / len(scores), 1))


print()
print("=" * 55)
print("PART 5  -  DICTIONARIES")
print("=" * 55)

student = {
    "name": "Maya",
    "age": 15,
    "favourite_language": "Python",
}

print("the whole dict:", student)
print("look up by key:", student["name"])

student["age"] = 16
student["campus"] = "McGill"
print("after editing:", student)

print("just the keys:", list(student.keys()))
print("just the values:", list(student.values()))

for key, value in student.items():
    print(f"   {key} = {value}")

classroom = [
    {"name": "Maya", "score": 88},
    {"name": "Liam", "score": 74},
    {"name": "Noor", "score": 91},
]

for person in classroom:
    print(f"   {person['name']}: {letter_grade(person['score'])}")


print()
print("=" * 55)
print("PART 6  -  CLASSES AND OBJECTS")
print("=" * 55)


class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

    def bark(self):
        print(f"  {self.name} says WOOF")

    def learn_trick(self, trick):
        self.tricks.append(trick)
        print(f"  {self.name} learned to {trick}")

    def describe(self):
        return f"{self.name} is a {self.breed} and knows {len(self.tricks)} trick(s)"


rex = Dog("Rex", "beagle")

rex.bark()
rex.learn_trick("sit")
rex.learn_trick("roll over")
print(" ", rex.describe())

bella = Dog("Bella", "husky")
bella.bark()
print(" ", bella.describe())
print("  rex's tricks:", rex.tricks)
print("  bella's tricks:", bella.tricks)


print()
print("=" * 55)
print("That is the whole refresher. Variables, functions, if/elif/else,")
print("lists, loops, dictionaries, classes. Every one of those shows up")
print("again this afternoon in the machine learning section.")
print("=" * 55)


# =============================================================================
#
#   S T O P
#
#   The answers are below, one part at a time.
#   Say out loud what the code does BEFORE you scroll to its notes.
#
# =============================================================================


































# =============================================================================
# NOTES - PART 1  -  VARIABLES
# =============================================================================
#
# score = 72
# score = 91
#   The second line overwrites the first. Only 91 survives. Variables hold
#   STATE: the value right now, which can change as the program runs.
#
# Python has a few basic types. You do not declare them, Python works it out.
#   student_name = "Maya"    str    text, in quotes
#   attempts     = 3         int    whole number
#   average      = 78.5      float  decimal number
#   is_enrolled  = True      bool   True or False
#
# score = score + 5
#   Read the old value, add 5, store the result back. 91 + 5 = 96.
#   Did you predict that before you read the output?
#
# type(average)
#   You can always ask Python what type something is.
#
# =============================================================================


































# =============================================================================
# NOTES - PART 2  -  FUNCTIONS
# =============================================================================
#
# def show_result(name, number):
#   `def` DEFINES a function. Nothing runs yet - this just creates it.
#   `name` and `number` are parameters: placeholders for values we pass in
#   later.
#
# def average_of(a, b): ... return total / 2
#   A function can also hand a value BACK to whoever called it, using `return`.
#   show_result prints and returns nothing. average_of returns a number.
#
# show_result("Maya", 88)
#   This is the CALL. This is where the code inside actually runs.
#   Three calls, one definition. That is the whole reason functions exist:
#   write the logic once, in one place, and reuse it.
#
# result = average_of(88, 74)
#   The returned value gets stored in `result`. (88 + 74) / 2 = 81.0
#
# =============================================================================


































# =============================================================================
# NOTES - PART 3  -  CONTROL FLOW  (if / elif / else)
# =============================================================================
#
# Python checks the conditions top to bottom and STOPS at the first true one.
#
# Order matters. For 95, all three are true: 95 >= 90 AND >= 80 AND >= 70.
# It returns "A" because that check comes first, and `return` exits the
# function immediately - nothing after it runs.
#
# Flip the order and put `number >= 70` first: now every passing score comes
# back "C". Try it.
#
# `else` is the catch-all: it runs when nothing above it matched.
#
# =============================================================================


































# =============================================================================
# NOTES - PART 4  -  LISTS AND LOOPS
# =============================================================================
#
# A list holds several related values, in order, in one name.
#
#   scores[0]     counting starts at 0, not 1. So [0] is the FIRST item.
#   scores[-1]    negative counts from the end. [-1] is the LAST item.
#   len(scores)   how many items.
#   .append(67)   adds one to the end. It changes the list in place.
#
# for one_score in scores:
#   A for loop repeats the body once per item in the list. `one_score` is a
#   name that points at each item in turn.
#
# range(3) produces 0, 1, 2. It STOPS BEFORE the number you give it.
#
# total = 0
# for one_score in scores:
#     total = total + one_score
#   Start empty, add to it on each pass. Loops are also how you build up a
#   result step by step.
#
# =============================================================================


































# =============================================================================
# NOTES - PART 5  -  DICTIONARIES
# =============================================================================
#
# A dictionary stores pairs: a KEY, and the VALUE that belongs to it.
#   A list answers "what is in position 2?"
#   A dict answers "what belongs to Maya?"
#
#   student["name"]         look up by key, not by position.
#   student["age"] = 16     assigning to an EXISTING key changes it.
#   student["campus"] = ..  assigning to a NEW key adds it.
#
#   .keys()     just the labels
#   .values()   just the contents
#   .items()    both halves of each pair - which is why the loop unpacks two
#               names:  for key, value in student.items():
#
# You can nest them: a LIST OF DICTS is how real data usually arrives. One dict
# per record, all the records in a list. Remember that shape - it comes back
# this afternoon when we load the dataset.
#
# =============================================================================


































# =============================================================================
# NOTES - PART 6  -  CLASSES AND OBJECTS
# =============================================================================
#
# A class is a blueprint. It groups DATA and the ACTIONS on that data together.
#
# __init__ runs automatically when you make a new Dog. You never call it
# yourself - Dog("Rex", "beagle") calls it for you.
#
# `self` is the specific dog being set up. Every method takes it as the first
# parameter, and you never pass it in yourself.
#
# self.name, self.breed, self.tricks are ATTRIBUTES: data belonging to this one
# dog. self.tricks starts empty and fills up later.
#
# bark, learn_trick and describe are METHODS: functions that live inside a
# class.
#
# Dog is the blueprint. `rex` is an actual object built from it.
# Each object keeps its OWN data. Two dogs, two separate names and trick lists.
# Teaching rex a trick does nothing to bella.
#
#   attributes = what it HAS      (rex.name, rex.tricks)
#   methods    = what it can DO   (rex.bark(), rex.learn_trick())
#
# =============================================================================
