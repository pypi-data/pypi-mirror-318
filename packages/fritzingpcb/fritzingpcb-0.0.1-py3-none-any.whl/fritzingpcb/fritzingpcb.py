from importlib.resources import files
from pprint import pprint
import hashlib
from datetime import datetime
from zipfile import ZipFile
import logging
import sys

import click
import xml.etree.ElementTree as ET

from .parse_yaml import parse_yaml
from .board import Board
from .breadboard_svg import breadboard_svg
from .pcb_svg import pcb_svg
from .schematic_svg import schematic_svg
from .fzp_xml import fzp_xml

types: {
    'dict': dict,
    'list': list,
    'str': (str, float, int), # Mainly for 'version', which could be any of these
    'float': (float, int),
    'int': int
}
    
@click.command()
@click.argument('input', type=click.File('rb'))
@click.option('-d', '--defaults', type=click.File('rb'),
              default=files(__package__).joinpath('defaults.yaml'),
              help='Alternative defaults file')
@click.option('-g', '--grid', is_flag=True,
              help='Add gridlines to all SVG')
def cli(input, defaults, grid):

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    log = logging.getLogger(__name__)
    
    log.info(f'Parsing YAML')
    config = parse_yaml(defaults, input)
    log.info(f'Setting missing values to defaults')
    set_missing_values(config, input.name)

    log.info(f'Processing input')
    board = Board(config)
    
    # pprint(config)
    # print(board.layout)

    def et_to_binary(et, encoding):
        return ET.tostring(et, encoding=encoding, xml_declaration=True) + b'\n'

    zipname = f"{config['metadata']['basename']}.fzpz"
    log.info(f"Opening zipfile '{zipname}' for writing")
    zipfile = ZipFile(zipname, 'w')

    breadboard_filename = f"svg.breadboard.{config['metadata']['SVGbasename']}_breadboard.svg"
    log.info(f"Constructing breadboard SVG '{breadboard_filename}'")
    breadboard = breadboard_svg(board, gridlines=grid)
    ET.indent(breadboard)
    encoded = et_to_binary(breadboard, config['metadata']['encoding'])
    zipfile.writestr(breadboard_filename, encoded)
    with open(breadboard_filename, 'wb') as f:
        f.write(encoded)

    pcb_filename = f"svg.pcb.{config['metadata']['SVGbasename']}_pcb.svg"
    log.info(f"Constructing PCB SVG '{pcb_filename}'")
    pcb = pcb_svg(board, gridlines=grid)
    ET.indent(pcb)
    encoded = et_to_binary(pcb, config['metadata']['encoding'])
    zipfile.writestr(pcb_filename, encoded)
    with open(pcb_filename, 'wb') as f:
        f.write(encoded)

    schematic_filename = f"svg.schematic.{config['metadata']['SVGbasename']}_schematic.svg"
    log.info(f"Constructing schematic SVG '{schematic_filename}'")
    schematic = schematic_svg(board, gridlines=grid)
    ET.indent(schematic)
    encoded = et_to_binary(schematic, config['metadata']['encoding'])
    zipfile.writestr(schematic_filename, encoded)
    with open(schematic_filename, 'wb') as f:
        f.write(encoded)

    fzp_filename = f"part.{config['metadata']['SVGbasename']}.fzp"
    log.info(f"Constructing FZP XML '{fzp_filename}'")
    fzp = fzp_xml(board, input.name, schematic_filename, pcb_filename, breadboard_filename)
    ET.indent(fzp)
    encoded = et_to_binary(fzp, config['metadata']['encoding'])
    zipfile.writestr(fzp_filename, encoded)
    with open(fzp_filename, 'wb') as f:
        f.write(encoded)

    zipfile.close()
    log.info(f"Wrote zipfile '{zipname}'")

def overlay(defaults, config):
    # Overlay the given config dict on top of the defaults dict
    # FIXME: Could do way more error checking of config
    for key, value in config:
        if key in defaults:
            if isinstance(defaults[key], dict):
                if not isinstance(value, dict):
                    raise ValueError(f'Expected {key} to be a dictionary')
                else:
                    overlay(defaults[key], value)
            elif isinstance(defaults[key], list):
                if not isinstance(value, list):
                    raise ValueError(f'Expected {key} to be a list')
                else:
                    defaults[key] = value
            elif isinstance(defaults[key], str):
                if not isinstance(value, (str, float, int)):
                    raise ValueError(f'Expected {key} to be a string')
                else:
                    defaults[key] = str(value)
            elif isinstance(defaults[key], float):
                if not isinstance(value, (float, int)):
                    raise ValueError(f'Expected {key} to be a float')
                else:
                    defaults[key] = float(value)
            elif isinstance(defaults[key], int):
                if not isinstance(value, int):
                    raise ValueError(f'Expected {key} to be an integer')
                else:
                    defaults[key] = str(value)
            elif isinstance(defaults[key], bool):
                if not isinstance(value, bool):
                    raise ValueError(f'Expected {key} to be an boolean')
                else:
                    defaults[key] = value
            else:
                raise ValueError(f'Unexpected type {type(defaults[key])} for default {key}, value: "{defaults[key]}"')
    else:
        defaults[key] = value

def set_missing_values(config, filename):
    # Fill in optional values missing from the input file, and that have
    # no defaullt
    log = logging.getLogger(__name__)

    if 'moduleId' not in config['metadata']:
        md5str = f'{config["metadata"]["author"]}|{config["metadata"]["version"]}|{config["metadata"]["title"]}|{filename}'
        
        hexdigest = hashlib.md5(md5str.encode('utf-8')).hexdigest()
        config['metadata']['moduleId'] = hexdigest
        log.info(f"Set moduleId to '{config['metadata']['moduleId']}'")
        
    if 'description' not in config['metadata']:
        config['metadata']['description'] = config['metadata']['title']
        log.info(f"Set description to '{config['metadata']['description']}'")
        
    if 'label' not in config['metadata']:
        config['metadata']['label'] = config['metadata']['title']
        log.info(f"Set label to '{config['metadata']['label']}'")
        
    if 'basename' not in config['metadata']:
        config['metadata']['basename'] = ''.join(filter(str.isalnum, config['metadata']['label']))
        log.info(f"Set basename to '{config['metadata']['basename']}'")

    if 'SVGbasename' not in config['metadata']:
        config['metadata']['SVGbasename'] = config['metadata']['basename'] + '_' + config['metadata']['moduleId']
        log.info(f"Set SVGbasename to '{config['metadata']['SVGbasename']}'")

    try:
        config['metadata']['date'] = config['metadata']['date'].strftime('%Y-%m-%d')
    except AttributeError:
        config['metadata']['date'] = str(config['metadata']['date'])
    except KeyError:
        config['metadata']['date'] = datetime.today().strftime('%Y-%m-%d')
    log.info(f"Set date to '{config['metadata']['date']}'")
