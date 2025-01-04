from dataclasses import dataclass, field
from typing import List
import math


GRAVITY = 1  # 6.67e-11


@dataclass
class Moon:
    name: str
    mass: float
    orbital_radius: float
    orbital_period: float = 0
    orbital_phase: float = 0
    geostationary: bool = False

    @property
    def frequency(self) -> float:
        return 1 / self.orbital_period

    @property
    def phase(self) -> float:
        return self.orbital_phase * math.tau

    def gravity(self, planet: 'Planet') -> float:
        return (GRAVITY * planet.mass * self.mass) / (self.orbital_radius ** 2)


@dataclass
class Planet:
    name: str
    mass: float
    moons: List[Moon] = field(default_factory=list)
