#! /usr/bin/env python3
"""Demonstate use of enumerate in for loop through word search

The use of enumerate eliminates the need to have a second counter in the for
loop.

"""

cat_in_the_hat = ("I will pick up the hook\n"
                  "You will see something new\n"
                  "Two Things And I call them\n"
                  "Thing One and Thing two\n"
                  "These Things will not bite you\n"
                  "They want to have fun\n"
                  "Then out of the box\n"
                  "Came Thing Two and Thing One\n"
                  "And they ran to us fast\n"
                  "They said How do you do\n"
                  "Would you like to shake hands\n"
                  "With Thing One and Thing Two")

word_list = cat_in_the_hat.lower().split()

# show the word positions in the passage
for postion, word in enumerate(word_list):
    print("Position: {}: {}".format(postion, word))

# find the position of all of the "thing"'s in the passage
thing_pos_list = []
for postion, word in enumerate(word_list):
    if word == "thing":
        thing_pos_list.append(postion)

print(thing_pos_list)
