import algorithms
import time, sys, pygame

HEIGHT = 900
WIDTH = 1536
DIMENSIONS = (WIDTH, HEIGHT)
BG_COLOR = "#a48be0"
LIGHT_PURPLE = (80, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

algorithms = {
    "SelectionSort" : algorithms.SelectionSort(),
    "BubbleSort" : algorithms.BubbleSort(),
    "InsertionSort" : algorithms.InsertionSort(),
    "MergeSort" : algorithms.MergeSort(),
    "QuickSort" : algorithms.QuickSort()
}

pygame.init()
display = pygame.display.set_mode(DIMENSIONS)



def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)



def update(algorithm, swap1=None, swap2=None, display=display):
    display.fill(pygame.Color(BG_COLOR))
    algorithm.time_elapsed = time.time() - algorithm.start_time
    pygame.display.set_caption(f"Sorting Visualizer    Algorithm: {algorithm.name}    Time elapsed: {algorithm.time_elapsed}    Status: Sorting...")

    k = int(WIDTH/len(algorithm.array))

    for i in range(len(algorithm.array)):
        color = LIGHT_PURPLE
        pygame.draw.rect(display, color, (i*k, HEIGHT, k, -algorithm.array[i]))

    check_events()

    pygame.display.update()



def keep_open(algorithm, display, time):
    pygame.display.set_caption(f"Sorting Visualizer    Algorithm: {algorithm.name}    Time elapsed: {time}    Status: Done!")
    while True:
        check_events()
        pygame.display.update()



def main():
        # argument handler
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.")
    else:
        if sys.argv[1] == "--list":
            for key in algorithms.keys() : print(key, end="")
            print("")
            sys.exit(0)
        
        display.fill(pygame.Color(BG_COLOR))

        try:
            algorithm = algorithms[sys.argv[1]]
            time_elapsed = algorithm.run()[1]
            keep_open(algorithm, display, time_elapsed)
            
        except:
            print("Finished.")
            sys.exit()

if __name__ == '__main__':
    main()