import math
import os.path
import shutil
from os.path import splitext
import sys

from PIL import Image


# import typer
# app = typer.Typer()

# @app.command()
# 裁剪空白透明区域
def crop_blank(file):
    with Image.open(file) as img:
        img2 = img.convert("RGBA")
        bbox = img2.getbbox()
        print(bbox)
        img_cropped = img.crop(bbox)
        img_cropped.save(splitext(file)[0] + "_cropped.png")

# @app.command()
# 透明化背景
def transparent_background(file):
    with Image.open(file) as img:
        img = img.convert("RGBA")
        data = img.getdata()
        newData = []
        (r, g, b) = img.getpixel((0, 0))
        for item in data:
            if item[0] == r and item[1] == g and item[2] == b:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        img.putdata(newData)
        img.save(splitext(file)[0] + "_transparent.png")


# 合并图片
def combine_image(path):
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    _merge_images(files, os.path.join(path + "combine.png"))


def _merge_images(files, output, scale=1.0):
    # COLS = int(input("请输入合并列数："))
    # ROWS = int(input("请输入合并行数："))
    COLS = math.ceil(math.sqrt(len(files)))
    ROWS = math.ceil(len(files) / COLS)
    images = [Image.open(file) for file in files]
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    max_height = max(heights)
    new_img = Image.new('RGB', (max_width * COLS, max_height * ROWS))
    index = 0
    for j in range(ROWS):
        for i in range(COLS):
            if index >= len(images):
                break
            img = images[index]
            new_img.paste(img, (i * max_width, j * max_height))
            index += 1
    new_img = new_img.resize((int(new_img.size[0] * scale), int(new_img.size[1] * scale)))
    new_img.save(output)


def _getbbox(img, alpha_threshold=0.01):
    img = img.copy()
    width, height = img.size
    threshold = 255 * alpha_threshold
    # 遍历图像的每个像素
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if a < threshold:
                img.putpixel((x, y), (255, 255, 255, 0))  # 将透明度小于阈值的像素设置为完全透明

    # 获取图像的边界框（bounding box），去除透明度小于0.1的区域
    return img.getbbox()


