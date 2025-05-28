import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.title('Welcome To The Snake Game!!')
screen.setup(600,600)
screen.tracer(0)

# segments = []
#
# for n in range(0,3):
#     turtle = Turtle('square')
#     turtle.color('white')
#     turtle.penup()
#     turtlex = int(n*-20)
#     turtle.setpos(turtlex,0)
#     # turtle.goto(turtlex, 0)
#     segments.append(turtle)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()
        score.updatescore()
        # snake.update_snake()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    # for seg_num in range(len(segments) - 1, 0 , -1):
    #     new_y = segments[seg_num - 1].ycor()
    #     new_x = segments[seg_num - 1].xcor()
    #     segments[seg_num].goto(new_x,new_y)
    #
    # segments[0].right(20)


screen.exitonclick()