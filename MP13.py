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
Sharpe = Image.new(imgPIL.mode, imgPIL.size)

#Ma trận thay thế để tính cho phương pháp laplician
matran = ([[0,-1,0],[-1,4,-1],[0,-1,0]])

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]

#khai báo ngưỡng và xy
X1 = 80
X2 = 150
Y1 = 400
Y2 = 500
nguong = 45

Rs = 0
Gs = 0
Bs = 0

for x in range (X1, X2):
    for y in range (Y1, Y2):
        
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        #biến này dùng để chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        
        R, G, B = imgPIL.getpixel((x,y))
                
        Rs +=R
        Gs +=G
        Bs +=B
        
    #size = (x2-x1+1)*(y2-y1+1)
    size = np.abs(X2-X1)*np.abs(Y2-Y1)
        
    Rs /=size
    Gs /=size
    Bs /=size
    
    for x in range (width):
        for y in range (height):
            R1, G1, B1 = imgPIL.getpixel((x,y))
            
            D = np.sqrt((R1-Rs)**2+(G1-Gs)**2+(B1-Bs)**2)

            
            if D <= nguong:
                Sharpe.putpixel((x, y),(255, 255, 255))
            else:
                Sharpe.putpixel((x, y),(B1,G1,R1))
            
# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anh3 = np.array(Sharpe)


cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Lam muot anh mask 3x3:', anh3)


cv2.waitKey(0)
cv2.destroyAllWindows()
