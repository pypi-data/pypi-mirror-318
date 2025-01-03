#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:01:58 2024

@author: deniz
"""

import functools
from time import time
import numpy as np
import pandas as pd
import json
from edempy import Deck
from .ExperimentBase import Experiment
from tqdm import tqdm
from collections import defaultdict


def timer(func):
    """Decorator to measure the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Timer Started for function: {func.__name__}")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"{func.__name__} took {end - start:.4f} secs with arguments: {args}, {kwargs}")
        return result

    return wrapper


class EDEMDataExtractor(Experiment):
    def __init__(self, experiment: Experiment):
        super().__init__(experiment.exp_path, experiment.name)
        self.deck = Deck(self.dem_file_path, mode="r")
        deck = self.deck
        self.num_timesteps = deck.numTimesteps
        # Skipping timestep 0, generating particles at times step 0, there might not be particles
        # particle_ids are not consistent throghout the timesteps
        self.timesteps, self.timestepvalues = map(np.array, zip(*[[k, deck.timestepValues[k]] for k in
                                                                  range(1, self.num_timesteps)]))
        self.particle_ids = np.array([deck.timestep[k].particle[0].getIds() for k in self.timesteps])
        self.num_particles = self.particle_ids.shape[1]
        self.geometryNames = deck.timestep[1].geometryNames
        self.bounding_box_name = next((item for i, item in enumerate(self.geometryNames) if ('Bound' in item) or ('bound' in item)))
        self.material_properties = None
        self.domainMin = deck.timestep[0].domainMin
        self.domainMax = deck.timestep[0].domainMax

    def getSystemEnergy(self) -> pd.DataFrame:
        data = []
        for k in self.timesteps:
            energy = self.deck.timestep[k].energy
            data.append({
                'timestep': k,
                'time': self.deck.timestepValues[k],
                'kinetic_energy': energy.getSystemKineticEnergy(),
                'potential_energy': energy.getSystemPotentialEnergy(),
                'total_energy': energy.getSystemEnergy(),
                'loss_from_contacts': energy.getLossFromContacts()
            })
        return pd.DataFrame(data)

    def saveSystemEnergy(self):
        systemEnergy = self.getSystemEnergy()
        systemEnergy.set_index('timestep', inplace=True)
        systemEnergy.to_csv(self.energy_path)
        print("System Energy Saved to {}".format(self.energy_path))
        return systemEnergy

    def getMaterialProperties(self):
        ts0 = self.deck.timestep[0]

        # Create a nested defaultdict structure
        materials = defaultdict(lambda: defaultdict(lambda: defaultdict(dict)))

        # Store individual material properties
        for name, density, mat_type, poisson, shear in zip(
                ts0.materials.names,
                ts0.materials.density,
                ts0.materials.type,
                ts0.materials.poisson_ratio,
                ts0.materials.shear_modulus
        ):
            materials[name].update({
                'density': density,
                'type': mat_type,
                'poisson_ratio': poisson,
                'shear_modulus': shear
            })

        # Store interaction properties
        for pair, rolling, restitution, static in zip(
                ts0.interactionPairs,
                ts0.interactions.rolling_friction,
                ts0.interactions.restitution,
                ts0.interactions.static_friction
        ):
            mat1, mat2 = pair.split('~')
            interaction_props = {
                'rolling_friction': rolling,
                'restitution': restitution,
                'static_friction': static
            }
            materials[mat1]['interactions'][mat2].update(interaction_props)
            materials[mat2]['interactions'][mat1].update(interaction_props)

        # Convert defaultdict to regular dict for final output
        return {k: dict(v) for k, v in materials.items()}

    def save_material_properties(self):
        """
        Save material properties to a JSON file.
        
        Args:
        material_properties (dict): The material properties dictionary.
        file_path (str): Path to save the JSON file.

        # Usage example
        material_properties = {k: dict(v) for k, v in materials.items()}
        """

        def convert_numpy(obj):
            if isinstance(obj, np.integer):
                return int(obj)
            elif isinstance(obj, np.floating):
                return float(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            return obj

        self.material_properties = self.getMaterialProperties()

        with open(self.mat_prop_file_path, 'w') as f:
            json.dump(self.material_properties, f, default=convert_numpy, indent=2)
        print(f"Material properties saved to {self.mat_prop_file_path}")



    def saveParticleProperties(self):
        particle = self.deck.timestep[10].particle[0]
        particle_data = {
            'mass': particle.getRawMass(),
            'radius': particle.getRawSphereRadii(),
            'volume': particle.getRawVolume(),
            'inertia': particle.getRawInertia(),
            'density': particle.getRawMass() / particle.getRawVolume()
            }
        for key, value in particle_data.items():
            if isinstance(value, np.ndarray):
                particle_data[key] = value.tolist()  # Convert ndarray to list

        with open(self.particle_prop_file_path, 'w') as f:
            json.dump(particle_data, f)
        print(f"Particle properties are saved to {self.particle_prop_file_path}")
        return particle_data

    def saveGeometryPositions(self):
        geometry_positions = []
        for k in self.timesteps:
            geometry = self.deck.timestep[k].geometry
            for geom_name, geom in geometry.items():
                geometry_positions.append({
                    'timestep': k,
                    'time': self.deck.timestepValues[k],
                    'geometry_name': geom_name,
                    'coords': geom.getCoords()
                })
        return pd.DataFrame(geometry_positions)

    def _get_sorted_property(self, property_func):
        property_unsorted = np.array([property_func(k) for k in self.timesteps])
        property_sorted = np.array([
            np.array([x for _, x in sorted(zip(self.particle_ids[n-1], property_unsorted[n-1]))])
            for n in self.timesteps])
        return property_sorted

    def get_positions(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getPositions())

    def get_orientations(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getOrientation())

    def get_velocities(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getVelocities())

    def get_angular_velocities(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getAngularVelocities())

    def get_forces(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getForce())
    
    def get_torque(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getTorque())

    def get_rot_matrices(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getRotationMatrices())

    def get_particle_kinetic_energy(self):
        ke = self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getKineticEnergy())
        #pe = self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getPotentialEnergy())
        return ke

    def save_kinematics(self):
        positions = self.get_positions()
        orientations = self.get_orientations()
        velocities = self.get_velocities()
        angular_velocities = self.get_angular_velocities()
        forces = self.get_forces()
        torque = self.get_torque()
        particle_energy = self.get_particle_kinetic_energy()
        print(f"saving positions to {self.position_path}")
        np.save(self.position_path, positions)
        print(f"saving orientations to {self.orientation_path}")
        np.save(self.orientation_path, orientations)
        print(f"saving velocities to {self.vel_path}")
        np.save(self.vel_path, velocities)
        print(f"saving angular velocities to {self.angular_velocity_path}")
        np.save(self.angular_velocity_path, angular_velocities)
        print(f"saving forces to {self.force_path}")
        np.save(self.force_path, forces)
        print(f"saving torque to {self.torque_path}")
        np.save(self.torque_path, torque)
        print(f"saving particle energies to {self.particle_energy_path}")
        np.save(self.particle_energy_path, particle_energy)
        print(f"saving rot matrices to {self.rot_matrix_path}")
        np.save(self.rot_matrix_path, self.get_rot_matrices())
        # return positions


    def saveContacts(self):
        """
        Extracts and saves comprehensive contact data for both surface-to-surface
        and surface-to-geometry contacts.
        """
        deck = self.deck
        surfSurf_data = []
        surfGeom_data = []

        for k in tqdm(self.timesteps, desc="Calculating Contacts"):
            # Surface-to-Surface contacts
            ss_contacts = deck.timestep[k].contact.surfSurf
            if ss_contacts.num_contacts > 0:
                ss_data = self.extractContactData(ss_contacts, k, 'surfSurf')
                surfSurf_data.extend(ss_data)

            # Surface-to-Geometry contacts
            sg_contacts = deck.timestep[k].contact.surfGeom
            if sg_contacts.num_contacts > 0:
                sg_data = self.extractContactData(sg_contacts, k, 'surfGeom')
                surfGeom_data.extend(sg_data)

        # Save the contact data to CSV files
        pd.DataFrame(surfSurf_data).to_feather(self.p2pcontact_path, index=False)
        pd.DataFrame(surfGeom_data).to_feather(self.p2gcontact_path, index=False)

        print(f"Saved surfSurf contacts to {self.p2pcontact_path}")
        print(f"Saved surfGeom contacts to {self.p2gcontact_path}")

        # return surfSurf_data, surfGeom_data


    def extractContactData(self, contacts, timestep, contact_type):
        """
        Extracts all available data for a given contact object.
        """
        data = []

        common_methods = [
            'getNumContacts', 'getIds', 'getContactNormal', 'getContactVector1', 'getContactVector2', 'getNormalForce',
            'getTangentialForce', 'getPositions', 'getOverlapVolume', 'getNormalOverlap', 'getTangentialOverlap',
        ]

