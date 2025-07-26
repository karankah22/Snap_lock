 # 🔐 Snap_Lock

**Version**: 1.1  
**Release Date**: 26/07/2025  
**Programmer**: Karan

---

## 📄 Description

Snap_Lock is a simple Python-based security application designed to capture the image of a person trying to access your system without permission.

### Features:
- User gets **3 attempts** to enter the correct PIN.
- If all attempts fail, the program:
  - Captures an image using the webcam.
  - Saves the image in `.jpg` format.
- Stores additional input (like a "pet name") into a `.txt` file.

---

## 🛠️ Installation

1. **Extract** the ZIP file.
2. Make sure you have Python and OpenCV installed:

   ```bash
   pip install opencv-python
