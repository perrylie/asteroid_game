import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    game_over = False
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    Score.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    score = Score(SCORE_POSITION_X, SCORE_POSITION_Y)
    AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000

        if not game_over:
            updatable.update(dt)
        
        screen.fill("black")
        
        if game_over:
            font_big = pygame.font.Font(None, 72)
            font_small = pygame.font.Font(None, 36)

            game_over_text = font_big.render("Game Over!", True, (255, 255, 255))
            score_text = font_small.render(f"Score: {score.get_score()}", True, (255, 255, 255))

            game_over_rect = game_over_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            )
            score_rect = score_text.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            )

            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_text, score_rect)

        if not game_over:
            for object in drawable:
                object.draw(screen)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f"Total score: {score.get_score()}")
                game_over = True
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score.update_score()
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
