# Mockup Maker

> A tool to set up video screen captures on a device mockup.

```
     _______________
    |,----------.  |\
    ||  Mockup   |=| |
    ||  Maker   || | |
    ||       . _o| | |
    |`-----------' |/
     ~~~~~~~~~~~~~~~

```

## Usage

Place videos to render into the `_input/` folder. Make sure the app screen touches the top and bottom of the video feed.

Run the following in terminal to start the video editing process. It can take 20 or more minutes to render.

```
python MockupMaker.py
```

By default your video will be rendered on a white iPhone X on a green background.

There are `white` and `blank` colors for `pixel`, `android` (wide pixel), and `iPhone`.

You can find your rendered video in the `_output/` folder.

### Attributes

Edit the `config.py` file to set up the render for your project.

```python
settings = dict(
    device = 'iphone',
    color = 'white',
    wallpaper = 'MoMoney',
    input_folder = './_input/',
    input_file = None,
    trim_start = 0,
    trim_end = 0,
    output_folder = '_output/',
    testing = True,
)
```

#### Device

> The mockup of the pysical device to impose the mockup video on.

Options:

* `'iphone'`
* `'pixel'`
* `'android'`

#### Color

> Variant of device graphic

Options:

* `'black'`
* `'white'`

#### Wallpaper

> The background image

Options:

* `'MoMoney'`
* `'MagneticArrows'`
* `'White'`

#### Input Folder

> Directory where the raw files are located.

#### Input File

> Render a specific file. Leave blank to render all files in the directory.

#### Trim Start

> Remove X seconds of footage from the start of the input file.

#### Trim End

> Remove X seconds of footage from the end of the input file.

#### Output Folder

> Directory where the rendered files are saved.

#### Testing

> Render a 0.5s clip fast to verify that your output file looks right.


## Installation

### Requirements

Requires python 3! I recomend using pyenv to install python 3.6.6 for this folder.

To install pyEnv paste the following for an installer.

```
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Once it's installed, use:

```
    pyenv install 3.6.6
    pyenv local 3.6.6
    python --version
```

`python --version` should read `3.6.6`

### Install the video utilities

Navigate to the folder in terminal and run the following. You can drop the folder into terminal from finder to get the path.

```
    cd pash/to/my/folder/
    pip install -r ./requirements.txt
```

You may also need to install FFmpeg. Instructions (If you need homebrew) http://macappstore.org/ffmpeg/

```
    brew install ffmpeg
```

## TODO

* More backgrounds
* GUI (may need to wait for new version of PyQt for latest OSX)
* Freeze and export as desktop app
