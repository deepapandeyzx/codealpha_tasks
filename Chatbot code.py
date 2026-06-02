# RULE BASED AI PYTHON CHATBOT

import datetime
import time

name=input("enter your name:")
presenthour=datetime.datetime.now().hour

if 5 <= presenthour <=11:
    print("Good Morning,",name)
elif 11 <= presenthour <= 17:
    print("Good afternoon,",name)
elif 17 <= presenthour <=20:
    print("Good evening,",name)
else:
    print("Good night,",name)

print("HEY!, WELCOME TO MY AI CHATBOT")
print("you can ask me basic questions, Type 'bye' to exit from the bot")

#CHATBOT MEMORY CREATION [dictionary of responses]

deeeresponses={
    "hello":"Hii,Welcome.How can i help  you?",
    "how are you":"I am fine.Thank you",
    "who are you":"I am a smart chatbot",
    "what is string":"It is a sequence of characters.It is immutable in nature, once it is created, cannot be changed.",
    "explain functions.":"It is a set of instructions that perform a specific task when it is called.",
    "who developed you":"I am developed by DEEPA PANDEY",
    "how many questions can you answered?":"I can ansewered only some basic questions that are defined",
    "motivate me":"don't give up learning, it will make you a better developer"
}

#functions to get response of chatbot

def getResponseBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachkey in responses:
        if eachkey in userQuestion:
            return responses[eachkey]
    return "I am not able to explain this bcoz I am in lerning mode but i will learn it soon."

#Take userinput

while True:
    
    userInput=input("Please ask your question:")
    reply=getResponseBot(userInput)
    print("Bot Respnse:",reply)

    if "bye" in userInput.lower():
        break

 
