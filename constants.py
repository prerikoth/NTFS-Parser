"""
I grouped all the constants in one file because some
constants are relevant to multiple classes.
"""

UNALLOCATED_ENTRY = b'\x01'
NO_SUCH_ATTRIBUTE = b'\x02'
DIRECTORY = b'\x03'
FAILURE = b'\x01'
READ_ENTIRE_MFT = b'\xff'
FILE_NAME_TYPE = 0x30
DATA_TYPE = 0x80
SECTOR_SIZE = 512
VBR_OFFSET = 1161216
CHUNK_SIZE = 1000
FILE_NAME_LENGTH = 0x58
FILE_NAME_DATA = 0x5a
DATA_LENGTH = 0x10
DATA_ATTRIBUTE_DATA = 0x18
ENTRY_INUSE = 0x16
ENTRY_DIRECTORY = 0x17
FIRST_ATTRIBUTE_OFFSET = 0x14
END_OF_ENTRY = 0xffffffff
IS_NON_RESIDENT_ATTRIBUTE = 0x8
RUN_LIST_OFFSET = 0x20
