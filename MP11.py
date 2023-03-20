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
Mask3x3 = Image.new(imgPIL.mode, imgPIL.size)
Mask5x5 = Image.new(imgPIL.mode, imgPIL.size)
Mask7x7 = Image.new(imgPIL.mode, imgPIL.size)
Mask9x9 = Image.new(imgPIL.mode, imgPIL.size)

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
                
                Rs +=R
                Gs +=G
                Bs +=B
            
        K = 3*3
        Rs = np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs = np.uint8(Bs/K)
        
        #Set điểm làm mượt vào ảnh
        Mask3x3.putpixel((x,y),(Bs,Gs,Rs))
        
        


for x in range (2, width-2):
    for y in range (2, height-2):
        
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        #biến này dùng để chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        
        #Tiến hành quét các điểm có trong mặt nạ
        for i in range (x-2, x+3):
            for j in range (y-2, y+3):
                R, G, B = imgPIL.getpixel((i,j))
                
                Rs +=R
                Gs +=G
                Bs +=B
            
        K = 5*5
        Rs = np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs = np.uint8(Bs/K)
        
        #Set điểm làm mượt vào ảnh
        Mask5x5.putpixel((x,y),(Bs,Gs,Rs))
        
        

for x in range (3, width-3):
    for y in range (3, height-3):
        
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        #biến này dùng để chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        
        #Tiến hành quét các điểm có trong mặt nạ
        for i in range (x-3, x+4):
            for j in range (y-3, y+4):
                R, G, B = imgPIL.getpixel((i,j))
                
                Rs +=R
                Gs +=G
                Bs +=B
            
        K = 7*7
        Rs = np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs = np.uint8(Bs/K)
        
        #Set điểm làm mượt vào ảnh
        Mask7x7.putpixel((x,y),(Bs,Gs,Rs))
        
        
        
        
for x in range (4, width-4):
    for y in range (4, height-4):
        
        # Lấy giá trị điểm ảnh tại vị trí (x,y)
        #biến này dùng để chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        
        #Tiến hành quét các điểm có trong mặt nạ
        for i in range (x-4, x+5):
            for j in range (y-4, y+5):
                R, G, B = imgPIL.getpixel((i,j))
                
                Rs +=R
                Gs +=G
                Bs +=B
            
        K = 9*9
        Rs = np.uint8(Rs/K)
        Gs = np.uint8(Gs/K)
        Bs = np.uint8(Bs/K)
        
        #Set điểm làm mượt vào ảnh
        Mask9x9.putpixel((x,y),(Bs,Gs,Rs))
        

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anh3 = np.array(Mask3x3)
anh5 = np.array(Mask5x5)
anh7 = np.array(Mask7x7)
anh9 = np.array(Mask9x9)

cv2.imshow('Anh mau RGB goc co gai Lena:', img)
cv2.imshow('Lam muot anh mask 3x3:', anh3)
cv2.imshow('Lam muot anh mask 3x3:', anh5)
cv2.imshow('Lam muot anh mask 3x3:', anh7)
cv2.imshow('Lam muot anh mask 3x3:', anh9)


cv2.waitKey(0)
cv2.destroyAllWindows()
