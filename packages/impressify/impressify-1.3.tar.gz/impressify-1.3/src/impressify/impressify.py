import argparse
import logging
import pathlib
import re
import sys
from PIL import Image

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# Constants
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.JPG', '.JPEG'}
FILENAME_PATTERN = re.compile(r'.*-\d*px$')


def resize_image(path: pathlib.Path, size: int, output: pathlib.Path, quality: int = 80,
                 optimize: bool = True, progressive: bool = False) -> pathlib.Path | None:
    """
    Resize an image to a specified size and save it to the output path.

    Args:
        path (pathlib.Path): Path to the input image.
        size (int): The maximum size (width/height) of the resized image.
        output (pathlib.Path): Path to save the resized image.
        quality (int): Quality of the saved image (1-100).
        optimize (bool): Whether to optimize the image.

    Returns:
        pathlib.Path | None: Path to the resized image or None if an error occurred.
    """
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(path) as image:
            image.thumbnail((size, size))
            if progressive:
                logger.info('🚀 Progressive')
                image.save(output, 'JPEG', quality=quality, optimize=optimize, progressive=True)
            else:
                image.save(output, quality=quality, optimize=optimize)
        logger.info(f"🟢 Resized and saved image: {output}")
        return output
    except Exception as e:
        logger.error(f"🔴 Error resizing image '{path}': {e}")
        return None


def process_directory(path: pathlib.Path, size: int, output: pathlib.Path, quality: int, optimize: bool,
                      overwrite: bool):
    """
    Process all images in a directory, resizing them and saving to the output directory.
    """



def run_impressify(path: pathlib.Path,
                   size: int, output: pathlib.Path | None,
                   quality: int,
                   optimize: bool,
                   overwrite: bool,
                   progressive: bool):
    """
    Main function to process a file or directory for image resizing.
    """

    if path.is_file():
        if path.suffix not in ALLOWED_EXTENSIONS:
            logger.warning(f"🟡 Unsupported file type: {path.suffix}")
            return

        output_img = None
        if output:
            if output.is_file():
                output_img = output
            else:
                output_img = output / f"{path.stem}-{size}px{path.suffix}"
        else:
            output_img = path.parent / f"{path.stem}-{size}px{path.suffix}"
        output_img.parent.mkdir(parents=True, exist_ok=True)

        if output_img.exists() and not overwrite:
            logger.info(f"🔷 Skipping existing file (overwrite disabled): {output_img}")
            return
        resize_image(path, size, output_img, quality, optimize)
    elif path.is_dir():
        output_dir = output if output else path
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            images = [f for f in path.iterdir() if f.suffix in ALLOWED_EXTENSIONS]
            if path == output_dir:
                images = [f for f in images if not FILENAME_PATTERN.match(f.stem)]
            for image in images:
                output_img = output_dir / f"{image.stem}-{size}px{image.suffix}"
                if output_img.exists() and not overwrite:
                    logger.info(f"🔷 Skipping existing file (overwrite disabled): {output_img}")
                    continue
                resize_image(image, size, output_img, quality, optimize, progressive)
        except Exception as e:
            logger.error(f"🔴 Error processing directory '{path}': {e}")
    else:
        logger.error(f"🔴 Invalid path: {path}")


def main():
    """
    Command-line entry point for the image resizing script.
    """
    parser = argparse.ArgumentParser(description="Resize images to a specified size.")
    parser.add_argument("path", type=str, help="Path to an image or directory.")
    parser.add_argument("size", type=int, help="Maximum size (width/height) of the resized image.")
    parser.add_argument("--output", type=str, default=None, help="Output directory (optional).")
    parser.add_argument("--quality", type=int, default=80, help="Image quality (1-100). Default is 80.")
    parser.add_argument("--optimize", action="store_true", help="Enable optimization. Default is disabled.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files. Default is disabled.")
    parser.add_argument("--progressive", action="store_true", help="Progressive Jpeg. Default is False.")




    args = parser.parse_args()

    path = pathlib.Path(args.path)
    if not path.exists():
        logger.error(f"🔴 Path does not exist: {path}")
        sys.exit(1)

    if args.size < 1:
        logger.error("🔴 Invalid size. Size must be greater than 0.")
        sys.exit(1)

    if not (1 <= args.quality <= 100):
        logger.error("🔴 Quality must be between 1 and 100.")
        sys.exit(1)

    output = pathlib.Path(args.output) if args.output else None
    run_impressify(path, args.size, output, args.quality, args.optimize, args.overwrite)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("❗ Program interrupted by the user.")
    except Exception as e:
        logger.error(f"❌ An unexpected error occurred: {e}")