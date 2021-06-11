import random
import check_collision
from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
# square = namedtuple('square', ['x', 'y', 'w'])
# circle = namedtuple('circle', ['x', 'y', 'r'])

def check_constraint(col, row, list_bus, r, check_constraint_toggle):
  if check_constraint_toggle == False:
    return True
  for bus_line in list_bus:
    p = point(float(col + 0.5), float(row + 0.5))
    if check_collision.check_2_segment(p, 1.00, bus_line, r) == False:
      return False
  return True

# list_num_crit_point = [10, 25, 50, 100, 200, 300, 400, 500, 1000]
# list_R = [0.50, 1.00, 2.00, 3.00]
# grid_w, grid_h = 42, 50
# num_bus = 60

def gen_critical_point(data_dir = 'data/', grid_w = 10, grid_h = 12, num_bus = 60,
                       list_num_crit_point = [10], list_R = [1.0]):
  for num_crit_point in list_num_crit_point:
    for R in list_R:
      file_name = 'crit_' + str(num_crit_point) + '_' + '{:0.2f}'.format(R) + '.txt'
      test_set = data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      src_data_dir = data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      list_bus = []

      for i in range(1, num_bus + 1):
        bus_loc_file = '{:02d}'.format(i) + '.txt'
        bus_loc_dir = src_data_dir + bus_loc_file
        bus_rf = open(bus_loc_dir, 'r')
        inp = bus_rf.read().split('\n')
        new_line = []
        for line in inp:
          x, y = line.split(' ')
          new_line.append(point(float(x), float(y)))
        list_bus.append(new_line)
        bus_rf.close()

      list_crit_point = []
      fail_point = []
      check_constraint_toggle = False

      for i in range(num_crit_point):
        while(1):
          col = random.randrange(0, grid_w)
          row = random.randrange(0, grid_h)
          new_point = str(col) + ' ' + str(row)
          # print(len(fail_point))
          if new_point in fail_point:
            continue
          if new_point not in list_crit_point:
            if check_constraint(col, row, list_bus, R, check_constraint_toggle):
              list_crit_point.append(new_point)
              print('get', i, '-th point:', new_point)
              break
            else:
              fail_point.append(new_point)

      wf = open(test_set + '/' + file_name, 'w')
      wf.write('\n'.join(list_crit_point))
      wf.close()
      print(file_name + ' completed')
      print('test set', num_crit_point, R, 'completed')