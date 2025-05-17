from turtle import Screen
import time
from food import Food
from Snake import Snake
from scoreboard import Score

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
score = Score()

# Controls
screen.listen()
# Arrow keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# WASD keys
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

# Game loop control flag
is_game_on = True

# Graceful exit handler
def stop_game():
    global is_game_on
    is_game_on = False

# Bind window close event
screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", stop_game)

# Game loop
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Collision with wall
    if (
        snake.head.xcor() < -290 or snake.head.xcor() > 290 or
        snake.head.ycor() < -290 or snake.head.ycor() > 290
    ):
        score.reset()
        with open("data.txt", mode="w") as file:
            file.write(str(score.high_score))
        snake.reset()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 7:
            score.reset()
            with open("data.txt", mode="w") as file:
                file.write(str(score.high_score))
            snake.reset()

# Clean exit
screen.bye()
