import os
import shutil
import argparse

# Function to copy image files from source_dir to destination_dir
def copy_images(source_dir, destination_dir):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

    for root, _, files in os.walk(source_dir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                destination_path = os.path.join(destination_dir, relative_path)

                # Ensure the destination directory structure exists
                os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                # Copy the image file to the destination directory
                shutil.copy2(source_path, destination_path)
                print("Copied: {} -> {}".format(source_path, destination_path))
    
    print("All done! Check out your newly found images.")

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy image files from a source directory to a destination directory.")
    parser.add_argument("source_directory", help="Source directory containing image files")
    parser.add_argument("destination_directory", help="Destination directory where image files will be copied")
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    source_directory = args.source_directory
    destination_directory = args.destination_directory

    if not os.path.exists(source_directory):
        print("Source directory does not exist.")
    else:
        copy_images(source_directory, destination_directory)
        print("Image copy process completed.")

if __name__ == "__main__":
    main()
