import datetime
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import struct

def generate():
    height, width = 40, 40 #in pixels
    spines = 'left', 'right', 'top', 'bottom'

    labels = ['label' + spine for spine in spines]

    tick_params = {spine : False for spine in spines}
    tick_params.update({label : False for label in labels})

    mat = np.random.randint(0, 255, (height, width))

    desired_width = 8 #in inches
    scale = desired_width / float(width)

    fig, ax = plt.subplots(1, 1, figsize=(desired_width, height*scale))
    img = ax.imshow(mat, cmap=cm.Greys_r, interpolation='none')

    #remove spines
    for spine in spines:
        ax.spines[spine].set_visible(False)

    #hide ticks and labels
    ax.tick_params(**tick_params)

    #preview
    # plt.show()

    file_path = 'generated/' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    #save
    fig.savefig(file_path + '.png', dpi=300)
    
    write_matrix(40,mat,file_path + '.bin')

    (len2, mat2) = read_matrix(file_path + '.bin')
    #print(len2)
    #print(mat2)

def write_matrix(len, matrix, file):
    if(len > 255):
        raise ValueError('Value larger than a byte:' + len)
    with open(file, 'wb') as f:
        f.write(chr(len))
        for i in range(len):
            for j in range(len):
                if(matrix[i][j] > 255):
                    raise ValueError('Value larger than a byte:' + matrix[i][j])
                f.write(chr(matrix[i][j]))

def read_matrix(file):
    with open(file, 'rb') as f:
        len = ord(f.read(1))
        mat = []
        for i in range(len):
            tmp = []
            for j in range(len):
                tmp.append(ord(f.read(1)))
            mat.append(tmp)
    return (len, mat)