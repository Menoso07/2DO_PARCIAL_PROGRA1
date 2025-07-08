import pygame
from Constantes import *
from Funciones import *

pygame.init()
bandera_juego = False
fuente = pygame.font.SysFont("Arial Narrow",40)
cuadro = crear_elemento_juego("textura_respuesta.jpg",250,50,200,200)
fondo_pantalla = pygame.transform.scale(pygame.image.load("fondo.jpg"),PANTALLA)
boton_volver = crear_elemento_juego("textura_respuesta.jpg",100,40,10,10)

bandera_juego = True
def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            #Estaria bueno forzarle al usuario que no pueda salir del juego hasta que guarde la puntuacion -> A gusto de ustedes
            retorno = "salir"
        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
            
            print(datos_juego["nombre"])
            
            if letra_presionada == "backspace" and len(datos_juego["nombre"]) > 0:
                datos_juego["nombre"] = datos_juego["nombre"][0:-1]#Elimino el ultimo
                print(datos_juego["nombre"])
                limpiar_superficie(cuadro,"textura_respuesta.jpg",250,50)
            
            if letra_presionada == "space":
                datos_juego["nombre"] += " "
            
            if len(letra_presionada) == 1:  
                if bloc_mayus != 0:
                    datos_juego["nombre"] += letra_presionada.upper()
                else:
                    datos_juego["nombre"] += letra_presionada
            
            if evento.key == pygame.K_ESCAPE:
                guardar_ranking(datos_juego["nombre"],datos_juego["puntuacion"])
                evento.type == pygame.QUIT
                pygame.mixer.music.stop()
                retorno = "salir"

         

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(cuadro["superficie"],cuadro["rectangulo"])
    mostrar_texto(cuadro["superficie"],datos_juego["nombre"],(10,0),fuente,COLOR_BLANCO)
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego["puntuacion"]} puntos",(250,100),fuente,COLOR_NEGRO)

    
    return retorno