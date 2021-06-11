import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from PIL import Image
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

# data = np.random.rand(42, 50) * 20
# size of gridlines
w, h = 42, 50
# size of image
img_w, img_h = 3500, 4200

# init data
data = [[0 for i in range(w)] for j in range(h)]

# read data
img_points = []
grid_points = []

f = open('raw_data/02.txt', 'r')
raw_data = f.read().split('\n')
# print(inp)
for point in raw_data:
  x, y = point.split(' ')
  img_points.append([x, y])
  point_column = int(float(x) * w / img_w)
  point_row = int(float(y) * h / img_h)
  print(point_row, point_column)
  data[point_row][point_column] = 2

# create discrete colormap
cmap = colors.ListedColormap(['white', 'blue'])
bounds = [0,1,2]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap, norm=norm)

# add fig
image = Image.open('HNBusData-crop.jpg')
width, height = image.size
my_dpi = 70
part = 5

scale_width = 1280 / w
scale_height = 720 / h
scale = min(scale_width, scale_height)
image = image.resize((int(width / scale), int(height / scale)), Image.ANTIALIAS)
fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)


# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=0.5)
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.set_xticks(np.arange(-0.5, w, 1))
ax.set_yticks(np.arange(-0.5, h, 1))
ax.imshow(image)
plt.show()