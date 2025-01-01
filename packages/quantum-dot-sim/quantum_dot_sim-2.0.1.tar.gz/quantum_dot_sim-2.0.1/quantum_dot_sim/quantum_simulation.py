import pygame
import numpy as np
import math
from scipy.spatial.transform import Rotation
from typing import List, Tuple, Optional
from dataclasses import dataclass
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

@dataclass
class Material:
    """Material properties for 3D rendering."""
    ambient: Tuple[float, float, float, float] = (0.2, 0.2, 0.2, 1.0)
    diffuse: Tuple[float, float, float, float] = (0.8, 0.8, 0.8, 1.0)
    specular: Tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0)
    shininess: float = 32.0

class Light:
    """Represents a light source in the 3D scene."""
    def __init__(self, position: Tuple[float, float, float, float], 
                 ambient: Tuple[float, float, float, float],
                 diffuse: Tuple[float, float, float, float],
                 specular: Tuple[float, float, float, float]):
        self.position = position
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.enabled = True

    def setup(self, light_index: int):
        """Setup light in OpenGL."""
        light = GL_LIGHT0 + light_index
        if self.enabled:
            glEnable(light)
            glLightfv(light, GL_POSITION, self.position)
            glLightfv(light, GL_AMBIENT, self.ambient)
            glLightfv(light, GL_DIFFUSE, self.diffuse)
            glLightfv(light, GL_SPECULAR, self.specular)
        else:
            glDisable(light)

class Particle:
    """Represents a particle with enhanced 3D rendering."""
    def __init__(self, x: float, y: float, z: float, velocity: np.ndarray, particle_type: str):
        self.position = np.array([x, y, z], dtype=float)
        self.velocity = velocity
        self.particle_type = particle_type
        self.charge = -1.0 if particle_type == "electron" else 1.0
        self.radius = 0.5 if particle_type == "electron" else 0.8
        self.material = Material(
            ambient=(0.1, 0.1, 0.5, 1.0) if particle_type == "electron" else (0.5, 0.1, 0.1, 1.0),
            diffuse=(0.0, 0.0, 1.0, 1.0) if particle_type == "electron" else (1.0, 0.2, 0.2, 1.0)
        )
        self.trail: List[np.ndarray] = []
        self.max_trail_length = 20

    def update(self, dt: float, quantum_dot_position: np.ndarray):
        """Update particle position and trail."""
        # Store current position in trail
        self.trail.append(self.position.copy())
        if len(self.trail) > self.max_trail_length:
            self.trail.pop(0)

        # Calculate quantum forces
        r = self.position - quantum_dot_position
        distance = np.linalg.norm(r)
        if distance > 1e-10:
            force = 1e-9 * self.charge * r / (distance ** 3)
            self.velocity += force * dt

        # Add quantum effects
        if self.particle_type == "electron":
            # Add quantum tunneling probability
            if distance < 5.0 and np.random.random() < 0.01:
                # Simulate tunneling by randomly repositioning
                angle = np.random.uniform(0, 2 * np.pi)
                self.position = quantum_dot_position + np.array([
                    6.0 * np.cos(angle),
                    6.0 * np.sin(angle),
                    np.random.uniform(-2, 2)
                ])

        # Update position
        self.position += self.velocity * dt

        # Add quantum uncertainty
        self.position += np.random.normal(0, 0.01, 3)
        
        # Add plasma-specific behavior
        if self.particle_type == "plasma":
            self.velocity += np.random.normal(0, 0.1, 3)
            # Add plasma oscillations
            self.velocity *= 0.99  # Damping
            plasma_frequency = 0.5
            self.velocity += 0.1 * np.sin(plasma_frequency * dt) * np.random.rand(3)

    def draw(self):
        """Draw particle with OpenGL."""
        glPushMatrix()
        glTranslatef(*self.position)
        
        # Apply material properties
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.material.ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.material.diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.material.specular)
        glMaterialf(GL_FRONT, GL_SHININESS, self.material.shininess)

        # Draw sphere for particle
        quad = gluNewQuadric()
        gluSphere(quad, self.radius, 16, 16)
        
        # Draw particle trail
        if len(self.trail) > 1:
            glDisable(GL_LIGHTING)
            glBegin(GL_LINE_STRIP)
            alpha = 1.0
            for pos in self.trail:
                glColor4f(*self.material.diffuse[:3], alpha)
                glVertex3f(*pos)
                alpha *= 0.9
            glEnd()
            glEnable(GL_LIGHTING)
        
        glPopMatrix()

