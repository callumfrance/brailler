# brailler

## Program Goals
 The goal is to get the software to be able to:
 1. Take braille unicode input and write it to a new text file in alphabetical English.
 2. Open a text file and print out a braille unicode translation.
 3. Allow a user to choose the input/output method (raspberry pi embedded system or CLI). The whole program should be representable in both methods.
 4. Code tests, makefile, documentation, easy install and portability

## Running this program
1. Download repo
2. Ways to run:
    - `make cli` runs the app in the console
    - `make braille` runs the app in the braille mode (for use with the Raspberry Pi)
    - `make test` runs the pytest
    - `make coverage` runs the pytest and checks how much code has been tested

## Installing LibLouis

1. Downloaded tarball from Github releases
2. Extracted into the folder ~/Documents/LibLouis
3. In terminal ran `./configure`
4. In terminal ran `make`
5. In terminal ran `sudo make install`

	The following command should now work in terminal:
	`echo "test" | lou_translate unicode.dis,en-gb-g1.utb`

6. In terminal go to python folder `cd ~/Documents/LibLouis/liblouis-.../python`
7. Install python binding with `sudo python3 setup.py install`

	The following python snippet should now work:

	```python
	import louis

	a_test = louis.translate(['unicode.dis', 'en-gb-g1.utb'], "a test string")
	print(a_test[0])
	```

	More information on the available methods and their parameters 
		is found in liblouis.../python/__init__.py
