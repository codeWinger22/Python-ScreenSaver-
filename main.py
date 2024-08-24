import pygame, time,ctypes
import sys
from pygame.locals import *



#function to display setting 
def show_settings():     #to handle the command line argument 
    ctypes.windll.user32.MessageBoxW(0,"No Settings Available", "Settings",0x40|0x1)

#function to start full screen screensaver
def start_full_screen():
    screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    run_screensaver(screen,1366,768)
    


#function to start preview mode 
def start_preview(window_id):
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    screen = pygame.display.set_mode((800, 600))  # Use actual dimensions or handle
    run_screensaver(screen,800,600)

#function to run the screen saver   
def run_screensaver(screen,screenwidth,screenheight):
    pygame.init()
    logoSpeed = [1,1]  #this contains x and y values at which our logo will move in both horizontal and vertical directions respectively
#binding these 2 values will give us a diagonal screen across the screen 
    backgroundColor = 0,0,0 #rgb values 


#screen = pygame.display.set_mode((screenwidth,screenheight))
#now we wil load our image through pygame 
    image = pygame.image.load("logo.png")
    image = pygame.transform.scale(image,(100,100))  #new width and height of the image 
    logoRect = image.get_rect()    #rectangle around the image

#now we need a loop which moves around the screen and bouncing when it collides with the edges
    exitgame = True
#for that we need while loop
    while(exitgame):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitgame = False
    
        screen.fill(backgroundColor)
        screen.blit(image,logoRect)   #to show the image onto the screen 
    #now we will move our image, now image is inside the rectangle,if we move the rectangle the logo will automatically move 
        logoRect = logoRect.move(logoSpeed)   #now the rectangle will move across the screen in logoSpeed 

    #now we need to write condition which will check if the logo/image is colliding with the edges of the screen it should go back in reverse
        if logoRect.left<0 or logoRect.right>screenwidth:
            logoSpeed[0] = -logoSpeed[0]
        if logoRect.top<0 or logoRect.bottom>screenheight:
            logoSpeed[1] = -logoSpeed[1]
        pygame.display.flip() #refreshes the screen
    #at what speed it should refresh the screen 
    # we dont want it too fast
        time.sleep(10/1000)   #0.01 second 
    pygame.quit()

#screenwidth , screenheight = 800,600 #suitable for tv and desktop , we will adjust according to our screen








if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] == '/c':
        show_settings()
    elif sys.argv[1] == '/s':
        start_full_screen()
    elif sys.argv[1].startswith('/p'):
        try:
            window_id = int(sys.argv[1].split()[1])
            start_preview(window_id)
        except IndexError:
            show_settings()
        except ValueError:
            show_settings()
    else:
        start_full_screen()






#to make the code more customizable what you can do is 
#you can change the screen width and screen height , you can change the background color, you can change the angle at which the image is moving
#you can change the speed at which the image is moving 
#you can make the size of the logo bigger or smaller



