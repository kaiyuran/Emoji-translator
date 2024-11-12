import json
from flask import Flask, request, jsonify
import random

def emojify(message):

    choiceWordDict = {
    #happy face
    "happy": "😊",
    "joy": "😊",
    "content": "😊",
    "smile": "😊",
    "grateful": "😊",
    "kind": "😊",
    "warm": "😊",
    "friendly": "😊",
    "pleasant": "😊",

    #laugh
    "laugh": "😂",
    "funny": "😂",
    "lol": "😂",
    "hilarious": "😂",
    "joke": "😂",
    "laughter": "😂",
    "giggle": "😂",
    "humor": "😂",
    "meme": "😂",
    "comedy": "😂",

    #heart
    "love": "❤️",
    "heart": "❤️",
    "affection": "❤️",
    "adore": "❤️",
    "romance": "❤️",
    "care": "❤️",
    "beloved": "❤️",
    "fondness": "❤️",
    "sweetheart": "❤️",

    #heart face
    "cute": "🥰",
    "adorable": "🥰",
    "sweet": "🥰",
    "crush": "🥰",
    "blush": "🥰",
    "heartwarming": "🥰",
    "charming": "🥰",
    "affectionate": "🥰",
    "darling": "🥰",


    "amazing": "😍",
    "admire": "😍",
    "wow": "😍",
    "beautiful": "😍",
    "attractive": "😍",
    "captivated": "😍",
    "enchanted": "😍",

    "think": "🤔",
    "ponder": "🤔",
    "wonder": "🤔",
    "curious": "🤔",
    "consider": "🤔",
    "question": "🤔",
    "reflect": "🤔",
    "speculate": "🤔",
    "doubt": "🤔",
    "analyze": "🤔",


    "grin": "😁",
    "excited": "😁",
    "positive": "😁",
    "enthusiasm": "😁",
    "joyful": "😁",
    "cheerful": "😁",
    "beam": "😁",
    "delight": "😁",

    "like": "👍",
    "approval": "👍",
    "agree": "👍",
    "okay": "👍",
    "support": "👍",
    "endorse": "👍",
    "respect": "👍",
    "commend": "👍",
    "thumb": "👍",
    "thumbs": "👍",

    "celebrate": "🎉",
    "party": "🎉",
    "event": "🎉",
    "fun": "🎉",
    "cheer": "🎉",
    "festivity": "🎉",
    "win": "🎉",
    "success": "🎉",
    "achievement": "🎉",

    "fire": "🔥",
    "hot": "🔥",
    "intense": "🔥",
    "awesome": "🔥",
    "trending": "🔥",
    "lit": "🔥",
    "energy": "🔥",
    "passion": "🔥",
    "power": "🔥",

    # Pizza
    "pizza": "🍕",
    "cheese": "🍕",
    "slice": "🍕",
    "italian": "🍕",
    "pepperoni": "🍕",

    # Burger
    "burger": "🍔",
    "cheeseburger": "🍔",
    "fries": "🍔",
    "grill": "🍔",
    "food": "🍔",

    # Taco
    "taco": "🌮",
    "mexican": "🌮",
    "salsa": "🌮",
    "spicy": "🌮",
    "guacamole": "🌮",

    # Sushi
    "sushi": "🍣",
    "fish": "🍣",
    "rice": "🍣",
    "soysauce": "🍣",
    "japanese": "🍣",

    # Ice Cream
    "icecream": "🍦",
    "dessert": "🍦",
    "vanilla": "🍦",
    "cone": "🍦",
    "frozen": "🍦",

    # Apple
    "apple": "🍎",
    "healthy": "🍎",
    "red": "🍎",
    "snack": "🍎",

    # Cake
    "cake": "🍰",
    "birthday": "🍰",
    "celebration": "🍰",

    # Donut
    "donut": "🍩",
    "glazed": "🍩",
    "glaze": "🍩",
    "sprinkles": "🍩",
    # Bread
    "bread": "🍞",
    "toast": "🍞",
    "bakery": "🍞",
    "sandwich": "🍞",
    "loaf": "🍞",

    # Watermelon
    "watermelon": "🍉",
    "fruit": "🍉",
    "refreshing": "🍉",
    "summer": "🍉",
}

    message = message.replace('"', "")
    message = message.replace("'", "")
    finalMessage = []
    print("message is:",message)
    message = message.split(" ")
    for word in message:
        try:
            finalMessage.append(word + " " + choiceWordDict[word.lower()])
            # print("Emojified word is:",word)
        except:
            finalMessage.append(word)
            pass
    print(finalMessage)
    final =" ".join([str(item) for item in finalMessage])
    # print(final)
    return final






app = Flask(__name__)

# Define a list of emojis to randomly select from
emojiList = ['😊', '😂', '❤️', '🥰', '😍', '🤔', '😁', '👍', '😎', '🎉', '🔥', '💯', '🌟', '🎈', '✨']

@app.route('/getemoji', methods=['GET'])
def get_random_emoji():
    # Get the 'letter' parameter from the URL
    message = request.args.get('message')
    print(message)
    # random_emoji = random.choice(emojiList)
    # Return the emoji in JSON format
    final = emojify(message)
    print(final)
    final = jsonify({final: 1})
    # print(final)
    return final
    # print(type({emojiList[1]: 1}))
    # return jsonify({emojiList[1]: 1})

if __name__ == '__main__':
    app.run(debug=True)