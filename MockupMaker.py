import configparser
from os import listdir, path
from os.path import isfile, join

from moviepy.editor import *

import config


# Global Variables
default = dict(
    wallpaper = 'MoMoney',
    device = 'iphone',
    color = 'white',
    testing = False,
    input_folder = './_input/',
    input_file = None,
    output_folder = '_output/',
)
settings = {**default, **config.config.settings}

# Device Placement
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
    testing=False
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
        settings['input_folder'] + input
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
    if testing == True:
        duration = 0.5
    else:
        duration = video_clip.duration

    # Temp for testing
    video_clip = video_clip.subclip(0,duration)

    mask_clip = mask_clip.set_duration(duration)
    video_clip = video_clip.set_mask(mask_clip).on_color(
            size=(1920,1080),
            color=(255, 0, 0),
            col_opacity=0,
        )

    export_filename = settings['output_folder']
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
        preset='ultrafast' if testing is True else 'medium',
        ffmpeg_params=[
            '-tune', 'animation',
            '-pix_fmt', 'yuv420p',
            '-crf', '18',
            '-c:a', 'aac',
            '-b:a', '192k',
        ]
    )


def getInputVideos():
    if settings['input_file'] is not None:
        # Render an explicit file
        overlayFootage(
            input=settings['input_file'],
            device=settings['device'],
            color=settings['color'],
            wallpaper=settings['wallpaper'],
            testing=settings['testing'],
        )
    else:
        #Render a Collection of files
        input_files = [
            file for file in listdir(settings['input_folder'])
                if isfile(join(settings['input_folder'], file))
        ]
        print(input_files)

        for file in input_files:
            overlayFootage(
                input=file,
                device=settings['device'],
                color=settings['color'],
                wallpaper=settings['wallpaper'],
                testing=settings['testing'],
            )


# kick it off
getInputVideos()
