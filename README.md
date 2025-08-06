# cmd-exif

A lightweight Python tool to extract and display EXIF metadata from image files.

## Features
- Extract detailed EXIF metadata from image files
- Simple command-line interface
- Docker support for easy deployment
- Compatible with most image formats that store EXIF data (JPEG, TIFF, etc.)

## Prerequisites
- Python 3.7+ or Docker
- [pip](https://pip.pypa.io/en/stable/) (for local installation)

## Installation

### Local Setup

```bash
git clone https://github.com/your-repo/cmd-exif.git
cd cmd-exif
pip install -r requirements.txt
```

### Docker Setup

No installation needed - just use Docker Compose:
```bash
git clone https://github.com/your-repo/cmd-exif.git
cd cmd-exif
```

## Usage

### Local Usage

```bash
python main.py path/to/your/image.jpg
```

### Docker Usage

```bash
# Create images directory and add your image
mkdir -p images
cp your-image.jpg images/sample.jpg

# Run with Docker Compose
docker-compose run --rm exif-reader

# Or run with a different image by overriding the command
docker-compose run --rm exif-reader sh -c "pip install -r requirements.txt && python main.py /images/another-image.jpg"
```

## Output

The tool displays EXIF metadata in a formatted structure, including:
- Camera make and model
- Date and time taken
- GPS coordinates (if available)
- Camera settings (ISO, aperture, shutter speed, etc.)
- Image dimensions and orientation
- And more...

## Example

```bash
python main.py vacation-photo.jpg
```

Output:
```
{'DateTime': '2024:07:15 14:30:00',
 'Make': 'Canon',
 'Model': 'Canon EOS R5',
 'ExifImageWidth': 6720,
 'ExifImageHeight': 4480,
 ...}
```

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
