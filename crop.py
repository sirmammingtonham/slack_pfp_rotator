import os
from PIL import Image

def crop_images_to_center_square(
    images_dir: str,
    size: int = 200,
    output_dir: str | None = None
) -> None:
    """
    Crop every image in `images_dir` to a center square of dimensions size×size.
    Saves cropped images to `output_dir` (defaults to overwriting in place).

    :param images_dir: Path to folder containing your images.
    :param size:      Side length (in pixels) of the square crop.
    :param output_dir:If provided, cropped images go here; otherwise overwrite originals.
    """
    if output_dir is None:
        output_dir = images_dir
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(images_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            continue

        src_path = os.path.join(images_dir, filename)
        dst_path = os.path.join(output_dir, filename)

        with Image.open(src_path) as img:
            w, h = img.size
            # Compute coordinates of center crop
            left   = max(0, (w - size) // 2)
            top    = max(0, (h - size) // 2)
            right  = left + size
            bottom = top + size

            cropped = img.crop((left, top, right, bottom))
            cropped.save(dst_path)

        print(f"Cropped {filename} → {dst_path}")

if __name__ == "__main__":
    crop_images_to_center_square("./squiddy_orig", size=350, output_dir="./squiddy")