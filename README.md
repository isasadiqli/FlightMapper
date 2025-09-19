# FlightMapper

FlightMapper is a Python application for **flight data analysis, mapping, and simulation** based on **image processing**.  
It extracts aircraft and target information (location, altitude, time, etc.) from EO/IR camera recordings using **OCR (Optical Character Recognition)**, applies preprocessing and anomaly correction, and visualizes movements on maps.  

This project was developed as part of a graduation project at Ankara Yildirim Beyazit University.

---

## Features

- **Video Processing**
  - Splits aircraft EO/IR recordings into frames using OpenCV.
  - Applies preprocessing (masking, blurring, thresholding, dilating) to enhance text readability.
  - Crops relevant regions to isolate flight data.

- **Data Extraction**
  - Uses **Tesseract OCR** to recognize flight information from frames.
  - Supports anomaly detection and correction for OCR errors (using statistical and dictionary-based methods).

- **Data Handling**
  - Saves processed data into **CSV files** for reuse without reprocessing.
  - Generates **KML files** for geographic visualization of aircraft and target routes.

- **Visualization & Simulation**
  - Displays extracted routes and targets on map applications (via KML).
  - Provides a **GUI (Tkinter-based)** for selecting inputs, controlling FPS, monitoring process status, and exporting results.

---

## Project Structure

| File / Module       | Purpose |
|---------------------|---------|
| `main.py`           | Entry point of the program. Runs preprocessing, OCR, anomaly detection, and visualization. |
| `ocr.py`            | Handles OCR operations on processed frames. |
| `tools.py`          | Utility functions (e.g. anomaly detection, corrections, data handling). |
| `gui_tools.py`      | GUI implementation using Tkinter for user interaction. |
| `environment.py`    | Configuration and setup (paths, parameters). |
| `words.txt`         | Dictionary for verifying and correcting OCR results. |

---

## Requirements

- Python 3.x
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Required Python packages:
  - `opencv-python`
  - `pytesseract`
  - `pillow`
  - `numpy`
  - `tkinter` (standard with Python on most systems)
  - `pyenchant` (for dictionary-based corrections)

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Install Tesseract OCR and make sure it is accessible from your system PATH.  
2. Run the program:

   ```bash
   python main.py
   ```

3. In the GUI, you can:
   - Select a video file for processing.
   - Adjust **FPS (frames per second)** to balance speed and accuracy.
   - Choose to process an existing CSV file instead of a video.
   - Export results as **CSV** or **KML**.
   - Monitor process status with a progress bar.

4. Open the generated **KML file** in Google Earth or another map application to view the aircraft and target paths.

---

## Results

- Correctly extracts and visualizes flight paths in most scenarios.  
- Anomaly detection corrects ~80% of OCR errors.  
- Works best with higher FPS and higher-quality video (less noisy frames).  
- Limitations remain with very noisy video and distorted characters.  

---

## Future Improvements

- Enhance preprocessing for noisy video.  
- Integrate **machine learning classification** for better accuracy.  
- Apply fuzzy logic or distance-based anomaly correction.  
- Improve GUI with more simulation features.  

---

## Authors

- İsa Sadiqli  
- Muhammed Mustafa Kapucu  
- Şükrü Fırtına  
- Supervised by Dr. Fahreddin Şükrü Torun  
