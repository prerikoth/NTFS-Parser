**NTFS Parser**

This is a NTFS Parser written in python3.

The program will find the MFT, iterate over it's listings and their $FILE_NAME. When the correct file is found it's $DATA attribute will be printed.

**Usage**

(1) Open the command line as an admin

(2) 
```diff
$ python3 main.py --file=hosts --disk=C -v -t
[] Searching for file hosts...
[] Found it!
[] hosts's contents:

b"# Copyright (c) 1993-2009 Microsoft Corp.\r\n#\r\n# This is a sample HOSTS file used by Microsoft TCP/IP...'

[] Parser finished execution, runtime -> 3.2952680587768555s...

Process finished with exit code 0
```

@Nitzan Adut
