# Ideally we will have something come in from the music translator and this will be the second step... we can break
# it up into multiple files if we need to but this will be the place that will link the speaker up with the AI for the
# most part

# ideally the AI sends this file (or rather we call a function from this class to play music from the speaker using
# info from the AI file) a formatted list.
# We will make it a 2d List for the time being... It also must be a list since we will need to append to it
# constantly

# format for the music list
'''
[[0, "0", "0404", 60],
["EQN"],["DQN"],["CQN"],["DQN"],
["EQN"],["EQN"],["EHN"],["DQN"],
["DQN"],["DHN"],["EQN"],["GQN"],
["GHN"],["EQN"],["DQN"],["CQN"],
["DQN"],["EQN"],["EQN"],["EQN"],
["EQN"],["DQN"],["DQN"],["EQN"],
["DQN"],["CWN"],
]
'''

# that is mary had a little lamb... Every array is a note and I will now explain what is going on!
# the first array is actually not a note but the information required to play the song! The first number
# Signifies the Clef that you are playing in a table of contents will be placed below for reference on what all
# the numbers mean. The second number signifies the key being played in. A table of contents will also be provided
# the third number is the time signature. which can range from 31/32 to 1/1 it must be saved in a string format...
# to make sure that all 4 digits are preserved and the first number being a 0 will not throw off the program
# the last number is the beats per minute... self explanatory!

# ---------- TOC --------------
#   Clef
#       0 - Treble Clef
#       1 - Bass Clef
#       2 - Alto Clef
#       3 - Tenor Clef
#
#   Key Signature
#       0 - C
#       1 - G
#       2 - D
#       3 - A
#       4 - E
#       5 - B/Cb
#       6 - F#/Gb
#       7 - Db/C#
#       8 - Ab
#       9 - Eb
#       A - Bb
#       B - F

# What will this file do?

# this file will take in the 2D List or perhaps just one list for simplicity and figure out what needs to be played
# and when. Then after it will reference the WAV files and then use the audio through the speaker on the raspberry pi.
