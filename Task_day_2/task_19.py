'''19. Write a program using decorators to print the traffic signal messages
Expected output -
RED : STOP
YELLOW : SLOW DOWN
GREEN : GO
The decorator should be working in this order'''

def traffic_signal(func):
    def wrapper(color):
        if color == "RED":
            print("RED : STOP")
        elif color == "YELLOW":
            print("YELLOW : SLOW DOWN")
        elif color == "GREEN":
            print("GREEN : GO")
        else:
            print("Invalid color")
        func(color)
    return wrapper

@traffic_signal
def signal(color):
    print("----")

signal("RED")
signal("YELLOW")
signal("GREEN")
