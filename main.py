from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by T.Rohith. you can call me crazy!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing goodnHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?", ]
    ],
    [
        r"I am facing a problem with my laptop",
        ["sorry to hear thatwh, what is the problem you are facing?:)", ]
    ],
    [
        r"Why my battery is draining fast?",
        ["may There could be too many processes running in the background", ]
    ],
    [
        r"Why my laptop stucks while i am using?",
        ["It can often indicate a problem with your computer's hardware.", ]
    ],
    [
        r"Which anti-virus software works effectively",
        ["I prefer Avast and Norton", ]
    ],
    [
        r"Bye",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot created by T.Rohith Kumar")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()