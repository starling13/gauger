import argparse
import logging
import sys

import yaml

import gauge.exporter
import gauge.round_gauge


def import_gauge_from_yaml(file_path: str) -> gauge.round_gauge.Object:
    g = gauge.round_gauge.Object()

    fp = open(file_path, "r")
    data = yaml.safe_load(fp)
    fp.close()

    if data is None:
        raise Exception("Not valid yaml file")

    g.from_dict(data)

    return g


def _main(argv: list[str]) -> int:
    parser: argparse.ArgumentParser
    args: argparse.Namespace
    rg: gauge.round_gauge.Object

    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(sys.argv)
    parser.add_argument(
        "-i",
        "--gauge_file",
        type=str,
        required=True,
        help="File of the gauge description in YAML format",
    )
    parser.add_argument(
        "-o",
        "--gauge_image",
        type=str,
        required=True,
        help="File of the gauge images in SVG format",
    )
    args = parser.parse_args()

    try:
        rg = import_gauge_from_yaml(args.gauge_file)
    except Exception as e:
        logging.critical(f"Error: {e}")
        return 1

    exp = gauge.exporter.Object()
    exp.export(rg, args.gauge_image)

    return 0


if __name__ == "__main__":
    sys.exit(_main(argv=sys.argv))