#        if contact_type == 'surfGeom':
#            common_methods.append('getSphereNumber')

        extracted_data = {method: getattr(contacts, method)() for method in common_methods}
        num_contacts = contacts.num_contacts

        for i in range(num_contacts):
            contact_info = {
                'timestep': timestep,
                'contact_type': contact_type
            }

            for method, values in extracted_data.items():
                if isinstance(values, np.ndarray):
                    if len(values.shape) == 1:
                        contact_info[method] = values[i] if i < len(values) else None
                    elif len(values.shape) == 2:
                        contact_info[method] = values[i].tolist() if i < len(values) else None
                else:
                    contact_info[method] = values

            data.append(contact_info)

        return data


    # def savecontacts(self):
    #     surfSurf_data, surfGeom_data = self.getContacts()
    #     return surfSurf_data, surfGeom_data


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

    #     return surfSurf_df, surfGeom_df


"""
       
print(material_properties['BulkMaterial 1']['density'])
print(material_properties['EquipMaterial 1']['interactions']['BulkMaterial 1']['rolling_friction'])
    



for k in range(numTimesteps):
   box = deck.timestep[k].geometry['bounding_box']
   factory = deck.timestep[k].geometry['factory_box']
   box.getForce() # returns matrix of size (12, 3)
   box.getPressure() # returns matrix of size 12x1
   factory.getVertexIds() # array([0, 1, 2, 3, 4, 5, 6, 7],
   box.getVertexIds() # array of size 8  array([ 8,  9, 10, 11, 12, 13, 14, 15], dtype=uint32) 8 corners
   box.getCoords() # 8,3 vertex coordinated
   box.getTriangleIds() # Shape 12 array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
   box.getTriangleNodes() # (12, 3)   triangle nodes that make up geometry (vertex ids used to make geometry triangle).
   factory.getTriangleNodes()
   box.getXCoords()
   factory.getXCoords()
        
        


    def _get_sorted_property(self, property_func):
        property_unsorted = np.array([property_func(k) for k in range(1, self.num_timesteps)])
        property_sorted = np.array([
            np.array([x for _, x in sorted(zip(self.particle_ids[n], property_unsorted[n]))])
            for n in range(self.num_timesteps - 1)
            ])
        return property_sorted

    def get_positions(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getPositions())

    def get_velocities(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getVelocities())

    def get_forces(self):
        return self._get_sorted_property(lambda k: self.deck.timestep[k].particle[0].getForce())

    @timer
    def extract_data(self):
        positions = self.get_positions()
        velocities = self.get_velocities()
        forces = self.get_forces()
        return positions, velocities, forces
        
"""
