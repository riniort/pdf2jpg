# pdf2jpg
PDF to JPG Converter
PDF to JPG Converter 
Python-based desktop application that allows you to batch-convert PDF pages into high-quality JPG images.
Featuring a user-friendly interface with drag-and-drop support and real-time progress tracking.

🚀 FeaturesDrag-and-Drop

Support: Simply drop your PDF files directly into the app window.Batch Processing: Convert multiple PDF files simultaneously.
High Resolution: Uses a $4.0$ scale factor (configurable) to ensure crisp, high-quality image output.Smart 
Tracking: Visual progress bar and detailed conversion logs.Flexible Output: Choose a custom saving location or default to your system's Downloads folder.


🛠️ Prerequisites
Before running the application, ensure you have Python 3.x installed.
The script will handle the installation of the following libraries for you:PyMuPDF (fitz) — for high-performance PDF rendering.tkinterdnd2 — for drag-and-drop functionality.

📦 Installation & UsageClone the Repository
Bashgit clone 
cd pdf-to-jpg-converter
Run the ApplicationSimply execute the Python script:Bashpython main.py

How to Convert
Step 1: Drag and drop your PDFs into the application window OR click Browse Files.
Step 2 (Optional): Click Browse next to the output entry to select a destination folder.
Step 3: Click Start Conversion.
Step 4: Monitor progress in the log area. Your files will be saved as Filename_page_X.jpg.🖥️ User Interface⚙️ How it WorksThe application utilizes PyMuPDF's matrix scaling to convert PDF vectors into rasterized images.$$\text{Output Resolution} = \text{Original Size} \times \text{Scale Factor}$$By default, the scale factor is set to 4.0, providing a high-definition output suitable for printing or professional presentations.
