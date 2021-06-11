Mô tả input:
Tên file: WxH_n_R.txt
	- lưới có kích thước WxH
	- trên lưới có n critical point
	- bán kính sensor là R
Mỗi file gồm:
	- 2 số nguyên W H, 1 số thực R: độ rộng, độ dài của lưới, bán kính của sensor
		(W, H, R<= 50)
	- 1 số nguyên num_bus: số lượng tuyến xe bus
	- 1 số nguyên num_point_i: số lượng các điểm mô tả tuyến xe bus thứ i
	- num_point_i dòng tiếp theo, mỗi dòng gồm 2 số thực x, y: hoành độ, tung độ của các điểm mô tả
		(0 <= x <= W,0 <= y <= H)
	- 1 số nguyên num_crit_point: số lượng điểm cần theo dõi
	- num_crit_point dòng tiếp theo, mỗi dòng gồm 2 số nguyên c, r: tọa độ cột, hàng của các ô cần theo dõi
		(0 <= c < W, 0 <= r < H) 

