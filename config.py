#     _______________
#    |,----------.  |\
#    ||  Mockup   |=| |
#    ||  Maker   || | |
#    ||       . _o| | |
#    |`-----------' |/
#     ~~~~~~~~~~~~~~~
#
#   Make sure to read Reamme.Md before
#   going any further.
#
#   Once this is configured run the script with
#   $ python MockupMaker.py
#

class config():
    settings = dict(
        # Controls the device.
        # Must be in 'quotes'
        device = 'iphone',

        # Controls the device varient.
        # Options are 'white', 'black'
        # Must be in 'quotes'
        color = 'white',

        # Controls the background graphic (jpg).
        # Options are 'MoMoney', 'MagneticArrows'
        # Must be in 'quotes'
        wallpaper = 'MoMoney',

        # Which folder to read videos from.
        # Must be in 'quotes'
        input_folder = './_input/',

        # Enables single file mode.
        # Either None or '/path/to/MyFile.mp4'
        # Must NOT be in 'quotes' if None
        input_file = None,

        # Which folder to save videos to.
        # Must be in 'quotes'
        output_folder = '_output/',

        # Useful if you're testing a new background.
        # True or False.
        # Must NOT be in 'quotes'
        testing = False,
    )
