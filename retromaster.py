import re
import json
import random
import time

# Output text to the user
def say(text):
    print(" :: " + text);
    time.sleep(random.randint(1, 10) / 10)

# Ask input from the user
def ask(text):
    say(text)
    return input("   >> ");

# Returns a random starter question
def getStarterQuestion():
    return random.choice(data['starters'])

# Returns a set of follow-up questions
def getFollowUpQuestions():
    return random.sample(data['followups'], random.randint(4,5))

# Returns a random continue response to keep a discussion going
def createContinueResponse():
    return random.choice(data['continues'])

# Returns a mirrored question based on the given answer
def createMirrorResponse(input):
    mirrors = data['mirrors'].copy()
    random.shuffle(mirrors)
    for mirror in mirrors:
        regex = re.compile(mirror['pattern'], re.IGNORECASE)
        match = regex.match(input)
        if match:
            return random.choice(mirror['responses']).format(match.group(mirror['group']))
    return createContinueResponse()

# Get a random closers
def getCloser():
    return random.choice(data['closers'])

###############################################################################

# Main loop
with open('data.json') as f:
    data = json.load(f)

say("========================================================================")
say("Hello there! I'm RetroMaster 3000 (tm)")
say("It's retro time, so let's get cracking!")
say("========================================================================")

ask(getStarterQuestion())
for question in getFollowUpQuestions():
    answer = ask(question)
    for x in range(1, random.randint(2,3)):
        answer = ask(createMirrorResponse(answer))


ask("On a scale of 1 through 5, how would you rate this sprint?")
say(getCloser())
