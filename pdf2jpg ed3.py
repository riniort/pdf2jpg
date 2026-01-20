import os
import sys
import subprocess
import fitz  # PyMuPDF for PDF-to-JPG conversion
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
from pathlib import Path

# Default Downloads folder
DOWNLOADS_FOLDER = str(Path.home() / "Downloads")

# Function to check and install dependencies
def check_and_install(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"{package_name} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"{package_name} installed successfully.")

# Check and install required dependencies
check_and_install("pymupdf")
check_and_install("tkinterdnd2")

# Function to convert PDF to JPG
def convert_pdf_to_images(pdf_path, output_folder, scale_factor=4.0, progress=None, file_index=None, total_files=None):
    failed_files = []
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  # Extract PDF file name without extension
    try:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(len(pdf_document)):
            image_path = os.path.join(output_folder, f"{pdf_name}_page_{page_number + 1}.jpg")
            try:
                # Set higher resolution using scaling matrix
                page = pdf_document.load_page(page_number)
                matrix = fitz.Matrix(scale_factor, scale_factor)
                pix = page.get_pixmap(matrix=matrix)
                pix.save(image_path)
                log_message(f"Successfully saved: {image_path}")
            except Exception as e:
                failed_files.append(image_path)
                log_message(f"Failed to save page {page_number + 1}: {e}")
        pdf_document.close()
    except Exception as e:
        log_message(f"An error occurred: {e}")

    if progress and file_index is not None and total_files is not None:
        progress['value'] = int((file_index + 1) / total_files * 100)
        root.update_idletasks()

    if not failed_files:
        log_message(f"\n{pdf_name} converted successfully!\n")
    else:
        log_message(f"\nSome pages failed to convert in {pdf_name}:")
        for file in failed_files:
            log_message(f" - {file}")

# Function to log messages in the GUI
def log_message(message):
    log_area.insert(tk.END, message + "\n")
    log_area.see(tk.END)

# Drag-and-drop handler
def on_drop(event):
    dropped_files = event.data.strip("{}").split(" ")  # Handle multiple files
    valid_files = [f for f in dropped_files if f.lower().endswith(".pdf")]
    if valid_files:
        for f in valid_files:
            log_message(f"PDF file loaded: {f}")
        pdf_files.extend(valid_files)
    else:
        messagebox.showerror("Invalid File", "Please drop valid PDF files.")

# Select output folder
def select_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder)
        log_message(f"Output folder selected: {folder}")

# Confirm and start conversion
def on_confirm():
    output_folder = output_entry.get().strip()
    if not pdf_files:
        messagebox.showerror("Error", "Please specify valid PDF files.")
        return

    if not output_folder:
        output_folder = DOWNLOADS_FOLDER  # Use Downloads folder by default
        log_message(f"Output folder not selected. Using default: {output_folder}")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        log_message(f"Created default output folder: {output_folder}")

    # Reset progress bar and start conversion
    progress_bar['value'] = 0
    total_files = len(pdf_files)

    log_message("\nStarting conversion...")
    for index, pdf_path in enumerate(pdf_files):
        convert_pdf_to_images(pdf_path, output_folder, progress=progress_bar, file_index=index, total_files=total_files)
    log_message("\nConversion complete.")
    messagebox.showinfo("Success", "Conversion complete!")

# GUI setup
root = TkinterDnD.Tk()
root.title("PDF to JPG Converter")
root.geometry("600x500")
root.resizable(False, False)

pdf_files = []  # List to store multiple PDF files

# Widgets
tk.Label(root, text="Drag and Drop PDF Files Here or Use Browse:").pack(pady=5)

browse_button = tk.Button(root, text="Browse Files", command=lambda: pdf_files.extend(filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])) or log_message("Files added."))
browse_button.pack(pady=5)

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

output_label = tk.Label(output_frame, text="Select Output Folder (optional):")
output_label.pack(side=tk.LEFT)
output_entry = tk.Entry(output_frame, width=50)
output_entry.pack(side=tk.LEFT)
output_button = tk.Button(output_frame, text="Browse", command=select_output_folder)
output_button.pack(side=tk.LEFT, padx=5)

confirm_button = tk.Button(root, text="Start Conversion", width=15, command=on_confirm)
confirm_button.pack(pady=10)

progress_label = tk.Label(root, text="Progress:")
progress_label.pack()

progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=500, mode='determinate')
progress_bar.pack(pady=5)

log_label = tk.Label(root, text="Conversion Log:")
log_label.pack()

log_area = scrolledtext.ScrolledText(root, width=70, height=10, state='normal')
log_area.pack(pady=5)

root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# Start the GUI event loop
root.mainloop()
