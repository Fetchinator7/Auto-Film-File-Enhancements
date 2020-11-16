#### This is a simple script for automatically normalizing clip audio and sorting out short clips. I use use this to sort through my footage after filming lots of clips.

This is built off of the [FFmpeg-Commands](https://github.com/Fetchinator7/FFmpeg-Commands) repo so this could get far more customized by incorporating some more of those methods since this only uses a fraction of that functionality.

## Installation

### Mac

All the dependencies can be installed using the [Homebrew](https://brew.sh/) package manager in a terminal window.

```shell
brew install git
brew install python3
brew install ffmpeg
```

### Windows

After [installing git](https://git-scm.com/download/win) all the dependencies can be installed using the [Chocolatey](https://chocolatey.org/install) package manager in a terminal window.

```shell
choco install python -y
choco install ffmpeg -y
```

### Both

In a terminal window, type `cd ` (with a space afterward), drag-and-drop the folder on your computer where you want to store this project on top of the terminal window, (this will add any escape characters) and press enter.
Since you have `git` now (it's one of the dependencies) clone the project by entering `git clone https://github.com/Fetchinator7/Auto-Film-File-Enhancements.git`. Next **change directory** into the project folder by entering `cd ` (with a space afterward) again, use the **tab** button to autocomplete the folder path, and import the submodules by entering `git submodule update --init --recursive`.

(If you're having issues running the project try entering `git pull --recurse-submodules` in case there were any updates to the submodules.)

## Running

Enter `python3 ` (with a space afterward), drag-and-drop the `auto_compress_video_files.py` file on the terminal, and press enter. This can of course be triggered other ways like a folder action but I won't go into that here.
