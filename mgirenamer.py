import os
import glob
import shutil
import argparse


def rename_files(source_directory, destination_directory, flowcell, lane):
    # Destination file name pattern
    destination_pattern = "{}_S{}_L001_R{}_001.fastq.gz"

    # Get the list of files that follow the original pattern in the source directory
    original_pattern = f"{flowcell}_{lane}_*.fq.gz"
    original_files = glob.glob(os.path.join(source_directory, original_pattern))

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_directory, exist_ok=True)

    # Dictionary to map identification number (ID) with the S number
    s_number = {}

    # Rename and write the files
    for original_file in original_files:
        # Extract the file name without extension
        file_name, extension = os.path.splitext(
            os.path.basename(original_file).split(".")[0]
        )

        # Extract the identification number from the original file
        identification_number = file_name.split("_")[2]

        # Check if the identification number already exists in the dictionary
        if identification_number in s_number:
            # Retrieve the S number associated with the identification number
            current_s_number = s_number[identification_number]
        else:
            # Get the next available S number
            current_s_number = len(s_number) + 1
            # Add the S number to the dictionary for the identification number
            s_number[identification_number] = current_s_number

        # Extract the read number from the original file
        read_number = file_name.split("_")[3]

        # Construct the new file name with the correct extension
        new_name = destination_pattern.format(
            identification_number, current_s_number, read_number
        )

        # Get the full path for the original file
        source_path = os.path.join(source_directory, original_file)

        # Get the full path for the destination file
        destination_path = os.path.join(destination_directory, new_name)

        # Copy the original file to the destination directory with the new name
        shutil.copyfile(source_path, destination_path)

        print(
            f"File renamed and written to {destination_directory}: {original_file} -> {new_name}"
        )

    print("Renaming and writing completed.")


def main():
    parser = argparse.ArgumentParser(description="Rename files in a directory")
    parser.add_argument("source_directory", help="Directory with the original files")
    parser.add_argument(
        "destination_directory", help="Destination directory for renamed files"
    )
    parser.add_argument("flowcell", help="Flowcell ID")
    parser.add_argument("lane", help="Lane ID, e.g., L01")
    args = parser.parse_args()

    source_directory = args.source_directory
    destination_directory = args.destination_directory
    flowcell = args.flowcell
    lane = args.lane

    rename_files(source_directory, destination_directory, flowcell, lane)


if __name__ == "__main__":
    main()

