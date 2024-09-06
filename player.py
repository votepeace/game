STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Screen
screen=Screen() 
screen.register_shape(r"C:\Users\votepeace\Desktop\mario.gif")


from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(r"C:\Users\votepeace\Desktop\mario.gif") 
        self.shapesize(-5, -5, -5)
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        print('Player turtle created')
        
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    
    def move_down(self):
        self.backward(MOVE_DISTANCE)
    
        
    def player_reset(self):
        self.setpos(STARTING_POSITION)
        self.setheading(90)

    