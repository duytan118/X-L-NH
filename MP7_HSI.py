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
Hue = Image.new(imgPIL.mode, imgPIL.size)
Saturation = Image.new(imgPIL.mode, imgPIL.size)
Intensity = Image.new(imgPIL.mode, imgPIL.size)
HSIImg = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]


for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
        
        
        #các công thức
        tu = ((R-G)+(R-B))/2
        mau = math.sqrt((R-G)*(R-G) + (R-B)*(G-B))
        theta = math.acos(tu/mau)
        
        H = 0
        
        if B<=G:
            H = theta
        else: 
            H = 2*math.pi - theta

        #chuyển đổi H sang độ(degree)
        H = np.uint8(H*180/math.pi)
            
        S = 1 - 3*(min(R, G, B))/(R + G + B)
        S = np.uint8(S*255)
            
        I = (R+G+B)/3
            
            
            
        
        # Gán giá trị các kênh màu C-M-Y-K vừa tính cho ảnh CMYK
        Hue.putpixel((x, y), (int(H), int(H), int(H)))
        Saturation.putpixel((x, y), (int(S), int(S), int(S)))
        Intensity.putpixel((x, y), (int(I), int(I), int(I)))
        
        HSIImg.putpixel((x, y), (int(I), int(S), int(H)))
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhH = np.array(Hue)
anhS = np.array(Saturation)
anhI = np.array(Intensity)
anhHSI = np.array(HSIImg)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Kenh Hue:', anhH)
cv2.imshow('Kenh Saturation:', anhS)
cv2.imshow('Kenh Intensity:', anhI)
cv2.imshow('Kenh HSI:', anhHSI)


cv2.waitKey(0)
cv2.destroyAllWindows()
