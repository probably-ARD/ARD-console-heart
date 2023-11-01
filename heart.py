from os import system
from math import pow


# get width and height cmd. need to hurt position
ans = 'n'
while not(ans.lower().count('y')):
    width = int(input('please enter the cmd width: '))
    height = int(input('please enter the cmd height: '))
    ans = str(input(f'\twidth: {width}\n\theight: {height}\ny/n: ')).lower()

system('cls')

frames = 10000 # frames in your animation

cmd_aspect = width / height # the ratio of the sides of the console if an elongated image is obtained without them
pixel_aspect = 11 / 24 # approximate ratio in pixels of the height and width of the symbol. need to preety hurt

light_gradient = ['@', '#', '$', '*', '!', '.', '`']

screen = ['' for i in range(width * height)]

for f in range(frames):
    for i in range(width):
        for j in range(height):
            # get x & y in [-1; 1] range
            x = (i / width * 2 - 1) * cmd_aspect * pixel_aspect
            y = (j / height * 2 - 1)
            
            # get hurt point positions
            hurt = pow(x, 2) + 2 * pow((3 * pow(pow(x, 2), 1/3) / 5 - y), 2)

            # get pixel
            pixel = ' '

            # if this pixel in figure make more light pixel
            if hurt <= 0.6: pixel = light_gradient[1]
            if hurt <= 0.3: pixel = light_gradient[0]

            # this place special to hurt animation
            
            
            # add pixel to str
            screen[-(i + j * width)] = pixel # - need to horizontal mirror frame
    
    print(''.join(screen))
    # if you have animation delete break
    break
