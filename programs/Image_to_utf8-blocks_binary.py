#Image to text converter v1.1

### IMPORTS
from PIL import Image

### FUNCTIONS
def load_img(name, w, h): #https://stackoverflow.com/questions/40727793/how-to-convert-a-grayscale-image-into-a-list-of-pixel-values#40729543
    if w and h:
        img = Image.open(name).convert('1').resize((w, h))
        W, H = w, h
    else:
        img = Image.open(name).convert('1')
        W, H = img.size
    data = list(img.getdata())
    print(f"Oh hey; {list(data[i] for i in range(50))}")
    return [int(i/255) for i in data], W, H

### MAIN
ui = 'none'
while True:
    ui = input("Filename : ")
    if not ui: break #exit
    try: #Resize
        w, h = input("width height : ").split(' ')
        w, h = int(w), int(h)
    except:
        w, h = 0, 0
    # w, h = (int(i) for i in input("width height : ").split())
    try: #Loads image
        imagedata, W, H = load_img(ui, w, h)
    except:
        print(" - Something went wrong trying to load the image -")
        continue
    # imagedata, W, H = load_img(ui, w, h)
    pattern = ''
    for row in range(H):
        pattern += '\n'+''.join('█░'[cell] for cell in imagedata[row*W:(row+1)*W])
    print(pattern)
    print("\n - Image '{}' with width {} and height {} -".format(ui, W, H))
