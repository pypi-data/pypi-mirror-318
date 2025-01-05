import pandas as pd
import numpy as np
import os
import glob
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import AllChem
from rdkit.ML.Descriptors import MoleculeDescriptors
from padelpy import padeldescriptor
from mordred import Calculator, descriptors
from rdkit.Chem import Lipinski
from molfeat.calc import FPCalculator
from molfeat.trans import MoleculeTransformer
from molfeat.calc import FP_FUNCS
print("""
**cal_rdkit_descriptor**(input_file, output_file, smiles_column):

    Description: This function calculates RDKit molecular descriptors for molecules specified in a CSV file (input_file) using 
    SMILES strings from a specified column (smiles_column). The calculated descriptors are appended as additional columns to the 
    original data and saved in a new CSV file named <input_file_name>_rdkit_descriptor.csv.




**cal_lipinski_descriptors**(file_path, smiles_column, verbose=False):

    Description: This function calculates Lipinski descriptors for molecules specified in a CSV file (file_path) using 
    SMILES strings from a specified column (smiles_column). It automatically saves the calculated descriptors to an output 
    file named <input_file_name>_lipinski_descriptors.csv.


**cal_morgan_fpts**(input_file, output_file, smiles_column):

    Description: Calculates Morgan fingerprints for molecules specified in a CSV file (input_file) using SMILES strings 
    from a specified column (smiles_column). The function saves the calculated fingerprints to an output file named 
    <input_file_name>_calculate_morgan_fpts.csv.


**cal_mordred_descriptors**(input_file, output_file, smiles_column):

    Description: Computes Mordred descriptors for molecules specified in a CSV file (input_file) using SMILES strings 
    from a specified column (smiles_column). The function saves the computed descriptors to an output file named 
    <input_file_name>_mordred_descriptors.csv.


**calculate_selected_fingerprints**(input_file, smiles_column)
    Description: Before using this function, execute the following code snippet to download and unzip necessary files:
    ```
    ! wget https://github.com/dataprofessor/padel/raw/main/fingerprints_xml.zip
    ! unzip fingerprints_xml.zip

    Description: This function allows selection and calculation of specific molecular fingerprints ['AtomPairs2DCount', 
    'AtomPairs2D', 'EState', 'CDKextended', 'CDK', 'CDKgraphonly','KlekotaRothCount', 'KlekotaRoth', 'MACCS', 'PubChem',
    'SubstructureCount', 'Substructure'] from a provided list for molecules in a CSV file (input_file) containing molecular 
    structures in SMILES format. Each selected fingerprint type is computed and saved as a separate CSV file alongside the 
    original input file.

**fps(filenmae, smiles_column,fp_type )
      
      Description: This function calculates a specified molecular fingerprint (fp_type) for each molecule in a CSV file.
      User must provide his CSV file, smiles column name in his CSV file, and choose one ofthese fingeprints
      ['maccs', 'avalon', 'pattern', 'layered', 'map4', 'secfp', 'erg', 'estate', 'avalon-count', 'ecfp', 'fcfp', 'topological', 
      'atompair', 'rdkit', 'ecfp-count', 'fcfp-count', 'topological-count', 'atompair-count', 'rdkit-count']

""")

"""# Calculate Rdkit Descriptors"""



def cal_rdkit_descriptor(input_file, smiles_column):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)

        # Add a new column 'mol' to store the RDKit molecule objects
        df['mol'] = df[smiles_column].apply(Chem.MolFromSmiles)


        # Calculate RDKit descriptors for each molecule
        calc = MoleculeDescriptors.MolecularDescriptorCalculator([x[0] for x in Descriptors._descList])
        desc_names = calc.GetDescriptorNames()

        # Calculate descriptors and add them to the DataFrame
        Mol_descriptors = [calc.CalcDescriptors(Chem.AddHs(mol)) for mol in df['mol']]
        df_with_descriptors = pd.concat([df.reset_index(drop=True), pd.DataFrame(Mol_descriptors, columns=desc_names)], axis=1)

        # Generate output CSV file name
        file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = file_name + "_rdkit_descriptor.csv"

        # Save the DataFrame with descriptors to a new CSV file
        df_with_descriptors.to_csv(output_file, index=False)

        print("Data with RDKit descriptors saved successfully in", output_file)

        # Display the DataFrame with calculated descriptors (optional)
        display(df_with_descriptors)

        return df_with_descriptors
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
#cal_rdkit_descriptor("output_1000.csv", "IsomericSMILES")

"""# Calculate Fingerprint"""


