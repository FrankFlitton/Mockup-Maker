# Mockup Maker

> A tool to set up video screen captures on a device mockup.

## Usage

Place videos to render into the `_input/` folder. Make sure the app screen touches the top and bottom of the video feed.

Run the following in terminal to start the video editing process. It can take 20 or more minutes to render.

```
python MockupMaker.py
```

By default your video will be rendered on a white iPhone X on a green background.

There are `white` and `blank` colors for `pixel`, `android` (wide pixel), and `iPhone`.

You can find your rendered video in the `_output/` folder.

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

`python --version` should read `3.3.6`

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

- Config File
- More backgrounds
- GUI
- Freeze and export as desktop app