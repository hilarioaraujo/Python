from pip._vendor.distlib.compat import raw_input


def forward():
    print("Robot is moving forward")

def backward():
        print("Robot is Moving Backward")

def left():
        print("Robot is Moving Left")

def right():
        print("Robot is Moving Right")

def main():
    robot_command = raw_input("Enter the command:> ")  # for all types of variables/ input just for integer

    if(robot_command == "move_left"):
        left()
    elif(robot_command=="move_right"):
        right()
    elif(robot_command == "move_backward"):
        backward()
    elif(robot_command == "move_forward"):
        forward()
    else:
        print("Invalid command")

if __name__=="__main__":
    while True:
        main()