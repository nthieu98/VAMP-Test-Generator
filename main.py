import gen_image
import gen_filled_square
import conver_data
import gen_critical_point
import data_gather
import gen_all

def main():
  pixel_data_dir = 'raw_data/'
  cord_data_dir = 'data/'
  data_set_dir = 'data_set/'
  image_map = 'image_bus_map/'
  image_each_bus_dir = 'image_bus/'
  image_each_bus_filled_square_dir = 'image_set_filled_square/'
  image_w, image_h = 3500, 4200
  grid_w, grid_h = 42, 50
  list_num_crit = [50]
  list_R = [0.5]
  num_bus = 5
  conver_data.convert_pixel_to_cordinate(pixel_data_dir, cord_data_dir, image_w, image_h, grid_w, grid_h, num_bus, 1, num_bus)
  gen_critical_point.gen_critical_point(cord_data_dir, grid_w, grid_h, num_bus, list_num_crit, list_R)
  gen_image.gen_image_for_each_bus(cord_data_dir, image_each_bus_dir, grid_w, grid_h, num_bus, list_num_crit, list_R)
  gen_filled_square.gen_image_with_filled_square(cord_data_dir, image_each_bus_filled_square_dir, grid_w, grid_h, num_bus, list_num_crit[0], list_R[0])
  gen_all.gen_all(cord_data_dir, image_map, grid_w, grid_h, num_bus, list_num_crit, list_R)
  data_gather.data_gather(cord_data_dir, data_set_dir, grid_w, grid_h, num_bus, list_num_crit, list_R)
main()