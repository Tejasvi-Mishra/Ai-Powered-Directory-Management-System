from collections import defaultdict
import shutil
import os
from file_filters import filter_by_size, filter_by_date  # Import filters

FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".py", ".java", ".cpp", ".html"],
    "Others": []
}

def categorize_files(directory, progress_var, file_count_var, selected_categories, summary_var, size_filter, date_filter):
    file_map = defaultdict(list)
    files_in_dir = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    total_files = len(files_in_dir)
    processed_files = 0

    # Apply filters (now handled by functions in file_filters.py)
    filtered_files = [
        file for file in files_in_dir
        if (not size_filter.get() or filter_by_size(os.path.join(directory, file))) and
           (not date_filter.get() or filter_by_date(os.path.join(directory, file)))
    ]

    total_files = len(filtered_files)  # Update after filtering

    for file in filtered_files:
        file_path = os.path.join(directory, file)
        _, extension = os.path.splitext(file)
        categorized = False

        for category, extensions in FILE_CATEGORIES.items():
            if extension.lower() in extensions and selected_categories[category].get() == 1:
                file_map[category].append(file_path)
                categorized = True
                break
        if not categorized and selected_categories["Others"].get() == 1:
            file_map["Others"].append(file_path)

        processed_files += 1
        progress_var.set((processed_files / total_files) * 100)
        file_count_var.set(f"Files Processed: {processed_files}/{total_files}")

    summary = "Files Organized:\n"
    for category, files in file_map.items():
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)
        for file_path in files:
            try:
                shutil.move(file_path, category_folder)
            except Exception as e:
                summary += f"Failed to move {file_path}: {str(e)}\n"
                continue

        summary += f"{category}: {len(files)} files\n"

    summary_var.set(summary)
