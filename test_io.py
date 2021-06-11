def plus(a, b):
  return a + b

list_crit_point = []
num_crit_point = 20
R = 2
grid_w, grid_h = 10, 12
num_bus = 60
# point = namedtuple('point', ['x', 'y'])

file_name = 'crit_' + str(num_crit_point) + '_' + '{:0.2f}'.format(R) + '.txt'
test_set = 'data/' + str(grid_w) + 'x' + str(grid_h) + '/'
src_data_dir = 'data/' + str(grid_w) + 'x' + str(grid_h) + '/'

f = open(test_set + '//' + file_name, 'w')
f.write('1')
f.close()