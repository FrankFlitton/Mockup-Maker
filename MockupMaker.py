from os import listdir, path
from os.path import isfile, join

from moviepy.editor import *


input_folder = './_input/'
output_folder = '_output/'
center_xy = {
    'pixel': ('center',136),
    'iphone': ('center',136),
    'android': ('center',136),
}
device_wh = {
    'pixel': [411,821],
    'iphone': [411,821],
    'android': [464,821],
}

def overlayFootage(
    input=None,
    wallpaper='MoMoney',
    device='iphone',
    color='white',
):
    wallpaper_img = './img/wallpaper/' + wallpaper + '.jpg'
    device_img = './img/device/' + device.lower() + '/' + color.lower() + '.png'
    mask_img = './img/device/' + device.lower() + '/' + 'mask.png'

    # define clipping mask area
    mask_clip = ImageClip(
        mask_img,
        ismask=True,
    )

    # Anayze clip that the composition will be based off of
    video_clip = VideoFileClip(
        input_folder + input
        ).fx(
            vfx.resize,
            width=(
                (device_wh[device][0] / device_wh[device][1]) * 1920
            ),
            height=device_wh[device][1],
        ).on_color(
            size=(1920,1080),
            color=(255, 0, 0),
            pos=center_xy[device],
            col_opacity=0,
        )

    # set local vars
    duration = video_clip.duration

    # Temp for testing
    # duration = 0.5
    # video_clip = video_clip.subclip(0,0.5)
    mask_clip = mask_clip.set_duration(duration)
    video_clip = video_clip.set_mask(mask_clip).on_color(
            size=(1920,1080),
            color=(255, 0, 0),
            col_opacity=0,
        )

    export_filename = output_folder
    export_filename += path.splitext(input)[0]
    export_filename += '-' + device.lower()
    export_filename += '-' + color.lower()
    export_filename += '.mp4'


    # Create video overlay
    wallpaper_clip = ImageClip(
        wallpaper_img
    ).set_duration(
        duration
    ).set_position(
        ('center', 'center')
    ).on_color(
        size=(1920,1080),
        color=(0, 0, 0),
        pos='center',
        col_opacity=0,
    )
    wallpaper_clip.fps = 24

    device_clip = ImageClip(
        device_img
    ).set_duration(
        duration
    ).set_position(
        ('center', 'center')
    ).on_color(
        size=(1920,1080),
        color=(0, 0, 0),
        pos='center',
        col_opacity=0,
    )

    # Stack video clips together
    overlay_clip = CompositeVideoClip(
        clips=[
            wallpaper_clip,
            device_clip,
            video_clip,
        ],
        use_bgclip=True
    )

    # Export video
    overlay_clip.write_videofile(
        export_filename,
        codec='h264',
        preset='fast',
        # preset='slow',
        ffmpeg_params=[
            '-tune', 'animation',
        ]
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
