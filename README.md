# FileLocker 🔐

**FileLocker** is a simple but effective Python script that allows users to restrict file write/modify access on Windows using the built-in `icacls` command. Ideal for learning about Windows file permissions, system scripting, and subprocess control in Python.

## 🚀 Features
- Lock a file against specific users in seconds
- Command-line interaction using Python’s `subprocess` module
- User input-driven — no hardcoded paths or users
- Useful for testing file restrictions or learning ACL management

## 🛠️ How It Works
1. User is prompted to enter the filename and a target user to restrict
2. The script runs `icacls` via `subprocess.run()` to deny write access
3. Output confirms success or failure of the operation

> 🗂️ **Note:** For multi-user testing, place the target file in `C:\Users\Public\` so it’s accessible to all accounts on the system.

## 🧪 Use Cases
- Testing file permission behavior across Windows users
- Practicing system automation with Python
- Building toward more advanced security scripts

## 📎 Notes
- Only works on Windows systems
- Target user must exist and have logged in at least once
- File must be present in the same directory as the script (or provide full path)
- 🔐 **Public folder (`C:\Users\Public`)** is recommended when working across multiple users

## 🔄 Future Enhancements
- Undo/restore access
- GUI version using Tkinter
- Multi-user restrictions in one run

---

**Tested on:** Windows 11 
**Language:** Python 3.10  
