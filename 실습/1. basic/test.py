import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

# bitmap = np.random.randint(0,256,(300,300))

# plt.imshow(bitmap, cmap='gray')
# plt.show()

image = img.imread("Lenna.png")
print(image.shape)
image[:,:,0] = image[:,:,0] * 0
image[:,:,1] = image[:,:,1] * 1
image[:,:,2] = image[:,:,2] * 0
image[:,:,3] = image[:,:,3] * .5
plt.imshow(image)
plt.show()