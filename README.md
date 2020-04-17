# brailler

## What is brailler?
brailler is software that you can put onto a Raspberry Pi Zero W to make a hand-held controller that will interpret an alphabetical English text file into a Braille output, as well as interpret a Braille input into an alphabetical English text file.

In the likely event you do not have a Braille controller, you can also use this software as a wrapper for the LibLouis library. Read plaintext alphabetical files into braille on your console. Practice writing braille into alphabetical English.

## Program Goals
 The goal is to get the software to be able to:
 1. Take Braille unicode input and write it to a new text file in alphabetical English.
 2. Open a text file and print out a Braille unicode translation.
 3. Allow a user to choose the input/output method (raspberry pi embedded system or CLI). The whole program should be representable in both methods.
 4. Code tests, makefile, documentation, (relatively) easy install and portability

## Running this program
1. Download repo
2. Install LibLouis on the device (see below)
3. Ways to run:
    - `make cli` runs the app in the console
    - `make braille` runs the app in the Braille mode (for use with the Raspberry Pi)
    - `make fastbraille` runs the app in the Braille mode but does not check pip requirements
    - `make test` runs the pytest
    - `make coverage` runs the pytest and checks how much code has been tested

## Installing LibLouis

1. Downloaded the lateest tarball from the LibLouis Github releases
2. Extracted into the folder ~/Documents/LibLouis
3. In terminal run `./configure` inside the install folder you just extracted
4. Next, in the same location in terminal run `make`
5. Likewise, then run `sudo make install`

	The following command should now work in terminal:
	`echo this is a test sentence | lou_translate unicode.dis,en-ueb-g2.ctb`

6. In terminal go to python folder `cd ~/Documents/LibLouis/liblouis-.../python`
7. Install python binding with `sudo python3 setup.py install`

	The following python snippet should now work, demonstrating a successful installation:

	```python
	import louis

	a_test = louis.translate(['unicode.dis', 'en-ueb-g2.ctb'], "a test string")
	print(a_test[0])
	```

	More information on the available methods and their parameters 
		is found in liblouis.../python/__init__.py
