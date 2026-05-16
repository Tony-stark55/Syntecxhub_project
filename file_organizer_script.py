from pathlib import Path
import shutil


# File type mapping
FILE_TYPES = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".txt": "TextFiles",
    ".py": "Code",
    ".docx": "Documents"
}


# Folder path
folder_path = Path("PracticeFolder")


# Read all files
for file in folder_path.iterdir():

    # Skip folders
    if file.is_dir():
        continue

    # Get extension
    extension = file.suffix.lower()

    # Decide destination folder
    folder_name = FILE_TYPES.get(extension, "Others")

    # Create destination folder
    destination_folder = folder_path / folder_name
    destination_folder.mkdir(exist_ok=True)

    # Final destination
    destination_file = destination_folder / file.name

    # Move file
    shutil.move(str(file), str(destination_file))

    print(f"Moved {file.name} → {folder_name}")