class QuantumDot:
    """Enhanced quantum dot with energy levels and quantum effects."""
    def __init__(self, x: float, y: float, z: float, radius: float):
        self.position = np.array([x, y, z], dtype=float)
        self.radius = radius
        self.material = Material(
            ambient=(0.2, 0.1, 0.0, 1.0),
            diffuse=(1.0, 0.65, 0.0, 1.0),
            specular=(1.0, 0.8, 0.0, 1.0),
            shininess=64.0
        )
        self.energy_levels = [1, 2, 3, 4, 5]
        self.excitation = 0.0
        self.orbital_rotation = 0.0
        self.electron_probability_cloud: List[np.ndarray] = []
        self.generate_probability_cloud()

    def generate_probability_cloud(self):
        """Generate points representing electron probability cloud."""
        n_points = 1000
        for _ in range(n_points):
            # Generate points based on quantum mechanical probability distribution
            r = np.random.exponential(2.0) * self.radius
            theta = np.random.uniform(0, np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            
            x = r * np.sin(theta) * np.cos(phi)
            y = r * np.sin(theta) * np.sin(phi)
            z = r * np.cos(theta)
            
            self.electron_probability_cloud.append(np.array([x, y, z]))

    def update(self, dt: float, particles: List[Particle]):
        """Update quantum dot state with quantum effects."""
        self.excitation = 0.0
        self.orbital_rotation += dt * 0.5
        
        # Calculate quantum dot excitation based on nearby particles
        for particle in particles:
            distance = np.linalg.norm(particle.position - self.position)
            if distance < self.radius * 3:
                # Quantum tunneling probability increases with proximity
                tunneling_prob = np.exp(-distance / self.radius)
                self.excitation += tunneling_prob * 0.2
                
                # Energy level transitions
                if particle.particle_type == "electron" and distance < self.radius * 1.5:
                    if np.random.random() < 0.05:  # Probability of energy level jump
                        self.excitation += 0.5
                        # Emit a photon (could be visualized as a brief flash)

    def draw(self):
        """Draw quantum dot with OpenGL."""
        glPushMatrix()
        glTranslatef(*self.position)
        
        # Apply material properties
        glMaterialfv(GL_FRONT, GL_AMBIENT, self.material.ambient)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.material.diffuse)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.material.specular)
        glMaterialf(GL_FRONT, GL_SHININESS, self.material.shininess)

        # Draw main sphere
        quad = gluNewQuadric()
        gluSphere(quad, self.radius, 32, 32)
        
        # Draw probability cloud
        if self.excitation > 0.1:
            glDisable(GL_LIGHTING)
            glPointSize(2.0)
            glBegin(GL_POINTS)
            for point in self.electron_probability_cloud:
                # Rotate points around Y axis
                rotated_point = np.array([
                    point[0] * np.cos(self.orbital_rotation) - point[2] * np.sin(self.orbital_rotation),
                    point[1],
                    point[0] * np.sin(self.orbital_rotation) + point[2] * np.cos(self.orbital_rotation)
                ])
                alpha = np.random.uniform(0.1, 0.3) * self.excitation
                glColor4f(1.0, 0.8, 0.0, alpha)
                glVertex3f(*rotated_point)
            glEnd()
            glEnable(GL_LIGHTING)

        # Draw energy level rings
        for i, level in enumerate(self.energy_levels):
            radius = self.radius * (1 + (i + 1) * 0.3)
            glDisable(GL_LIGHTING)
            glColor4f(1.0, 0.8, 0.0, 0.2)
            glBegin(GL_LINE_LOOP)
            for angle in range(0, 360, 10):
                rad = math.radians(angle)
                x = radius * math.cos(rad)
                y = radius * math.sin(rad)
                glVertex3f(x, y, 0)
            glEnd()
            glEnable(GL_LIGHTING)
            
        glPopMatrix()

