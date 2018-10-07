#! /usr/bin/env python3
"""While loop with else used build invitation list and print if successful
"""

processing = True
invitees = []

while processing:
    next_name = input("Enter a name, 'done' to exit, or 'cancel' to cancel: ")

    if next_name == "cancel":
        print("Cancelling Name List Creation")
        invitees = []
        break
    elif next_name == "done":
        processing = False
    else:
        invitees.append(next_name)
else:
    print("These are the people you invited {}".format(invitees))
