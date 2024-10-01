import numpy as np
from CSIKit.reader import get_reader
from CSIKit.util import csitools

file_path = 'example_csi_data/40mhz_1600085286.pcap'
reader = get_reader(file_path)
csi_data = reader.read_file(file_path, scaled=True)
csi_matrix, no_frames, no_subcarriers = csitools.get_CSI(csi_data)
print(csi_matrix)
print(no_frames)
print(no_subcarriers)
