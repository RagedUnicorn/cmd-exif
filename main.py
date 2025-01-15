import sys
import logging
import pprint

from PIL import Image

logging.basicConfig(
    stream=sys.stdout,
    level=10,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def get_info_data(path):
    """Read info data from an image file."""
    try:
        image = Image.open(path)
        return image.info
    except Exception as e:
        logging.exception(f"Error reading info data: {e}")
        return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    info_data = get_info_data(image_path)

    if info_data:
        print(pprint.pformat(info_data))

    else:
        print("Error reading info data.")
