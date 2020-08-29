import imageio
import numpy as np
from skimage.transform import resize

raw_img = imageio.imread('image.png')
h, w, c = raw_img.shape

useful_img = raw_img[:,:,3]
resized_img = resize(useful_img, (32, 160), anti_aliasing=True)
print(resized_img.min(), resized_img.max(), np.mean(resized_img))
resized_img[resized_img >= 0.25] = 255
resized_img = resized_img.astype(np.uint8)

h, w = resized_img.shape
imageio.imwrite('image_1c_resize.png', resized_img)

with open('test_01.txt', 'w') as fp:
    for r in range(h):
        for c in range(w):
            if resized_img[r,c] != 0:
                fp.write('#')
            else:
                fp.write(' ')
        fp.write('\n')
