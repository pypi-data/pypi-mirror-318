import numpy as np

import matplotlib

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from .ExperimentBase import Experiment
from .DataExtractor import EDEMDataExtractor
import imageio
from multiprocessing import Pool, cpu_count
import pyvista as pv
from tqdm import tqdm
matplotlib.use('TkAgg')

pv.OFF_SCREEN = True

num_cpus = 16
particle_mass= 1.3089969389957472 # kg

def process_frame(args):
    time_step, particle_positions, surfSurf_df, surfGeom_df, static_cube = args
    plotter = pv.Plotter(off_screen=True)
    plotter.add_mesh(static_cube, color='lightblue', opacity=0.15, style='wireframe')

    cloud = pv.PolyData(particle_positions)
    plotter.add_mesh(cloud, color='yellow', point_size=40, render_points_as_spheres=True, opacity=0.6)

    current_surfSurf_contacts = surfSurf_df[surfSurf_df['timestep'] == time_step]
    current_surfGeom_contacts = surfGeom_df[surfGeom_df['timestep'] == time_step]

    contact_points = []
    contact_lines_points = []
    contact_lines_indices = []
    geomcontact_lines_points = []
    geomcontact_lines_indices = []
    for _, contact in current_surfSurf_contacts.iterrows():
        ids = eval(contact['getIds']) if isinstance(contact['getIds'], str) else contact['getIds']
        pos = eval(contact['getPositions']) if isinstance(contact['getPositions'], str) else contact['getPositions']

        contact_points.append(pos)

        if len(ids) >= 2:
            start_point = particle_positions[ids[0] - 1]
            end_point = particle_positions[ids[1] - 1]

            idx = len(contact_lines_points)
            contact_lines_points.extend([start_point, end_point])
            contact_lines_indices.extend([2, idx, idx + 1])

    for _, contact in current_surfGeom_contacts.iterrows():
        pos_geom = eval(contact['getPositions']) if isinstance(contact['getPositions'], str) else contact['getPositions']
        ids = eval(contact['getIds']) if isinstance(contact['getIds'], str) else contact['getIds']
        if len(ids) >= 2:
            start_point = pos_geom
            end_point = particle_positions[ids[0] - 1]

            idx = len(geomcontact_lines_points)
            geomcontact_lines_points.extend([start_point, end_point])
            geomcontact_lines_indices.extend([2, idx, idx + 1])

    if contact_points:
        contact_points = pv.PolyData(np.array(contact_points))
        plotter.add_mesh(contact_points, color='green', point_size=3, render_points_as_spheres=True)

    if contact_lines_points:
        lines = pv.PolyData(np.array(contact_lines_points), lines=np.array(contact_lines_indices))
        plotter.add_mesh(lines, color='red', line_width=2)

    if geomcontact_lines_points:
        linesgeom = pv.PolyData(np.array(geomcontact_lines_points), lines=np.array(geomcontact_lines_indices))
        plotter.add_mesh(linesgeom, color='blue', line_width=2)

    plotter.add_text(f"Time step: {time_step}", position='upper_left', font_size=10)
    plotter.camera_position = [(1.5, 1.5, 1.5), (0.5, 0.5, 0.5), (0, 0, 1)]

    image = plotter.screenshot(transparent_background=True)
    plotter.close()
    return image

def precompute_static_elements():
    cube = pv.Cube(center=(0, 0, 0), x_length=1, y_length=1, z_length=1)
    cube.compute_normals(inplace=True)
    return cube

class Visualisation(EDEMDataExtractor):
    def __init__(self, experiment: Experiment, positions):
        super().__init__(experiment)
        self.positions = positions


    def animate_deck(self, save=True, show=False, particle_size=20):
        positions = self.positions
        frame_rate = 30
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        beat = np.arange(self.timestepvalues[1], self.timestepvalues[-1], step=1 / frame_rate)
        frame_indices = [np.abs(np.array(self.timestepvalues) - t).argmin() for t in beat]
        pos0 = positions[0]
        x0, y0, z0 = [pos0[:, _] for _ in range(3)]

        def animate(i):
            pos = positions[i]
            x, y, z = [pos[:, _] for _ in range(3)]
            ax.cla()
            limits = np.array([self.domainMin, self.domainMax])
            ax.set_xlim(limits[:, 0])
            ax.set_ylim(limits[:, 1])
            ax.set_zlim(limits[:, 2])
            ax.scatter3D(x, y, z, alpha=0.7, marker='.', c="blue", s=particle_size)
            if i < 10:
                ax.scatter3D(x0, y0, z0, alpha=0.1, marker='.', c="red")
            ax.view_init(20, i / frame_rate, 0)
            ax.set_title(f"Simulation time: {self.timestepvalues[i]:.4f}")
