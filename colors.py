def colors():
    return ["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]
def color_code(color):
    return colors().index(color)

print(color_code("violet"))