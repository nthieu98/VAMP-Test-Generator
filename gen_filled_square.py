
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.patches as patches
import numpy as np
import os
from matplotlib import colors
try:
    from PIL import Image
except ImportError:
    import Image


# image = Image.open('HNBusData-c rop.jpg')
# width, height = image.sizessss
def gen_image_with_filled_square(data_dir = 'data/', image_dir = 'image_set_filled_square/', grid_w = 25, grid_h = 30,
                                num_bus = 60, num_crit = 10, R = 2.0, my_dpi = 300):
  print('Genearting image for each bus with filled critical square...')
  dir_path = data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
  crit_file = dir_path + 'crit_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'
  img_dir = image_dir + str(grid_w) + 'x' + str(grid_h) + '/'

  if not os.path.exists(img_dir):
    os.makedirs(img_dir)
  # f = open(data_file, 'r')
  # inp = f.read().split('\n')
  # list_points = []
  # for point in inp:
  #   x, y = point.split(' ')
  #   list_points.append([float(x), float(y)])
  # f.close()

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

  for i in range(1, num_bus+1):
    line_x = []
    line_y = []
    file_name = '{:02d}.txt'.format(i)
    data_file = dir_path + file_name
    f = open(data_file, 'r')
    inp = f.read().split('\n')
    for point in inp:
      x, y = point.split(' ')
      line_x.append(float(x))
      line_y.append(float(y))
      plt.plot(line_x, line_y, 'r-')
    f.close()

  # for point in list_points:
  #   x, y = point
  #   real_x = x 
  #   real_y = y
  #   line_x.append(real_x)
  #   line_y.append(real_y)
  #   plt.plot(line_x, line_y, 'r-')

  for crit in list_crit:
    col, row = crit
    y = row * myInterval_y
    x = col * myInterval_x
    r = R * myInterval_x
    line_w = 1

    rectangle = plt.Rectangle((x, y), 1, 1, fc='blue',ec="black")
    plt.gca().add_patch(rectangle)
    
    # arc_patch((x,y), r, 180, 270, fill=False, color='blue')
    # text_x = myInterval_x/2. + col * myInterval_x
    # text_y = myInterval_y/2 +  row * myInterval_y
    # ax.text(text_x, text_y,'{:d} {:d}'.format(col, row),color='r',ha='center',va='center',fontsize=15)

    # circle = plt.Circle((x, y), r, color='b', fill=False)
    # ax.add_artist(circle)
  plt.plot([0, 0], [0, grid_h], color = 'black', lw = line_w)
  plt.plot([0, grid_w], [grid_h, grid_h], color = 'black', lw = line_w)
  plt.plot([grid_w, grid_w], [grid_h, 0], color = 'black', lw = line_w)
  plt.plot([grid_w, 0], [0, 0], color = 'black', lw = line_w)

  plt.xlim(left=0)
  plt.xlim(right=grid_w)
  plt.ylim(bottom=0)
  plt.ylim(top=grid_h)
  ax.plot()

  # plt.show()
  # Save the figure
  image_name = str(num_crit) + '_' + '{:0.2f}'.format(R) + '.jpg'
  plt.savefig(img_dir + image_name, dpi=300)
  
  plt.cla()
  plt.clf()
  # fig.savefig('busmap-grid42x50.jpg',dpi=300)