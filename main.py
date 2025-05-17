from turtle import Screen
import time
import tkinter as tk
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
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

is_game_on = True

def custom_game_over_popup():
    global is_game_on

    popup = tk.Toplevel()
    popup.title("Game Over")
    popup.config(bg="#222222")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Game Over!\nPlay Again?", fg="white", bg="#222222",
                     font=("Courier", 18, "bold"))
    label.pack(pady=20)

    button_frame = tk.Frame(popup, bg="#222222")
    button_frame.pack()

    def yes():
        popup.destroy()
        snake.reset()
        score.reset()
        food.refresh()
        global is_game_on
        is_game_on = True
        game_loop()  # Restart game loop

    def no():
        popup.destroy()
        with open("data.txt", mode="w") as file:
            file.write(str(score.high_score))
        global is_game_on
        is_game_on = False
        screen.bye()  # Close the turtle window
        
    # Handle closing window with X button as "No"
    popup.protocol("WM_DELETE_WINDOW", no)

    yes_button = tk.Button(button_frame, text="Yes", command=yes, width=8,
                           bg="#4CAF50", fg="white", font=("Courier", 14, "bold"), relief="raised")
    yes_button.grid(row=0, column=0, padx=10)

    no_button = tk.Button(button_frame, text="No", command=no, width=8,
                          bg="#F44336", fg="white", font=("Courier", 14, "bold"), relief="raised")
    no_button.grid(row=0, column=1, padx=10)

    popup.attributes('-topmost', True)
    popup.update_idletasks()

    # Center the popup window
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f'{width}x{height}+{x}+{y}')

    popup.mainloop()

def game_loop():
    global is_game_on
    is_game_on = True
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
            is_game_on = False
            custom_game_over_popup()

        # Collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 7:
                is_game_on = False
                custom_game_over_popup()

game_loop()
