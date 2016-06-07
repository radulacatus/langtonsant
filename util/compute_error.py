from generate_grayscale import *
import numpy as np
import math

(_, mat1) = read_matrix("generated/20160607164435.bin") 
(_, mat2) = read_matrix("generated/20160607171416.bin")

absdif = np.abs(np.array(mat1) - np.array(mat2))
print(np.sum(absdif)/(40*40))

absdif = np.abs(np.array(mat1) - np.array(mat1))
print(np.sum(absdif)/(40*40))