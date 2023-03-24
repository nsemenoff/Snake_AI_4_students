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
            seg.reset()
#        self.snake.clear()
        self.snake = []
        for i in range(3):
            if i>0:  self.snake.append(self.make_segment('gray','turtle'))
            else:    self.snake.append(self.make_segment('black','turtle'))
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
        if h == 0:
            # move right
            status = [20*self.N - x,
                      20*self.N - y,
                      x - 20*self.N,
                      self.food.xcor() - x,
                      self.food.ycor() - y,
                      6]
        elif h == 90:
            # move up
            status = [20*self.N - y,
                      y - 20*self.N,
                      20*self.N - y,
                      self.food.xcor() - x,
                      self.food.ycor() - y,
                      6]
        elif h == 180:
            # move up
            status = [20*self.N - x,
                      20*self.N - y,
                      x - 20*self.N,
                      self.food.xcor() - x,
                      self.food.ycor() - y,
                      6]
        else:
            # move down
            status = [20*self.N - x,
                      20*self.N - y,
                      x - 20*self.N,
                      self.food.xcor() - x,
                      self.food.ycor() - y,
                      6]
        return status
