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
kenhX = Image.new(imgPIL.mode, imgPIL.size)
kenhY = Image.new(imgPIL.mode, imgPIL.size)
kenhZ = Image.new(imgPIL.mode, imgPIL.size)
XYZImg = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]


for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
        
        X = np.uint8(0.4124564*R + 0.3575761*G + 0.1804375*B)
        Y = np.uint8(0.2126729*R + 0.7151522*G + 0.0721750*B)
        Z = np.uint8(0.0193339*R + 0.1191920*G + 0.9503041*B)
        
        
        
        # Gán giá trị các kênh màu C-M-Y-K vừa tính cho ảnh CMYK
        kenhX.putpixel((x, y), (X,X,X))
        kenhY.putpixel((x, y), (Y,Y,Y))
        kenhZ.putpixel((x, y), (Z,Z,Z))
        
        XYZImg.putpixel((x, y), (Z,Y,X))
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhX = np.array(kenhX)
anhY = np.array(kenhY)
anhZ = np.array(kenhZ)
anhXYZ = np.array(XYZImg)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Kenh X:', anhX)
cv2.imshow('Kenh Y:', anhY)
cv2.imshow('Kenh Z:', anhZ)
cv2.imshow('Kenh XYZ:', anhXYZ)


cv2.waitKey(0)
cv2.destroyAllWindows()
