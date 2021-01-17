import pygame
import random
import time

pygame.init()

vindusbredde = 1000 #100 pe, 10-80-10
vindushoyde = 500

# Farger (roed, grønn, blaa)
blaa  = (0,0,153)
graa  = (200,200,200)
hvit  = (255,255,255)
lilla = (102,0,204)
roed  = (255,51,51)

# Fonter
font1 = pygame.font.SysFont(None, 25)
font2 = pygame.font.Font("freesansbold.ttf", 30)
font3 = pygame.font.Font("freesansbold.ttf", 35)
font4 = pygame.font.Font("freesansbold.ttf", 90)
font5 = pygame.font.Font("freesansbold.ttf", 115)

vindu = pygame.display.set_mode((vindusbredde,vindushoyde))
pygame.display.set_caption("Paraball")

klokke = pygame.time.Clock()

bilde_bakgrunn = pygame.image.load("meadow.jpg")

bilde_ball = pygame.image.load("Tennisball.png")
ball_diameter = 32

knapper = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

def bakgrunn():
    vindu.blit(bilde_bakgrunn, (-100,-100))

def ball(x,y):
    vindu.blit(bilde_ball, (x,y))

def person():
    pygame.draw.circle(vindu, lilla, (80,303), 30)
    pygame.draw.polygon(vindu, lilla, ((70,330), (40,470), (70,400), (100,470), (85,370), (130,350), (83,355), (80,350), (130,350)))

def plate(plate_x, plate_y, plate_b, plate_h):
    pygame.draw.rect(vindu, roed, (plate_x, plate_y, plate_b, plate_h))

def score(antall):
    tekst_score = font1.render("Score: "+str(antall), True, blaa)
    vindu.blit(tekst_score, (10,10))

def tekster(tekst, font, farge):
    tekst_s = font.render(tekst, True, farge)
    return tekst_s, tekst_s.get_rect()

def knapp(msg,x,y,b,h,ic,ac,handling=None):
    mus = pygame.mouse.get_pos()
    klikk = pygame.mouse.get_pressed()

    if x+b > mus[0] > x and y+h > mus[1] > y:
        pygame.draw.rect(vindu, ac, (x,y,b,h))
        if klikk[0] == 1 and handling != None:

            if handling == "intro":
                global i
                i = 1
                return i

            if handling == "fart opp":
                global fart_opp
                if msg == "1":
                    fart_opp = -6.00
                if msg == "2":
                    fart_opp = -6.21
                if msg == "3":
                    fart_opp = -6.42
                if msg == "4":
                    fart_opp = -6.63
                if msg == "5":
                    fart_opp = -6.84
                if msg == "6":
                    fart_opp = -7.05
                if msg == "7":
                    fart_opp = -7.26
                if msg == "8":
                    fart_opp = -7.47
                if msg == "9":
                    fart_opp = -7.68
                if msg == "10":
                    fart_opp = -7.89
                if msg == "11":
                    fart_opp = -8.11
                if msg == "12":
                    fart_opp = -8.32
                if msg == "13":
                    fart_opp = -8.53
                if msg == "14":
                    fart_opp = -8.74
                if msg == "15":
                    fart_opp = -8.95
                if msg == "16":
                    fart_opp = -9.16
                if msg == "17":
                    fart_opp = -9.37
                if msg == "18":
                    fart_opp = -9.58
                if msg == "19":
                    fart_opp = -9.79
                if msg == "20":
                    fart_opp = -10.00

                return fart_opp

            if handling == "fart bort":
                global fart_bort
                if msg == "1":
                    fart_bort = 11.55
                if msg == "2":
                    fart_bort = 11.89
                if msg == "3":
                    fart_bort = 12.23
                if msg == "4":
                    fart_bort = 12.57
                if msg == "5":
                    fart_bort = 12.91
                if msg == "6":
                    fart_bort = 13.25
                if msg == "7":
                    fart_bort = 13.59
                if msg == "8":
                    fart_bort = 13.93
                if msg == "9":
                    fart_bort = 14.27
                if msg == "10":
                    fart_bort = 14.61
                if msg == "11":
                    fart_bort = 14.94
                if msg == "12":
                    fart_bort = 15.28
                if msg == "13":
                    fart_bort = 15.62
                if msg == "14":
                    fart_bort = 15.96
                if msg == "15":
                    fart_bort = 16.30
                if msg == "16":
                    fart_bort = 16.64
                if msg == "17":
                    fart_bort = 16.98
                if msg == "18":
                    fart_bort = 17.32
                if msg == "19":
                    fart_bort = 17.66
                if msg == "20":
                    fart_bort = 18.00

                return fart_bort

            if handling == "neste runde":
                if msg == "Spill igjen":
                    global spiller
                    spiller = True

                    global n
                    n = 1

                    return spiller

                if msg == "Exit":
                    pygame.quit()

    else:
        pygame.draw.rect(vindu, ic, (x,y,b,h))

    tekst_s, tekst_r = tekster(msg, font2, blaa)
    tekst_r.center = ((x + b/2), (y + h/2))
    vindu.blit(tekst_s, tekst_r)

