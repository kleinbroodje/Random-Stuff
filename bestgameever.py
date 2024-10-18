import pygame
import pygame.gfxdraw
from pprint import pprint


pygame.init()

WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Tee():
    def __init__(self, x, y, index_x, index_y):
        self.x = x
        self.y = y 
        self.index_x = index_x
        self.index_y = index_y
        self.empty = False
        self.rad = 30
        self.rect = pygame.Rect(self.x - self.rad, self.y - self.rad, self.rad*2, self.rad*2)
        self.color = (255, 0, 0)


    def update(self):
        global started 

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                if event.button == 1:
                    if not started:
                        tees[self.index_y][self.index_x].empty = True
                        started = True

                    else:
                        if not self.empty: 
                            if self not in selected:
                                if len(selected) == 0:
                                    selected.append(self)
                            else:
                                selected.remove(self)

                        
                        elif self in selectable_empty and not tees[int((self.index_y + selected[0].index_y)/2)][int((self.index_x + selected[0].index_x)/2)].empty: 
                            self.empty = False
                            tees[selected[0].index_y][selected[0].index_x].empty = True
                            tees[int((self.index_y + selected[0].index_y)/2)][int((self.index_x + selected[0].index_x)/2)].empty = True
                            selected.clear()


        if self.empty:
            self.color = (100, 100, 100)
        elif self in selected:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 0)

        pygame.gfxdraw.filled_circle(screen, self.x, self.y, self.rad, self.color)


def init_tees():
    rows = 5
    columns = 5
    for y in range(rows):
        for x in range(columns):

            ratio = 0
            if columns > 1:
                ratio = (x/(columns-1)-0.5) * 100

            tees[y].append(Tee(600 + int(ratio) * (columns-1), 250 + y * 85, x, y))

        columns -= 1

def restart():
    for row in tees:
        for tee in row:
            tee.empty = False

tees = [[], [], [], [], []]
selected = []
selectable_empty = []
options = []
started = False
font = pygame.font.Font(None, 36)
text = font.render("Choose starting spot", True, (255, 255, 255))
end_text = font.render("Game Over", True, (255, 255, 255))

running = True
init_tees()
while running:
    screen.fill((40, 40, 40))

    game_over = True
    for row in tees:
        for tee in row:
            if not tee.empty:
                if row.index(tee) > 1:
                    if not row[row.index(tee)-1].empty and row[row.index(tee)-2].empty:
                        game_over = False
                        break
                if row.index(tee) < len(row)-2:
                    if not row[row.index(tee)+1].empty and row[row.index(tee)+2].empty:
                        game_over = False
                        break

                if tees.index(row) > 1:
                    if not tees[tees.index(row)-1][row.index(tee)].empty and tees[tees.index(row)-2][row.index(tee)].empty:
                        game_over = False
                        break
                    if not tees[tees.index(row)-1][row.index(tee)+1].empty and tees[tees.index(row)-2][row.index(tee)+1].empty:
                        game_over = False
                        break

                if tees.index(row) < 3:
                    if row.index(tee) < len(tees[tees.index(row)+1])-1:
                        if not tees[tees.index(row)+1][row.index(tee)].empty and tees[tees.index(row)+2][row.index(tee)].empty:
                            game_over = False
                            break   
                    
                    if row.index(tee) > 1:
                        if not tees[tees.index(row)+1][row.index(tee)-1].empty and tees[tees.index(row)+2][row.index(tee)-2].empty:
                            game_over = False
                            break
        
    if game_over and started:
        screen.blit(end_text, (WIDTH/2 - end_text.width/2, HEIGHT/6))

    if not started:
        screen.blit(text, (WIDTH/2 - text.width/2, HEIGHT/6))

    events =  pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if game_over and started:
                if event.key == pygame.K_r:
                    restart()
                    started = False

    if selected:
        for y in tees:
            if selected[0] in y:
                selected_index = (y.index(selected[0]), tees.index(y))
                break
    
        options = [(selected_index[0]-2, selected_index[1]), 
                (selected_index[0]+2, selected_index[1]), 
                (selected_index[0], selected_index[1]+2), 
                (selected_index[0], selected_index[1]-2),
                (selected_index[0]+2, selected_index[1]-2),
                (selected_index[0]-2, selected_index[1]+2)]
    else:
        options.clear()
        selectable_empty.clear()
    

    for x, y in options:
        try:
            if tees[y][x].empty and y >= 0 and x >= 0:
                selectable_empty.append(tees[y][x])
        except IndexError:
            continue
    
    for row in tees:
        for tee in row:
            tee.update()

    pygame.display.update()
    