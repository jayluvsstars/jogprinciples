import pygame, random

# Set display surface
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.se

FPS = 20
clock = pygame.time.Clock()

# Set game values
SNAKE_SIZE = 20
# TODO: create a head_x variable and assign it a value of WINDOW_WIDTH // 2
# TODO: repeat for head_y and assign it a value of WINDOW_HEIGHT // 2 + 100
snake_dx = 0
snake_dy = 0
score = 0

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
DARKGREEN= (10, 50, 10)
DARKRED = (150, 0, 0)

font = pygame.font.SysFont('gabriola', 48)

def create_text_and_rect(text, color, background_color, **locations):
    text = font.render(text, True, color, background_color)
    rect = text.get_rect()
    for location in locations.keys():
        if location == "center":
            rect.center = locations[location]
        if location == "topleft"
            rect.topleft = locations[location]
    return text, rect

title_text, title_rect = create_text_and_rect("~~Snake~~", GREEN, DARKRED,
                                             center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

score_text = font.render("Score: " + str(score), True, GREEN, DARKRED)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAMEOVER", True, RED, DARKGREEN)
game_over_rect = game_over_text.get_rect("Press any key to play again")
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

pick_up_sound = pygame.mixer.Sound("pick_up_sound.wav")

apple_coord = (500, 500,SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)
body_coords =

# The main game loop
running = True
is_paused = False

ef move_snake(event):
    global snake_dx, snake_dy
    if event.type == pygame.KEYDOWN:
        key = event.key
        if event.type == pygame.K_LEFT
            snake_dx = -1 * SNAKE_SIZE and snake_dy = 0
        if evemt.type == pygame.K_RIGHT
            snake_dx SNAKE_SIZE and snake_dy = 0
        if event.type == pygame.K_UP
            snake_dx = 0 * snake_dy = -1 * SNAKE_SIZE
        if event.type == pygame.K_DOWN
            snake_dx = 0 * snake_dy = SNAKE_SIZE


def check_quit(event):
    global running
    if event.type == pygame.QUIT = false

def check_events():
    loop = pygame.event.get()
        if event == check_quit(event)
        if other == move_snake(event)



def handle_snake():
    global body_coords
    global head_x
    global head_y
    global head_coord
    global snake_dx, snake_dy
    global = body_coords.insert(0, head_coord)
    global body_coords.pop()
    # TODO: add snake_dx to head_x
    # TODO: add snake_dy to head_y
    # TODO: set head_coord to (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)

    def reset_game_after_game_over(event):
        global is_paused, score, head_x, head_y, head_coord, body_coords, snake_dx, snake_dy
        # TODO: if event.type is equal to pygame.KEYDOWN
        # TODO: set score to 0
        # TODO: set head_x to WINDOW_WIDTH // 2
        # TODO: set head_y to WINDOW_HEIGHT // 2 + 100
        # TODO: set head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: set body_coords to an empty list
        # TODO: set snake_dx to 0
        # TODO: set snake_dy to 0
        # TODO: set is_paused to False
        pass  # TODO: remove this when done.

    def check_end_game_after_game_over(event):
        global is_paused
        global running
        # TODO: if event.type is equal to pygame.QUIT
        # TODO: set is_paused to False
        # TODO: set running to False
        pass  # TODO: remove this when done.

    def check_game_over():
        global head_rect
        global head_coord
        global body_coords
        global running
        global is_paused
        # TODO: if head_rect.left is negative or head_rect.right is greater than WINDOW_WIDTH or head_rect.top is negative or head_rect.bottom is greater than WINDOW_HEIGHT
        # or head_coord in body_coords
        # TODO: then do the following
        # TODO: call display_surface.blit(game_over_text, game_over_rect)
        # TODO: call display_surface.blit(continue_text, continue_rect)
        # TODO: call pygame.display.update()
        # TODO: set is_paused to True
        # TODO: while is_paused
        # TODO: for event in pygame.event.get()
        # TODO: call reset_game_after_game_over(event)
        # TODO: call check_end_game_after_game_over(event)

    def check_collisions():
        global score, apple_x, apple_y, apple_coord, body_coords
        # TODO: if head_rect.colliderect(apple_rect)
        # TODO: add 1 to the score
        # TODO: call pick_up_sound.play()
        # TODO: set apple_x to random.randint(0, WINDOW_WIDTH - SNAKE_SIZE)
        # TODO: set apple_y to random.randint(0, WINDOW_HEIGHT - SNAKE_SIZE)
        # TODO: set apple_coord to (apple_x, apple_y, SNAKE_SIZE, SNAKE_SIZE)
        # TODO: call body_coords.append(head_coord)
        pass  # TODO: remove this pass when done.


def blit_hud():
    # TODO: call display_surface.blit(title_text, title_rect)
    # TODO: call display_surface.blit(score_text, score_rect)
    pass  # TODO: remove this pass when done.


def blit_assets():
    global head_rect, apple_rect
    # TODO: for body in body_coords:
    # TODO: call pygame.draw.rect(display_surface, DARKGREEN, body)
    # TODO: set head_rect to pygame.draw.rect(display_surface, GREEN, head_coord)
    # TODO: set apple_rect to pygame.draw.rect(display_surface, RED, apple_coord)
    pass  # TODO: remove this pass when done.


def update_display_and_tick_clock():
    # TODO: call pygame.display.update()
    # TODO: call clock.tick(FPS)
    pass  # TODO: remove this pass when done.


while running:
    # Check pygame events
    check_events()

    # handle growing and manipulating the snake
    handle_snake()

    # Check for game over
    check_game_over()

    # Check for collisions
    check_collisions()

    # Update HUD
    # TODO: set score_text to font.render("Score: " + str(score), True, GREEN, DARKRED)


    display_surface.fill(WHITE)

    # Blit HUD
    blit_hud()

    # Blit assets
    blit_assets()

    # Update display and tick clock
    update_display_and_tick_clock()

# End the game
pygame.quit()