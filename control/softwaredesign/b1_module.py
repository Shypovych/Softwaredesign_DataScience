# b1 module
band_members = ["Peter", "Bjorn", "John"]


# b1.1 module
print(f"------------- b1.1 module:")
for member in band_members:
    print(member) # inside the loop is missing indentation.


# b1.2 module
print(f"------------- b1.2 module:")
for member in band_members:
    print(f"{member} played great in this song.") # for each band member in loop
print(f"I can not wait to hear {member} play in the next song.") # last value of member — John


# b1.3 module
print(f"------------- b1.3 module:")
for member in band_members:
    print(f"{member} played great in this song.")              # inside loop — runs once per member
    print(f"I can not wait to hear {member} play in the next song.")  # also inside loop
    print(f"I can not wait to hear all of you at the next gig.")      # also inside loop
# 3-line block repeats three times — once for Peter, Bjorn, and John.


# b1.4 module
print(f"------------- b1.4 module:")
for member in band_members:
    print(f"{member} played great in this song.")                 # inside loop — runs once per member
    print(f"I can not wait to hear {member} play in the next song.")  # also inside loop

print("I can not wait to hear all of you at the next gig.")       # outside loop — runs once after loop ends