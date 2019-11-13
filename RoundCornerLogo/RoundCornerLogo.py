from PIL import Image
#aggdraw http://www.effbot.org/zone/pythondoc-aggdraw.htm
import aggdraw
import os


def AddBackGround(image):
    width, height = image.size
    background = Image.new('RGBA', image.size,(255,255,255))
    image = image.convert('RGBA')
    background.paste(image, (0, 0, width, height), image)
    # out = Image.blend(image,background,0.5)
    return background

def round_corner_percent(image, CornerSize ,percent = True):
    """generate round corner for image"""
    width, height = image.size
    mask = CreatRoundCornerMask(width,height,CornerSize)
    image = image.convert('RGBA')
    image.putalpha(mask)
    return image

def CreatRoundCornerMask(width,height,CornerSize ,percent = True):
    mask = Image.new('L', (width,height))  # filled with black by default
    draw = aggdraw.Draw(mask)
    draw.setantialias(True)
    brush = aggdraw.Brush('white')
    if True == percent:
        radius = int(width * CornerSize)
    else:
        radius = int(CornerSize)
    # 生成四个圆角
    # upper-left corner
    draw.pieslice((0, 0, radius * 2, radius * 2), 90, 180, None, brush)
    # upper-right corner
    draw.pieslice((width - radius * 2, 0, width, radius * 2), 0, 90, None, brush)
    # bottom-left corner
    draw.pieslice((0, height - radius * 2, radius * 2, height), 180, 270, None, brush)
    # bottom-right corner
    draw.pieslice((width - radius * 2, height - radius * 2, width, height), 270, 360, None, brush)
    # center rectangle  #生成中间区域
    draw.rectangle((radius, radius, width - radius, height - radius), brush)
    # four edge rectangle   #生成四边矩形区域
    draw.rectangle((radius, 0, width - radius, radius), brush)
    draw.rectangle((0, radius, radius, height - radius), brush)
    draw.rectangle((radius, height - radius, width - radius, height), brush)
    draw.rectangle((width - radius, radius, width, height - radius), brush)
    # 更新关联的图像。如果绘图区域附加到PIL Image对象，则必须调用此方法以确保图像已更新。
    draw.flush()
    return mask


def get_filePath_fileName_fileExt(fileUrl):
    """
    获取文件路径， 文件名， 后缀名
    :param fileUrl:
    :return:
    """
    filepath, tmpfilename = os.path.split(fileUrl)
    shotname, extension = os.path.splitext(tmpfilename)
    return filepath, shotname, extension

def CreatError(ErrMsg):
    rt = [False]
    rt.append(ErrMsg)
    return rt

def MakeDir(path = ''):
    rt = path
    if None != path:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except:
                rt = CreatError("创建文件夹失败")
    return rt


if __name__ == '__main__':
    data_path = './input/'
    noBackGround_pic = './input/NoEdge/'
    outDir = MakeDir("./output/")
    img_list = os.listdir(data_path)
    for item in img_list:
        imgName = os.path.splitext(item)
        # print(imgName)
        if imgName[1] == '.png' or imgName[1] == '.jpg':
            im = Image.open(data_path+item)
            im = round_corner_percent(im, 0.225)
            im.save(outDir+"/"+os.path.basename(imgName[0])+'_round.png')
    img_list = os.listdir(noBackGround_pic)
    for item in img_list:
        imgName = os.path.splitext(item)
        # print(imgName)
        if imgName[1] == '.png' or imgName[1] == '.jpg':
            im = Image.open(noBackGround_pic+item)
            im = AddBackGround(im)
            im = round_corner_percent(im, 0.225)
            im.save(outDir+"/"+os.path.basename(imgName[0])+'_round.png')