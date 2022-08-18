import pygame
import time
negro = 0,0,0
blanco = 255,255,255

def draw_text(surface, text, size, x, y): #Función que mostrará el contador de puntos en pantalla
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def main():
    pygame.init() #inicia pygame
    size = 800,600 #tamaño de la ventana
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Mi primer juego")

    width, height = 800,600
    speed = [2, 2]

    white = 128, 101, 133

    #se carga una imagen
    ball = pygame.image.load('balon.png')
    ballrect = ball.get_rect(center=(width/2,height/2))

    #barra de rebote
    barra = pygame.image.load('barra.png')
    barrarect1 = barra.get_rect()
    barrarect2 = barra.get_rect()

    #se ubican las barras en cada lado de la pantalla del jugador
    barrarect1.move_ip(1,260)
    barrarect2.move_ip(735,260)

    clock = pygame.time.Clock()   
    run = True
    #Contador del juego
    marcador_1 = 0
    marcador_2 = 0

    #Definimos las fuentes y declaramos los carteles del Puntaje
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("Puntaje:", 0, (blanco)) 
    texto2 = fuente.render("Puntaje:", 0, (blanco))

    fuenteSistema = pygame.font.SysFont("Berlin Sans FB Demi", 50)
    
    while run:
        pygame.time.delay(3) #delay que contralará la velocidad            
        
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False

        #se detecata si se ha pulsado alguna tecla
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
          if barrarect1.y > 0: 
            barrarect1 = barrarect1.move(0, -1)
        if keys[pygame.K_s]:
          if barrarect1.y < height-barrarect1.height:
            barrarect1 = barrarect1.move(0, 1)

        #Revisa la barra dos 
    
        if keys[pygame.K_UP]:
          if barrarect2.y > 0: 
              barrarect2 = barrarect2.move(0, -1)
       
       
        if keys[pygame.K_DOWN]:
          if barrarect2.y < height-barrarect2.height:
            barrarect2 = barrarect2.move(0, 1)

        #se detemina si hay colisiones 
        if barrarect1.colliderect(ballrect):
            speed[0] = -speed[0]

        if barrarect2.colliderect(ballrect):
            speed[0] = -speed[0]    

        ballrect = ballrect.move(speed) #se mueve el objeto

        #se determinan los límites del objeto
        if ballrect.left <-60 or ballrect.right > width+60:
            if ballrect.left < -60: 
              marcador_2+=1
              
            if ballrect.right > width+60: 
              marcador_1+=1
              

            speed[0] = -speed[0]
            ballrect = ball.get_rect(center=(width/2,height/2))
            time.sleep(1)
            

        if ballrect.top < 0 or ballrect.bottom > height:
          speed[1] = -speed[1]

        #se borra la pantalla anterior con el fondo blanco
        
        screen.fill(white)
        screen.blit(ball, ballrect)
        screen.blit(barra,barrarect1)
        screen.blit(barra,barrarect2)
        
        screen.blit(texto, (0,0))
        screen.blit(texto2, (600,0))
        draw_text(screen, str(marcador_1), 30, 100, 35)
        draw_text(screen, str(marcador_2), 30, 670, 35) #Se llama a la función que imprimirá el score en pantalla

        pygame.display.flip()
        #clock.tick(144)
        
    pygame.quit() #se termina el juego

if __name__ == "__main__":
    main()