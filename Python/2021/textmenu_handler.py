import pygame


class MenuPygame:

    image = pygame.Surface((50,50),pygame.SRCALPHA)
    cursor = pygame.Surface((5,5),pygame.SRCALPHA)
    pygame.draw.rect(image,"black",pygame.Rect(0,0,50,50))
    pygame.draw.rect(cursor,"white",pygame.Rect(0,0,5,5))

    def __init__(self,
        window:pygame.display,
        loaded_text:dict,
        position:tuple=(0,0),
        size:tuple=(50,50),
        menu:dict={ 
            "a":{"aa":0,"ab":0},
            "b":{"ba":0,"bb":0},
            "c":{"ca":0,"cb":0},
            },
        layers:list = [ ],
        text_size:int=12,
        ):
        
        #Menus turn a tiny dictionary into an interactable menu! 
        self.menu = menu #There is a raw menu, used as a reference in case the program gets lost,
        self.current_menu = self.menu.copy()#and the "current menu", which is the one used to display text data
        self.current_menu_keys = tuple(self.current_menu.keys())#the keys are used to make a reference with the index in order to enter a specific menu
        
        self.layers = layers #the layers are what is used to build a new "current menu" when something is selected
        self.index = 0 #current index to place cursor 
        
        self.update_menu()#calling update menu just to be safe 
        self.box_pos = position#menu position
        self.bg = pygame.transform.scale(MenuPygame.image,size)#resizing menu
        self.window = window #the window for displaying the box

        self.exit_code = None #this is similar to a return statement, as this will constantly be checked.

    def update(self):
        self.graphics()

    def graphics(self):
        #bg box placement
        window.blit(self.bg,self.box_pos)
        #cursor placement
        window.blit(MenuPygame.cursor,(self.box_pos[0],(self.box_pos[1]+(self.index+1) * 10)))
        #text placement
        # for _ in range(len(self.current_menu_keys)):
        #     display_text(
        #         text=self.current_menu_keys[_],
        #         resize=30,
        #         position=( 
        #             self.box_pos[0]+50 , 
        #             self.box_pos[1] + ((_+1)*50),
        #             )
        #         )

    def update_menu(self):
        #MENUS CONTINUED
        #Whenever a menu is touched or interacted with or whatnot, this is run.
        #This takes the layer count and continually nests the indexes within the dictionary.
        #Or, worded better, just the outermost layer you are looking at.
        #First, it resets the current_menu
        self.current_menu = self.menu.copy()
        for layer in self.layers:
            #Second, it repeatedly redefines the menu by going into its indexes. It only really looks at the keys when displaying the menu
            self.current_menu = self.current_menu[layer]
        #Third, it checks to see if the current menu is actually a directory.
        #If it is not, it becomes the EXIT CODE.
        if type(self.current_menu) != dict:
            self.exit_code = str(self.layers[len(self.layers)-1])
            return
        #Fourth, the keys are updates
        self.current_menu_keys = tuple(self.current_menu.keys())
        #Finally, the index is reset
        self.index = 0

    def controls(self,event):

        if event.type == pygame.KEYDOWN:
            #moving indexes
            if event.key == pygame.K_DOWN and self.index < (len(self.current_menu_keys)-1):
                self.index += 1
            if event.key == pygame.K_UP and self.index > 0:
                self.index -= 1

            #selecting
            if event.key == pygame.K_SPACE:
                #advancing a layer
                self.layers.append(self.current_menu_keys[self.index])
                self.update_menu()
            if event.key == pygame.K_BACKSPACE:
                #exiting if there are no layers added
                if len(self.layers) == 0:
                    self.exit_code = "BACK/EXIT"
                    return
                #going back a layer
                self.layers.pop((len(self.layers)-1))
                self.update_menu()


loaded_text = {}
run = True ; FPS = 15
clock=pygame.time.Clock()
window = pygame.display.set_mode((500,500))

menu=MenuPygame(window,loaded_text,size=(300,300))

while run:
    window.fill('white')
    clock.tick(FPS)
    menu.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            run = False
        menu.controls(event)
    pygame.display.update()
pass

#MENU PSEUDOCODE
"""
input: position, size, loaded text, 
"""