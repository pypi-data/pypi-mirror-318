import os

class Config:
    """Configuration class for paths, settings, and environment variables."""
    
    def __init__(self):
        self.dataset_path = os.getenv(
            'DATASET_PATH', 
            r"C:\arjun-project\quantum_dot_sim\data\unified_combined_physics_dataset.npy"
        )
        self.model_path = os.getenv(
            'MODEL_PATH', 
            r"C:\arjun-project\quantum_dot_sim\models\quantum_unifiedphysics_model.h5"
        )
    
        self.log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        self.log_file = os.getenv('LOG_FILE', r"C:\arjun-project\quantum_dot_sim\output\simulation.log")
    
        self.interactive_mode = os.getenv('INTERACTIVE_MODE', 'True').lower() == 'true'
        self.default_plot_type = os.getenv('DEFAULT_PLOT_TYPE', 'line')  
    
        self.default_radius = float(os.getenv('DEFAULT_RADIUS', 1e-9))  # in meters (1 nm by default)
        self.max_wavefunction_levels = int(os.getenv('MAX_WAVEFUNCTION_LEVELS', 5))  # Default 5
        
        self.energy_levels_file = os.getenv('ENERGY_LEVELS_FILE', r"C:\arjun-project\quantum_dot_sim\data\energy_levels.npy")
        self.wavefunctions_file = os.getenv('WAVEFUNCTIONS_FILE', r"C:\arjun-project\quantum_dot_sim\data\wavefunctions.npy")
        
        # directories for output are created
        self.output_dir = os.getenv('OUTPUT_DIR', r"C:\arjun-project\quantum_dot_sim\output")
        os.makedirs(self.output_dir, exist_ok=True)

        # Debug mode flag (useful for development)
        self.debug_mode = os.getenv('DEBUG_MODE', 'False').lower() == 'true'

    def print_config(self):
        """Print the current configuration for debugging or validation purposes."""
        print(f"Dataset Path: {self.dataset_path}")
        print(f"Model Path: {self.model_path}")
        print(f"Log Level: {self.log_level}")
        print(f"Log File: {self.log_file}")
        print(f"Interactive Mode: {self.interactive_mode}")
        print(f"Default Plot Type: {self.default_plot_type}")
        print(f"Default Quantum Dot Radius: {self.default_radius} meters")
        print(f"Max Wavefunction Levels: {self.max_wavefunction_levels}")
        print(f"Energy Levels File: {self.energy_levels_file}")
        print(f"Wavefunctions File: {self.wavefunctions_file}")
        print(f"Output Directory: {self.output_dir}")
        print(f"Debug Mode: {self.debug_mode}")

# Instantiate CONFIG at the end of the file
CONFIG = Config()
