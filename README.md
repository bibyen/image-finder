# image-finder

Collect all images from a given folder and copy them into another folder!

Hi Mom!

Here's a Python program that accepts the filepaths of two folders:

1. Source folder - the [filepath\*](#how-do-i-get-a-filepath-to-a-folderfile) of the folder that you want to search and copy all images from.

2. Destination folder - the [filepath\*](#how-do-i-get-a-filepath-to-a-folderfile) of the folder that you want to _paste_ all copied images into.

> [_**Wait, how do I get a filepath to a folder/file?**_](#how-do-i-get-a-filepath-to-a-folderfile)
>
> Open up File Explorer and right-click on the file/folder whose filepath you need.
> Copy the filepath into your clipboard by selecting the "copy path" option from the dropdown menu!

## Setting up

### Installing Python

We need Python (version 3.11) installed on your machine before we run the Python program!

When installing Python, we need to select the correct installer for your machine. For WIndows 10+, there are two types of installers; one for 32-bit and another for 64-bit machines.

Here are some instructions that might help you find out which installer you need:

1. Click the Start button.

2. Select Settings.

3. Select System.

4. Select About.

5. Check the bit version on the System type field.

Once you know which version your system needs, download the corresponding installer from the [Python downloads](https://www.python.org/downloads/windows/) website, for Windows.

Run the installer and follow the instructions to finish installing Python on your machine!

### Confirming successful installation of Python 3.11

Launch **Command Prompt** and enter:

    python --version

You should get a message that states your Python version:

<p align="center">
  <img src="assets/confirm-python-installation.png" alt="Example terminal output for successful Python 3.11 installation">
</p>

### Save a copy of the program

Create a text file on your laptop, and name it `image-finder.py`. This is our Python program.

## Running the program

1. Take note of your Python program's filepath. We will refer to this as `<path-to-program>`.

   ### How do I do this?

   1. Launch File Explorer.

   2. Open the folder that had `image-finder.py` in it.

   3. Right-click on your file, and select the "copy path" option. The filepath should now be saved in your clipboard.

2. Launch **Command Prompt** and run the following:

   <path-to-program> <source-folder> <destination-folder>

If any images are found, you should now see a bunch of lines coming up in tis format:

    "Copied: <filepath-of-image> -> <location-of-copied-image>"

Once the program is finished running, you'll see `All done! Check out your newly found images.` printed.

\*Note that `<location-of-copied-image>` is where your image is saved.
