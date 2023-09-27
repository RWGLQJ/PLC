import cv2

# 读取图片
image = cv2.imread('mb.jpg')

# 缩小图片
width = int(image.shape[1] * 0.5)
height = int(image.shape[0] * 0.5)
resized_image = cv2.resize(image, (width, height))

# 在打开的图片上点击鼠标选择文本所在的区域
# 这里会打开一个窗口显示缩小后的图片，请在窗口上点击鼠标选择矩形区域

# 定义回调函数，处理鼠标事件
def mouse_callback(event, x, y, flags, param):
    # 当鼠标左键按下时
    if event == cv2.EVENT_LBUTTONDOWN:
        # 记录鼠标按下的坐标并还原到原始图片的尺寸
        original_x = int(x * 2)
        original_y = int(y * 2)
        print("文字的横坐标：", original_x)
        print("文字的纵坐标：", original_y)

# 创建窗口并将回调函数与窗口绑定
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

# 在窗口中显示缩小后的图片
cv2.imshow('image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()