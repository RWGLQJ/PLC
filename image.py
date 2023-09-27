import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
import textwrap

def generate_image():
    # 获取用户输入的信息
    text_content = {}
    text_content["姓名"] = name_entry.get()
    text_content["性别"] = gender_entry.get()
    text_content["民族"] = minzu_entry.get()
    text_content["出生日期"] = birth_entry.get()
    text_content["身份证号码"] = id_entry.get()
    text_content["户口地"] = address_entry.get()

    # 打开原始图片
    background_image = Image.open("mb.jpg")

    # 创建一个用于绘制文字的ImageDraw对象
    draw = ImageDraw.Draw(background_image)

    # 指定文本的字体和字号
    font = ImageFont.truetype("Arial.ttf", 30)

    # 指定文本的颜色
    text_color = (0, 0, 0)  # RGB格式，此处为黑色

    # 指定每个文本的位置和间距
    positions = [
        (732, 430),   # 姓名的位置
        (732, 506),   # 性别的位置
        (732, 576),   # 民族位置
        (726, 646),   # 出生日期的位置
        (728, 712),   # 身份证号码的位置
        (728, 790)    # 户口地的位置
    ]

    # 去掉指定的文本
    for i in range(len(positions)-1):
        draw.line([(positions[i][0], positions[i][1]+80), (positions[i+1][0]+300, positions[i+1][1]+80)], fill=(255, 255, 255), width=0)
        if i < len(positions)-1:
            draw.line([(positions[i][0], positions[i][1]+80), (positions[i+1][0]+300, positions[i+1][1]+80)], fill=(255, 255, 255), width=3)

    # 在指定位置绘制每个文本
    for key, position in zip(text_content.keys(), positions):
        text = f"{text_content[key]}"
        # 对文本进行换行处理
        wrapped_text = textwrap.fill(text, width=10)
        draw.text(position, wrapped_text, fill=text_color, font=font)

    # 获取用户输入的要添加的图片地址
    overlay_image_path = image_entry.get()

    # 打开要添加的图片
    overlay_image = Image.open(overlay_image_path)

    # 指定要添加图片的位置和尺寸
    position = (34, 426)  # 要添加图片的左上角位置坐标
    width = 300  # 要添加图片的宽度，高度会按比例自动调整

    # 计算调整后的高度，保持比例不变
    aspect_ratio = overlay_image.width / overlay_image.height
    height = int(width / aspect_ratio)

    # 调整图片大小
    overlay_image.thumbnail((width, height))

    # 添加图片到原始图片上
    background_image.paste(overlay_image, position)

    # 保存修改后的图片
    background_image.save("output.jpg")

    result_label.config(text="已生成图片：output.jpg")

# 创建GUI窗口
window = tk.Tk()
window.title("生成图片")
window.geometry("400x400")

# 姓名输入框
name_label = tk.Label(window, text="姓名：")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# 性别输入框
gender_label = tk.Label(window, text="性别：")
gender_label.pack()
gender_entry = tk.Entry(window)
gender_entry.pack()

# 民族输入框
minzu_label = tk.Label(window, text="民族：")
minzu_label.pack()
minzu_entry = tk.Entry(window)
minzu_entry.pack()

# 出生日期输入框
birth_label = tk.Label(window, text="出生日期：")
birth_label.pack()
birth_entry = tk.Entry(window)
birth_entry.pack()

# 身份证号码输入框
id_label = tk.Label(window, text="身份证号码：")
id_label.pack()
id_entry = tk.Entry(window)
id_entry.pack()

# 户口地输入框
address_label = tk.Label(window, text="户口地：")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()

# 图片地址输入框
image_label = tk.Label(window, text="图片地址：")
image_label.pack()
image_entry = tk.Entry(window)
image_entry.pack()

# 生成图片按钮
generate_button = tk.Button(window, text="生成图片", command=generate_image)
generate_button.pack()

# 显示结果标签
result_label = tk.Label(window, text="")
result_label.pack()

# 运行GUI窗口
window.mainloop()