def intro():
    spillintro = True

    global i
    i = 0

    while spillintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        vindu.fill(blaa)

        tekst_s, tekst_r = tekster("Paraball", font5, hvit)
        tekst_r.center = ((vindusbredde/2), (vindushoyde/3))
        vindu.blit(tekst_s, tekst_r)

        knapp("Spill",400,300,200,100,hvit,graa,"intro")

        pygame.display.update()
        klokke.tick(15)

        if i != 0:
            return i

def fart_oppover():
    fartoppover = True

    while fartoppover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        bakgrunn()

        ball(x,y)
        person()
        plate(plate_x, plate_y, plate_b, plate_h)
        score(poeng)

        tekst_s, tekst_r = tekster("Hastighetsnivå oppover:", font3, blaa)
        tekst_r.center = ((vindusbredde/2), (vindushoyde/7))
        vindu.blit(tekst_s, tekst_r)

        knapp_x = 255
        knapp_y = 125

        for i in range(len(knapper)):
            knapp(knapper[i],knapp_x,knapp_y,40,50,hvit,graa,"fart opp")
            knapp_x += 50
            if (i+1) % 10 == 0:
                knapp_x = 255
                knapp_y = 185

        if fart_opp != 0:
            return fart_opp

        pygame.display.update()
        klokke.tick(15)

def fart_bortover():
    fartbortover = True

    time.sleep(2)

    while fartbortover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        bakgrunn()

        ball(x,y)
        person()
        plate(plate_x, plate_y, plate_b, plate_h)
        score(poeng)

        tekst_s, tekst_r = tekster("Hastighetsnivå bortover:", font3, blaa)
        tekst_r.center = ((vindusbredde/2), (vindushoyde/7))
        vindu.blit(tekst_s, tekst_r)

        knapp_x = 255
        knapp_y = 125

        for i in range(len(knapper)):
            knapp(knapper[i],knapp_x,knapp_y,40,50,hvit,graa,"fart bort")
            knapp_x += 50
            if (i+1) % 10 == 0:
                knapp_x = 255
                knapp_y = 185

        if fart_bort != 0:
            return fart_bort

        pygame.display.update()
        klokke.tick(15)

def kast():

    global tid

    kast_ferdig = False

    while not kast_ferdig:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        global y
        global x

        bakgrunn()
        ball(x,y)
        person()
        plate(plate_x, plate_y, plate_b, plate_h)
        score(poeng)
        tid += 1

        if y + int(fart_opp * tid/25 + 1/2 * 7 * (tid/25)**2) < plate_y - ball_diameter:
            y += int(fart_opp * tid/25 + 1/2 * 7 * (tid/25)**2)    # s = v0 * t + 1/2 * a * t**2 med noen justeringer
            x += int(0.2 * fart_bort * tid/25)
        else:
            kast_ferdig = True

        pygame.display.update()
        klokke.tick(60)

    global spillrunde
    if plate_x < x and x + ball_diameter < plate_x + plate_b:     # Begge sidene av tennisballen må være innenfor streken for at man skal få poeng
        spillrunde = True
    else:
        spillrunde = False
    return spillrunde


def runde():
    global x
    x = 120
    global y
    y = 330
    global tid
    tid = 0

    global plate_h
    plate_h = 5
    global plate_b
    if poeng < 5:
        plate_b = 200
    elif poeng < 10:
        plate_b = random.randint(100,200)
    else:
        plate_b = random.randint(50,100)
    global plate_x
    plate_x = random.randrange(350,vindusbredde-plate_b)
    global plate_y
    plate_y = 470

    global fart_opp
    fart_opp = 0
    global fart_bort
    fart_bort = 0

    fart_oppover()
    fart_bortover()
    kast()

    return spillrunde

def neste_runde(poeng):
    nesterunde = True

    global n
    n = 0

    while nesterunde:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        vindu.fill(blaa)

        tekst_s, tekst_r = tekster("Du tapte", font4, hvit)
        tekst_r.center = ((vindusbredde/2), (vindushoyde/5))
        vindu.blit(tekst_s, tekst_r)

        tekst_s, tekst_r = tekster("Score: "+str(poeng), font4, hvit)
        tekst_r.center = ((vindusbredde/2), (2*vindushoyde/5))
        vindu.blit(tekst_s, tekst_r)

        knapp("Spill igjen", 100,300,200,100,hvit,graa,"neste runde")
        knapp("Exit",700,300,200,100,hvit,graa,"neste runde")

        pygame.display.update()
        klokke.tick(15)

        if n != 0:
            return spiller

def spill():
    intro()

    spiller = True

    while spiller:
        global poeng
        poeng = 0

        global spillrunde
        spillrunde = True

        while spillrunde:
            runde()
            if spillrunde:
                poeng += 1

        neste_runde(poeng)

spill()