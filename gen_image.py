
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.patches as patches
from matplotlib import colors
try:
    from PIL import Image
except ImportError:
    import Image
    
# my_dpi = 70
#   grid_w, grid_h = 10, 12
#   num_bus = 60
#   list_num_crit = [50]
#   list_R = [0.50, 1.00, 2.00]

def gen_image_for_each_bus(data_dir = 'data/', image_dir = 'image/', grid_w = 42, grid_h = 50, 
                           num_bus = 60, list_num_crit = [50], list_R = [0.5], my_dpi = 70):
  print('Generating image for each bus line...')
  for num_crit in list_num_crit:
    for R in list_R:
      test_set = str(grid_w) + 'x' + str(grid_h) + '/'
      dir_path = data_dir + test_set 
      img_dir =  image_dir + test_set + str(num_crit) + '_' + '{:0.2f}'.format(R) + '/'
      crit_file = dir_path + 'crit_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'

      if not os.path.exists(img_dir):
        os.makedirs(img_dir)
      
      for i in range(1, num_bus+1):
        file_name = '{:02d}.txt'.format(i)
        data_file = dir_path + file_name
        f = open(data_file, 'r')
        inp = f.read().split('\n')
        list_points = []
        for point in inp:
          x, y = point.split(' ')
          list_points.append([float(x), float(y)])
        f.close()
        
        # file_name = '{:02d}-2.txt'.format(i)
        # data_file = dir_path + file_name
        # f = open(data_file, 'r')
        # inp = f.read().split('\n')
        # list_points_2 = []
        # for point in inp:
        #   x, y = point.split(' ')
        #   list_points_2.append([float(x), float(y)])
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
        line_x = []
        line_y = []
        line_w = 1
        line_x_2 = []
        line_y_2 = []
        
        # for point in list_points_2:
        #   x, y = point
        #   real_x = x 
        #   real_y = y
        #   line_x_2.append(real_x)
        #   line_y_2.append(real_y)
        # plt.plot(line_x_2, line_y_2, 'g-', lw = line_w)
        
        for point in list_points:
          x, y = point
          real_x = x 
          real_y = y
          line_x.append(real_x)
          line_y.append(real_y)
        plt.plot(line_x, line_y, 'r-', lw = line_w)
        
        

        for crit in list_crit:
          col, row = crit
          y = row * myInterval_y
          x = col * myInterval_x
          r = R * myInterval_x
          
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

        # grid border
        plt.plot([0, 0], [0, grid_h], color = 'black', lw = line_w)
        plt.plot([0, grid_w], [grid_h, grid_h], color = 'black', lw = line_w)
        plt.plot([grid_w, grid_w], [grid_h, 0], color = 'black', lw = line_w)
        plt.plot([grid_w, 0], [0, 0], color = 'black', lw = line_w)

        ax.plot()
        plt.tick_params(labelsize=25)

        # plt.show()
        # Save the figure
        image_name = '{:02d}.jpg'.format(i)
        plt.savefig(img_dir + image_name ,dpi=100)
        fig.clf()
        plt.figure().clear()
        plt.close()
        plt.cla() 
        plt.clf()
        print(image_name + ' completed')
      print(num_crit, R, 'completed')