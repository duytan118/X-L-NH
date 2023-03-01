import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
file = r'lena512x512.jpg'
img = cv2.imread(file, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)

#Tạo 1 ảnh có cùng kích thước và mode với ảnh PIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Grayscale
avg = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = avg.size[0]
height = avg.size[1]


for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
        
        Max = max(R, G, B)
        Min = min(R, G, B)
        gray = np.uint8((Min+Max)/2)
        
        # Gán giá trị mức xám vừa tính cho ảnh xám
        avg.putpixel((x, y), (gray, gray, gray))

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhmucxam = np.array(avg)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Anh muc xam Lightness:', anhmucxam)

cv2.waitKey(0)
cv2.destroyAllWindows()
