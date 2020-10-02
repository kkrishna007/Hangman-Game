import pygame,math,random

pygame.init()
WIDTH,HEIGHT=1000,500
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game!")

#load images
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#button variables
RADIUS=20
GAP=15
letters=[]
A=65
startx=round((WIDTH-(RADIUS*2+GAP)*13)/2)
starty=400
for i in range(26):
    x=startx+GAP*2+((RADIUS*2+GAP)*(i%13))
    y=starty+((i//13)*(GAP+RADIUS*2))
    letters.append([x,y,chr(A+i),True])

#game variables
hangman_status=0
words=["PYGAME","DOCUMENTATION","DEVELOPER","HANGMAN"]
word=random.choice(words)
guessed=[]

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)

#fonts
LETTER_FONT = pygame.font.SysFont("comicsans",40)
WORD_FONT = pygame.font.SysFont("comicsans",60)
TITLE_FONT= pygame.font.SysFont("comicsans",80)

#setup game loop
FPS=60
clock=pygame.time.Clock()
run=True

def draw():
    win.fill(WHITE)

    #draw title
    text=TITLE_FONT.render("HANGMAN GAME",1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,20))

    #draw word
    display_word=" "
    for letter in word:
        if letter in guessed:
            display_word+=letter+" "
        else:
            display_word+="_ "
    text=WORD_FONT.render(display_word,1,BLACK)
    win.blit(text,(400,200))

    #draw buttons
    for letter in letters:
        x,y,ltr,visible=letter
        if visible:
            pygame.draw.circle(win,BLACK,(x,y),RADIUS,3)
            text=LETTER_FONT.render(ltr,1,BLACK)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
        
    win.blit(images[hangman_status],(100,100))
    pygame.display.update()

def display_message(msg):
    pygame.time.delay(1500)
    win.fill(WHITE)
    text=WORD_FONT.render(msg,1,BLACK)
    win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2))
    pygame.display.update()
    pygame.time.delay(3000)


while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            mx,my=pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis=math.sqrt((x-mx)**2+(y-my)**2)
                    if dis < RADIUS:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
                            
    draw()
    
    won=True                       
    for letter in word:
        if letter not in guessed:
            won=False
            break
        
    if won:
        display_message("You Won!!")
        break
    
    if hangman_status==6:
        display_message("You Lost!!")
        break


pygame.quit()
