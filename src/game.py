import pygame
import requests

# version 0.3
# added colors selection by room

text_to_draw = ""

def draw_text(font_size=24):
    if text_to_draw == "":
        return
    font = pygame.font.Font(None, font_size)
    lines = text_to_draw.split("\n")
    line_height = font.get_linesize()

    # Calculate the y-coordinate of the center of the screen
    screen_center_y = screen.get_rect().center[1]

    # Calculate the starting y-coordinate for the text
    start_y = screen_center_y - (len(lines) * line_height) // 2

    # Loop through each line and render it to the screen
    for i, line in enumerate(lines):
        text_surface = font.render(line.strip(), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(screen.get_rect().centerx, start_y + i * line_height))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()


def check_color(probe):
    if probe == (0, 0, 0, 255):
        print("black")
    elif probe == (255, 0, 0, 255):
        print("red")
    else:
        print("else")


openai_api_key = "put-here-your-api-key"
openai_api_url = "https://api.openai.com/v1/chat/completions"


def generate_task(domain):
    global text_to_draw
    text_to_draw = "Proszę czekać, wymyślam pytanie..."
    draw_text()
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {openai_api_key}"}
    data = {"messages": [
        {"role": "system", "content": "Quiz generator"},
        {"role": "user",
         "content": f'Napisz jedno pytanie z dziedziny ${domain}, zrozumiałe dla ucznia liceum, z czterema możliwymi odpowiedziami.'}],
        "model": "gpt-3.5-turbo"}
    response = requests.post(openai_api_url, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"]


def generate_answer(task):
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {openai_api_key}"}
    data = {
        "messages": [
            {"role": "user",
             "content": f'Odpowiedź na pytanie ${task["question"]}, uwzględniająć ${task["answers"]["a"]},'
                        f' ${task["answers"]["b"]}, ${task["answers"]["c"]}, ${task["answers"]["d"]} w postaci A, B, C, D'}
        ],
        "model": "gpt-3.5-turbo"}
    response = requests.post(f"{openai_api_url}", headers=headers, json=data)
    answer = response.json()["choices"][0]["message"]["content"]
    print("Odpowiedź: ", answer)
    return answer


zik_room_executed = False
hr_room_executed = False
rob_room_executed = False
confid_room_executed = False
azure_room_executed = False
office_room_executed = False
zab_room_executed = False
helpd_room_executed = False
ceo_room_executed = False
bil_room_executed = False


def draw_image(image_filename, position):
    image = pygame.image.load(image_filename)
    screen.blit(image, position)


def zik_room_action():
    global zik_room_executed, text_to_draw

    draw_image("star_zik.png", (150, 120))

    if not zik_room_executed:
        text_to_draw = generate_task("monty python")
        zik_room_executed = True


def hr_room_action():
    global hr_room_executed, text_to_draw

    draw_image("star_hr.png", (150, 280))

    if not hr_room_executed:
        text_to_draw = generate_task("HR task")
        hr_room_executed = True


def rob_room_action():
    global rob_room_executed, text_to_draw

    draw_image("star_rob.png", (150, 410))

    if not rob_room_executed:
        text_to_draw = generate_task("Architecture")
        rob_room_executed = True


def confid_room_action():
    global confid_room_executed, text_to_draw

    draw_image("star_confid.png", (150, 545))

    if not confid_room_executed:
        text_to_draw = generate_task("spy job")
        confid_room_executed = True


def azure_room_action():
    global azure_room_executed, text_to_draw

    draw_image("star_azure.png", (450, 530))

    if not azure_room_executed:
        text_to_draw = generate_task("Azure cloud")
        azure_room_executed = True


def office_room_action():
    global office_room_executed, text_to_draw

    draw_image("star_office.png", (930, 468))

    if not office_room_executed:
        text_to_draw = generate_task("sekretarka")
        office_room_executed = True


def zab_room_action():
    global zab_room_executed, text_to_draw

    draw_image("star_zab.png", (1520, 530))

    if not zab_room_executed:
        text_to_draw = generate_task("żabka")
        zab_room_executed = True


def helpd_room_action():
    global helpd_room_executed, text_to_draw

    draw_image("star_helpd.png", (1160, 120))

    if not helpd_room_executed:
        text_to_draw = text_to_draw = generate_task("HELPDESK")
        helpd_room_executed = True


def ceo_room_action():
    global ceo_room_executed, text_to_draw

    draw_image("star_ceo.png", (660, 120))

    if not ceo_room_executed:
        text_to_draw = generate_task("management")
        ceo_room_executed = True


def bil_room_action():
    global bil_room_executed, text_to_draw

    draw_image("star_bil.png", (1680, 120))

    if not bil_room_executed:
        text_to_draw = generate_task("sport games")
        bil_room_executed = True


def black_color():
    print("wall is ahead")


# initialize pygame
pygame.init()

# define screen size
screen_width = 1880
screen_height = 750

# load background image
background_img = pygame.image.load("background.png")

# create screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# set caption for the window
pygame.display.set_caption("My Game")

# load frog image
frog_img = pygame.image.load("frog.png")
frog_width = 20
frog_height = 20

# get the black and white version of the background image
background_bw = pygame.Surface((background_img.get_width(), background_img.get_height()))
background_bw.blit(background_img, (0, 0))
pygame.transform.threshold(background_bw, background_bw, (0, 0, 0), (255, 255, 255), (0, 0, 0), 1, 0)

# set starting position for frog
frog_x = screen_width // 2
frog_y = screen_height // 2

# set the speed of the frog
frog_speed = 5

# create a clock to control the frame rate
clock = pygame.time.Clock()

# flag to check if red color is achieved
red_achieved = False

# game loop
running = True
while running:

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # get the keys that are currently pressed
    keys = pygame.key.get_pressed()

    # move the frog based on the keys pressed
    if keys[pygame.K_UP]:

        # check_color
        #        print((background_bw.get_at((frog_x, frog_y))))

        if background_bw.get_at((frog_x, frog_y - frog_speed)) != (0, 0, 0, 255):
            frog_y -= frog_speed
    if keys[pygame.K_DOWN]:
        if background_bw.get_at((frog_x, frog_y + frog_speed + frog_height)) != (0, 0, 0, 255):
            frog_y += frog_speed
    if keys[pygame.K_LEFT]:
        if background_bw.get_at((frog_x - frog_speed, frog_y)) != (0, 0, 0, 255):
            frog_x -= frog_speed
    if keys[pygame.K_RIGHT]:
        if background_bw.get_at((frog_x + frog_speed + frog_width, frog_y)) != (0, 0, 0, 255):
            frog_x += frog_speed

    # draw the background image on the screen
    screen.blit(background_img, (0, 0))

    # draw the frog image on the screen
    screen.blit(frog_img, (frog_x, frog_y))

    # check if the frog has reached the red color
    if background_img.get_at((frog_x, frog_y)) == (253, 243, 208, 255):
        zik_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (255, 174, 201, 255):
        hr_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (159, 206, 99, 255):
        rob_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (191, 191, 191, 255):
        confid_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (241, 205, 177, 255):
        azure_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (174, 171, 171, 255):
        office_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (245, 194, 66, 255):
        zab_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (224, 235, 246, 255):
        helpd_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (229, 240, 219, 255):
        ceo_room_action()
    elif background_img.get_at((frog_x, frog_y)) == (175, 185, 200, 255):
        bil_room_action()
    else:
        text_to_draw = ""

    draw_text()

    # update the display
    pygame.display.update()

    # set the frame rate
    clock.tick(60)

# quit pygame
pygame.quit()
