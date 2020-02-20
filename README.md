# brailler

Maps text to braille characters.

## Running this program
1. Download repo
2. Ways to run:
    - `make all` runs the app in the console
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
7. Install python binding with `sudo python setup.py install`

	The following python snippet should now work:

	```python
	import louis

	a_test = louis.translate(['unicode.dis', 'en-gb-g1.utb'], "a test string")
	print(a_test[0])
	```

	More information on the available methods and their parameters 
		is found in liblouis.../python/__init__.py
