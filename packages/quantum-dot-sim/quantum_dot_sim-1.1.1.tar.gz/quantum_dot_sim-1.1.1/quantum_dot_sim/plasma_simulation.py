import pygame
import numpy as np
import random

class PlasmaSimulation:
    def __init__(self, screen_width=800, screen_height=600, num_particles=100):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Plasma Simulation with Quantum Dot Interaction")
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_particles = num_particles

        # Particle properties: position, velocity, and charge
        self.particles = [
            {
                "pos": np.array([random.uniform(0, screen_width), random.uniform(0, screen_height)]),
                "vel": np.array([random.uniform(-1, 1), random.uniform(-1, 1)]),
                "charge": random.choice([-1, 1])
            }
            for _ in range(num_particles)
        ]

        # Quantum dot properties
        self.quantum_dot_center = np.array([screen_width // 2, screen_height // 2])
        self.quantum_dot_radius = 50
        self.quantum_dot_potential = -10  # Negative potential to attract positive charges

    def apply_forces(self):
        """Apply Coulomb forces between particles and interactions with the quantum dot."""
        k = 9e9  # Coulomb's constant (scaled for visualization)
        for i, particle in enumerate(self.particles):
            force = np.zeros(2)

            # Interaction with other particles
            for j, other in enumerate(self.particles):
                if i != j:
                    r_vec = other["pos"] - particle["pos"]
                    r_mag = np.linalg.norm(r_vec) + 1e-5  # Avoid division by zero
                    force += k * particle["charge"] * other["charge"] * r_vec / (r_mag ** 3)

            # Interaction with quantum dot
            r_vec_dot = self.quantum_dot_center - particle["pos"]
            r_mag_dot = np.linalg.norm(r_vec_dot) + 1e-5
            force += k * particle["charge"] * self.quantum_dot_potential * r_vec_dot / (r_mag_dot ** 3)

            # Update particle velocity
            particle["vel"] += force * 0.1  # Adjust scaling for smooth simulation

    def update_positions(self):
        """Update the position of each particle and handle boundary conditions."""
        for particle in self.particles:
            particle["pos"] += particle["vel"]

            # Reflect particles off walls
            for dim in range(2):
                if particle["pos"][dim] < 0 or particle["pos"][dim] > [self.screen_width, self.screen_height][dim]:
                    particle["vel"][dim] *= -1
                    particle["pos"][dim] = np.clip(particle["pos"][dim], 0, [self.screen_width, self.screen_height][dim])

    def draw_particles(self):
        """Draw all particles on the screen."""
        for particle in self.particles:
            color = (0, 0, 255) if particle["charge"] > 0 else (255, 0, 0)
            pygame.draw.circle(self.screen, color, particle["pos"].astype(int), 4)

    def draw_quantum_dot(self):
        """Draw the quantum dot on the screen."""
        pygame.draw.circle(self.screen, (0, 255, 0), self.quantum_dot_center.astype(int), self.quantum_dot_radius, 2)

    def run(self):
        """Main loop for running the plasma simulation."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Clear the screen
            self.apply_forces()
            self.update_positions()
            self.draw_particles()
            self.draw_quantum_dot()

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Cap the frame rate

        pygame.quit()
