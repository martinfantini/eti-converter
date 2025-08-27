# Copyright (C) 2025 R Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from app.definition_helper import DefinitionHelper
import importlib
import traceback
import sys
from argparse import ArgumentParser, SUPPRESS
from app.parser import Parser
from app.schema import *
from app.definition_helper import *

def main() -> None:
    parser = ArgumentParser(prog='eti-converter-gen', description='ETI codec generator')
    parser.add_argument('--schema', help='path to xml schema', required=True)
    parser.add_argument('--destination', help='path to directory where codec will be written', required=True)
    parser.add_argument('--generator', help='choose generator (available: cpp, cppns or rust)', default='cpp', type=str)
    parser.add_argument('--package', help='override model name property', default='', type=str)
    parser.add_argument('--byteorder', help='override byte order, default littleEndian (available: littleEndian, bigEndian)', default='littleEndian', type=str)

    args = parser.parse_args()

    try:
        module = importlib.import_module(f'app.generation.{args.generator}')
        Generator = getattr(module, 'Generator')
        
        byte_order = None
        if args.byteorder == 'bigEndian':
           byte_order = ByteOrder.BIG_ENDIAN
        elif args.byteorder == 'littleEndian':
            byte_order = ByteOrder.LITTLE_ENDIAN

        package_name = None
        if len(args.package) != 0:
            package_name = args.package

        schema = Parser.from_file(args.schema).get_schema(byte_order, package_name)
        generator = Generator(args.destination)
        generator.generate(DefinitionHelper.get_schema_definition(schema))
    except Exception as e:
        sys.exit(traceback.format_exc())
        sys.exit(f'error: {e}')

if __name__ == '__main__':
    main()
