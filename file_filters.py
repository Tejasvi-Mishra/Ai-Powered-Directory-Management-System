import os
import datetime

def filter_by_size(file_path, size_limit_mb=1):
    """Filters files based on size (default: files larger than 1 MB)."""
    file_size = os.path.getsize(file_path) / (1024 * 1024)  # Convert to MB
    return file_size >= size_limit_mb

def filter_by_date(file_path, days_limit=30):
    """Filters files based on the modification date (default: last 30 days)."""
    file_mtime = os.path.getmtime(file_path)
    file_date = datetime.datetime.fromtimestamp(file_mtime)
    return (datetime.datetime.now() - file_date).days <= days_limit
