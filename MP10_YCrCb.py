import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
import math

file = r'lena512x512.jpg'

img = cv2.imread(file, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)

#Tạo 1 ảnh có cùng kích thước và mode với ảnh PIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang HSI
kenhY = Image.new(imgPIL.mode, imgPIL.size)
kenhCr = Image.new(imgPIL.mode, imgPIL.size)
kenhCb = Image.new(imgPIL.mode, imgPIL.size)
YCrCbImg = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]


for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
        
        Y = np.uint8(16 + 65.738/256*R + 129.057/256*G + 25.064/256*B)
        Cr = np.uint8(128 - 37.945/256*R - 74.494/256*G + 112.439/256*B)
        Cb = np.uint8(128 + 112.439/256*R - 94.154/256*G - 18.285/256*B)
        
        
        
        # Gán giá trị các kênh màu C-M-Y-K vừa tính cho ảnh CMYK
        kenhY.putpixel((x, y), (Y,Y,Y))
        kenhCr.putpixel((x, y), (Cr,Cr,Cr))
        kenhCb.putpixel((x, y), (Cb,Cb,Cb))
        
        YCrCbImg.putpixel((x, y), (Cb,Cr,Y))
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhY = np.array(kenhY)
anhCr = np.array(kenhCr)
anhCb = np.array(kenhCb)
anhYCrCb = np.array(YCrCbImg)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Kenh Y:', anhY)
cv2.imshow('Kenh Cr:', anhCr)
cv2.imshow('Kenh Cb:', anhCb)
cv2.imshow('Kenh YCrCb:', anhYCrCb)


cv2.waitKey(0)
cv2.destroyAllWindows()
