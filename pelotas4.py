#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 07:54:12 2023

@author: Aglez Banderas 
"""
from typing import Tuple
from dataclasses import dataclass
from pygame.surface import Surface

import numpy as np
import pygame

# Inicializar Pygame
pygame.init()

# Definimos constantes globales (de PyGame)
WIDTH, HEIGHT = 1920, 1080  # Altura y Ancho de la ventana
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Creamos el objeto ventana
CLOCK = pygame.time.Clock()  # Creamos el reloj
FPS = 60  # Frames Per Second


@dataclass
class BallProperties:
    """
    Data Class for properties
    """

    pos: list[float]
    vel: list[float]
    mass: float
    c_f: float
    color: Tuple[float]
    r: float


class Ball:
    """
    Objeto pelota
    """

    def __init__(self: "Ball", properties: BallProperties) -> None:
        self.pos = properties.pos
        self.vel = properties.vel
        self.mass = properties.mass
        self.c_f = properties.c_f
        self.color = properties.color
        self.r = properties.r

    def move(self: "Ball", h: float = 0.01) -> None:
        """
        Mueve la pelota usando método de Euler
        """
        self.vel[0] += -(self.c_f * self.vel[0]) / (self.mass) * h
        self.vel[1] += (-9.809 * self.mass - self.c_f * self.vel[1]) / (self.mass) * h
        self.pos[0] += self.vel[0] * h
        self.pos[1] += self.vel[1] * h
        # Cambio de color
        aux: float = np.sqrt(self.vel[0] * self.vel[0] + self.vel[1] * self.vel[1])
        self.color = (
            min(255, round(aux * 1.5)),
            0,
            max(0, round(255 - aux * 1.5)),
        )
        # Choque con el suelo
        if self.pos[1] < self.r:
            self.vel[1] = -self.vel[1] * 1.01
            self.pos[1] = self.r + 0.01
        # Choque contra las paredes
        if self.pos[0] < self.r:
            self.vel[0] = -self.vel[0] * 1.01
            self.pos[0] = self.r
        if self.pos[0] > WIDTH - self.r:
            self.vel[0] = -self.vel[0] * 1.01
            self.pos[0] = WIDTH - self.r
        # Choque con el techo
        if self.pos[1] > HEIGHT - self.r:
            self.vel[1] = -self.vel[1] * 1.01
            self.pos[1] = HEIGHT - self.r

    def draw(self: "Ball", win: "Surface" = WIN) -> None:
        """
        Dibuja la pelota en la ventana win.
        """
        pygame.draw.circle(win, self.color, (self.pos[0], HEIGHT - self.pos[1]), self.r)

    def distance(self: "Ball", other_ball: "Ball") -> float:
        """
        Regresa la distancia entre está pelota y otra.
        """
        return np.sqrt(
            (self.pos[0] - other_ball.pos[0]) ** 2
            + (self.pos[1] - other_ball.pos[1]) ** 2
        )


class System:
    """
    Clase Sistema, contiene todas las pelotas.
    """

    def __init__(self: "System", n: int = 1000) -> None:
        self.n = n
        self.balls = []
        for _ in range(n):
            ball_props = BallProperties(
                pos=[
                    np.random.uniform(0, WIDTH),
                    np.random.uniform(0, HEIGHT),
                ],  # Posición (m)
                vel=[
                    np.random.uniform(-50, 50),
                    np.random.uniform(-50, 50),
                ],  # Velolcidad  (m/s)
                mass=10,  # mass (Kg)
                c_f=0.01,  # Friction_coef
                color=(0, 50, 200),  # color (RGB)
                r=10,
            )
            self.balls.append(Ball(ball_props))

    def move(self: "System", h: float = 0.01) -> None:
        """
        Mueve todas las pelotas en el sistema.
        """
        for ball in self.balls:
            ball.move(h)

    def crashes(self: "System") -> None:
        """
        Detecta coliciones en el movimiento y corrige velocidades y posiciones.
        """
        for i in range(self.n):
            a = self.balls[i]
            for j in range(i + 1, self.n):
                b = self.balls[j]
                dist = a.distance(b)
                if dist < (a.r + b.r):
                    a_x = a.vel[0]
                    a_y = a.vel[1]
                    b_x = b.vel[0]
                    b_y = b.vel[1]
                    n_x = a.pos[0] - b.pos[0]
                    n_y = a.pos[1] - b.pos[1]
                    a.pos[0] += n_x / 4
                    a.pos[1] += n_y / 4
                    b.pos[0] -= n_x / 4
                    b.pos[1] -= n_y / 4
                    a.vel[0] = (a_x * (a.mass - b.mass) + 2 * b_x * b.mass) / (
                        a.mass + b.mass
                    )
                    a.vel[1] = (a_y * (a.mass - b.mass) + 2 * b_y * b.mass) / (
                        a.mass + b.mass
                    )
                    b.vel[0] = (b_x * (b.mass - a.mass) + 2 * a_x * a.mass) / (
                        a.mass + b.mass
                    )
                    b.vel[1] = (b_y * (b.mass - a.mass) + 2 * a_y * a.mass) / (
                        a.mass + b.mass
                    )

    def update(self: "System", h: float = 0.01) -> None:
        """
        Actualiza el frame.
        """
        self.crashes()
        self.move(h)

    def draw(self: "System") -> None:
        """
        Dibuja el frame.
        """
        for ball in self.balls:
            ball.draw()


def main() -> None:
    """
    Programa principal
    """

    dt = 0.1  # Time Step
    m = 300  # Número de particulas
    sistema = System(m)  # crea un objeto "system" con m pelotas
    # Ciclo de animación
    while True:
        # Salir del juego para que no se quedo Zombie
        for event in pygame.event.get():
            # Si cerramos la ventana, cierra el juego
            if event.type == pygame.QUIT:
                return
            # Si apretamos escape, cierra el juego
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        # Hay que repintar el fondo cada frame
        WIN.fill((10, 10, 10))  # Rellenar de negro

        # actualizamos el sistema
        sistema.update(dt)
        sistema.draw()
        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()