class QuantumSimulation:
    """Enhanced 3D quantum dot simulation."""
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
        self.width = width
        self.height = height
        self.clock = pygame.time.Clock()
        
        # Initialize OpenGL
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        
        # Setup perspective
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (width/height), 0.1, 500.0)
        
        # Initialize scene
        self.camera_distance = 50.0
        self.camera_rotation = [0.0, 0.0]
        self.quantum_dot = QuantumDot(0, 0, 0, 2.0)
        self.particles: List[Particle] = []
        self.lights: List[Light] = self.setup_lights()
        self.running = True

    def setup_lights(self) -> List[Light]:
        """Setup lighting for the scene."""
        lights = [
            Light(
                position=(50.0, 50.0, 50.0, 1.0),
                ambient=(0.2, 0.2, 0.2, 1.0),
                diffuse=(1.0, 1.0, 1.0, 1.0),
                specular=(1.0, 1.0, 1.0, 1.0)
            ),
            Light(
                position=(-30.0, -30.0, 50.0, 1.0),
                ambient=(0.1, 0.1, 0.1, 1.0),
                diffuse=(0.3, 0.3, 0.4, 1.0),
                specular=(0.3, 0.3, 0.4, 1.0)
            )
        ]
        return lights

    def handle_events(self):
        """Handle input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # Toggle second light
                    self.lights[1].enabled = not self.lights[1].enabled

        # Camera controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.camera_distance -= 1.0
        if keys[pygame.K_s]: self.camera_distance += 1.0
        
        # Mouse rotation
        if pygame.mouse.get_pressed()[0]:
            rel_x, rel_y = pygame.mouse.get_rel()
            self.camera_rotation[0] += rel_y * 0.5
            self.camera_rotation[1] += rel_x * 0.5
        else:
            pygame.mouse.get_rel()

    def update(self):
        """Update simulation state."""
        dt = 0.1
        for particle in self.particles:
            particle.update(dt, self.quantum_dot.position)
        self.quantum_dot.update(dt, self.particles)

    def draw(self):
        """Draw the scene."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        # Setup camera
        glTranslatef(0, 0, -self.camera_distance)
        glRotatef(self.camera_rotation[0], 1, 0, 0)
        glRotatef(self.camera_rotation[1], 0, 1, 0)
        
        # Setup lights
        for i, light in enumerate(self.lights):
            light.setup(i)
        
        # Draw coordinate axes
        glDisable(GL_LIGHTING)
        glBegin(GL_LINES)
        # X axis (red)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(10, 0, 0)
        # Y axis (green)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 10, 0)
        # Z axis (blue)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 10)
        glEnd()
        glEnable(GL_LIGHTING)

        # Draw quantum dot
        self.quantum_dot.draw()
        
        # Draw particles
        for particle in self.particles:
            particle.draw()
        
        pygame.display.flip()

    def run(self):
        """Main simulation loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

class ElectronSimulation(QuantumSimulation):
    """Enhanced electron-quantum dot interaction simulation."""
    def __init__(self, width: int = 800, height: int = 600):
        super().__init__(width, height)
        pygame.display.set_caption("Quantum Dot - Electron Interaction (Enhanced 3D)")
        
        # Add initial electrons with more varied initial conditions
        for _ in range(15):
            # Create electrons in a spherical distribution
            phi = np.random.uniform(0, 2 * np.pi)
            theta = np.random.uniform(0, np.pi)
            r = np.random.uniform(10, 30)
            
            pos = np.array([
                r * np.sin(theta) * np.cos(phi),
                r * np.sin(theta) * np.sin(phi),
                r * np.cos(theta)
            ])
            
            # Initial velocity tangent to sphere
            vel = np.cross(pos, np.array([0, 0, 1]))
            vel = 0.3 * vel / np.linalg.norm(vel)
            vel += np.random.uniform(-0.1, 0.1, 3)
            
            self.particles.append(Particle(*pos, vel, "electron"))

class PlasmaSimulation(QuantumSimulation):
    """Enhanced plasma-quantum dot interaction simulation."""
    def __init__(self, width: int = 800, height: int = 600):
        super().__init__(width, height)
        pygame.display.set_caption("Quantum Dot - Plasma Interaction (Enhanced 3D)")
        
        # Add initial plasma particles
        for _ in range(25):
            # Create plasma particles in a toroidal distribution
            theta = np.random.uniform(0, 2 * np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(15, 25)
            R = 20  # Major radius of torus
            
            pos = np.array([
                (R + r * np.cos(theta)) * np.cos(phi),
                (R + r * np.cos(theta)) * np.sin(phi),
                r * np.sin(theta)
            ])
            
            # Initial velocity following toroidal field lines
            vel = np.array([
                -np.sin(phi),
                np.cos(phi),
                0.1 * np.cos(theta)
            ])
            vel = 0.2 * vel / np.linalg.norm(vel)
            
            self.particles.append(Particle(*pos, vel, "plasma"))

    def update(self):
        """Update simulation state with enhanced plasma effects."""
        super().update()
        
        # Add new plasma particles to maintain density
        if np.random.random() < 0.02:
            theta = np.random.uniform(0, 2 * np.pi)
            phi = np.random.uniform(0, 2 * np.pi)
            r = np.random.uniform(15, 25)
            R = 20
            
            pos = np.array([
                (R + r * np.cos(theta)) * np.cos(phi),
                (R + r * np.cos(theta)) * np.sin(phi),
                r * np.sin(theta)
            ])
            
            vel = np.array([
                -np.sin(phi),
                np.cos(phi),
                0.1 * np.cos(theta)
            ])
            vel = 0.2 * vel / np.linalg.norm(vel)
            
            self.particles.append(Particle(*pos, vel, "plasma"))
        
        # Remove particles that get too far away
        self.particles = [p for p in self.particles if np.linalg.norm(p.position) < 100]

def run_simulation(sim_type: str = "electron"):
    """Run the specified type of enhanced 3D simulation."""
    if sim_type.lower() == "electron":
        sim = ElectronSimulation()
    elif sim_type.lower() == "plasma":
        sim = PlasmaSimulation()
    else:
        raise ValueError("Invalid simulation type. Choose 'electron' or 'plasma'.")
    
    sim.run()

if __name__ == "__main__":
    import sys
    sim_type = sys.argv[1] if len(sys.argv) > 1 else "electron"
    run_simulation(sim_type)