import pygame
from pygame.locals import *
from snake import *
from apple import Apple
from score import Score



GAME_ON = True
SPEED = 10 
game_over = False

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake Game-Python Begginer')
clock = pygame.time.Clock()

snake = Snake()
apple = Apple()
score = Score(pygame.font.Font(None, 36), pos=(50,20))


apple.set_random_position(400)

font_big = pygame.font.Font(None, 60)
font_small = pygame.font.Font(None, 30)



def reset_game():
    print("Resetting game...")
    global snake, apple, score, SPEED
    snake = Snake()
    apple = Apple()
    score = Score(pygame.font.Font(None, 36), pos=(60, 20))
    try:
        apple.set_random_position(300, 300)
    except TypeError:
        apple.set_random_position(300)
    SPEED = 10

while GAME_ON:
    clock.tick(SPEED)  # Control the speed of the snake
    snake.crawl()

     # Set a random position for the apple
   

    
    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False
        
        
        if event.type == KEYDOWN:
            if event.key==K_UP and snake.direction != DOWN:
                print("UP")
                snake.direction = UP                
            elif event.key==K_LEFT and snake.direction != RIGHT:
                print("LEFT")
                snake.direction = LEFT                
            elif event.key==K_DOWN and snake.direction != UP:
                print("DOWN")
                snake.direction = DOWN                
            elif event.key==K_RIGHT and snake.direction != LEFT:
                print("RIGHT")
                snake.direction = RIGHT
    

    
    if snake.wall_collision(400) or snake.self_collision(): 
        print("Game Over!")
        game_over = True
        while game_over:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    game_over = False
                    GAME_ON = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_r:     # reiniciar
                        # aquí podrías resetear snake, apple, score...
                        reset_game()
                        game_over = False
                        GAME_ON = True
                    elif e.key == pygame.K_ESCAPE:
                        game_over = False
                        GAME_ON = False

            screen.fill((20, 20, 20))

            txt1 = font_big.render("GAME OVER", True, (255, 50, 50))
            rect1 = txt1.get_rect(center=(200, 180))
            screen.blit(txt1, rect1)

            txt2 = font_small.render("Pulsa R para reiniciar, ESC para salir", True, (255, 255, 255))
            rect2 = txt2.get_rect(center=(200, 240))
            screen.blit(txt2, rect2)
            
            txt_score = font_small.render(f"Score: {score.score}", True, (255, 255, 255))
            rect_score = txt_score.get_rect(center=(300,300))
            screen.blit(txt_score, rect_score)

            pygame.display.flip()
            clock.tick(60)

     

    if snake.snake_eat_apple(apple_pos=apple.position):
        apple.set_random_position(400)
        snake.snake_bigger()
        SPEED +=0.5 
        print("Snake grew!")
        score.score_up()
        print(f"Score: {score.score}")
    screen.fill((0, 0, 0))

    # Snake
    for pos in snake.snake:
        screen.blit(snake.skin, pos)

    # Apple
    screen.blit(apple.apple, apple.position)

    # Score (siempre en cada frame)
    score.update()
    score.draw(screen)

    pygame.display.flip()

      # Clear the screen with black

    for snake_pos in snake.snake[0:-1]:
       screen.blit(snake.skin, snake_pos)
    screen.blit(snake.head, snake.snake[-1])
    screen.blit(apple.apple,apple.position)  # Draw the snake head

    

    pygame.display.update()
pygame.quit()




