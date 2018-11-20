from os import listdir
from os.path import isfile, join

from moviepy.editor import *


input_folder = './_input/'
output_folder = '_output/'


def overlayFootage(
    input=None,
    wallpaper='MoMoney',
    device='pixel',
    color='white',
):
    video_clip = VideoFileClip(
        input_folder + input
        ).fx(
            vfx.resize,
            height=821
        ).set_position(
            ('center', 'center')
        )
    duration = video_clip.duration

    wallpaper_img = './img/wallpaper/' + wallpaper + '.jpg'
    device_img = './img/device/' + device.lower() + '/' + color.lower() + '.png'
    mask_img = './img/device/' + device.lower() + '/' + 'mask.png   '

    mask_clip = ImageClip(
        device_img,
        ismask=True,
    )

    wallpaper_clip = ImageClip(
        img=wallpaper_img,
        ismask=False,
        transparent=True,
    ).set_duration(
        duration
    ).set_mask(
        mask_clip
    )

    device_clip = ImageClip(
        device_img
    ).set_duration(
        duration
    ).set_mask(
        mask_clip
    )


    video = CompositeVideoClip(
        [
            video_clip,
            wallpaper_clip,
            device_clip,
        ]
    )

    video.write_videofile(
        "test.mp4",
        codec='mpeg4',
        preset='slow',
    )

def getInputVideos():
    input_files = [
        file for file in listdir(input_folder)
            if isfile(join(input_folder, file))
    ]
    print(input_files)

    # for file in input_files:
    #     overlayFootage(
    #         input=file
    #     )
    overlayFootage(
        input=input_files[0]
    )

# clip = VideoFileClip("myHolidays.mp4")
getInputVideos()
