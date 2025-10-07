import pygame
from pygame import Color


class NumberRect():
    def __init__(self,x,y,width,height):
        self.rect=pygame.Rect(x,y,width, height)
        self.number=0

    def setNumber(self,tempNum):
        self.number=tempNum

    def getNumber(self):
        return self.number

    def draw(self,tempSurface):
        pygame.draw.rect(tempSurface,Color(255,255,255,255),self.rect)

def draw_all(window, AlgorithmsRectangles):
    window.fill((0, 0, 0))

    for rectArr in AlgorithmsRectangles:
        for rect in rectArr:
            rect.draw(window)

def update_rectangles(rectangles, numbers, base_y=300, height_ratio=4.0):
    for rect, num in zip(rectangles, numbers):

        base_height = 100
        height = base_height + num * height_ratio
        if height < 1:
            height = 1

        rect.rect.height = height
        rect.rect.y = base_y - height
        rect.setNumber(num)