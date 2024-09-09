import random

# Syllable collections for each line of the haiku
five_syllables = [
    "An old silent pond", 
    "A world of dew", 
    "Autumn moonlight",
    "The light of a candle", 
    "In the cicada's cry"
]

seven_syllables = [
    "A frog jumps into the pond", 
    "Summer grasses all that remains",
    "Snow softly falling in night", 
    "The scent of wisteria", 
    "Through the empty window"
]

# Function to generate a haiku
def generate_haiku():
    line1 = random.choice(five_syllables)
    line2 = random.choice(seven_syllables)
    line3 = random.choice(five_syllables)
    haiku = f"{line1}\n{line2}\n{line3}"
    return haiku

# Main program
if __name__ == "__main__":
    print("Your Random Haiku:")
    print(generate_haiku())
