import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
file = r'lena512x512.jpg'

img = cv2.imread(file, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)

#Tạo 1 ảnh có cùng kích thước và mode với ảnh PIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang CMYK
Cyan = Image.new(imgPIL.mode, imgPIL.size)
Magenta = Image.new(imgPIL.mode, imgPIL.size)
Yellow = Image.new(imgPIL.mode, imgPIL.size)
Black = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]


for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
        
        # Gán giá trị các kênh màu C-M-Y-K vừa tính cho ảnh CMYK
        Cyan.putpixel((x, y), (B, G, 0))
        Magenta.putpixel((x, y), (B, 0, R))
        Yellow.putpixel((x, y), (0, G, R))
        
        K = min(R, G, B)
        Black.putpixel((x, y), (K, K, K))
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhCyan = np.array(Cyan)
anhMagenta = np.array(Magenta)
anhYellow = np.array(Yellow)
anhBlack = np.array(Black)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Kenh Cyan:', anhCyan)
cv2.imshow('Kenh Magenta:', anhMagenta)
cv2.imshow('Kenh Yellow:', anhYellow)
cv2.imshow('Kenh Black:', anhBlack)


cv2.waitKey(0)
cv2.destroyAllWindows()
