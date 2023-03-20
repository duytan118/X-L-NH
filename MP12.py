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
matran = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])

#Lấy kích thước của ảnh từ imgPIL
width = imgPIL.size[0]
height = imgPIL.size[1]


for x in range (1, width-1):
    for y in range (1, height-1):
        
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        #biến này dùng để chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        
        #Tiến hành quét các điểm có trong mặt nạ
        for i in range (x-1, x+2):
            for j in range (y-1, y+2):
                R, G, B = imgPIL.getpixel((i,j))
                
                Rs +=R*matran[i - x + 1, j - y + 1]
                Gs +=G*matran[i-x+1,j-y+1]
                Bs +=B*matran[i-x+1,j-y+1]
            
        R1, G1, B1 = imgPIL.getpixel((x,y))
        SharpeR = R1+Rs
        SharpeG = G1+Gs
        SharpeB = B1+Bs
        
        
        if (SharpeR<0):
            SharpeR = 0
        elif(SharpeR > 255):
            SharpeR = 255
        if (SharpeG < 0):
            SharpeG = 0
        elif (SharpeG > 255):
            SharpeG = 255
        if (SharpeB < 0):
            SharpeB = 0
        elif (SharpeB > 255):
            SharpeB = 255;
        #Set điểm làm mượt vào ảnh
        Sharpe.putpixel((x,y),(SharpeB,SharpeG,SharpeR))
        
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anh3 = np.array(Sharpe)


cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Lam muot anh mask 3x3:', anh3)


cv2.waitKey(0)
cv2.destroyAllWindows()
