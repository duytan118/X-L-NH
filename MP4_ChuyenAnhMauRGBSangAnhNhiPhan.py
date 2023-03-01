import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
file = r'lena512x512.jpg'
img = cv2.imread(file, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)

#Tạo 1 ảnh có cùng kích thước và mode với ảnh PIL
#Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Binary
binary = Image.new(imgPIL.mode, imgPIL.size)

#Lấy kích thước của ảnh từ imgPIL
width = binary.size[0]
height = binary.size[1]

# Thiết lập một giá trị ngưỡng để tính điểm ảnh nhị phân
nguong = 130

for x in range (width):
    for y in range (height):
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        R, G, B = imgPIL.getpixel((x, y))
       
        gray = np.uint8(0.2126*R+0.7152*G+0.0722*B)
        
        # Xác định giá trị điểm nhị phân
        if (gray < nguong):
            binary.putpixel((x, y), (0, 0, 0))
        else:
            binary.putpixel((x, y), (255, 255, 255))

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhnhiphan = np.array(binary)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Anh nhi phan (Binary): ', anhnhiphan)

cv2.waitKey(0)
cv2.destroyAllWindows()
