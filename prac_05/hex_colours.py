COLOURS = {"blue": "#0000ff", "red": "#ff0000", "purple": "#9b30ff", "green": "#00ff00", "black": "#000000",
           "yellow": "#ffff00", "orange": "#ffa500", "pink": "#ffb5c5", "cyan": "#00ffff", "gold": "#ffd700"}

colour = input("Enter a colour: ")
while colour != "":
    if colour.lower() in COLOURS:
        print("{} colour hex-code is {}".format(colour.lower(), COLOURS[colour.lower()]))
    else:
        print("Colour not in dictionary")
    colour = input("Enter a colour: ")

