#Image to text converter v1.1

"""Initialisation"""
from PIL import Image

"""Functions"""
def load_img(name, w, h): #https://stackoverflow.com/questions/40727793/how-to-convert-a-grayscale-image-into-a-list-of-pixel-values#40729543
    if w and h:
        img = Image.open(name).convert('L').resize((w, h))
        W, H = w, h
    else:
        img = Image.open(name).convert('L')
        W, H = img.size
    data = list(img.getdata())
    return [ int(4*i/255) for i in data], W, H

"""Main Loop"""
ui = 'none'
while True:
    ui = input("Insert name of file to convert (same folder as script): ")
    if not ui: break #exit
    try: #Resize
        w, h = input("Input width and height as 'w h' or leave blank: ").split(' ')
        w, h = int(w), int(h)
    except:
        w, h = 0, 0
    try: #Loads image
        imagedata, W, H = load_img(ui, w, h)
    except:
        print(" - Something went wrong while loading image! -")
        continue
    pattern = ''
    for row in range(H):
        pattern += '\n'+''.join('█▓▒░ '[cell] for cell in imagedata[row*W:(row+1)*W])
    print(pattern)
    print("\n - Image '{}' with width {} and height {} -".format(ui, W, H))
