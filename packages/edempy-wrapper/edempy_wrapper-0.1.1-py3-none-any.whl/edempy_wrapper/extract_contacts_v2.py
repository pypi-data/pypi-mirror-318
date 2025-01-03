import pandas as pd
import numpy as np
from tqdm import tqdm
from .ExperimentBase import Experiment
from .DataExtractor import EDEMDataExtractor


class ExtractContacts(EDEMDataExtractor):
    def __init__(self, experiment: Experiment):
        super().__init__(experiment)

    def getContacts(self):
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

        # pd.DataFrame(surfSurf_data).to_csv(self.p2pcontact_path, index=False)
        # pd.DataFrame(surfGeom_data).to_csv(self.p2gcontact_path, index=False)

        pd.DataFrame(surfSurf_data).to_feather(self.p2pcontact_path)
        pd.DataFrame(surfGeom_data).to_feather(self.p2gcontact_path)


        print(f"Saved surfSurf contacts to {self.p2pcontact_path}")
        print(f"Saved surfGeom contacts to {self.p2gcontact_path}")

        return surfSurf_data, surfGeom_data

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

    def savecontacts(self):
        surfSurf_data, surfGeom_data = self.getContacts()
        return surfSurf_data, surfGeom_data

    def read_contacts(self):
        def eval_list_str(column):
            return column.apply(
                lambda x: eval(x) if isinstance(x, str) and x.startswith('[') and x.endswith(']') else x)

        surfSurf_df = pd.read_feather(self.p2pcontact_path, dtype_backend='pyarrow')
        surfGeom_df = pd.read_feather(self.p2gcontact_path, dtype_backend='pyarrow')

        # Convert string representations of lists back to lists
        for column in surfSurf_df.columns:
            surfSurf_df[column] = eval_list_str(surfSurf_df[column])

        for column in surfGeom_df.columns:
            surfGeom_df[column] = eval_list_str(surfGeom_df[column])

        return surfSurf_df, surfGeom_df

# Example usage
# experiment = Experiment(...)  # Initialize your Experiment object
# extractor = ExtractContacts(experiment)
# extractor.savecontacts()
# surfSurf_df, surfGeom_df = extractor.read_contacts()
