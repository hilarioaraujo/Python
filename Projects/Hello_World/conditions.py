from pip._vendor.distlib.compat import raw_input

robot_command = raw_input("Enter the command:> ") #for all types of variables/ input just for integer

if(robot_command == "move_left"):
    print("Robot is Moving Left")
elif(robot_command=="move_right"):
    print("Robot is Moving Right")
elif(robot_command == "move_backward"):
    print("Robot is Moving Backward")
elif(robot_command == "move_forward"):
    print("Robot is moving forward")
else:
    print("Invalid command")
