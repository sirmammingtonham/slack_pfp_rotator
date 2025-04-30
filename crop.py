import os
from PIL import Image

def crop_images_to_center_square(
    images_dir: str,
    size: int = 200,
    output_dir: str | None = None,
    top_offset: int = 0
) -> None:
    """
    Crop every image in `images_dir` to a square of dimensions size×size,
    centered horizontally with an optional vertical offset.

    :param images_dir: Path to folder containing images.
    :param size: Side length (px) of the square crop.
    :param output_dir: Destination folder for cropped images; defaults to images_dir.
    :param top_offset: Vertical offset (px) added to the top coordinate of the crop.
                       Positive values move the crop downward.
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
            # Compute horizontal center
            left = max(0, (w - size) // 2)
            # Compute vertical center and apply offset
            center_top = (h - size) // 2
            top = center_top + top_offset
            # Clamp within bounds
            top = max(0, min(top, h - size))

            right = left + size
            bottom = top + size

            cropped = img.crop((left, top, right, bottom))
            cropped.save(dst_path)

        print(f"Cropped {filename} → {dst_path}")

if __name__ == "__main__":
    crop_images_to_center_square("./squiddy_orig", size=300, output_dir="./squiddy", top_offset=50)