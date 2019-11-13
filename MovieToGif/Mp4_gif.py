from moviepy.editor import *
import matplotlib.pyplot as plt
from moviepy.editor import TextClip
# print ( TextClip.list("font") )

FONT_URL = r'simfang.ttf'

begin = 1.2
end = 4.5
time = end - begin

clip = (VideoFileClip(r"J:\\Desktop\\1.mp4").resize(1))#.subclip(begin,end)
# txt_clip = (TextClip('加油',fontsize=25,color='blue',font = FONT_URL,kerning = 10).set_position('bottom').set_duration(time))
# clip = CompositeVideoClip([clip, txt_clip]) # Overlay text on video
tempFrame = clip.get_frame(1.2)
plt.imshow(tempFrame) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()

# clip.speedx(2).write_gif(r"J:\\Desktop\\1.gif")

# print(video.size())

# TotalLen = 0
# for frame in clip.iter_frames(fps=clip.fps, logger=None, dtype='uint8'):
#     TotalLen += len(frame)
#
# print(float(TotalLen)/8/1024)