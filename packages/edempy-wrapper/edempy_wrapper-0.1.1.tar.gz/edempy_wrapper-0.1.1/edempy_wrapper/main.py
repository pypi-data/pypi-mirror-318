# #%%
# from .ExperimentBase import Experiment
# from .DataExtractor import EDEMDataExtractor
# # from ExtractKinematics import ExtractKinematics

# from .extract_contacts_v2 import ExtractContacts
# #from extract_contacts_mp import ExtractContacts
# from .LoadExperimentData import ExpData

# from .visualisation import Visualisation
# import os

# #dem_folder_path = '/media/deniz/CommonStorage/Datasets/EDEMv2/collision_box/'
# #name = 'exp_4'
# #exp = Experiment(exp_path=dem_folder_path,name=name)

# def extract(dem_folder_path,name, contacts_video=False, animate_deck=False, only_video=False, save_contacts=False):
#     exp = Experiment(exp_path=dem_folder_path,name=name)
#     if only_video:
#             positions = ExpData(exp).positions
#             visualisation = Visualisation(exp, positions)
#             contacts = ExtractContacts(exp)
#             print("Reading contacts")
#             p2p, p2g = contacts.read_contacts()
#             print("Creating contact video")
#             visualisation.contact_video(p2p, p2g, save=True, start_step=1, fps=30)
#     else:
#         DATASET_FOLDER = dem_folder_path
#         SUB_FOLDERS = ["particles", "metadata", "gifs", "contacts", "energy"]
#         SUBSUBFOLDERS = ["positions", "velocities", "forces", "orientations","rot_matrices","torque","angular_velocity", "energy"]

#         for folder in SUB_FOLDERS:
#             os.makedirs(os.path.join(DATASET_FOLDER, folder), exist_ok=True)
#         for subfolder in SUBSUBFOLDERS:
#             os.makedirs(os.path.join(DATASET_FOLDER, "particles", subfolder), exist_ok=True)
#         os.makedirs(os.path.join(DATASET_FOLDER, "contacts", "videos"), exist_ok=True)
#         extractor = EDEMDataExtractor(exp)
#         extractor.saveSystemEnergy()
#         extractor.save_material_properties()
#         extractor.saveParticleProperties()
#         extractor.save_kinematics()
#         if save_contacts:
#             print("Saving contacts")
#             contacts = ExtractContacts(exp)
#             contacts.savecontacts()
#         if contacts_video or animate_deck:
#             positions = ExpData(exp).positions
#             visualisation = Visualisation(exp, positions)
#             if animate_deck:
#                 print("saving animation of the deck")
#                 visualisation.animate_deck(save=True, show=False)
#             if contacts_video:
#                 print("Reading contacts")
#                 p2p, p2g = contacts.read_contacts()
#                 print("Creating contact video")
#                 visualisation.contact_video(p2p, p2g, save=True, start_step=1, fps=30)
#         print(f"Extracting {exp.name} is done")
from concurrent.futures import ProcessPoolExecutor
import os
from .ExperimentBase import Experiment
from .DataExtractor import EDEMDataExtractor
from .extract_contacts_v2 import ExtractContacts
from .LoadExperimentData import ExpData
from .visualisation import Visualisation

def process_dem_file(dem_file_path, contacts_video, animate_deck, save_contacts):
    """
    Helper function to process a single .dem file.
    """
    dem_folder_path, dem_file_name = os.path.split(dem_file_path)
    name, _ = os.path.splitext(dem_file_name)
    extract(dem_folder_path, name, contacts_video=contacts_video, animate_deck=animate_deck, save_contacts=save_contacts)

def extract(dem_folder_path, name=None, contacts_video=False, animate_deck=True, only_video=False, save_contacts=False, all_in_path=False, num_cores=4):
    """
    Modified extract function to handle processing multiple .dem files in parallel if all_in_path is True.
    """
    if all_in_path:
        # Find all .dem files in the folder
        dem_files = [os.path.join(dem_folder_path, file) for file in os.listdir(dem_folder_path) if file.endswith(".dem")]
        if not dem_files:
            print("No .dem files found in the specified folder.")
            return

        print(f"Found {len(dem_files)} .dem files. Processing them in parallel...")
        # Process each .dem file in parallel using ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=num_cores) as executor:
            executor.map(process_dem_file, dem_files, [contacts_video] * len(dem_files), [animate_deck] * len(dem_files), [save_contacts] * len(dem_files))
        print("Processing completed.")
        return

    # Single file processing (default behavior)
    exp = Experiment(exp_path=dem_folder_path, name=name)
    if only_video:
        positions = ExpData(exp).positions
        visualisation = Visualisation(exp, positions)
        contacts = ExtractContacts(exp)
        print("Reading contacts")
        p2p, p2g = contacts.read_contacts()
        print("Creating contact video")
        visualisation.contact_video(p2p, p2g, save=True, start_step=1, fps=30)
    else:
        DATASET_FOLDER = dem_folder_path
        SUB_FOLDERS = ["particles", "metadata", "gifs", "contacts", "energy"]
        SUBSUBFOLDERS = ["positions", "velocities", "forces", "orientations", "rot_matrices", "torque", "angular_velocity", "energy"]

        for folder in SUB_FOLDERS:
            os.makedirs(os.path.join(DATASET_FOLDER, folder), exist_ok=True)
        for subfolder in SUBSUBFOLDERS:
            os.makedirs(os.path.join(DATASET_FOLDER, "particles", subfolder), exist_ok=True)
        os.makedirs(os.path.join(DATASET_FOLDER, "contacts", "videos"), exist_ok=True)
        extractor = EDEMDataExtractor(exp)
        extractor.saveSystemEnergy()
        extractor.save_material_properties()
        extractor.saveParticleProperties()
        extractor.save_kinematics()
        if save_contacts:
            print("Saving contacts")
            contacts = ExtractContacts(exp)
            contacts.savecontacts()
        if contacts_video or animate_deck:
            positions = ExpData(exp).positions
            visualisation = Visualisation(exp, positions)
            if animate_deck:
                print("Saving animation of the deck")
                visualisation.animate_deck(save=True, show=False)
            if contacts_video:
                print("Reading contacts")
                p2p, p2g = contacts.read_contacts()
                print("Creating contact video")
                visualisation.contact_video(p2p, p2g, save=True, start_step=1, fps=30)
        print(f"Extracting {exp.name} is done")
