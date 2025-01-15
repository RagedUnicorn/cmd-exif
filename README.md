# cmd-exif

A lightweight Python project to read EXIF data from images.

## Features
- Extract detailed EXIF metadata from image files.
- Simple and easy-to-use Python script.
- Compatible with most image file types that store EXIF data.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or later
- [pip](https://pip.pypa.io/en/stable/)

### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/cmd-exif.git
   cd cmd-exif
   ```

2. **Create a Virtual Environment**
   Using IntelliJ:
    - Open the project in IntelliJ.
    - Navigate to `File > Project Structure > Modules` and set up a virtual environment.

   Or, create one manually:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project
You can use IntelliJ’s run configuration to execute the script. Make sure to set the path to the image you want to analyze in the script or as a command-line argument.

Alternatively, run the script directly from the command line:
```bash
python main.py --image /path/to/your/image.jpg
```

## Usage
1. Ensure your image file is accessible.
2. Run the script using IntelliJ or the command line.
3. View the extracted EXIF data in the output.

# License

MIT License

Copyright (c) 2025 Michael Wiesendanger

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