# 切分图片
# reverse 逆序切分
def split_image(file, reverse=False):
    COLS = int(input("请输入切分列数："))
    ROWS = int(input("请输入切分行数："))
    results = []
    with Image.open(file) as img:
        width, height = img.size
        min_bbox = None

        for j in range(ROWS):
            for i in range(COLS):
                img_split = img.crop(
                    (i * width // COLS, j * height // ROWS, (i + 1) * width // COLS, (j + 1) * height // ROWS))
                if bbox := img_split.getbbox():  # _getbbox(img_split,0.1):
                    print(i, j, bbox)
                    if min_bbox is None:
                        min_bbox = bbox
                    else:
                        min_bbox = [min(min_bbox[0], bbox[0]), min(min_bbox[1], bbox[1]), max(min_bbox[2], bbox[2]),
                                    max(min_bbox[3], bbox[3])]
                    # img_split = img_split.transpose(Image.FLIP_LEFT_RIGHT) #镜像
                    if reverse:
                        results.insert(0, img_split)
                    else:
                        results.append(img_split)

    # 写文件
    # 创建子目录
    if not os.path.exists(splitext(file)[0]):
        os.makedirs(splitext(file)[0])
    index = 0
    for img in results:
        if min_bbox is not None:
            img = img.crop(min_bbox)
        img.save(splitext(file)[0] + "/" + f"{index}".zfill(2) + ".png")
        index = index + 1

    # 打开文件夹
    # os.system(f"start explorer {splitext(file)[0]}")
    gif = _images_to_gif(splitext(file)[0], 20);
    os.system(f"start explorer {gif}")


# 把git每一帧存为图片
def _gif_to_images(file, MAX_FRAME=32):
    import imageio
    images = imageio.mimread(file)
    image_path = file.split(".")[0]
    # 减少帧数，大致在9~16帧
    images = images[::math.ceil(len(images) / MAX_FRAME)]
    for i, image in enumerate(images):
        imageio.imwrite(splitext(file)[0] + f"_frame_{i}.png", image)

    # 合并图片
    files = [splitext(file)[0] + f"_frame_{i}.png" for i in range(len(images))]

    _merge_images(files, splitext(file)[0] + "_merged.png", 0.5)
    for f in files:
        os.remove(f)
    # 显示图像
    with Image.open(splitext(file)[0] + "_merged.png") as img:
        img.show()


# 把mp4存成图片
def _mp4_to_images(file, MAX_FRAME=32):
    import cv2
    cap = cv2.VideoCapture(file)
    image_path = file.split(".")[0]
    frame_count = 0
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
        frame_count += 1
    frames = frames[::math.ceil(len(frames) / MAX_FRAME)]
    for frame_count, frame in enumerate(frames):
        cv2.imwrite(splitext(file)[0] + f"_frame_{frame_count}.png", frame)
    cap.release()

    # 合并图片
    files = [splitext(file)[0] + f"_frame_{i}.png" for i in range(frame_count)]
    _merge_images(files, splitext(file)[0] + "_merged.png", 0.5)
    for f in files:
        os.remove(f)
    # 显示图像
    with Image.open(splitext(file)[0] + "_merged.png") as img:
        img.show()


def video_to_images(file):
    if file.endswith(".gif"):
        _gif_to_images(file)
    elif file.endswith(".mp4"):
        _mp4_to_images(file)


def _images_to_gif(path, fps=10):
    import imageio.v2 as imageio
    # 遍历path
    images = []
    for file in os.listdir(path):
        if file.endswith(".png"):
            images.append(imageio.imread(os.path.join(path, file)))
    output_file = os.path.join(path + "_output.gif")
    imageio.mimsave(os.path.join(output_file), images, fps=fps)
    return output_file


# def image_to_gif(file):
#     split_image(file)
#     _images_to_gif(splitext(file)[0])
#     shutil.rmtree(splitext(file)[0])


# 对角线镜像
# is_left_bottom=True 以对角线左下方为基准镜像图片，否则以右上方
def _mirror_45(img, is_left_bottom=True):
    # 检查图像是否为正方形，如果不是可以先将其裁剪为正方形
    width, height = img.size
    assert width == height, "图片必须是正方形"
    # 对角线镜像
    img_mirror = img.transpose(Image.TRANSPOSE)
    if is_left_bottom:
        for i in range(width):
            for j in range(i, height):
                img_mirror.putpixel((i, j), img.getpixel((i, j)))
    else:
        for i in range(width):
            for j in range(0, i):
                img_mirror.putpixel((i, j), img.getpixel((i, j)))
    # 保存镜像后的图像
    return img_mirror


# 镜像左右及上下，从一个角生成9宫格填充图片
def mirror_to_9grid(file):
    if not os.path.exists(splitext(file)[0]):
        os.makedirs(splitext(file)[0])
    with Image.open(file) as img:
        width, height = img.size
        if(width/height > 1.9 or height/width > 1.9):
            raise Exception("图片长宽比必须在0.5~2之间")
        hw = width // 2 + 1
        hh = height // 2 + 1
        while (hw % 3 != 0):
            hw = hw - 1
        while (hh % 3 != 0):
            hh = hh - 1
        index = 0
        halfs = [hw,hh]
        for half_index , half in enumerate(halfs):
            # img_corners = [img.crop((0, 0, hw, hh)), img.crop((width - hw, 0, width, hh)).transpose(Image.FLIP_LEFT_RIGHT),
            #                img.crop((0, height - hh, hw, height)).transpose(Image.FLIP_TOP_BOTTOM),
            #                img.crop((width - hw, height - hh, width, height)).transpose(Image.FLIP_LEFT_RIGHT).transpose(
            #                    Image.FLIP_TOP_BOTTOM)]
            img_corners = [img.crop((0, 0, half, half)), img.crop((width - half, 0, width, half)).transpose(Image.FLIP_LEFT_RIGHT),
                           img.crop((0, height - half, half, height)).transpose(Image.FLIP_TOP_BOTTOM),
                           img.crop((width - half, height - half, width, height)).transpose(Image.FLIP_LEFT_RIGHT).transpose(
                               Image.FLIP_TOP_BOTTOM)]
            full = 2*half
            OLD_MOD = False#True
            for img_corner in img_corners:
                print(f"正在生成第{index+1}/{len(img_corners)*len(halfs)}张图片")
                img_corner = _mirror_45(img_corner, half_index == 1)
                if OLD_MOD : #旧的图片格式
                    newImg = Image.new("RGBA", (full*4//3, full), (0, 0, 0, 0))
                else:
                    newImg = Image.new("RGBA", (full*4//3, full*4//3), (0, 0, 0, 0))
                newImg.paste(img_corner, (0, 0))  # 左上
                newImg.paste(img_corner.transpose(Image.FLIP_LEFT_RIGHT), (half, 0))  # 右上
                newImg.paste(img_corner.transpose(Image.FLIP_TOP_BOTTOM), (0, half))  # 左下
                newImg.paste(img_corner.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM), (half, half))  # 右下

                grid = full//3
                if OLD_MOD:
                    centerImg = newImg.crop((grid, grid, grid*2, grid*2))
                    for j in range(3):
                        newImg.paste(centerImg, (full,j * grid))
                else:
                    # 生成凹角图片
                    imgConcave = _mirror_45(newImg.crop((grid,0, grid*2,grid)))
                    newImg.paste(imgConcave, (full, 0))  # 右上凹角
                    newImg.paste(imgConcave.transpose(Image.FLIP_TOP_BOTTOM), (full, grid))  # 右下凹角
                    newImg.paste(imgConcave.transpose(Image.FLIP_LEFT_RIGHT), (0, full))  # 左下凹角
                    newImg.paste(imgConcave.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM), (grid, full))  # 左上凹角

                newImg.save(os.path.join(splitext(file)[0], f"grid_{index}.png"));
                index += 1
    # 打开目录
    os.system(f"start explorer {splitext(file)[0]}")

def main():
    if len(sys.argv) < 2 or (not os.path.exists(sys.argv[1])):
        print("Usage: jimg <file>")
        sys.exit(1)

    # 显示处理选项
    process = [("裁剪空白区域", crop_blank), ("切分图片", split_image), ("合并图片", combine_image),
               ("mp4/gif等视频转图片集", video_to_images), ("透明化背景", transparent_background),
               ("生成上下左右镜像9宫图", mirror_to_9grid)]
    for i, (name, _) in enumerate(process):
        print(f"{i + 1}. {name}")
    choice = 0
    while True:
        choice = input("请选择操作：")
        if not (choice.isdigit() and int(choice) in range(1, len(process) + 1)):
            print("无效的选择")
        else:
            break
    print(f"你选择了 {process[int(choice) - 1][0]}")
    process[int(choice) - 1][1](sys.argv[1])
    print("处理完成")


if __name__ == "__main__":
    main()
