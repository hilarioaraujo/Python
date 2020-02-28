robot_x = 0.1
robot_y = 0.1

while (robot_x<2 and robot_y<2):
    robot_x+=0.1
    robot_y+=0.1

    print("Current Position", robot_x,robot_y)

print("Reached Destination (While)")

for i in range(0,100):
    robot_x += 0.1
    robot_y += 0.1
    print("Current Position", robot_x,robot_y)

    if(robot_x>4 and robot_y>4):
        print("Reached Destination (For)")
        break