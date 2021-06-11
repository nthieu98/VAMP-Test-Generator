import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import os
# img_w, img_h = 3500, 4200
#   num_files = 60
#   start_file = 1
#   end_file = 60

def convert_pixel_to_cordinate(inp_data_dir = 'raw_data/', out_data_dir = 'data/', 
                               img_w = 3500, img_h = 4200, grid_w = 42, grid_h = 50, 
                               num_file = 60, start_file = 1, end_file = 60):
  # size of gridlines
  print("Converting pixel point to cordinate point...")
  w, h = grid_w, grid_h

  # size of image
  
  test_set = str(w) + 'x' + str(h)

  # read data
  img_points = []
  grid_points = []

  for i in range(start_file, end_file + 1):
    file_name = '{:02d}.txt'.format(i)
    f = open(inp_data_dir + file_name, 'r')
    raw_data = f.read().split('\n')
    output = []
    # print(inp)
    for point in raw_data:
      x, y = point.split(' ')
      img_points.append([x, y])
      point_x = '{:0.2f}'.format(float(x) * w / img_w)
      point_y = '{:0.2f}'.format(h - float(y) * h / img_h)
      output.append(str(point_x) + ' ' + str(point_y))
    out_dir = out_data_dir + test_set
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    wf = open(out_dir + '/' + file_name, 'w')
    wf.write('\n'.join(output))
    print(file_name + ' completed')

