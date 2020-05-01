# brailler

## What is brailler?
brailler is software that you can put onto a Raspberry Pi to make a hand-held controller that will interpret an alphabetical English text file into a Braille output, as well as interpret a Braille input into an alphabetical English text file.

In the likely event you do not have a Braille controller, you can also use this software as a wrapper for the LibLouis library. Read plaintext alphabetical files into braille on your console. Practice writing braille into alphabetical English.

[Here is the example schematic for a Braille interface.](docs/brailler.png) Note that the motors are outputs and the pushbuttons are inputs. This is connected in the same manner as written in the program.

## Program Functions
 - Take Braille unicode input and write it to a text file in alphabetical English
 - Open a text file and print out a Braille unicode translation
 - User can choose to perform this program using a command line interface, or using a braille interface

## Running this program
1. Install LibLouis on the device
2. Setup LibLouis for Python
3. Install and setup this program (brailler)
3. Ways to run:
    - `make cli` runs the app in the console
    - `make braille` runs the app in the Braille mode (for use with the Raspberry Pi)
    - `make fastbraille` runs the app in the Braille mode but does not check pip requirements
    - `make test` runs the pytest
    - `make coverage` runs the pytest and checks how much code has been tested

## Installing LibLouis for Python

#### Install LibLouis
1. Ensure your device has the following packages using `apt` or equivalent
	`sudo apt-get install autoconf m4 libtool perl pkg-config`
2. Clone (or download) the latest tarball from the LibLouis Github releases
	```shell
	mkdir louis
	cd louis
	git clone https://github.com/liblouis/liblouis.git
	git tag
	git checkout v3.13.0
	git branch -l
	```
3. Navigate into the LibLouis folder
	```shell
	cd liblouis/
	```
4. In terminal run the following commands in order to install LibLouis
	```shell
	sudo ./autogen.sh
	sudo ./configure
	sudo make
	sudo make install
	sudo /sbin/ldconfig -v
	```
6. The following command should now work in terminal:
	`echo this is a test sentence | lou_translate unicode.dis,en-ueb-g2.ctb`

#### Python setup for LibLouis
1. Ensure your device has the following packages using `apt` or equivalent
	```shell
	sudo apt install python3-distutils
	```
2. In terminal go to python folder `cd ~/Documents/LibLouis/liblouis-.../python`
3. Install python binding with `sudo python3 setup.py install`
4. The following python snippet should now work, demonstrating a successful installation:

	```python
	import louis

	a_test = louis.translate(['unicode.dis', 'en-ueb-g2.ctb'], "a test string")
	print(a_test[0])
	```

	More information on the available methods and their parameters 
		is found in liblouis.../python/__init__.py

## Installing this program
1. Ensure your device has the following packages using `apt` or equivalent
	```shell
	sudo apt install python3-pip python3-env
	```
2. Clone or download this repository
	```shell
	mkdir brailler
	cd brailler
	git clone https://github.com/callumfrance/brailler.git
	```
3. Install the requirement packages (alternatively rely on venv exclusively)
	```shell
	pip3 install -r requirements.txt
	```
4. Create a directory for the programs virtual environment to run inside of
	```shell
	python3 -m venv venv
	```

## How to get this program to run on startup on a Raspberry Pi
If you want to run this program as the first thing that happens when you power 
on a Raspberry Pi device (as intended), you can do the following. Note that this
advice applies to the Raspbian Lite (console view, not desktop view).

First, edit the `raspi-config` to not require a login.

Next, you need to edit the file `rc.local`. Ensure that the exit condition, if
present, is removed or commented out, and add the following line to the bottom
of the file:
	```
	(cd home/pi/brailler && make Braille)
	```
This will run program, provided that the directory you have installed it in is
`home/pi/brailler/`.
