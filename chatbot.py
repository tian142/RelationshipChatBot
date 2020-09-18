# get random moduel from the random library
from random import choice


# combine functions and conditionals to get a response from the bot
def get_bot_response(user_response):

 # added bot responses to this list
    bot_response_couple_happy = ["Thats great! Keep taking good care of each other!",
                                 "how sweet, I'm happy for you both!", "Good for you!", "Life is short, enjoy while it lasts :)"]
    bot_response_couple_sad = ["Maybe it'll get better tomorrow!",
                               "Hope you both make good decisions!", "Sorry to hear that, I whish you both the best."]
    bot_response_single_happy = [
        "Good for you!", "Nice, you have lots of time for your self than people in relationships!", "Happy single people make for best parterners!"]
    bot_response_single_sad = ["It's ok, plenty of fishes in the sea",
                               "It will come, don't rush and take care of your self", "Sorry to hear that, I wish the best for you!"]

    if user_response == "y" and user_response2 == "y":
        return choice(bot_response_couple_happy)
    elif user_response == "y" and user_response2 == "n":
        return choice(bot_response_couple_sad)
    elif user_response == "n" and user_response2 == "y":
        return choice(bot_response_single_happy)
    elif user_response == "n" and user_response2 == "n":
        return choice(bot_response_single_sad)
    else:
        return "I wish you the best!"


# Ask user to input answer
print("Welcome to Couple or Single")
print("Are you currently single?")

user_response = ""
user_response2 = ""

# keep repeating until the user enters "done".
while True:
    user_response = input("Are you currently in a relationship? (y/n) ")
    user_response2 = input("Are you happy about it? (y/n)")

    if user_response == 'done':
        break

# call get_bot_response and input user responses
    bot_response = get_bot_response(user_response)
    print(bot_response)
