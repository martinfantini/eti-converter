# Copyright (C) 2025 R Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

import importlib
import traceback
import sys
from argparse import ArgumentParser, SUPPRESS
from app.parser import Parser

def main() -> None:
    parser = ArgumentParser(prog='eti-converter-gen', description='ETI codec generator')
    parser.add_argument('--schema', help='path to xml schema', required=True)
    parser.add_argument('--destination', help='path to directory where codec will be written', required=True)
    parser.add_argument('--generator', help='choose generator (available: cpp, rust, python)', default='cpp')
    parser.add_argument('--package', help='override model mane property')

    args = parser.parse_args()

    try:
        module = importlib.import_module(f'app.generation.{args.generator}')
        Generator = getattr(module, 'Generator')
        schema = Parser.from_file(args.schema).get_schema()
        generator = Generator(args.destination)
        generator.generate(schema, package=args.package)
    except Exception as e:
        sys.exit(traceback.format_exc())
        sys.exit(f'error: {e}')

if __name__ == '__main__':
    main()
