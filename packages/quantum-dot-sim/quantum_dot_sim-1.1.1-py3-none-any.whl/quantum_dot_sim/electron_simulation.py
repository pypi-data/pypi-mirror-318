import pygame
import numpy as np
import random

class ElectronSimulation:
    def __init__(self, screen_width=800, screen_height=600, num_electrons=100):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Electron Simulation with Quantum Dot Interaction")
        self.clock = pygame.time.Clock()
        self.running = True
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_electrons = num_electrons

        # Electron properties: position, velocity, and charge
        self.electrons = [
            {
                "pos": np.array([random.uniform(0, screen_width), random.uniform(0, screen_height)]),
                "vel": np.array([random.uniform(-1, 1), random.uniform(-1, 1)]),
                "charge": -1  # Electrons are negatively charged
            }
            for _ in range(num_electrons)
        ]

        # Quantum dot properties
        self.quantum_dot_center = np.array([screen_width // 2, screen_height // 2])
        self.quantum_dot_radius = 50
        self.quantum_dot_potential = 10  # Positive potential to attract electrons

        # External field parameters
        self.electric_field = np.array([0.1, 0.1])  # Uniform electric field (x, y components)

    def apply_forces(self):
        """Apply Coulomb forces and external fields."""
        k = 9e9  # Coulomb's constant (scaled for visualization)
        for electron in self.electrons:
            force = np.zeros(2)

            # Interaction with quantum dot
            r_vec_dot = self.quantum_dot_center - electron["pos"]
            r_mag_dot = np.linalg.norm(r_vec_dot) + 1e-5
            force += k * electron["charge"] * self.quantum_dot_potential * r_vec_dot / (r_mag_dot ** 3)

            # Add external electric field
            force += self.electric_field * electron["charge"]

            # Update velocity
            electron["vel"] += force * 0.1  # Adjust scaling for smooth simulation

    def update_positions(self):
        """Update electron positions and handle boundary conditions."""
        for electron in self.electrons:
            electron["pos"] += electron["vel"]

            # Reflect electrons off walls
            for dim in range(2):
                if electron["pos"][dim] < 0 or electron["pos"][dim] > [self.screen_width, self.screen_height][dim]:
                    electron["vel"][dim] *= -1
                    electron["pos"][dim] = np.clip(electron["pos"][dim], 0, [self.screen_width, self.screen_height][dim])

    def draw_electrons(self):
        """Draw all electrons on the screen."""
        for electron in self.electrons:
            pygame.draw.circle(self.screen, (0, 255, 255), electron["pos"].astype(int), 4)

    def draw_quantum_dot(self):
        """Draw the quantum dot on the screen."""
        pygame.draw.circle(self.screen, (255, 255, 0), self.quantum_dot_center.astype(int), self.quantum_dot_radius, 2)

    def run(self):
        """Main loop for running the electron simulation."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Clear the screen
            self.apply_forces()
            self.update_positions()
            self.draw_electrons()
            self.draw_quantum_dot()

            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Cap the frame rate

        pygame.quit()
