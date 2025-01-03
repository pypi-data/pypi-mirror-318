import os
from dataclasses import dataclass

@dataclass
class Experiment:
    exp_path: str
    name: str
    def __post_init__(self):
        self.p2pcontact_path = os.path.join(self.exp_path, 'contacts', f"contacts_surfSurf_{self.name}.feather")
        self.p2gcontact_path = os.path.join(self.exp_path, 'contacts', f"contacts_surfGeom_{self.name}.feather")
        self.position_path = os.path.join(self.exp_path, 'particles', "positions", f"positions_{self.name}.npy")
        self.vel_path = os.path.join(self.exp_path, 'particles', "velocities", f"velocities_{self.name}.npy")
        self.force_path = os.path.join(self.exp_path, 'particles', "forces", f"forces_{self.name}.npy")
        self.orientation_path = os.path.join(self.exp_path, 'particles', "orientations", f"orientations_{self.name}.npy")
        self.torque_path = os.path.join(self.exp_path, 'particles', "torque", f"torque_{self.name}.npy")
        self.angular_velocity_path = os.path.join(self.exp_path, 'particles', "angular_velocity", f"angular_velocity_{self.name}.npy")
        self.particle_energy_path = os.path.join(self.exp_path, 'particles', "energy", f"ke_{self.name}.npy")
        self.rot_matrix_path = os.path.join(self.exp_path, 'particles', "rot_matrices", f"rot_matrices_{self.name}.npy")
#        self.accel_path = os.path.join(self.exp_path, 'particles', "accelerations", f"accels_{self.name}.npy")
        self.dem_name = self.name + '.dem'
        self.dem_file_path = os.path.join(self.exp_path, self.dem_name)
        self.mat_prop_file_path = os.path.join(self.exp_path, 'metadata', f"material_properties_{self.name}.json")
        self.particle_prop_file_path = os.path.join(self.exp_path, 'metadata', f"particle_properties_{self.name}.json")
        self.energy_path = os.path.join(self.exp_path, 'energy', 'energy_'+f"{self.name}.csv")
        self.gif_path = os.path.join(self.exp_path, 'gifs', f"{self.name}.gif")
        self.contact_video_path = os.path.join(self.exp_path, 'contacts', 'videos', f"{self.name}.mp4")


