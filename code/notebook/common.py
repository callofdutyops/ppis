import os

# constants
R = 8.314 / 4184

# dir and path: dir -> a folder, path: a file
# base data dir
data_dir = "../../data"

# raw data
skempi_dir = os.path.join(data_dir, "skempi_v2")
skempi_pdbs_dir = os.path.join(skempi_dir, "PDBs")
skempi_csv_path = os.path.join(skempi_dir, "skempi_v2.csv")
pdb_ext = "pdb"

# processed data
processed_data_dir = os.path.join(data_dir, "processed")
delta_g_path = os.path.join(processed_data_dir, "delta_g.csv")
id_seq_path = os.path.join(processed_data_dir, "id_seq.csv")