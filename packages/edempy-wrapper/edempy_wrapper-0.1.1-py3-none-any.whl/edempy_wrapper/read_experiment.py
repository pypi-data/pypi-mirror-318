import numpy as np
import os
import pandas as pd
from .ExperimentBase import Experiment
import json
"""
dem_folder_path = '/media/deniz/CommonStorage/Datasets/EDEMv2/collision_box/'
name = 'exp_1'

exp = Experiment(
    exp_path=dem_folder_path,
    name=name,
    )

"""

def load_energy(exp_obj):
    return pd.read_csv(exp_obj.energy_path)


def load_particle_energy(exp_obj):
    return np.load(exp_obj.particle_energy_path)

def load_material_props(exp_obj):
    """
    Load material properties from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    dict: The loaded material properties dictionary.
    """
    with open(exp_obj.mat_prop_file_path, 'r') as f:
        material_properties = json.load(f)
    print(f"Material properties loaded from {exp_obj.mat_prop_file_path}")
    return material_properties


def load_particle_props(exp_obj):
    """
    Load Particle properties from a JSON file.

    Args:
    file_path (str): Path to the JSON file.

    Returns:
    dict: The loaded Particle properties dictionary.
    """
    with open(exp_obj.particle_prop_file_path, 'r') as f:
        particle_properties = json.load(f)
    print(f"Particle properties loaded from {exp_obj.particle_prop_file_path}")
    return particle_properties



def load_kinematics(exp_obj):
    position = np.load(exp_obj.position_path)
    velocity = np.load(exp_obj.vel_path)
    force = np.load(exp_obj.force_path)
    return position, velocity, force

def eval_list_str(column):
    return column.apply(lambda x: eval(x) if isinstance(x, str) and x.startswith('[') and x.endswith(']') else x)


def load_contacts(exp_obj):
    p2p_contacts = pd.read_feather(exp_obj.p2pcontact_path)
    p2g_contacts = pd.read_feather(exp_obj.p2gcontact_path)
    for column in p2p_contacts.columns:
        p2p_contacts[column] = eval_list_str(p2p_contacts[column])
    
    for column in p2g_contacts.columns:
        p2g_contacts[column] = eval_list_str(p2g_contacts[column])

    return p2p_contacts, p2g_contacts


# def read_contacts(self):
#     def eval_list_str(column):
#         return column.apply(
#             lambda x: eval(x) if isinstance(x, str) and x.startswith('[') and x.endswith(']') else x)

#     surfSurf_df = pd.read_csv(self.p2pcontact_path)
#     surfGeom_df = pd.read_csv(self.p2gcontact_path)

#     # Convert string representations of lists back to lists
#     for column in surfSurf_df.columns:
#         surfSurf_df[column] = eval_list_str(surfSurf_df[column])

#     for column in surfGeom_df.columns:
#         surfGeom_df[column] = eval_list_str(surfGeom_df[column])

#         return surfSurf_df, surfGeom_df