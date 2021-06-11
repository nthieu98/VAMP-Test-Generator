import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np


# size of gridlines
w, h = 30, 36
# size of image
img_w, img_h = 3500, 4200
num_files = 60
start_file = 1
end_file = 60
test_set = str(w) + 'x' + str(h)

# read data
img_points = []
grid_points = []

for i in range(start_file, end_file + 1):
  file_name = '{:02d}.txt'.format(i)
  wfile_name = '{:02d}-2.txt'.format(i)
  f = open('raw_data/' + file_name, 'r')
  raw_data = f.read().split('\n')
  output = []
  # print(inp)
  for point in reversed(raw_data):
    x, y = point.split(' ')    
    output.append(str(x) + ' ' + str(y))
  wf = open('raw_data/'+ wfile_name, 'w')
  wf.write('\n'.join(output))
  print(file_name + ' completed')

