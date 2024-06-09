import random
import pygame
import sys
from moviepy.editor import VideoFileClip

def play_intro(video_path):
    video = VideoFileClip(video_path)

    desired_width = 1000
    desired_height = 720  
    video = video.resize((desired_width, desired_height))

    video.preview()

def initialize_pygame():
    pygame.init()

def draw_goal_post():
    screen.fill(WHITE)
    screen.blit(goal_post, (0, 0))

video_path = 'ucl_intro.mp4'

play_intro(video_path)

def ask_to_play():
    while True:
        play = input("Do you want to play the Penalty Shootout Game? (y/n): ").lower()
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")

def show_end_message(screen, message):
    font = pygame.font.Font(None, 40)
    screen.fill((0, 0, 0)) 
    text = font.render(message, True, (255, 255, 255))  
    text_rect = text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

def play_game():
    initialize_pygame()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Penalty Shootout Game")

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    goal_post = pygame.image.load('goalpost.webp')
    ball = pygame.image.load('ucl_ball.webp')
    ball = pygame.transform.scale(ball, (50, 50))
    ball_rect = ball.get_rect()

    goalkeeper = pygame.image.load('goalkeeper4.png')
    goalkeeper = pygame.transform.scale(goalkeeper, (150, 200))
    goalkeeper_rect = goalkeeper.get_rect()

    goal_positions = {
        'q': (150, 250),  
        'e': (670, 250),  
        'a': (150, 450),  
        'd': (650, 450),  
        'w': (400, 300)   
    }

    options = list(goal_positions.keys())

    player_score = 0
    ai_score = 0
    rounds = 5

    font = pygame.font.Font(None, 36)

    def draw_goal_post():
        screen.fill(WHITE)
        screen.blit(goal_post, (0, 0))

    def place_ball_center():
        ball_rect.center = (WIDTH // 2, HEIGHT - 50)
        screen.blit(ball, ball_rect)
        pygame.display.flip()

    def place_goalkeeper_center():
        goalkeeper_rect.center = (WIDTH // 2, 400)
        screen.blit(goalkeeper, goalkeeper_rect)
        pygame.display.flip()

    def rotate_goalkeeper(direction):
        angles = {
            'q': 45, 
            'e': -45,  
            'a': 90,  
            'd': -90,  
            'w': 0   
        }
        if direction in angles:
            return pygame.transform.rotate(goalkeeper, angles[direction])
        return goalkeeper

    def move_ball_and_goalkeeper(ball_position, keeper_position):
        ball_target_pos = goal_positions[ball_position]
        keeper_rotated = rotate_goalkeeper(keeper_position) if keeper_position != 'w' else goalkeeper
        keeper_target_pos = goal_positions[keeper_position]

        if keeper_position == 'e':  
            keeper_target_pos = (keeper_target_pos[0] - 50, keeper_target_pos[1] - 5)
        elif keeper_position == 'd':  
            keeper_target_pos = (keeper_target_pos[0], keeper_target_pos[1] + 20)

        draw_goal_post()

        ball_rect.center = ball_target_pos
        goalkeeper_rect.center = keeper_target_pos
        screen.blit(ball, ball_rect)
        screen.blit(keeper_rotated, goalkeeper_rect)
        pygame.display.flip()
        pygame.time.wait(500)

    def draw_scoreboard():
        text_player = font.render(f"Real Madrid: {player_score}", True, WHITE)
        text_ai = font.render(f"Chelsea: {ai_score}", True, WHITE)
        screen.blit(text_player, (20, 20))
        screen.blit(text_ai, (WIDTH - 140, 20))
        pygame.display.flip()

    print("Welcome to the Penalty Shootout Game!")

    round_number = 1
    while True:
        print("Round", round_number)
        draw_goal_post()
        place_ball_center()
        place_goalkeeper_center()

        pygame.display.flip()
        draw_scoreboard()

        print("Your turn to shoot!")
        player_choice = None
        while player_choice is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_e, pygame.K_a, pygame.K_d, pygame.K_w]:
                        player_choice = chr(event.key)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        keeper_choice = random.choice(options)
        print("Goalkeeper dives to:", keeper_choice)

        move_ball_and_goalkeeper(player_choice, keeper_choice)

        if player_choice == keeper_choice:
            print("Saved by the goalkeeper!")
        else:
            print("Goal!")
            player_score += 1

        pygame.time.wait(1000)
        draw_goal_post()
        place_ball_center()
        place_goalkeeper_center()

        pygame.display.flip()
        draw_scoreboard()

        pygame.time.wait(1000)

        print("Your turn to save!")
        ai_choice = random.choice(options)

        player_dive = None
        while player_dive is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_q, pygame.K_e, pygame.K_a, pygame.K_d, pygame.K_w]:
                        player_dive = chr(event.key)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        print("AI shoots to:", ai_choice)

        move_ball_and_goalkeeper(ai_choice, player_dive)

        if player_dive == ai_choice:
            print("You saved the shot!")
        else:
            print("AI scores!")
            ai_score += 1

        pygame.time.wait(1000)
        draw_goal_post()
        place_ball_center()
        place_goalkeeper_center()

        pygame.display.flip()
        draw_scoreboard()

        pygame.time.wait(1000)

        if round_number >= 5:
            if player_score != ai_score:
                break

        round_number += 1

    print("Penalty shootout complete!")
    print(f"Your final score: {player_score} out of {round_number}")
    print(f"AI final score: {ai_score} out of {round_number}")

    if player_score > ai_score:
        print("AYY, NOT BAD, you win!")
        def play_intro(video_path):
            video = VideoFileClip(video_path)

            desired_width = 1000
            desired_height = 720  
            video = video.resize((desired_width, desired_height))

            video.preview()

        def draw_goal_post():
            screen.fill(WHITE)
            screen.blit(goal_post, (0, 0))

        video_path = 'madrid_ucl.mp4'

        play_intro(video_path)
        show_end_message(screen, "Congratulations! You won! Do you want to play again?")
    else:
        print("You lose, better luck next time.")
        def play_intro(video_path):
            video = VideoFileClip(video_path)

            desired_width = 1000
            desired_height = 720  
            video = video.resize((desired_width, desired_height))

            video.preview()

        def draw_goal_post():
            screen.fill(WHITE)
            screen.blit(goal_post, (0, 0))

        video_path = 'chelsea_ucl.mp4'
        play_intro(video_path)
        show_end_message(screen, "You lost! Do you want to play again?")

while True:
    play_game()
    if not ask_to_play():
        initialize_pygame() 
        screen = pygame.display.set_mode((800, 600))
        show_end_message(screen, "Thanks for playing! Hope you had fun!")

        print("See ya bro, hope you had fun, bye bye!")
        break
