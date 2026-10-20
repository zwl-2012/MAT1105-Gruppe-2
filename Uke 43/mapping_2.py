########## Import packages ##########
########################################
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
########################################



########## Convert image to array ##########
def convert_image2array(image_name):
    """image_name : str
        Name of the image file
    ----------------------------------
    ----------------------------------
    f : array (2D)
        2D array of the image
    ----------------------------------"""
    f = Image.open(image_name).convert('L')     # 'L' = greytone
    f = np.array(f)                             # convert to 2D-array
    return f





########## Plot image min,max = [0,255] ##########
def plot_image(f, title=None):
    """f : array (2D)
    ----------------------------------
    ----------------------------------
    Plot grey scale of image matrix f
    ----------------------------------"""
    plt.imshow(f, cmap='gray', vmin=0, vmax=255, aspect='auto') # 0=black, 255=white
    if title is not None: plt.title(title)
    plt.show()





########## Plot image with 3 points ##########
def plot_image_points(f, points, title=None):
    """f : array (2D)
    ----------------------------------
    points : list
        List of points
    ----------------------------------
    ----------------------------------
    Plot grey scale of image matrix f
    ----------------------------------"""
    plt.imshow(f, cmap='gray', vmin=0, vmax=255, aspect='auto') # 0=black, 255=white
    for p in points:
        plt.plot(p[0], p[1], "ro")
    if title is not None: plt.title(title)
    plt.show()



########## forward mapping ##########
def transform_forward(f, fm, a0, a1, a2, b0, b1, b2):
    """f : array (2D)
        Old grid
    ----------------------------------
    fm : array (2D)
        New grid
    ----------------------------------
    a0, a1, a2, b0, b1, b2 : float
        Mapping coefficients
    ----------------------------------
    ----------------------------------
    fnew : array (2D)
        New grid mapped
    ----------------------------------"""
    rows1, cols1 = np.shape(f)
    rows, cols = np.shape(fm)
    fnew = np.zeros((rows, cols))
    for x in range(rows1):
        for y in range(cols1):
            x_f = round(a0*x + a1*y + a2)
            y_f = round(b0*x + b1*y + b2)
            if x_f < 0 or x_f > rows-1 or y_f < 0 or y_f > cols-1:
                continue
            else: 
                fnew[x_f, y_f] = f[x, y]
    return fnew




########## inverse mapping ##########
def transform_inverse(f, fm, a0, a1, a2, b0, b1, b2):
    """f : array (2D)
        Old grid
    ----------------------------------
    fm : array (2D)
        New grid
    ----------------------------------
    a0, a1, a2, b0, b1, b2 : float
        Inverse mapping coefficients
    ----------------------------------
    ----------------------------------
    fnew : array (2D)
        New grid mapped
    ----------------------------------"""
    rows1, cols1 = np.shape(f)
    rows, cols = np.shape(fm)
    fnew = np.zeros((rows, cols))
    for x_f in range(rows):
        for y_f in range(cols):
            x = round(a0*x_f + a1*y_f + a2)
            y = round(b0*x_f + b1*y_f + b2)
            if x < 0 or x > rows1-1 or y < 0 or y > cols1-1:
                continue
            else: 
                fnew[x_f, y_f] = f[x, y]
    return fnew





########################################
########## RESULTS ####################
########################################
if __name__=="__main__":
    print("\n---------- Matriser II ----------\n")

    image_name = "dice.jpg"
    f = convert_image2array(image_name)         # 458 x 458
    print(f.shape)
    #plot_image(f)


    points = [[230,135], [230,410], [423,93]]
    plot_image_points(f, points)
    
    new_f = np.zeros((458, 458))


    ##### Inverse mapping #####
    a0_i, a1_i, a2_i = 0.6018, -0.0919, 135.0037
    b0_i, b1_i, b2_i = 0, 0.4222, 229.9490
    f_transform = transform_inverse(f, new_f, a0_i, a1_i, a2_i, b0_i, b1_i, b2_i)
    plot_image(f_transform)
    


    ##### Forward mapping #####
    """
    a0, a1, a2 = 1.6618, 0.3617, -307.5217
    b0, b1, b2 = 0, 2.3684, -544.6111
    f_transform_forward = transform_forward(f, new_f, a0, a1, a2, b0, b1, b2)
    plot_image(f_transform_forward)
    """
