
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.patches as patches
import numpy as np
from matplotlib import colors
try:
    from PIL import Image
except ImportError:
    import Image


# image = Image.open('HNBusData-crop.jpg')
# width, height = image.size
my_dpi=50
grid_w, grid_h = 30, 36
R = 1.00
num_crit = 200


dir_path = 'data/'+ str(grid_w) + 'x' + str(grid_h) + '/'
data_file = dir_path + '16.txt'
crit_file = dir_path + 'crit_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'

f = open(data_file, 'r')
inp = f.read().split('\n')
list_points = []
for point in inp:
  x, y = point.split(' ')
  list_points.append([float(x), float(y)])
f.close()

f = open(crit_file, 'r')
inp = f.read().split('\n')
list_crit = []
for point in inp:
  row, col = point.split(' ')
  list_crit.append([int(row), int(col)])
f.close()
# data = [[0 for i in range(width)] for j in range(height)]

# Set up figure
# fig=plt.figure(figsize=(float(image.size[0])/my_dpi,float(image.size[1])/my_dpi),dpi=my_dpi)
# 

# Remove whitespace from around the image
# fig.subplots_adjust(left=0,right=1,bottom=0,top=1)


# cmap = colors.ListedColormap(['white', 'blue'])
# bounds = [0,1,2]
# norm = colors.BoundaryNorm(bounds, cmap.N)

# fig, ax = plt.subplots()
fig = plt.figure(figsize=(grid_h,grid_w), dpi = my_dpi)
ax = fig.add_subplot(111)

# Set the gridding interval: here we use the major tick interval
myInterval_x = 1.0
myInterval_y = 1.0
loc_x = plticker.MultipleLocator(base=myInterval_x)
loc_y = plticker.MultipleLocator(base=myInterval_y)
ax.xaxis.set_major_locator(loc_x)
ax.yaxis.set_major_locator(loc_y)

# Add the grid
ax.grid(which='major', axis='both', linestyle='-')
ax.set_aspect('equal')
# Add the image
# ax.imshow(image)
# ax.imshow(data, cmap=cmap, norm=norm)

# Find number of gridsquares in x and y direction
# nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval_x)))
# ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval_y)))

# nx=abs(grid_w)
# ny=abs(grid_h)

# Add some labels to the gridsquares
# for j in range(ny):
#     y=myInterval_x/2+j*myInterval_y
#     for i in range(nx):
#         x=myInterval_x/2.+float(i)*myInterval_x
#         ax.text(x,y,'{:d} {:d}'.format(j, i),color='r',ha='center',va='center',fontsize=15)

line_x = []
line_y = []

for point in list_points:
  x, y = point
  real_x = x 
  real_y = y
  line_x.append(real_x)
  line_y.append(real_y)
  # y = myInterval_x/2 + row*myInterval_y
  # x = myInterval_x/2. + float(column)*myInterval_x
  # ax.text(x,y,'O',color='r',ha='center',va='center',fontsize=20)
plt.plot(line_x, line_y, 'r-')

for crit in list_crit:
  col, row = crit
  y = row * myInterval_y
  x = col * myInterval_x
  r = R * myInterval_x
  line_w = 1
  #quarter circle 1
  arc1 = patches.Arc((x, y), r*2, r*2, 0, 180, 270, color='blue', lw = line_w)
  ax.add_patch(arc1)
  #quarter circle 2
  arc2 = patches.Arc((x + myInterval_x, y), r*2, r*2, 0, 270, 0, color='blue', lw = line_w)
  ax.add_patch(arc2)
  #quarter circle 1
  arc3 = patches.Arc((x + myInterval_x, y + myInterval_y), r*2, r*2, 0, 0, 90, color='blue', lw = line_w)
  ax.add_patch(arc3)
  #quarter circle 1
  arc4 = patches.Arc((x, y + myInterval_y), r*2, r*2, 0, 90, 180, color='blue', lw = line_w)
  ax.add_patch(arc4)
  # 4 line to complete poly
  plt.plot([x, x + myInterval_x], [y - r, y - r], 'b-', lw = line_w)
  plt.plot([x + myInterval_x + r, x + myInterval_x + r], [y, y + myInterval_y], 'b-', lw = line_w)
  plt.plot([x + myInterval_x, x], [y + myInterval_y + r, y + myInterval_y + r], 'b-', lw = line_w)
  plt.plot([x - r, x - r], [y, y + myInterval_y], 'b-', lw = line_w)

  # arc_patch((x,y), r, 180, 270, fill=False, color='blue')
  text_x = myInterval_x/2. + col * myInterval_x
  text_y = myInterval_y/2 +  row * myInterval_y
  # ax.text(text_x, text_y,'{:d} {:d}'.format(col, row),color='r',ha='center',va='center',fontsize=15)

  # circle = plt.Circle((x, y), r, color='b', fill=False)
  # ax.add_artist(circle)
plt.plot([0, 0], [0, grid_h], color = 'black', lw = line_w)
plt.plot([0, grid_w], [grid_h, grid_h], color = 'black', lw = line_w)
plt.plot([grid_w, grid_w], [grid_h, 0], color = 'black', lw = line_w)
plt.plot([grid_w, 0], [0, 0], color = 'black', lw = line_w)

ax.plot()

plt.show()
# Save the figure
fig.savefig('busmap-grid42x50.jpg',dpi=300)