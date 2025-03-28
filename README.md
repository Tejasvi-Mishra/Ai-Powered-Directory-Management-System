# Ai-Powered-Directory-Management-System
An intuitive Python-based application that organizes files in a selected folder using AI-powered logic and user-defined filters. This system categorizes files into different types, applies filters based on size and date, and provides a clean, automated directory structure to improve folder management.
🔑 Key Features
File Categorization: Automatically organizes files into predefined categories (Images, Videos, Documents, etc.).
User Filters:
Filter by File Size: Include files larger than a specified size (default: 1 MB).
Filter by Last Modified Date: Include files modified within the last 30 days (configurable).
GUI Interface: User-friendly Tkinter-based GUI with checkboxes, progress tracking, and file organization buttons.
Themes: Light and dark mode support for better usability.
Keyboard Shortcuts: Access key functions quickly using keyboard shortcuts.
Modular Code Structure: Functions are separated into modules for better readability and maintainability.
🛠 Installation Guide
Clone the Repository:

git clone <repository_url>
cd AI-Directory-Manager
Install Dependencies:
Ensure you have Python 3.x installed. Then, run the following command:

pip install -r requirements.txt  # (if applicable)
🚀 How to Use
Run the Application:
Launch the application by running:

python main.py
Select a Folder:
Click the "Select Folder and Organize Files" button to choose the folder you want to organize.

Apply Filters:

Size Filter: Optionally filter files larger than the specified size (default: 1 MB).
Date Filter: Optionally filter files modified within the last 30 days.
Track Progress:
Monitor file processing through the on-screen progress bar.

Switch Themes:
Toggle between light mode and dark mode for a better visual experience.

📂 Project Structure (Diagrammatic View)
Below is the directory structure of the project and how categorized folders are created dynamically:

AI-Directory-Manager/
│
├── main.py               --> Main GUI logic (handles user interface and user interactions)
│
├── file_organizer.py     --> File categorization logic (organizes files into Images, Videos, etc.)
│
├── file_filters.py       --> Filtering logic (filters files by size and date)
│
├── README.md             --> Project documentation
│
└── .gitignore            --> Specifies files and folders to ignore in version control
🗂 Categorized Folders (After Running the Program)
Selected Folder/                --> The folder you choose to organize
│
├── Images/                     --> Categorized folder for image files (.jpg, .png, etc.)
│   ├── file1.jpg
│   └── file2.png
│
├── Videos/                     --> Categorized folder for video files (.mp4, .mkv, etc.)
│   ├── video1.mp4
│   └── video2.mkv
│
├── Documents/                  --> Categorized folder for document files (.pdf, .txt, etc.)
│   ├── doc1.pdf
│   └── doc2.txt
│
├── Music/                      --> Categorized folder for music files (.mp3, .wav, etc.)
│   ├── song1.mp3
│   └── song2.wav
│
└── Others/                     --> Uncategorized files
    ├── file1.exe
    └── file2.zip
⚙️ How File Filtering Works:
1. File Size Filter:
Default: Files larger than 1 MB are included during the filtering process.
Customizable: The size limit can be changed through the GUI.
2. Date Filter:
Default: Files modified within the last 30 days are included.
Customizable: The date limit can be changed through the GUI.
🛡 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

🤝 Contributing
Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

Steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Submit a pull request.
📧 Contact
For any queries or suggestions, you can reach out at mishratejasvi61@gmail.com.
