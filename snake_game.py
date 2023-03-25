import turtle as t
from random import randrange
import numpy as np
import time

class Snake:

###########################################################################
    def __init__(self, N):
        self.N = N
        self.screen = t.Screen()
        self.screen.bgcolor('orange')
        self.screen.setup(20*N+10,20*N+10)
        self.screen.tracer(0)
        self.step = 20
        self.loop = N*N/10
        self.snake = []
        brd = t.Turtle()
        brd.hideturtle()
        brd.penup()
        brd.goto(-20*N-10, -10*N-10)
        brd.pendown()
        for i in range(4):
            brd.forward(20*N+20)
            brd.right(90)
        self.food = self.make_segment('yellow','circle')
        self.make_snake()

###########################################################################
    def make_segment(self, color, shape):
            snake_segment = t.Turtle()
            snake_segment.shape(shape)
            snake_segment.penup()
            snake_segment.color(color)
            snake_segment.penup()
            snake_segment.goto(0,0)
            return snake_segment

###########################################################################
    def make_snake(self):
        for seg in self.snake:
#            self.screen.remove(seg)
            seg.clear()
            seg.reset()
        for element in self.screen.turtles():
            element.reset()
            element.clear()
#            self.screen.remove(element)
#        self.screen.remove(food)
#        self.screen.clear()
#        del(self.snake)
#        self.food.clear()
#        del(self.food)

        brd = t.Turtle()
        brd.hideturtle()
        brd.penup()
        brd.goto(-10*self.N-10, -10*self.N-10)
        brd.pendown()
        for i in range(4):
            brd.forward(20*self.N+20)
            brd.left(90)

        self.snake = []
        for i in range(3):
            if i>0:  self.snake.append(self.make_segment('gray','turtle'))
            else:    self.snake.append(self.make_segment('black','turtle'))
        self.food = self.make_segment('yellow','circle')
        self.move_food()

###########################################################################
    def move_food(self):
        N = self.N
        self.food.goto(randrange(-10*N, 10*N, self.step), randrange(-10*N, 10*N, self.step))

###########################################################################
    def move(self, control):
        q = np.argmax(control)
        if q == 0: # turn left
            self.snake[0].setheading( self.snake[0].heading() - 90 )
        elif q == 2: # turn right
            self.snake[0].setheading( self.snake[0].heading() + 90 )

        for i in range( len(self.snake)-1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x, y)
            self.snake[i].setheading( self. snake[i-1].heading() )
        self.snake[0].forward(self.step)

        x = self.snake[0].xcor()
        y = self.snake[0].ycor()
        brd_size = self.N*self.step/2
        if x>brd_size or x<-brd_size or y>brd_size or y<-brd_size:
            self.make_snake()
            return 1 # status = ERROR

        if self.snake[0].distance(self.food) < self.step:
            self.move_food()
            self.snake.append(self.make_segment('gray','turtle'))
            return 2 # status = FOOD

        self.screen.update()
        time.sleep(0.1)
        self.loop -= 1
        if self.loop < 1:
            self.loop = 100;
            self.make_snake()
            return 1

        return 0

    ###########################################################################
    def read_status(self):
        h = self.snake[0].heading()
        x = self.snake[0].xcor()
        y = self.snake[0].ycor()
        dist_x = 20*self.N - x
        dist_y = 20*self.N - y
        tail = self.snake[len(self.snake)-1]
        dist_tail = self.snake[0].distance(tail)
        dist_apple_x = self.food.xcor() - x
        dist_apple_y = self.food.ycor() - y
        h = np.abs( dist_apple_x ) + np.abs( dist_apple_y )
        if h == 0:
            # move right
            status = [dist_x,
                      dist_y,
                      dist_tail,
                      dist_apple_x,
                      dist_apple_y,
                      h]
        elif h == 90:
            # move up
            status = [dist_x,
                      dist_y,
                      dist_tail,
                      dist_apple_x,
                      dist_apple_y,
                      h]
        elif h == 180:
            # move up
            status = [dist_x,
                      dist_y,
                      dist_tail,
                      dist_apple_x,
                      dist_apple_y,
                      h]
        else:
            # move down
            status = [dist_x,
                      dist_y,
                      dist_tail,
                      dist_apple_x,
                      dist_apple_y,
                      h]
        return status