def calculate_fingerprint(df_unique, smiles_column, fingerprint_type):
    xml_files = glob.glob("*.xml")
    xml_files.sort()

    FP_list = ['AtomPairs2DCount', 'AtomPairs2D', 'EState', 'CDKextended', 'CDK', 'CDKgraphonly',
               'KlekotaRothCount', 'KlekotaRoth', 'MACCS', 'PubChem', 'SubstructureCount', 'Substructure']

    fp = dict(zip(FP_list, xml_files))

    if fingerprint_type not in fp:
        raise ValueError(f"Fingerprint type '{fingerprint_type}' not found in FP_list.")

    fingerprint_output_file = f'{fingerprint_type}.csv'
    fingerprint_descriptortypes = fp[fingerprint_type]

    df2 = pd.DataFrame(df_unique[smiles_column])  # Ensure DataFrame structure
    df2.to_csv('molecule.smi', sep='\t', index=False, header=False)

    padeldescriptor(mol_dir='molecule.smi', d_file=fingerprint_output_file,
                    descriptortypes=fingerprint_descriptortypes, detectaromaticity=True,
                    standardizenitro=True, standardizetautomers=True, threads=2, removesalt=True,
                    log=True, fingerprints=True)

    descriptors = pd.read_csv(fingerprint_output_file)


    return descriptors
def calculate_selected_fingerprints(input_file, smiles_column):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(input_file)

    # Define the 12 fingerprint types to choose from
    fingerprint_types = ['AtomPairs2DCount', 'AtomPairs2D', 'EState', 'CDKextended', 'CDK', 'CDKgraphonly',
                         'KlekotaRothCount', 'KlekotaRoth', 'MACCS', 'PubChem', 'SubstructureCount', 'Substructure']

    # Print available options for the user
    print("Available fingerprint types:")
    for i, fp_type in enumerate(fingerprint_types, start=1):
        print(f"{i}. {fp_type}")

    # Ask user for input
    user_input = input("Enter comma-separated indices of the fingerprints you want to calculate (e.g., 1,2,5): ")
    selected_indices = [int(idx.strip()) - 1 for idx in user_input.split(',')]

    selected_fps = [fingerprint_types[idx] for idx in selected_indices]

    for fingerprint_type in selected_fps:
        # Calculate fingerprints for each selected type
        descriptors = calculate_fingerprint(df, smiles_column, fingerprint_type)

        # Merge descriptors with original DataFrame
        df_with_fps = pd.concat([df.reset_index(drop=True),descriptors.reset_index(drop=True)], axis=1)

        # Construct output file name based on input file name and fingerprint type
        output_file_name = f'{input_file.split(".csv")[0]}_with_{fingerprint_type}.csv'

        # Save DataFrame with merged descriptors to a CSV file
        df_with_fps.to_csv(output_file_name, index=False)
        display(df_with_fps.head(2))
        print(f"Saved {fingerprint_type} descriptors added to '{input_file}' to '{output_file_name}'")

    print("All selected fingerprints added to original file and saved.")

# Example usage:
#calculate_selected_fingerprints("output_1000.csv", "IsomericSMILES")

"""# Calculate Lipinski Descriptors"""


def cal_lipinski_descriptors(file_path, smiles_column, verbose=False):
    """
    Calculate Lipinski descriptors for a SMILES column in a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.
    - smiles_column (str): Name of the SMILES column in the CSV file.
    - verbose (bool, optional): If True, print additional information. Default is False.

    Returns:
    - pd.DataFrame: DataFrame containing Lipinski descriptors for each molecule.
    """

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)

        # Extract SMILES column
        smiles_column = smiles_column

        # Initialize list to store RDKit molecule objects
        mol_data = []

        # Convert SMILES strings to RDKit molecule objects
        for smiles in df[smiles_column]:
            mol = Chem.MolFromSmiles(smiles)
            mol_data.append(mol)

        # Initialize an empty array to store descriptor values
        base_data = np.empty((len(mol_data), 4))

        # Calculate descriptors for each molecule
        for i, mol in enumerate(mol_data):
            base_data[i, 0] = Descriptors.MolWt(mol)
            base_data[i, 1] = Descriptors.MolLogP(mol)
            base_data[i, 2] = Lipinski.NumHDonors(mol)
            base_data[i, 3] = Lipinski.NumHAcceptors(mol)

        # Create DataFrame with Lipinski descriptors
        column_names = ["MW", "LogP", "NumHDonors", "NumHAcceptors"]
        descriptors = pd.DataFrame(data=base_data, columns=column_names)

        # Concatenate descriptors DataFrame with original DataFrame
        df_with_descriptors = pd.concat([df, descriptors], axis=1)

        # Generate output CSV file name
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        output_file = file_name + "_lipinski_descriptors.csv"

        # Save the concatenated DataFrame to a CSV file
        df_with_descriptors.to_csv(output_file, index=False)

        print(f"Data with Lipinski descriptors saved successfully in {output_file}")
        display(df_with_descriptors.head(2))

        # Display the concatenated DataFrame if verbose mode is enabled
        if verbose:
            display(df_with_descriptors.head(2))

        return f"Data with Lipinski descriptors saved successfully in {output_file}"

    except Exception as e:
        print("An error occurred:", e)
    return

# Example usage:
#cal_lipinski_descriptors("output_1000.csv", "IsomericSMILES")  # Calculate Lipinski descriptors and save to CSV automatically

"""# Calculate Morgan Fingerprint"""


