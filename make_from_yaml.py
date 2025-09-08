# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Module of the exporting script from yaml description
"""

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

    if "gauge" not in data:
        raise Exception("No 'gauge' object")

    gauge_o = data.get("gauge")
    if gauge_o is None:
        logging.warning("Empty gauge object")
        return

    g.from_dict(gauge_o)

    return g


def _main(argv: list[str]) -> int:
    parser: argparse.ArgumentParser
    args: argparse.Namespace
    rg: gauge.round_gauge.Object

    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser()
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
    args = parser.parse_args(args=argv[1:])

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
