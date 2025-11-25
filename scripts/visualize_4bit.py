#!/usr/bin/env python3
import argparse
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
# Palette mapping (0–F)
PALETTE = {
    0x0: (0, 0, 0),               # black
    0x1: (0, 0, 139),             # dark blue
    0x2: (0, 128, 0),             # green
    0x3: (0, 128, 128),           # teal
    0x4: (139, 0, 0),             # red
    0x5: (128, 0, 128),           # purple
    0x6: (139, 69, 19),           # brown
    0x7: (192, 192, 192),         # light gray
    0x8: (105, 105, 105),         # dark gray
    0x9: (106, 90, 205),          # violet/blue
    0xA: (152, 251, 152),         # light green
    0xB: (127, 255, 212),         # light blue
    0xC: (240, 128, 128),         # light red
    0xD: (255, 105, 180),         # pink
    0xE: (255, 255, 0),           # yellow
    0xF: (255, 255, 255),         # white
}

# ANSI escape colors for ASCII mode
ANSI_COLORS = {
    n: f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m"
    for n, rgb in PALETTE.items()
}
ANSI_RESET = "\033[0m"


def read_nibbles(file_path, offset, length):
    """Read bytes and convert to a list of 4-bit values."""
    with open(file_path, "rb") as f:
        f.seek(offset)
        data = f.read(length)

    nibbles = []
    for b in data:
        nibbles.append((b >> 4) & 0xF)  # high nibble
        nibbles.append(b & 0xF)        # low nibble
    return nibbles


from PIL import Image, ImageDraw, ImageFont

def save_image(nibbles, rows, cols, outfile, pixel_size=20, overlay=False):
    """Create and save an image visualization, with optional text overlay."""
    if len(nibbles) != rows * cols:
        raise ValueError("rows * cols must equal number of nibbles!")

    width = cols * pixel_size
    height = rows * pixel_size

    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Choose a font size proportional to pixel size
    font_size = max(8, pixel_size // 2)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    idx = 0
    for y in range(rows):
        for x in range(cols):
            val = nibbles[idx]
            idx += 1

            color = PALETTE[val]

            # Pixel rectangle
            x0 = x * pixel_size
            y0 = y * pixel_size
            x1 = x0 + pixel_size
            y1 = y0 + pixel_size
            draw.rectangle([x0, y0, x1, y1], fill=color)

            # Draw nibble value overlay text
            if overlay:
                text = f"{val:X}"

                # Use textbbox instead of deprecated textsize
                bbox = draw.textbbox((0, 0), text, font=font)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]

                tx = x0 + (pixel_size - text_w) // 2
                ty = y0 + (pixel_size - text_h) // 2

                # For readability: choose black/white text automatically
                r, g, b = color
                luminance = (0.299*r + 0.587*g + 0.114*b)
                text_color = (0, 0, 0) if luminance > 128 else (255, 255, 255)

                draw.text((tx, ty), text, fill=text_color, font=font)

    img.save(outfile)
    print(f"Saved image: {outfile}")


def print_ascii(nibbles, rows, cols, colored=True):
    """Print the 4-bit values as ASCII with optional ANSI colors."""
    if len(nibbles) != rows * cols:
        raise ValueError("rows * cols must equal number of nibbles!")

    idx = 0
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            val = nibbles[idx]
            idx += 1
            if colored:
                row_str += f"{ANSI_COLORS[val]} {val:X} {ANSI_RESET}"
            else:
                row_str += f"{val:X} "
        print(row_str)


def parse_int(value):
    """Parser to allow decimal or hex input."""
    value = value.strip().lower()
    if value.startswith("0x"):
        return int(value, 16)
    return int(value)


def main():
    parser = argparse.ArgumentParser(
        description="Visualize 4-bit nibble data from a binary file."
    )

    parser.add_argument("file", help="Input binary file")
    parser.add_argument("--offset", required=True, type=parse_int,
                        help="Starting byte offset (decimal or hex like 0x200)")
    parser.add_argument("--length", required=True, type=parse_int,
                        help="Number of bytes to read")
    parser.add_argument("--rows", required=True, type=int,
                        help="Number of output rows")
    parser.add_argument("--cols", required=True, type=int,
                        help="Number of output columns")

    # Output modes
    parser.add_argument("--ascii", action="store_true",
                        help="Print data as ASCII grid instead of an image")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable ANSI color in ASCII mode")
    parser.add_argument("--image", metavar="OUTFILE",
                        help="Save visualization to an image file")

    parser.add_argument("--pixel-size", type=int, default=20,
                        help="Pixel size for image output (default=20)")
    parser.add_argument("--overlay", action="store_true",
                    help="Overlay nibble values on top of pixels in the image")


    args = parser.parse_args()

    # Read data
    length = int(args.rows * args.cols/2)
    print(f"Number of bytes:{length}")
    print(f"Number of nibbles:{length*2}")
    print(f"Bytes: {args.offset} - {args.offset+length}")
    #nibbles = read_nibbles(args.file, args.offset, args.length)
    nibbles = read_nibbles(args.file, args.offset, length)

    # Validate size
    if len(nibbles) != args.rows * args.cols:
        raise SystemExit(
            f"Error: rows*cols = {args.rows * args.cols} "
            f"but nibble count = {len(nibbles)}"
        )

    # ASCII output
    if args.ascii:
        print_ascii(nibbles, args.rows, args.cols, colored=not args.no_color)
        return

    # Image output
    if args.image:
        save_image(nibbles, args.rows, args.cols,args.image, args.pixel_size, args.overlay)
    return


    # If no output option is given
    print("Nothing to do. Use --ascii or --image OUTFILE.")


if __name__ == "__main__":
    main()

'''
# Example uses:
python visualize_4bit.py rom.bin --offset 0x1000 --length 64 --rows 16 --cols 8 --ascii
python visualize_4bit.py rom.bin --offset 0x1000 --length 64 --rows 16 --cols 8 --ascii --no-color
python visualize_4bit.py rom.bin --offset 2048 --length 128 --rows 32 --cols 8 --image block.png
python visualize_4bit.py rom.bin --offset 0x200 --length 128 --rows 16 --cols 16 --image block.png --pixel-size 10
'''

