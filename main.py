import pygame, sys, random

def pomeraj_x():
    global igrac, moving_auto_right, moving_auto_left
    if moving_auto_right:
        igrac.x += 2
        if igrac.x >= sirina - igrac.width:
            moving_auto_right = False
    elif moving_auto_left:
        igrac.x -= 2
        if igrac.x <= 0:
            moving_auto_left = False

pygame.init()

clk = pygame.time.Clock()

sirina, duzina = 680, 600

def kake():
    for poop in poop_list:
        pygame.draw.rect(prozor, pygame.Color("chocolate"), poop)
        poop.y += 0.5

def protivnici():
    for protivnik in lista_protivnika:
        pygame.draw.rect(prozor, pygame.Color("Black"), protivnik)
        protivnik.y += 5
        if protivnik.y >= 430:
            protivnik.x = random.randint(0, 680)
            protivnik.y = 1

level = 0
hearts = 5
fps = 60
points = 0
brzina_y = 0
gravitacija = 0.5
skok_sila = -10
brojac_klikova = 0

def dodirni_se():
    global points
    for kaka in poop_list:
        if igrac.colliderect(kaka):
            kaka.x = random.randint(10, 670)
            kaka.y = random.randint(10, 670)
            points += 1

def dodirni_se_sa_protivnikom():
    global hearts
    for protivnik in lista_protivnika:
        if igrac.colliderect(protivnik):
            protivnik.x = random.randint(10, 670)
            protivnik.y = random.randint(10, 670)
            hearts -= 1

def dodir_sa_blokadom():
    if igrac.colliderect(barijera):
        pygame.quit()

def izgubio_si():
    if hearts < 1:
        pygame.quit()

prozor = pygame.display.set_mode((sirina, duzina))
pygame.display.set_caption("NJU FOLDER")

boja = (179, 217, 126)
boja2 = (126, 217, 147)
boja3 = (106, 247, 182)
boja4 = (9, 235, 193)

font_level = pygame.font.SysFont(None, 50)
font_heart = pygame.font.SysFont(None, 50)
font_fps = pygame.font.SysFont(None, 30)
font_point = pygame.font.SysFont(None, 30)

igracX, igracY, igracSirina, igracDuzina = 100, 100, 30, 30
igrac = pygame.Rect(igracX, igracY, igracSirina, igracDuzina)
moving_auto_right = False
moving_auto_left = False

def povecaj_poene():
    global level, brojac_klikova
    if brojac_klikova % 5 == 0 and brojac_klikova != 0:
        level += 1
        brojac_klikova = 0  # Reset the counter after level increment

def pravi_protivnika():
    x_protivnik = random.randint(10, 670)
    y_protivnik = random.randint(10, 100)
    return pygame.Rect(x_protivnik, y_protivnik, 25, 25)

lista_protivnika = [pravi_protivnika() for _ in range(4)]

def go_back_poop():
    for i in poop_list:
        if i.y >= 430:
            i.x = random.randint(0, 680)
            i.y = 1  

def create_random_rect():
    x = random.randint(0, 600)
    y = random.randint(0, 300)
    return pygame.Rect(x, y, 20, 20)

poop_list = [create_random_rect() for _ in range(8)]

barijera = pygame.Rect(1, 480, 680, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                brzina_y = skok_sila
                brojac_klikova += 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_auto_left = True
                moving_auto_right = False
            if event.key == pygame.K_RIGHT:
                moving_auto_right = True
                moving_auto_left = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_auto_left = False
            if event.key == pygame.K_RIGHT:
                moving_auto_right = False

    brzina_y += gravitacija
    igrac.y += brzina_y

    if igrac.y > duzina - igracDuzina:
        igrac.y = duzina - igracDuzina
        brzina_y = 0

    prozor.fill(boja)
    pygame.draw.rect(prozor, boja2, (1, 490, 680, 110))
    pygame.draw.rect(prozor, boja3, (1, 490, 200, 110))
    pygame.draw.rect(prozor, boja4, (480, 490, 200, 110))

    text_heart = font_heart.render(f"Hearts: {hearts}", True, pygame.Color("Black"))
    text_level = font_level.render(f"Level: {level}", True, pygame.Color("Black"))
    text_fps = font_fps.render(f"fps: {fps}", True, pygame.Color("Red"))
    text_point = font_point.render(f"Points: {points}", True, pygame.Color("Red"))

    prozor.blit(text_heart, (500, 530))
    prozor.blit(text_level, (20, 530))
    prozor.blit(text_fps, (290, 510))
    prozor.blit(text_point, (290, 550))

    pygame.draw.rect(prozor, pygame.Color("gold"), igrac)
    pygame.draw.rect(prozor, pygame.Color("tomato"), barijera)
    pomeraj_x()
    kake()
    go_back_poop()
    protivnici()
    dodirni_se()
    dodirni_se_sa_protivnikom()
    dodir_sa_blokadom()
    izgubio_si()
    povecaj_poene()

    pygame.display.update()
    clk.tick(fps)

pygame.quit()
sys.exit()