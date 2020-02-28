from pip._vendor.distlib.compat import raw_input

class Robot:

    def __init__(self):
        print("started robot")

    def move_forward(self,distance):
        print("Robot is moving forward " + str(distance) + "m")

    def move_backward(self,distance):
            print("Robot is Moving Backward "+ str(distance) + "m")

    def move_left(self,distance):
            print("Robot is Moving Left "+ str(distance) + "m")

    def move_right(self,distance):
            print("Robot is Moving Right "+ str(distance) + "m")

    def __del__(self):
        print("Robot Stopped")

def main():
    obj = Robot()
    obj.move_forward(2)
    obj.move_backward(2)
    obj.move_right(2)
    obj.move_left(2)

if __name__=="__main__":
    while True:
        main()