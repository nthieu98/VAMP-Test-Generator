
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
# width, height = image.size
#  my_dpi = 300
#   grid_w, grid_h = 42, 50
#   list_num_crit = [10]
#   list_R = [0.50, 1.00, 2.00, 3.00]
#   num_bus = 60

def gen_all(data_dir = 'data/', image_dir = 'image_set/', grid_w = 42, grid_h = 50, 
            num_bus = 60, list_num_crit = [10], list_R = [0.50], my_dpi = 300):
  print('Genearting image with all bus line...')
  
  for num_crit in list_num_crit:
    for R in list_R:
      dir_path = data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      crit_file = dir_path + 'crit_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'
      img_dir = image_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      if not os.path.exists(img_dir):
        os.makedirs(img_dir)
      f = open(crit_file, 'r')
      inp = f.read().split('\n')
      list_crit = []
      for point in inp:
        row, col = point.split(' ')
        list_crit.append([int(row), int(col)])
      f.close()

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
        line_x_2 = []
        line_y_2 = []
        # file_name = '{:02d}-2.txt'.format(i)
        # data_file = dir_path + file_name
        # f = open(data_file, 'r')
        # inp = f.read().split('\n')
        # for point in inp:
        #   x, y = point.split(' ')
        #   line_x_2.append(float(x))
        #   line_y_2.append(float(y))
        #   plt.plot(line_x_2, line_y_2, 'g-')
        # f.close()
        
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

      # plt.show()
      # Save the figure
      image_name = str(num_crit) + '_' + '{:0.2f}'.format(R) + '.jpg'
      plt.savefig(img_dir + image_name, dpi=300)
      print(image_name, 'completed')
      # fig.savefig('busmap-grid42x50.jpg',dpi=300)