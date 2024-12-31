"""
Basic CLI for Playa's "eager" API.  Writes CSV to standard output.
"""

import argparse
import logging
import csv
from pathlib import Path

import playa
from playa.pdftypes import ContentStream


def make_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdfs", nargs="+", type=Path)
    parser.add_argument(
        "-t",
        "--stream",
        type=int,
        help="Extract the contents of an object or content stream",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        help="File to write output (or - for standard output)",
        type=argparse.FileType("wt"),
        default="-",
    )
    parser.add_argument(
        "-s",
        "--space",
        help="Coordinate space for output objects",
        choices=["screen", "page", "default"],
        default="screen",
    )
    parser.add_argument(
        "--debug",
        help="Very verbose debugging output",
        action="store_true",
    )
    return parser


def main() -> None:
    parser = make_argparse()
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.WARNING)
    for path in args.pdfs:
        with playa.open(path, space=args.space) as doc:
            if args.stream is not None:  # it can't be zero either though
                stream = doc[args.stream]
                if not isinstance(stream, ContentStream):
                    parser.error(f"Indirect object {args.stream} is not a stream")
                args.outfile.buffer.write(stream.buffer)
            else:
                writer = csv.DictWriter(args.outfile, fieldnames=playa.fieldnames)
                writer.writeheader()
                for dic in doc.layout:
                    writer.writerow(dic)


if __name__ == "__main__":
    main()
