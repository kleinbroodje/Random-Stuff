from settings import *
import csv

def start():
    global running

    running = True
    while running:
        screen.fill((255, 255, 255))

        pygame.mixer.pause()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  
                if event.key == pygame.K_SPACE:
                    countdown()
        
        pygame.display.update()


def countdown():
    global running

    pygame.mixer.Sound.play(audio, -1)
    start_time = pygame.time.get_ticks()

    while running:
        screen.fill((255, 255, 255))
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if current_time - start_time < 1000:
            screen.blit(pygame.image.load("assets/number3.png"), (pygame.display.Info().current_w/2 - 310, pygame.display.Info().current_h/2 - 250))
        if current_time - start_time >= 1000 < 2000:
            screen.blit(pygame.image.load("assets/number2.png"), (pygame.display.Info().current_w/2 - 310, pygame.display.Info().current_h/2 - 250))
        if current_time - start_time >= 2000 < 3000:
            screen.blit(pygame.image.load("assets/number1.png"), (pygame.display.Info().current_w/2 - 310, pygame.display.Info().current_h/2 - 250))
        if current_time - start_time >= 3000 < 4000:
            game()
            return
        
        pygame.display.update()
            
    
def game():
    global running
    global runs
    
    start_time = pygame.time.get_ticks()
    order = [
        ["5.0", "3.2", "6.0", "5.1", "7.2", "4.0", "8.2", "6.1", "7.0"],
        ["1.1", "8.0", "2.1", "3.1", "6.2", "4.2", "7.1", "1.2", "5.0"],
        ["1.2", "5.1", "4.2", "3.0", "2.0", "6.1", "7.2", "9.0", "8.1"],
        ["4.2", "7.2", "1.1", "3.0", "2.1", "7.1", "5.1", "8.2", '3.1'],
        ["6.0", "1.1", "3.2", "4.2", "2.1", "1.2", "8.0", "5.2", '4.0']
    ] 
    img = 0
    last_img = 0
    amount_wrong = 0
    wrong = True
    sum_ = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

                rev_num = {v: k for k, v in nums.items()}
                for i in range(1, 10):
                    if eval(f"event.key == pygame.K_{i} and rev_num[nums[order[runs][img]]][0] == str({i})"):
                            
                            time = pygame.time.get_ticks() - start_time - last_img 
                            last_img = pygame.time.get_ticks() - start_time
                            data.append(f"{time}ms")
                            sum_ += time
                            wrong = False
                            img += 1   

                            if img >= len(order[runs]):
                                data.append(f"{sum_/len(data)}ms")
                                data.append(amount_wrong)
                                with open("resultaten.csv", "a") as f:
                                    csvwriter = csv.writer(f)
                                    csvwriter.writerow(data)
                                data.clear()
                                runs += 1
                                return
                if wrong:
                    amount_wrong += 1

        wrong = True
        screen.blit(nums[order[runs][img]], (0, 50))
        pygame.display.update()


start()

pygame.quit()
