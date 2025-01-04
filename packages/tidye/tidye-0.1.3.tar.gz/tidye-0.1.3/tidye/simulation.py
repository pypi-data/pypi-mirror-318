import math

import matplotlib.pyplot as plt
import numpy as np

from tidye.model import Moon, Planet


class TidalSimulation:

    def __init__(self, planet: Planet, duration: float = 0) -> None:
        self.planet = planet
        if not duration:
            max_period = max(moon.period for moon in planet.moons)
            duration = 2 * max_period * math.tau
        self.duration = duration

    def tidal_force(self, t: np.ndarray) -> np.ndarray:
        return np.sum([self.lunar_force(moon, t) for moon in self.planet.moons], axis=0)

    def lunar_force(self, moon: Moon, t: np.ndarray) -> np.ndarray:
        amplitude = moon.gravity(self.planet)
        if moon.geostationary:
            return np.full(t.shape, amplitude)  # constant force for a geostationary moon
        # force = amplitude * sin((frequency * t) + phase)
        # https://worldbuilding.stackexchange.com/a/112
        return np.sin((t * moon.frequency) + moon.phase) * amplitude

    def simulate(self) -> None:
        t = np.linspace(0, self.duration, max(100, int(self.duration) * 20))
        waves = [self.lunar_force(moon, t) for moon in self.planet.moons]
        waves.append(self.tidal_force(t))

        _, ax = plt.subplots()
        names = [moon.name for moon in self.planet.moons] + ['All']
        for wave, name in zip(waves, names):
            ax.plot(t, wave, label=name)

        min_force = np.min(waves)
        max_force = np.max(waves)
        ax.set(
            xlim=(0, self.duration),
            ylim=(min_force + (min_force * 0.1), max_force + (max_force * 0.1)),
            xlabel='Time',
            ylabel='Tidal Force',
        )

        plt.legend(loc='upper right')
        plt.show()
