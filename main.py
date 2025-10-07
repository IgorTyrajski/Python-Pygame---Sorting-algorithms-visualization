import pygame
import random
from sys import exit

from NumberClass import NumberRect, update_rectangles, draw_all
from SortAlg import bubble_sort_gen, quick_sort_gen, merge_sort_gen

speed_dir={"slow":30,"medium":60,"fast":90, "ultra-fast":150}

SIM_SIZE =80
SPEED="medium" #input here "slow", "medium","fast" or "ultra-fast"



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
    x = 210
    for num in AlgNumArr[i]:
        min_num = -SIM_SIZE // 2
        max_num = SIM_SIZE // 2 - 1
        min_height = 5
        max_height = 280
        height = min_height + (num - min_num) * (max_height - min_height) / (max_num - min_num)
        newRect = NumberRect(x, y - height, rectWidth, height)
        newRect.setNumber(num)
        rectangles.append(newRect)
        x += rectWidth + 7
    AlgorithmsRectangles.append(rectangles)
    y += 333

# sorting algorithms
bubble_gen = bubble_sort_gen(AlgNumArr[0])
quick_gen = quick_sort_gen(AlgNumArr[1])
merge_gen = merge_sort_gen(AlgNumArr[2])

colours=[pygame.Color(0, 235, 0),pygame.Color(255, 251, 0),pygame.Color(255, 0, 0)] #colors of rects of algorithms depending on speed (fastest to end is green, second yellow , etc)
c=0
HadChanged=[False, False, False]
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
        if (HadChanged[0]!=True):
            for rect in AlgorithmsRectangles[0]:
                rect.setColor(colours[c])
            HadChanged[0] = True
            c+=1

        pass
    try:
        current_state = next(quick_gen)
        update_rectangles(AlgorithmsRectangles[1], current_state, base_y=650, height_ratio=3.0)
    except StopIteration:
        if (HadChanged[1] != True):
            for rect in AlgorithmsRectangles[1]:
                rect.setColor(colours[c])
            HadChanged[1] = True
            c += 1
        pass

    try:
        current_state = next(merge_gen)
        update_rectangles(AlgorithmsRectangles[2], current_state, base_y=940, height_ratio=3.0)
    except StopIteration:
        if (HadChanged[2] != True):
            for rect in AlgorithmsRectangles[2]:
                rect.setColor(colours[c])
            HadChanged[2] = True
            c += 1
        pass

    draw_all(window, AlgorithmsRectangles)

    x=1590
    y=[300, 550,900] #y positions of 1 text ("bubble sort"), seconds etc
    i=0
    for text in text_surfaces:
        window.blit(text,(x,y[i]))
        i+=1

    pygame.display.update()
    clock.tick(speed_dir[SPEED])


