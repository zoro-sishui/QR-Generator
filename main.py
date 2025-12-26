# main.py

import argparse
import sys

from src.qr_generator.generator import generate_qr
from src.qr_generator.validator import validate_data
from src.qr_generator.utilis import prepare_outputpath


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a QR code from text input."
    )
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", default="qr_code.png")
    return parser.parse_args()


def main():
    args = parse_args()

    is_valid, error = validate_data(args.data)
    if not is_valid:
        print(f"Validation error: {error}")
        sys.exit(1)

    output_path = prepare_outputpath(args.output)

    if not generate_qr(args.data, output_path):
        print("Failed to generate QR code.")
        sys.exit(1)

    print(f"QR code generated: {output_path}")


if __name__ == "__main__":
    main()
