from os import listdir
from os.path import isfile, join

from moviepy.editor import *


input_folder = './_input/'
output_folder = '_output/'


def overlayFootage(
    input=None,
    overlay='MoMoney',
    device='ios',
):
    clip = VideoFileClip(input_folder + input)
    video = CompositeVideoClip([clip,clip])
    print('tada')
    video.write_videofile("test.mp4")

def getInputVideos():
    input_files = [
        file for file in listdir(input_folder)
            if isfile(join(input_folder, file))
    ]
    print(input_files)

    for file in input_files:
        overlayFootage(
            input=file
        )


# clip = VideoFileClip("myHolidays.mp4")
getInputVideos()
