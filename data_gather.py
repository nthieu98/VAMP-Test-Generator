import os
# grid_w, grid_h = 42, 50
# num_bus = 60
# list_num_crit = [10, 25, 50, 100, 200, 300, 400, 500, 1000]
# list_R = [0.50, 1.00, 2.00, 3.00]

def data_gather(inp_data_dir = 'data/', out_data_dir = 'data_set/', grid_w = 42, grid_h = 50, 
                num_bus = 60, list_num_crit = [10], list_R = [1.0]):
  print('Gathering data...')
  for num_crit in list_num_crit:
    for R in list_R:
      src_data_dir = inp_data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      des_data_dir = out_data_dir + str(grid_w) + 'x' + str(grid_h) + '/'
      if not os.path.exists(des_data_dir):
        os.makedirs(des_data_dir)
      
      data_set_file = str(grid_w) + 'x' + str(grid_h) + '_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'
      data_set_dir = des_data_dir + data_set_file
      ds = open(data_set_dir, 'w')
      ds.write(str(grid_w) + ' ' + str(grid_h) + ' ' + '{:0.2f}'.format(R) + '\n')
      ds.write(str(num_bus) + '\n')

      for i in range(1, num_bus + 1):
        bus_loc_file = '{:02d}'.format(i) + '.txt'
        bus_loc_dir = src_data_dir + bus_loc_file

        bus_rf = open(bus_loc_dir, 'r')
        inp = bus_rf.read().split('\n')
        bus_rf.close()
        num_loc = len(inp)
        # reverse line
        # print(num_loc)
        # bus_loc_file_2 = '{:02d}'.format(i) + '-2.txt'
        # bus_loc_dir_2 = src_data_dir + bus_loc_file_2

        # bus_rf_2 = open(bus_loc_dir_2, 'r')
        # inp_2 = bus_rf_2.read().split('\n')
        # bus_rf_2.close()
        # num_loc_2 = len(inp_2)
        # print(num_loc_2)
        
        # total no.location of busline
        # ds.write(str(num_loc + num_loc_2) + '\n')
        ds.write(str(num_loc) + '\n')
        
        # total no.location of busline 1
        ds.write(str(num_loc) + '\n')
        for point in inp:
          ds.write(point + '\n')
        
        
        # total no.location of busline 2
        # ds.write(str(num_loc_2) + '\n')
        # for point in inp_2:
        #   ds.write(point + '\n')
        

      ds.write(str(num_crit) + '\n')
      crit_point_dir = src_data_dir + 'crit_' + str(num_crit) + '_' + '{:0.2f}'.format(R) + '.txt'
      crit_rf = open(crit_point_dir, 'r')
      inp = crit_rf.read().split('\n')
      ds.write('\n'.join(inp))
      crit_rf.close()
      ds.close()
      print(data_set_dir, 'completed')