import json
import os, sys
os.environ['DISPLAY'] = ':0'
from graphics import *

MAX_X = 800
MAX_Y = 400
MAX_TASKS = 6
LINE_SPACE = int(MAX_Y/(MAX_TASKS + 0.5))
X_OFFSET = 20
Y_OFFSET = int(LINE_SPACE*6/5)
BOX_HEIGHT = int(LINE_SPACE*2/5)
ARROW_HEIGHT = int(LINE_SPACE*3/5)
ARROW_WIDTH = 5

def drawUpArrow(x,y,h,w,win):
    line = Line(Point(x,y), Point(x,y-h))
    slant_left = Line(Point(x,y-h),Point(x-w,y-h+w))
    slant_right = Line(Point(x,y-h),Point(x+w,y-h+w))
    line.draw(win)
    slant_left.draw(win)
    slant_right.draw(win)

def drawDownArrow(x,y,h,w,win):
    line = Line(Point(x,y), Point(x,y-h))
    slant_left = Line(Point(x,y),Point(x-w,y-w))
    slant_right = Line(Point(x,y),Point(x+w,y-w))
    line.draw(win)
    slant_left.draw(win)
    slant_right.draw(win)

def drawLine(start_x, start_y, end_x, end_y, win):
    line = Line(Point(start_x,start_y), Point(end_x,end_y))
    line.draw(win)

def drawColoredRectangle(x_one, y_one, x_two, y_two, color, win):
    r = Rectangle(Point(x_one,y_one), Point(x_two, y_two))
    r.setFill(color)
    r.draw(win)
    
    
def vis(in_name):

    json_file = in_name
    with open(json_file) as data_file:
        data = json.load(data_file)

    tasks = data["tasks"]
    max_t = data["max_t"]
    executions = data["executions"]

    UNIT_PER_TIME = int((MAX_X-2*X_OFFSET)/max_t)

    color=[color_rgb( 72,  12, 131), #purple
           color_rgb(131,  12,  72), #rose
           color_rgb( 12,  12, 131), #dark blue
           color_rgb( 12, 131,  12), #green
           color_rgb(131,  72,  12), #brown
           color_rgb( 12, 131, 131)] #teal

    win = GraphWin("Schedule", MAX_X, MAX_Y)
    
    # Draw a light gray rectangle to avoid excessive cropping
    r = Rectangle(Point(0, 0), Point(MAX_X, MAX_Y))
    r.setFill("gray99")
    r.draw(win)

    # Draw each execution
    for e in executions:
        drawColoredRectangle(X_OFFSET+(UNIT_PER_TIME*e['start']),
                Y_OFFSET+(e['taskNum']*LINE_SPACE),
                X_OFFSET+(UNIT_PER_TIME*e['end']),
                Y_OFFSET+(e['taskNum']*LINE_SPACE)-BOX_HEIGHT,
                color[e['taskNum']],
                win)

    # Draw line, arrival times, and deadlines for each task
    for task in tasks:
        # Draw line
        drawLine(X_OFFSET, 
                Y_OFFSET+(task["num"]*LINE_SPACE), 
                X_OFFSET+(max_t*UNIT_PER_TIME), 
                Y_OFFSET+(task["num"]*LINE_SPACE), 
                win)

        # Draw arrows
        t=task["phase"]
        while t <= max_t:
            # Draw job arrival
            drawUpArrow(X_OFFSET+(UNIT_PER_TIME*t),
                    Y_OFFSET+(task["num"]*LINE_SPACE), 
                    ARROW_HEIGHT, 
                    ARROW_WIDTH, 
                    win)

            # Check, then draw job deadline if within max_t
            if t+task["deadline"] <= max_t:
                drawDownArrow(X_OFFSET+(UNIT_PER_TIME*(t+task["deadline"])),
                        Y_OFFSET+(task["num"]*LINE_SPACE), 
                        ARROW_HEIGHT, 
                        ARROW_WIDTH, 
                        win)
            # Advance time to next job arrival
            if "period" in task:
                t=t+task["period"]
            else:
                break


    win.postscript(file = "schedule.ps")
    win.close()

