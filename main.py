import pygame
import random
from sys import exit

from NumberClass import NumberRect, update_rectangles, draw_all
from SortAlg import bubble_sort_gen, quick_sort_gen, merge_sort_gen

SIM_SIZE = 100

#pygame init
pygame.init()
full_hd=(1920,1080)
window = pygame.display.set_mode(full_hd)
pygame.display.set_caption("Sorting Algorithms Visualization")

text_font=pygame.font.Font("Pixeltype.ttf",40)
BubbleSort_text_surface=text_font.render("BubbleSort",False,(255,255,255)).convert()
QuickSort_text_surface=text_font.render("QuickSort",False,(255,255,255)).convert()
MergeSort_text_surface=text_font.render("MergeSort",False,(255,255,255)).convert()
text_surfaces=[BubbleSort_text_surface, QuickSort_text_surface, MergeSort_text_surface]

clock = pygame.time.Clock()

#data init
AlgNumArr = []
for i in range(3):
    numArr = list(range(-SIM_SIZE // 2, SIM_SIZE // 2))
    random.shuffle(numArr)
    AlgNumArr.append(numArr)

AlgorithmsRectangles = []
rectWidth = 10
y = 380
for i in range(3):
    rectangles = []
    x = 0
    for num in AlgNumArr[i]:
        min_num = -SIM_SIZE // 2
        max_num = SIM_SIZE // 2 - 1
        min_height = 5
        max_height = 280
        height = min_height + (num - min_num) * (max_height - min_height) / (max_num - min_num)
        newRect = NumberRect(x, y - height, rectWidth, height)
        newRect.setNumber(num)
        rectangles.append(newRect)
        x += rectWidth + 5
    AlgorithmsRectangles.append(rectangles)
    y += 333

# sorting algorithms
bubble_gen = bubble_sort_gen(AlgNumArr[0])
quick_gen = quick_sort_gen(AlgNumArr[1])
merge_gen = merge_sort_gen(AlgNumArr[2])

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))

    try:
        current_state = next(bubble_gen)
        update_rectangles(AlgorithmsRectangles[0], current_state, base_y=380, height_ratio=3.0)
    except StopIteration:
        pass

    try:
        current_state = next(quick_gen)
        update_rectangles(AlgorithmsRectangles[1], current_state, base_y=630, height_ratio=3.0)
    except StopIteration:
        pass

    try:
        current_state = next(merge_gen)
        update_rectangles(AlgorithmsRectangles[2], current_state, base_y=960, height_ratio=3.0)
    except StopIteration:
        pass

    draw_all(window, AlgorithmsRectangles)

    x=1550
    y=[300, 550,900]
    i=0
    for text in text_surfaces:
        window.blit(text,(x,y[i]))
        i+=1

    pygame.display.update()
    clock.tick(60)


