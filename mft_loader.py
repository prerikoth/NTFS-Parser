from constants import MFT_ENTRY_SIZE, SECTOR_SIZE, DATA_TYPE
from attribute_parser import AttributeParser
from physical_drive import PhysicalDrive
from sector_reader import SectorReader
from mft_entry import MFTEntry
from data_attribute import DataAttribute


class MFTLoader:
    def __init__(self):
        self.drive = PhysicalDrive(0)
        self.sector_reader = SectorReader(r'\\.\physicaldrive0')
        self.mft = self._load_mft()

    def _load_mft(self):
        mft_entry = self.sector_reader.read_from(self.drive.locate_largest_partition_mft_starting_sector()
                                                 + self.drive.locate_largest_partition_vbr_offset(),
                                                 round(MFT_ENTRY_SIZE / SECTOR_SIZE))
        data_attribute = AttributeParser.get_attribute(DATA_TYPE, MFTEntry(mft_entry))

        return DataAttribute(data_attribute,
                             self.drive.locate_largest_partition_sectors_per_cluster(),
                             self.drive.locate_largest_partition_vbr_offset()).get_data()
