#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:24:21 2024

@author: deniz
"""

from .ExperimentBase import Experiment
from . import read_experiment

class ExpData(Experiment):
    def __init__(self, exp: Experiment):        
        self.__dict__.update(exp.__dict__)
        self.positions, self.velocities, self.forces = read_experiment.load_kinematics(exp)
        #self.p2p_contacts, self.p2g_contacts = read_experiment.load_contacts(exp)
        self.sys_energy = read_experiment.load_energy(exp)
        self.part_kin_energy = read_experiment.load_particle_energy(exp)
        self.particle_props =  read_experiment.load_particle_props(exp)
        self.material_props =  read_experiment.load_material_props(exp)


"""
dem_folder_path = '/media/deniz/CommonStorage/Datasets/EDEMv2/collision_box/'
name = 'base'
exp = Experiment(exp_path=dem_folder_path,name=name)

particle_data = ExpData(exp)

particle_data.positions
particle_data.velocities
particle_data.p2p_contacts
particle_data.sys_energy
particle_data.part_kin_energy
particle_data.particle_props
particle_data.material_props


particle_speeds = np.linalg.norm(particle_data.velocities,axis=2)
calc_kin = 0.5*particle_data.particle_props['mass']*particle_speeds**2


import matplotlib.pyplot as plt
plt.figure()
plt.plot(particle_data.sys_energy.total_energy, label='total energy')
plt.plot(particle_data.sys_energy.potential_energy, label='potential energy')
plt.plot(particle_data.sys_energy.kinetic_energy, label='kinetic energy')
plt.plot(particle_data.sys_energy.kinetic_energy + particle_data.sys_energy.potential_energy, '.',label='kinetic + potential energy')
plt.plot(particle_data.part_kin_energy.sum(axis=1), '.g',label = 'total particle kinetic energy')
plt.plot(-particle_data.sys_energy.loss_from_contacts, label = 'loss from contacts')
plt.plot(calc_kin.sum(axis=1), label='calculated particle kinetic energy')
plt.xlabel('Time')
plt.legend()
"""
