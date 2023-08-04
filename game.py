import pygame
import random
import time
import tkinter as tk
from tkinter import messagebox
from sys import exit

# --- Game Initialization ---

pygame.init()

screen_width = 800
screen_height = 468
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch Falling Balls')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

# --- Load Images ---

sky_img = pygame.image.load("graphics/sky.png").convert_alpha()
ground_img = pygame.image.load("graphics/ground.png").convert_alpha()
basket_img = pygame.image.load("graphics/basket.png").convert_alpha()

basket_height = 50
basket_width = 80
basket_img = pygame.transform.scale(basket_img, (basket_width, basket_height))

basket_rect = pygame.Rect((screen_width - basket_width) // 2, screen_height - basket_height - 10, basket_width, basket_height)

ball_images = [pygame.image.load(f"graphics/ball_{i}.png").convert_alpha() for i in range(1, 10)]
ball_images = [pygame.transform.scale(ball_img, (30, 30)) for ball_img in ball_images]

# --- Game Variables ---

score = 0
balls = []

# --- Game Functions ---

def check_collision(ball_rect):
    return basket_rect.colliderect(ball_rect)

def get_top_scores():
    try:
        with open("high_scores.txt", "r") as file:
            top_scores = [int(line.strip()) for line in file.readlines()]
            return sorted(top_scores, reverse=True)[:5]
    except FileNotFoundError:
        return []

def save_top_scores(top_scores):
    with open("high_scores.txt", "w") as file:
        for score in top_scores:
            file.write(str(score) + "\n")

def show_game_over_message():
    root = tk.Tk()
    root.withdraw()

    message = f"Game Over! Your Score: {score}"
    top_scores = get_top_scores()

    if score > 0 and (len(top_scores) < 5 or score > min(top_scores)):
        top_scores.append(score)
        top_scores = sorted(top_scores, reverse=True)[:5]
        save_top_scores(top_scores)
        if score == top_scores[0]:
            message += "\n    NEW HIGH SCORE!\n"

    top_scores_text = "\nTop Scores:\n"
    for i, top_score in enumerate(top_scores, start=1):
        top_scores_text += f"{i}. {top_score}\n"
    message += top_scores_text

    messagebox.showinfo("Catch Falling Balls", message)

    if messagebox.askyesno("Catch Falling Balls", "Try Again?"):
        restart_game()
    else:
        pygame.quit()
        exit()

def restart_game():
    global score, balls, start_time
    score = 0
    balls = []
    start_time = time.time()

# --- Main Game Loop ---

start_time = time.time()
total_time = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move the basket left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.move_ip(-15, 0)
    if keys[pygame.K_RIGHT] and basket_rect.right < screen_width:
        basket_rect.move_ip(15, 0)

    # Generate new ball
    if random.random() < 0.02:
        ball_rect = pygame.Rect(random.randint(0, screen_width - 30), -30, 30, 30)
        ball_speed = random.randint(1, 5)
        ball_img = random.choice(ball_images)
        balls.append((ball_rect, ball_speed, ball_img))

    # Update ball positions
    for i in range(len(balls)):
        ball_rect, ball_speed, ball_img = balls[i]
        ball_rect.move_ip(0, ball_speed)
        balls[i] = (ball_rect, ball_speed, ball_img)

    # Check for collisions and update score
    for ball in balls[:]:
        ball_rect, _, _ = ball
        if check_collision(ball_rect):
            score += 1
            balls.remove(ball)

    # Calculate remaining time
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, total_time - elapsed_time)

    # Draw the background

    screen.blit(sky_img, (0, 0))
    screen.blit(ground_img, (0, 300))

    # Draw the falling balls
    for ball in balls:
        ball_rect, _, ball_img = ball
        screen.blit(ball_img, ball_rect)

    # Draw the basket
    screen.blit(basket_img, basket_rect.topleft)

    # Display the score and remaining time on the top of the screen
    score_text = font.render(f"Score: {score}", True, 'black')
    time_text = font.render(f"Time: {remaining_time}", True, 'black')
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (screen_width - 90, 10))

    pygame.display.update()
    clock.tick(60)

    # Check if time is up
    if elapsed_time >= total_time:
        show_game_over_message()
