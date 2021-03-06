from taichi.misc.util import *
from taichi.two_d import *

if __name__ == '__main__':
    resolution = tuple([128, 128])
    simulator = create_mpm_simulator(resolution, 20, 0.1, max_delta_t=0.002)

    simulator.add_event(-1, lambda s: s.add_particles_sphere(Vector(0.5, 0.35), 0.20, 'dp',
                                                             velocity=Vector(0.0, -0.1)))

    levelset = simulator.create_levelset()
    levelset.add_polygon([(0.05, 0.05), (0.95, 0.05), (0.95, 0.95), (0.05, .95)], True)
    simulator.set_levelset(levelset)
    window = SimulationWindow(640, simulator, color_schemes['snow'], levelset_supersampling=2, show_images=True)
