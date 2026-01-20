# PDF to JPG Converter (GUI)

A powerful, user-friendly Python desktop application that converts PDF documents into high-quality JPG images. This tool supports batch processing, drag-and-drop functionality, and automatic dependency management.

## 🚀 Key Features

* **Drag-and-Drop Interface:** Simply drop your PDF files into the application to queue them for conversion.
* **Batch Conversion:** Process multiple PDF files at once with a single click.
* **High-Quality Output:** Uses a scaling matrix of $4.0$ to ensure the resulting JPGs are crisp and professional (approx. 4x the standard resolution).
* **Automatic Setup:** The script automatically detects and installs missing dependencies (`PyMuPDF` and `tkinterdnd2`) on its first run.
* **Real-Time Logging:** A built-in log viewer allows you to track the progress of every page being converted.
* **Smart Defaults:** Automatically saves to your `Downloads` folder if no output directory is specified.

---



---

## 🛠️ Prerequisites

* **Python 3.x** installed on your system.
* **Windows/macOS/Linux** (Tkinter support required).

The application will handle the installation of:
1.  **PyMuPDF (`fitz`)**: For high-performance PDF rendering.
2.  **tkinterdnd2**: For the drag-and-drop engine.


## ⚙️ Technical Details

The conversion resolution is calculated using a scaling matrix to ensure high DPI:

$$\text{Output Width} = \text{Original Width} \times 4.0$$
$$\text{Output Height} = \text{Original Height} \times 4.0$$

Each page is exported as an individual `.jpg` file named after the original PDF and the corresponding page number.

## 📜 License

This project is licensed under the MIT License.
