#### This is a simple script for automatically normalizing clip audio and sorting out short clips. I use use this to sort through my footage after filming lots of clips.

This is built from the [FFmpeg-Commands](https://github.com/Fetchinator7/FFmpeg-Commands) repo so this could get far more customized by incorporating some more of those methods since this only uses a fraction of that functionality.

## Installation

### Mac

All the dependencies can be installed using the [Homebrew](https://brew.sh/) package manager in a terminal window.

```shell
brew install git
brew install python3
brew install ffmpeg
```

In a terminal window, type `cd ` (with a space afterward), drag-and-drop the folder on your computer where you want to store this project on top of the terminal window, (this will add any escape characters) and press enter.

### Windows

After [installing git](https://git-scm.com/download/win) install the `ffmpeg` dependency by using the [Chocolatey](https://chocolatey.org/install) package manager in a terminal window.

```shell
choco install ffmpeg -y
```

If you don't already have python, enter `python` in the terminal window and this should open the Microsoft Store so then you can complete the installation process. Whichever version to download it shows is fine, but feel free to select the latest version.

Open a new `File Explorer` window, navigate to the folder on your computer where you want to store this project and select `file` > `Open Windows Powershell` > `Open Windows Powershell` (optionally `Open Windows Powershell as administrator`)

### **Both**

Since you have `git` now (it's one of the dependencies) clone the project by entering `git clone https://github.com/Fetchinator7/Auto-Film-File-Enhancements.git`. Next **change directory** into the project folder by entering `cd ` (with a space afterward) again, use the **tab** button to autocomplete the folder path before entering, and import the submodules by entering `git submodule update --init --recursive`.

## Running It

### **Both**

**NOTE:** Be sure you have some files in the `In` folder or else it won't look like it's doing anything since there's nothing for it to process.

(If you're having issues running the project try entering `git pull --recurse-submodules` in case there were any updates to the submodules.)

### Mac

Enter `python3 ` (with a space afterward), drag-and-drop the `auto_compress_video_files.py` file on the terminal or, type `au` and **tab,** then press enter. This can of course be triggered other ways like a folder action but I won't go into that here.

### Windows

Enter `au`, **tab** complete the path to the `auto_compress_video_files.py` file so then you can press enter. If a window pops up asking for an application to open choose python and check the box to have it always use this application for `.py` files. (The window only stays open while it's running.)
