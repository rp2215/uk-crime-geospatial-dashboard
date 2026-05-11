from . import config
import pandas as pd

# Find every CSV file in data/raw (subfolders as well)
def find_csv_files(raw_data_dir):

    csv_files = sorted(raw_data_dir.rglob("*.csv"))

    return csv_files

# Read one csv file into dataframe
def read_csv_file(file_path):

    data_frame = pd.read_csv(file_path,usecols=config.REQUIRED_COLUMNS, low_memory=False)
    data_frame["source_file"] = file_path.name # stores where each row came from

    return data_frame

# Load all raw CSV files and combine into one dataframe
def read_raw_csvs():

    files = find_csv_files(config.RAW_DATA_DIR)
    num_files_found = len(files)

    frames = []
    skipped_files = []

    if not files:
        print("No CSV files found in data/raw")
        return pd.DataFrame()
    
    print(f"Found {num_files_found} CSV file(s).")

    for file_path in files:
        try:
            # read and add to list
            data_frame = read_csv_file(file_path)
            frames.append(data_frame)
            print(f"Loaded {file_path.name} with: {len(data_frame)} row(s)")

        except Exception as error:
            # report any errors
            skipped_files.append(file_path.name)
            print(f"Skipped {file_path.name} error: {error}")

    # every file failed to load
    if not frames:
        print("No usable CSV files were loaded")
        return pd.DataFrame()
    
    combined_dataframes = pd.concat(frames, ignore_index=True)

    print("Loading Complete")

    print(f"Files Found: {num_files_found}")
    print(f"Files Loaded: {len(frames)}")
    print(f"Files Skipped: {len(skipped_files)}")

    print(f"Rows Loaded: {len(combined_dataframes):,}")

    return combined_dataframes


# Run this file directly for a quick test
if __name__ == "__main__":

    raw_data = read_raw_csvs()  # Load all raw CSV files

    print(raw_data.head())  # Show the first five rows

    print(raw_data.shape)  # Show the number of rows and columns