def calculate_morgan_fpts(data,radius, bit_string):
    Morgan_fpts = []
    bit_string=int(bit_string)
    radius=int(radius)
    for i in data:
        mol = Chem.MolFromSmiles(i)
        fpts = AllChem.GetMorganFingerprintAsBitVect(mol, radius, bit_string)
        mfpts = np.array(fpts)
        Morgan_fpts.append(mfpts)
    return np.array(Morgan_fpts)

def cal_morgan_fpts(input_file, smiles_column, radius=2,bit_string=2048):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)

        # Add a new column 'mol' to store the RDKit molecule objects
        df['mol'] = df[smiles_column].apply(Chem.MolFromSmiles)

        # Remove duplicates based on the specified SMILES column
        df.drop_duplicates(subset=smiles_column, inplace=True)

        # Calculate Morgan fingerprints for each molecule
        morgan_fpts = calculate_morgan_fpts(df[smiles_column], radius,bit_string)

        # Add the Morgan fingerprints to the DataFrame
        morgan_fpt_names = [f'MorganFpt_{i}' for i in range(morgan_fpts.shape[1])]
        df_with_morgan_fpts = pd.concat([df.reset_index(drop=True), pd.DataFrame(morgan_fpts, columns=morgan_fpt_names)], axis=1)

        # Generate output CSV file name
        file_name = os.path.splitext(os.path.basename(input_file))[0] + "_raduis_is "+ str(radius)+"bit_string is "+str(bit_string)+ "_morgan_fpts.csv"

        # Save the cleaned data with Morgan fingerprints to a new CSV file
        df_with_morgan_fpts.to_csv(file_name, index=False)

        print(f"Data with Morgan fingerprints saved successfully in {file_name}")

        # Display the DataFrame with Morgan fingerprints (optional)
        display(df_with_morgan_fpts.head(2))

        return f"Data with Morgan fingerprints saved successfully in {file_name}"

    except Exception as e:
        print("An error occurred:", e)
    return

# Example usage:
#cal_morgan_fpts("output_1000.csv", "IsomericSMILES",radius= 3, bit_string=2048)  # Calculate Morgan fingerprints and save to CSV automatically

"""# Calculate Mordred Descriptors"""



def calculate_mordred_descriptors(smiles_column):
    calc = Calculator(descriptors, ignore_3D=False)

    # Get Mordred descriptors
    mols = [Chem.MolFromSmiles(smi) for smi in smiles_column]
    mordred_descriptors = calc.pandas(mols)

    return mordred_descriptors

def cal_mordred_descriptors(input_file, smiles_column):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)

        # Remove duplicates based on the specified SMILES column
        df.drop_duplicates(subset=smiles_column, inplace=True)

        # Calculate Mordred descriptors for each molecule
        mordred_descriptors = calculate_mordred_descriptors(df[smiles_column])

        # Add the Mordred descriptors to the DataFrame
        df_with_mordred_descriptors = pd.concat([df.reset_index(drop=True), mordred_descriptors.reset_index(drop=True)], axis=1)

        # Generate output CSV file name
        file_name = input_file.split('.')[0]  # Assuming input_file has an extension like '.csv'
        output_file = file_name + "_mordred_descriptors.csv"

        # Save the cleaned data with Mordred descriptors to a new CSV file
        df_with_mordred_descriptors.to_csv(output_file, index=False)

        print(f"Data with Mordred descriptors saved successfully in {output_file}")

        # Display the DataFrame with Mordred descriptors (optional)
        display(df_with_mordred_descriptors.head(2))

        return (f"Data with Mordred descriptors saved successfully in {output_file}")

    except Exception as e:
        print("An error occurred:", e)
    return
# Example usage:
#cal_mordred_descriptors("output_1000.csv", "IsomericSMILES")  # Calculate Mordred descriptors and save to CSV automatically


####

def fps(filename, smiles_column, fp_type):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Convert the fingerprint type to a string (not strictly necessary if it's already a string)
    fp_type = str(fp_type)

    # Create a fingerprint calculator and transformer
    calc = FPCalculator(fp_type)
    trans = MoleculeTransformer(calc)

    # Use the correct column from the DataFrame based on the passed column name
    fp_array = trans.transform(df[smiles_column].values)  # Access the column by name

    # Stack the fingerprints array into a 2D array
    arr = np.stack(fp_array)

    # Create a DataFrame from the array of fingerprints
    df2 = pd.DataFrame(arr)

    # Add the fingerprint type as a prefix to the columns in the new DataFrame
    df2 = df2.add_prefix(fp_type)

    # Concatenate the original DataFrame with the new fingerprint columns
    df = pd.concat([df, df2], axis=1)

    # Save the DataFrame with the added fingerprints as a new CSV file
    output_filename = f"{filename}_{fp_type}.csv"
    df.to_csv(output_filename, index=False)  # index=False to avoid saving row indices

    # Message to indicate success
    message = ("Your fingerprint was added and saved in CSV file", output_filename)
    print(message)

    # Optionally display the first few rows of the resulting DataFrame
    display(df.head(4))

    return message

# Example usage
#fps("output_1000.csv", "IsomericSMILES", "pattern")
