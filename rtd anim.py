import pyglet, sys, os, time, random

def animgif_to_ASCII_animation(animated_gif_path):
    # map greyscale to characters
    chars = ('#', '#', '@', '%', '=', '+', '*', ':', '-', '.', ' ')
    clear_console = 'clear' if os.name == 'posix' else 'CLS'

    # load image
    anim = pyglet.image.load_animation(animated_gif_path)

    # Step through forever, frame by frame
    while True:
        for frame in anim.frames:

            # Gets a list of luminance ('L') values of the current frame
            # data = frame.image.get_data('L', frame.image.width)
            data = bytes(frame.image.get_data('L', frame.image.width))
            # Built up the string, by translating luminance values to characters
            outstr = ''
            for (i, pixel) in enumerate(data):
                outstr += chars[int(pixel * (len(chars) - 1) / 255)] + \
                          ('\n' if (i + 1) % frame.image.width == 0 else '')

            # Clear the console
            os.system(clear_console)

            # Write the current frame on stdout and sleep
            sys.stdout.write(outstr)
            sys.stdout.flush()
            time.sleep(0.1)

# run the animation based on some animated gif
dice = random.choice([1, 2, 3, 4, 5, 6])
if dice == 1:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/1.gif')
    pass
elif dice == 2:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/2.gif')
    pass
elif dice == 3:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/3.gif')
    pass
elif dice == 4:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/4.gif')
    pass
elif dice == 5:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/5.gif')
    pass
elif dice == 6:
    animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/6.gif')
    pass
else:
    print('what the hell happened?!')




# animgif_to_ASCII_animation(u'/Users/falcga/Documents/GitHub/falcga/verticalanim.gif')