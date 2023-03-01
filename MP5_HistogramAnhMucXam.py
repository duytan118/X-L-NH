import cv2
from PIL import Image #thư viện ảnh pillow hỗ trợ nhiều định dạng ảnh
import numpy as np
import matplotlib.pyplot as plt # thư viện vẽ biểu đồ


# Hàm chuyển chuyển đổi ảnh màu sang ảnh mức xám
# theo phương pháp Luminance
def ChuyenDoiAnhMauSangAnhMucXamLuminance(imgPIL):
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
        
            gray = np.uint8(0.2126*R+0.7152*G+0.0722*B)
            
            # Gán giá trị mức xám vừa tính cho ảnh xám
            avg.putpixel((x, y), (gray, gray, gray))

    return avg


#Hàm tính histogram của ảnh xám
def TinhHistogram(AnhxamPIL):
    # Mỗi pixel có giá trị từ 0 - 255, nên phải khia báo 1 mảng có giá trị 256 phần tử để chứa số đếm của các pixel có cùng giá trị
    his =  np.zeros(256)
    # Kích thước ảnh
    w = AnhxamPIL.size[0]
    h = AnhxamPIL.size[1]
    for x in range (w):
        for y in range (h):
            # Lấy giá trị xám tại điểm (x, y)
            gR, gG, gB = AnhxamPIL.getpixel((x,y)) # ảnh xám nên giá trị gray 3 kênh màu như nhau
            # Giá trị gray tính ra cũng chính là phần tử thứ gray trong mảng his đã khai báo, sẽ tăng số đếm của phần tử thứ gray lên 1
            his[gR] += 1
    return his


# Vẽ biểu đồ Histogram dùng tư viện matplotlib
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh xám',figsize = (((w, h))), dpi = 100)        
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, his, color = 'orange')
    plt.title('Biểu đồ histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()
    
    
# Chương trình chính, các hàm con phải khai báo trước khi chương trình chính gọi


# Khai báo đường dẫn file hinh
file = r'bird_small.jpg'

#Đọc ảnh màu dùng thư viện PIL, Ảnh PIL này chúng ta sẽ dùng để thực hiện các tác vụ xử lý và tính toán thay vì opencv
imgPIL = Image.open(file)

# Chuyển sang ảnh mức xám
AnhXamPIL = ChuyenDoiAnhMauSangAnhMucXamLuminance(imgPIL)

#Tính histogram
his = TinhHistogram(AnhXamPIL)

# Chuyển từ imgPIL sang img trên opencv để hiển thị bằng opencv
anhmucxam = np.array(AnhXamPIL)

cv2.imshow('Anh muc xam:', anhmucxam)

#Vẽ biểu đồ histogram
VeBieuDoHistogram(his)

cv2.waitKey(0)
cv2.destroyAllWindows()

    