#            fig.tight_layout()

        ani = animation.FuncAnimation(fig, animate, frames=frame_indices, interval=1000 / frame_rate, repeat=True)
        if save:
            ani.save(self.gif_path, dpi=200, fps=frame_rate, writer='pillow')
        if show:
            plt.show()
            plt.pause(0.1)
            plt.close()

    def contact_video(self, surfSurf_df, surfGeom_df, save=False, start_step=1, end_step=None, fps=20):
        positions = self.positions
        if end_step is None:
            end_step = self.num_timesteps

        static_cube = precompute_static_elements()

        args_list = [(time_step, self.positions[time_step - 1], surfSurf_df, surfGeom_df, static_cube)
                     for time_step in range(start_step, end_step)]

        print("Writing video...")
        if save:
#            imageio.mimsave(self.contact_video_path, frames, fps=fps)
            with Pool(processes=num_cpus) as pool:
                frames = list(tqdm(pool.imap(process_frame, args_list, chunksize=10), total=len(args_list), desc="Creating Contacts Video"))
            with imageio.get_writer(self.contact_video_path, fps=fps) as writer:
                for f in frames:
                    writer.append_data(f)





    # def contact_video(self, surfSurf_df, surfGeom_df, save=False, start_step=1, end_step=None, fps=20):
    #     positions = self.positions
    #     if end_step is None:
    #         end_step = self.num_timesteps

    #     static_cube = precompute_static_elements()

    #     plotter = pv.Plotter(off_screen=True)
    #     plotter.enable_shadows()
    #     plotter.add_mesh(static_cube, color='lightblue', opacity=0.15, style='wireframe')

    #     if save:
    #         with imageio.get_writer(self.contact_video_path, fps=fps) as writer:
    #             for time_step in tqdm(range(start_step, end_step), desc="Creating Contacts Video"):
    #                 particle_positions = positions[time_step - 1]

    #                 plotter.clear()  # Clear previous frame
    #                 plotter.enable_shadows()
    #                 # plotter.camera_position = [(1.5, 1.5, 1.5), (0.5, 0.5, 0.5), (0, 0, 1)]

    #                 plotter.add_mesh(static_cube, color='lightblue', opacity=0.15, style='wireframe')
    #                 cloud = pv.PolyData(particle_positions)
    #                 plotter.add_mesh(cloud, color='yellow', point_size=40, render_points_as_spheres=True, opacity=0.6)

                    
    #                 current_surfSurf_contacts = surfSurf_df[surfSurf_df['timestep'] == time_step]
    #                 current_surfGeom_contacts = surfGeom_df[surfGeom_df['timestep'] == time_step]

    #                 contact_points = []
    #                 contact_lines_points = []
    #                 contact_lines_indices = []
    #                 geomcontact_lines_points = []
    #                 geomcontact_lines_indices = []

    #                 for _, contact in current_surfSurf_contacts.iterrows():
    #                     ids = eval(contact['getIds']) if isinstance(contact['getIds'], str) else contact['getIds']
    #                     pos = eval(contact['getPositions']) if isinstance(contact['getPositions'], str) else contact['getPositions']

    #                     contact_points.append(pos)

    #                     if len(ids) >= 2:
    #                         start_point = particle_positions[ids[0] - 1]
    #                         end_point = particle_positions[ids[1] - 1]

    #                         idx = len(contact_lines_points)
    #                         contact_lines_points.extend([start_point, end_point])
    #                         contact_lines_indices.extend([2, idx, idx + 1])

    #                 for _, contact in current_surfGeom_contacts.iterrows():
    #                     pos_geom = eval(contact['getPositions']) if isinstance(contact['getPositions'], str) else contact['getPositions']
    #                     ids = eval(contact['getIds']) if isinstance(contact['getIds'], str) else contact['getIds']
    #                     if len(ids) >= 2:
    #                         start_point = pos_geom
    #                         end_point = particle_positions[ids[0] - 1]

    #                         idx = len(geomcontact_lines_points)
    #                         geomcontact_lines_points.extend([start_point, end_point])
    #                         geomcontact_lines_indices.extend([2, idx, idx + 1])

    #                 if contact_points:
    #                     contact_points = pv.PolyData(np.array(contact_points))
    #                     plotter.add_mesh(contact_points, color='green', point_size=3, render_points_as_spheres=True)

    #                 if contact_lines_points:
    #                     lines = pv.PolyData(np.array(contact_lines_points), lines=np.array(contact_lines_indices))
    #                     plotter.add_mesh(lines, color='red', line_width=2)

    #                 if geomcontact_lines_points:
    #                     linesgeom = pv.PolyData(np.array(geomcontact_lines_points), lines=np.array(geomcontact_lines_indices))
    #                     plotter.add_mesh(linesgeom, color='blue', line_width=2)

    #                 plotter.add_text(f"Time step: {time_step}", position='upper_left', font_size=10)


    #                 image = plotter.screenshot(transparent_background=True)
    #                 writer.append_data(image)
    #                 plotter.clear()  # Clear the plotter for the next frame