from collections import namedtuple
import numpy as np

square = namedtuple('square', ['x', 'y', 'w'])
point = namedtuple('point', ['x', 'y'])

def check_position(square, point, r, eps=0.000001):
  # -1: out
  # 1: on/in
  
  circleDistance_x = abs(point.x - square.x)
  circleDistance_y = abs(point.y - square.y)

  

  if circleDistance_x > (square.w/2 + r):
    return -1
  if circleDistance_y > (square.w/2 + r):
    return -1

  if circleDistance_x == (square.w/2):
    return 1
  if circleDistance_y == (square.w/2):
    return 1
  
  if circleDistance_x < (square.w/2):
    return 1
  if circleDistance_y < (square.w/2):
    return 1

  cornerDistance_sq = pow(circleDistance_x - square.w/2, 2) + pow(circleDistance_y - square.w/2, 2)
  if cornerDistance_sq - pow(r, 2) > eps:
    return -1
  elif cornerDistance_sq - pow(r, 2) < eps:
    return 1
  return 1

def check_2_out(square, r, fpoint, spoint, step = 0.01, eps = 0.000001):
  sign_x = 1 if fpoint.x < spoint.x else -1
  for x in np.arange(fpoint.x, spoint.x + step, step * sign_x):
    y = (spoint.y - fpoint.y) * (x - fpoint.x) / (spoint.x - fpoint.x) + fpoint.y
    if check_position(square, point(x, y), r) == 1:
      return 2
  
  sign_y = 1 if fpoint.y < spoint.y else -1
  for y in np.arange(fpoint.y, spoint.y + step, step * sign_y):
    x = (spoint.x - fpoint.x) * (y - fpoint.y) / (spoint.y - fpoint.y) + fpoint.x
    if check_position(square, point(x, y), r) == 1:
      return 2
  return 0

def check_2_segment(point, w, list_points, r):
  sqr = square(point.x, point.y, w)
  num_collision = 0
  n = len(list_points)
  fp = check_position(sqr, list_points[0], r)
  if fp == 2:
    num_collision = 1
  for i in range(1, n):
    sp = check_position(sqr, list_points[i], r)
    if fp * sp < 0:
      num_collision += 1
    elif fp == -1 and sp == -1:
      # col_1 = check_2_out(sqr, r, list_points[i], list_points[i-1], 1.0)
      # if col_1 == 2:
      #   num_collision += col_1
      # else:
      #   col_01 = check_2_out(sqr, r, list_points[i], list_points[i-1], 0.1)
      #   if col_01 == 2:
      #     num_collision += col_01
      #   else:
      col_001 = check_2_out(sqr, r, list_points[i], list_points[i-1], 0.01)
      num_collision += col_001
      # num_collision += check_2_out(sqr, r, list_points[i], list_points[i-1])
    fp = sp
    if num_collision > 2:
      return False
  return True

if __name__ == "__main__":
    # 1.13 7.27
    # 3.00 7.29
    # 1, 6
    # 6.47 4.13
    # 5.28 4.12
    # 7.93 6.22
    # 8.30 5.17
    # 6.48 3.89
    # 6 5
    # print(check_position(square(1.5, 6.5, 0.5), point(1.13, 7.27), 1.00))
    # print(check_position(square(1.5, 6.5, 0.5), point(3.00, 7.29), 1.00))
    print(check_position(square(6.5, 5.5, 1), point(7.93, 6.22), 1.00))
    print(check_position(square(6.5, 5.5, 1), point(8.30, 5.17), 1.00))
    print(check_position(square(6.5, 5.5, 1), point(6.48, 3.89), 1.00))
    print(check_position(square(6.5, 5.5, 1), point(6.47, 4.13), 1.00))
    print(check_position(square(6.5, 5.5, 1), point(5.28, 4.12), 1.00))