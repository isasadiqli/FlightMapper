# FlightMapper

FlightMapper is a Python application that extracts, processes, and visualizes flight‑information from image sources (e.g. scanned tickets or boarding passes). It uses Optical Character Recognition (OCR) plus custom logic / GUI tools to map flight data into structured form.

---

## Features

- OCR-based text extraction from images.  
- GUI tools for assisting in manual correction / verification of OCRed content.  
- Parsing and mapping of extracted words into structured flight‐related data.  
- An environment module to setup needed configurations.  
- Tools for cleaning, filtering, or enhancing OCR output.  

---

## Project Structure

| File / Module | Purpose |
|---|---|
| `environment.py` | Configuration settings, environment setup, possibly managing API‐keys, paths, or thresholds. |
| `ocr.py` | Handles OCR operations – reading images, extracting text, preprocessing for better recognition. |
| `tools.py` | General utility/helper functions used across the application. |
| `gui_tools.py` | Graphical user interface components to assist users in reviewing and editing extracted data. |
| `main.py` | Entry point of the application; orchestrates calling OCR, GUI tools, parsing, etc. |
| `words.txt` | A dictionary / wordlist used in processing or verifying OCR output (e.g. to check for valid words). |
| `res/` | Resources directory (e.g. images, templates, sample data). |

---

## Requirements

- Python 3.x  
- OCR library (e.g. [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) or any other used library)  
- GUI toolkit (e.g. Tkinter, PyQt, etc.—depending what `gui_tools.py` uses)  
- Any other python packages (e.g. `pillow`, `opencv`, `numpy`)  

You can install the dependencies via:

```bash
pip install -r requirements.txt
```

*(If a `requirements.txt` does not yet exist, you may generate one by inspecting imports and using `pip freeze`.)*

---

## Usage

1. Place your image(s) containing flight tickets, boarding passes, or other relevant printed text into a designated folder.  
2. Run the application via:

   ```bash
   python main.py
   ```

3. The OCR module will process the image(s), extract raw text.  
4. Use the GUI tools to view, verify, and correct any OCR errors or misparsed words.  
5. Final output will be structured data capturing the flight relevant fields (flight number, date, time, origin, destination, etc.).

---

## Possible Improvements / TODOs

- Add unit tests for the parsing logic.  
- Improve error handling when OCR fails or images are low-quality.  
- Support more image formats and batch processing.  
- Add export functionality (e.g. JSON, CSV) for structured flight data.  
- Internationalization support (different languages/fonts).  

---

## Contributing

Contributions are welcome! If you want to contribute:

1. Fork the repository.  
2. Create a new branch for your feature or bugfix.  
3. Commit your changes with clear messages.  
4. Submit a pull request.  

---

## License

*(Specify license here, e.g. MIT, Apache 2.0, etc. If none yet, consider adding one.)*

---

## Contact

For questions or feedback, contact [Your Name or Maintainer] at [Email / GitHub].  
