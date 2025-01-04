from typing import List
import argparse
import json
import math
import os.path
import sys

from tidye.model import Moon, Planet
from tidye.simulation import TidalSimulation


class TidyeMain:

    def __init__(self) -> None:
        parsed_args = self.parse_args(sys.argv[1:])
        self.file_path = parsed_args.file
        self.duration = parsed_args.duration
        self.planet = self.parse_config()

    @classmethod
    def parse_args(cls, args: List[str]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Simulate lunar tides from a provided configuration file.')
        parser.add_argument('file', help='Path to config file (e.g., config.json)')
        parser.add_argument('-d', '--duration', type=float, default=0,
                            help='Simulation duration (defaults to two full orbits)')
        return parser.parse_args(args)

    def parse_config(self) -> Planet:
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Config file not found: {self.file_path}")
        with open(self.file_path) as config_file:
            config = json.load(config_file)
        if 'planet' not in config:
            raise ValueError("Missing 'planet' key in config file")
        if 'mass' not in config['planet']:
            raise ValueError("Missing 'planet.mass' key in config file")
        planet = Planet(name=config['planet'].get('name', 'Planet'), mass=config['planet']['mass'])
        if 'moons' not in config or not isinstance(config['moons'], list) or not config['moons']:
            raise ValueError("Missing 'moons' key in config file")
        for i, moon in enumerate(config['moons']):
            if 'mass' not in moon:
                raise ValueError(f"Missing 'moons[{i}].mass' key in config file")
            if 'orbital_radius' not in moon:
                raise ValueError(f"Missing 'moons[{i}].orbital_radius' key in config file")
            if 'orbital_period' not in moon and ('geostationary' not in moon or not moon['geostationary']):
                raise ValueError(f"Missing orbital period or geostationary flag for 'moons[{i}]' in config file")
            if 'orbital_phase' in moon and (moon['orbital_phase'] < 0 or moon['orbital_phase'] > 1):
                raise ValueError(f"Orbital phase for 'moons[{i}]' in config file must be between 0 and 1")
            planet.moons.append(Moon(name=moon.get('name', f'M{i+1}'),
                                     mass=moon['mass'],
                                     orbital_radius=moon['orbital_radius'],
                                     orbital_period=moon.get('orbital_period', 0),
                                     orbital_phase=moon.get('orbital_phase', 0),
                                     geostationary=moon.get('geostationary', False)))
        return planet

    def run(self) -> None:
        TidalSimulation(planet=self.planet, duration=self.duration).simulate()


def main() -> None:
    TidyeMain().run()


if __name__ == '__main__':
    main()
