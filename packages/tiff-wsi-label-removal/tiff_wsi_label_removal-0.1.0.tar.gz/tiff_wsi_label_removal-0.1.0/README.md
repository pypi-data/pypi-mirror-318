---

# TIFF Label Removal Tool

A **Proof of Concept** tool to remove label pages from TIFF/BigTIFF files without loading the entire file into memory.
This utility is especially helpful when dealing with **Whole Slide Images (WSIs)** where a **label page** is present and may contain sensitive information.

## Why This Is Useful for Whole Slide Images (WSIs) — Label Page Found in WSI

In many Whole Slide Imaging (WSI) workflows—particularly within pathology or clinical research—TIFF files can contain additional pages labeled with patient details or institutional data. These **label pages** often reside alongside the main high-resolution scan. By removing the label page:

- You **reduce privacy concerns** by stripping away potentially identifying metadata.
- You **retain** the primary macro or full-resolution image necessary for analysis and sharing.
- You **avoid** loading the entire file into memory, which is critical when working with large WSI data.

## Features

- Removes **Label** pages from TIFF/BigTIFF files (including WSIs).
- Preserves **Macro** and other non-label pages.
- Modifies XML metadata to remove references to label images.
- Operates at a **low-level** file structure, minimizing memory usage.

## Installation

1. **Clone** the repository:

   * `git clone https://github.com/<your-username>/tiff-label-removal.git`
   * `cd tiff-label-removal`
2. **Install** dependencies:

   * `python -m pip install -r requirements.txt`

   Ensure you have a compatible Python version (e.g., Python 3.7+).
3. (Optional) **Install** as a package:

   * `pip install .`
     This step allows you to run the tool via a command-line entry point (e.g., `remove-label`) if you have a `setup.py` or `pyproject.toml` configured.

---

## Usage

You can use the script **directly** or via the  **installed CLI** .

### Direct usage

`python remove_label.py <input_tiff_file> <output_tiff_file>`

Example:

`python remove_label.py sample_input.tiff sample_output.tiff`

### CLI usage (if installed)

If you have installed this package locally (via `pip install .`), then run:

`remove-label <input_tiff_file> <output_tiff_file>`

Example:

`remove-label sample_input.tiff sample_output.tiff`

---

## Project Structure

Below is a recommended file structure. Some files might differ if you adapt or expand the project:

* **tiffprocessor.py**
  Contains the core functionality:
  * **verify_pages** : Detect label/macro pages.
  * **modify_xml_metadata** : Removes label references from XML metadata.
  * **copy_tiff_low_level** : Performs the low-level reading and writing of TIFF data, skipping label pages.
* **remove_label.py**
  Simple command-line script that parses arguments and calls the functions in `tiffprocessor.py`.
* **requirements.txt**
  Lists dependencies (e.g., `tifffile`). Update as necessary.
* **README.md**
  This documentation file.
* **LICENSE**
  MIT

---

## How It Works

1. **Page Verification** : The script reads the TIFF structure via `tifffile`. It identifies pages based on the `ImageDescription` tag, looking for entries with `"Label"` or `"Macro"`.
2. **XML Modification** : For the first page (usually containing metadata), the code extracts the XML, parses it (with `xml.etree.ElementTree`), and removes references to the label information (looking for `PIM_DP_IMAGE_TYPE` = `"LABELIMAGE"`).
3. **Low-Level Copy** : The script copies the file **IFDs (Image File Directories)** and image data segments, but **skips** the label page. It preserves the overall structure (page offsets, IFD chains) so the resulting TIFF remains valid.
4. **Result** : You end up with a TIFF file that excludes the label page but retains other pages and images.

---

## Planned Optimizations

* **Performance** :
* Reduce file seeks by collecting and sorting I/O regions.
* Use configurable buffer sizes for copying.
* Merge contiguous byte regions to minimize I/O calls.
* **IFD Chain Integrity** :
* Perform deeper checks to ensure removing pages doesn’t break references.
* Test against different TIFF variants (e.g., multi-page, BigTIFF).
* **Comprehensive Testing** :
* Run tests on larger and more diverse TIFF datasets.
* Validate other metadata tags (beyond `ImageDescription`).
* **Technical Analysis** :
* Further review of TIFF/BigTIFF standards.
* Check how tools like QuPath handle label metadata and page chains.

---

## Contributing

Contributions are welcome!

* **Issues** : If you find a bug or have a question, open a GitHub issue.
* **Pull Requests** : If you’d like to fix something or add a new feature, feel free to create a PR.
