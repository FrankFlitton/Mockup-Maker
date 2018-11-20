from os import listdir, path
from os.path import isfile, join

from moviepy.editor import *


input_folder = './_input/'
output_folder = '_output/'
center_xy = {
    'pixel': (753,136),
    'iphone': (753,136),
}

def overlayFootage(
    input=None,
    wallpaper='MoMoney',
    device='pixel',
    color='white',
):
    # Anayze clip that the composition will be based off of
    video_clip = VideoFileClip(
        input_folder + input
        ).fx(
            vfx.resize,
            height=821
        ).set_position(
            ('center', 'center')
        ).on_color(
            size=(1920,1080),
            color=(0, 0, 0),
            pos=center_xy[device],
            col_opacity=1,
        ).set_position(
            ('center', 'center')
        )

    # set local vars
    duration = video_clip.duration

    wallpaper_img = './img/wallpaper/' + wallpaper + '.jpg'
    device_img = './img/device/' + device.lower() + '/' + color.lower() + '.png'
    mask_img = './img/device/' + device.lower() + '/' + 'mask.png'

    export_filename = output_folder
    export_filename += path.splitext(input)[0]
    export_filename += '-' + device.lower()
    export_filename += '-' + color.lower()
    export_filename += '.mp4'

    # define clipping mask area
    mask_clip = ImageClip(
        mask_img,
        ismask=True,
    )

    # Create video overlay
    wallpaper_clip = ImageClip(
        wallpaper_img
    ).set_duration(
        duration
    ).set_position(
        ('center', 'center')
    )

    device_clip = ImageClip(
        device_img
    ).set_duration(
        duration
    ).set_position(
        ('center', 'center')
    )

    video_clip = video_clip.set_mask(
        mask_clip
    )

    # Stack video clips together
    overlay_clip = CompositeVideoClip(
        clips=[
            wallpaper_clip,
            device_clip,
        ],
    )

    video = CompositeVideoClip(
        [
            # overlay_clip,
            wallpaper_clip,
            device_clip,
            video_clip,
        ],
        use_bgclip=True
    )

    # Export video
    video.write_videofile(
        export_filename,
        codec='mpeg4',
        preset='ultrafast',
    )

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

getInputVideos()
