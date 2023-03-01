import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
import matplotlib.pyplot as plt # thư viện vẽ biểu đồ


# Khai báo đường dẫn file hinh
file = r'bird_small.jpg'

# Đọc ảnh màu dùng thư viện opencv
img = cv2.imread(file, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)




#Hàm tính histogram của ảnh mau
def TinhHistogram(AnhxamPIL):
    # Mỗi pixel có giá trị từ 0 - 255, nên phải khia báo 1 mảng có giá trị 256 phần tử để chứa số đếm của các pixel có cùng giá trị
    hisR = np.zeros(256)
    hisG = np.zeros(256)
    hisB = np.zeros(256)
    # Kích thước ảnh
    w = AnhxamPIL.size[0]
    h = AnhxamPIL.size[1]
    for x in range (w):
        for y in range (h):
            # Lấy giá trị xám tại điểm (x, y)
            gR, gG, gB = imgPIL.getpixel((x,y)) # ảnh xám nên giá trị gray 3 kênh màu như nhau
            # Giá trị gray tính ra cũng chính là phần tử thứ gray trong mảng his đã khai báo, sẽ tăng số đếm của phần tử thứ gray lên 1
            hisR[gR] += 1
            hisG[gG] += 1
            hisB[gB] += 1
    return hisR, hisG, hisB


# Vẽ biểu đồ Histogram dùng tư viện matplotlib
def VeBieuDoHistogram(hisR, hisG, hisB):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh mau',figsize = (((w, h))), dpi = 100)        
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, hisR, color = 'red')
    plt.plot(trucX, hisG, color = 'green')
    plt.plot(trucX, hisB, color = 'blue')
    plt.title('Biểu đồ histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()
    
    


# Khai báo đường dẫn file hinh
file = r'bird_small.jpg'

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)



#Tính histogram
hisR, hisG, hisB = TinhHistogram(imgPIL)

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhmau = np.array(imgPIL)

cv2.imshow('Anh mau:', img)

#Vẽ biểu đồ histogram
VeBieuDoHistogram(hisR, hisG, hisB)

cv2.waitKey(0)
cv2.destroyAllWindows()

    