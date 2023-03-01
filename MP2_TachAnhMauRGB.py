import cv2
import numpy as np


#Đọc ảnh màu dùng thư viện OpenCV
img  = cv2.imread('lena512x512.jpg', cv2.IMREAD_COLOR)


#Lấy kích thước của ảnh
height = len(img[0])
width = len(img[1])

#Khai báo 3 biến để chứa hình 3 kênh R, G, B
red  = np.zeros((width, height, 3), np.uint8)    #Số 3 là 3 kênh R, G, B, mỗi kênh 8bit
green  = np.zeros((width, height, 3), np.uint8)
blue  = np.zeros((width, height, 3), np.uint8)

#Ban đầu set zero cho tất cả điểm ảnh có trong cả 3 kênh trong mỗi hình
red[:] = [0, 0, 0]
green[:] = [0, 0, 0]
blue[:] = [0, 0, 0]

#Mỗi hình là một ma trận 2 chiều nên sẽ dùng 2 vòng lặp for để đọc hết tất cả điểm ảnh (pixel) có trong hình
for x in range(width):
    for y in range(height):
        #Lấy giá trị điểm ảnh tại vị trí (x, y)
        R = img[x, y, 2]
        G = img[x, y, 1]
        B = img[x, y, 0]

        #Thiết lập màu cho các kênh R, G, B
        red[x, y, 2] = R
        green[x, y, 1] = G
        blue[x, y, 0] = B

#Hiển thị hình dùng thư viện OpenCV
cv2.imshow('Nhom 15 sang thu 2 hinh mau RGB goc:', img)
cv2.imshow('Nhom 15 sang thu 2 Kenh red', red)
cv2.imshow('Nhom 15 sang thu 2 Kenh green', green)
cv2.imshow('Nhom 15 sang thu 2 Kenh blue', blue)



#Bấm phím bất kỳ để đóng cửa sổ hiển thị hình
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ hiển thị hình
cv2.destroyAllWindows()

