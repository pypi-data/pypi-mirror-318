# Impressify 🎨👨‍🎨

**Impressify** is a Python-based CLI tool for image resizing and optimization. It simplifies the process of batch resizing and compressing images, making them suitable for web use, thumbnails, or any application requiring efficient image handling.

---

## Features ✨

- **Batch Resizing**: Process entire directories of images at once.
- **Format Support**: Compatible with `.png`, `.jpg`, and `.jpeg` formats.
- **Quality Control**: Specify output quality (1-100).
- **Optimized Output**: Use advanced optimization for smaller file sizes without compromising quality.
- **Customizable Output**: Define custom output paths and control overwriting behavior.
- **CLI Friendly**: Simple and intuitive command-line interface.

---

## Installation 📦

To install **Impressify**, ensure you have Python 3.9+ and Poetry installed, then run:

```bash
pip install impressify
```


## Usage 🚀

### CLI Commands

Run the tool from the command line with the following syntax:



```bash
impressify <path> <size> [--output <output_path>] [--quality <quality>] [--optimize] [--overwrite]
```

### Arguments
- <path>: Path to an image or directory containing images.
- <size>: Target size (max dimension in pixels) for resizing.

### Optional Flags
- --output: Custom output directory for resized images.
- --quality: Image quality (default: 80, range: 1-100).
- --optimize: Optimize images for reduced size (default: enabled).
- --overwrite: Overwrite existing files (default: disabled).
- --progressive: progressive jpeg.


### Github Actions

```markdown

   - name: 🥦 Install impressify
      run: pip install impressify
      
    - name: 🥒 Resize
      run: |
        impressify moscow/imgs 100
        impressify moscow/imgs 220

```

## Examples

#### Resize a Single Image

```bash
impressify /path/to/image.jpg 300 --quality 90 --optimize
```

#### Batch Resize Images in a Directory

```bash
impressify /path/to/images/ 500 --output /path/to/output/ --overwrite
```

#### Resize with Default Settings

```bash
impressify /path/to/image.png 200
```

### Requirements 📋
- Python >= 3.9
- Pillow >= 11.0.0


## License 📜

Impressify is released under the MIT License. See the LICENSE file for details.