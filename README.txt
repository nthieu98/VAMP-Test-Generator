Ngôn ngữ: Python 3
Môi trường: Window 10

Các chương trình trong bộ sinh test:
* get_pixel.py: Chương trình đọc pixel trên ảnh
- Chạy trực tiếp file sau khi sửa đường dẫn đến ảnh và thư mục lưu trữ
- Thư mục mặc định là raw_data
- Mỗi tuyến bus được lưu trong 1 file riêng

* main.py: Chương trình chính

* conver_data.py: Chương trình đổi toạ độ từ pixel ra toạ độ thực theo kích thước lưới
- Toạ độ sau khi đổi được lưu ra thư mục data
- Mỗi tuyến bus được lưu trong 1 file riêng
- Tham số đầu vào: 
	+ thư mục nguồn, đích, 
	+ kích thước ảnh, 
	+ kích thước lưới, 
	+ số tuyến bus

* gen_critical.py: Chương trình sinh ngẫu nhiên critical point trong lưới
- Danh sách các điểm được lưu trong thư mục data với tiền tố 'crit'
- Tham số đầu vào: 
	+ thư mục nguồn dữ liệu
	+ kích thước lưới
	+ số tuyến bus
	+ danh sách số điểm critical cần sinh 
	+ danh sách bán kính sensor

* gen_image.py: Chương trình sinh ảnh minh hoạ cho từng tuyến bus với vùng tương tác giữa sensor và critical point
- Ảnh được lưu ở thư mục image_bus
- Tham số đầu vào:
	+ thư mục dữ liệu nguồn, đích
	+ kích thước lưới
	+ số tuyến bus
	+ danh sách số điểm critical cần sinh 
	+ danh sách bán kính sensor


* gen_filled_square.py: Chương trình sinh ảnh minh hoạ cho từng tuyến bus và các điểm critical point
- Ảnh được lưu ở thư mục image_bus
- Tham số đầu vào:
	+ thư mục dữ liệu nguồn, đích
	+ kích thước lưới
	+ số tuyến bus
	+ số điểm critical cần sinh (ko phải dạng list)
	+ bán kính sensor (ko phải dạng list)
	
* gen_all.py: Chương trình sinh ảnh minh hoạ cho tất cả tuyến bus với vùng tương tác giữa sensor và critical point
- Ảnh được lưu ở thư mục image_bus
- Tham số đầu vào:
	+ thư mục dữ liệu nguồn, đích
	+ kích thước lưới
	+ số tuyến bus
	+ số điểm critical cần sinh (ko phải dạng list)
	+ bán kính sensor (ko phải dạng list)
	
* gather_data.py: Chương trình tổng hợp dữ liệu về 1 file
- Thư mục mặc định data_set
- Định dạng được mô tả trong file README_input_format.txt
**********
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