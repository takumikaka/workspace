import turtle
import time
import threading

def drawLine(draw):
    turtle.pensize(5)
    turtle.pu()
    turtle.fd(3)

    if draw:
        turtle.pd()
    else:
        turtle.pu()

    turtle.fd(24)
    turtle.pu()
    turtle.fd(3)
    turtle.right(90)

def drawNum(num, color):

    turtle.colormode(255)
    turtle.color(eval(color))

    if num in [2, 3, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 3, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 6, 8]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.left(90)

    if num in [0, 4, 5, 6, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 2, 3, 5, 6, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        drawLine(True)
    else:
        drawLine(False)

    turtle.pu()
    turtle.left(180)
    turtle.fd(30)
    #turtle.left(90)
    #turtle.fd(-30)
    turtle.update()

def drawDate(date, color = '(0, 0, 0)'):
    for i in date:
        drawNum(eval(i), color)

def Tick_year():
    now = time.localtime()
    turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    turtle.fd(-300)

    drawDate(str(now.tm_year), '(255, 69, 0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('Y', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(86400, Tick_year)
    timer.start()

def Tick_month():
    now = time.localtime()
    #turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    #turtle.fd(-300)

    drawDate(str(now.tm_mon), '(0, 139, 0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('M', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(86400, Tick_month)
    timer.start()

def Tick_day():
    now = time.localtime()
    #turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    #turtle.fd(-300)

    drawDate(str(now.tm_mday), '(0, 0, 139)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('D', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(86400, Tick_day)
    timer.start()

def Tick_hour():
    now = time.localtime()
    #turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    #turtle.fd(-300)

    drawDate(str(now.tm_hour))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('H', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(1800, Tick_hour)
    timer.start()

def Tick_min():
    now = time.localtime()
    #turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    #turtle.fd(-300)

    drawDate(str(now.tm_min))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('M', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(30, Tick_min)
    timer.start()

def Tick_sec():
    now = time.localtime()
    turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    turtle.fd(-300)

    drawDate(str(now.tm_sec))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('S', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(0.5, Tick_sec)
    timer.start()

def Tick():
    now = time.localtime()
    turtle.reset()
    turtle.hideturtle()
    turtle.pu()
    turtle.fd(-300)

    drawDate(str(now.tm_year), '(255, 69, 0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('Y', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    drawDate(str(now.tm_mon), '(0, 139, 0)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('M', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    drawDate(str(now.tm_mday), '(0, 0, 139)')
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('D', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    drawDate(str(now.tm_hour))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('H', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    drawDate(str(now.tm_min))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('M', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    time_check = time.localtime()
    print(now.tm_sec, time_check.tm_sec)
    drawDate(str(now.tm_sec))
    turtle.fd(10)
    turtle.right(90)
    turtle.fd(30)
    turtle.write('S', align = 'center', font = ("Courier", 30, "bold"))
    turtle.left(180)
    turtle.fd(30)
    turtle.right(90)
    turtle.fd(30)

    timer = threading.Timer(0.1, Tick)
    timer.start()

def main():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.tracer(0)
    turtle.pu()
    turtle.fd(-300)
    Tick()
    #Tick_year()
    #Tick_month()
    #Tick_day()
    #Tick_hour()
    #Tick_min()
    #Tick_sec()
    turtle.done()

main()
