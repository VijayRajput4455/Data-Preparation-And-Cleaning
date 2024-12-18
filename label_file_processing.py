import os

class LabelFileProcessor:
    """
    A class to process label files in a specified folder. Supports modifying values in files based on a mapping 
    and filtering lines based on indices.
    """

    def __init__(self, folder_path):
        """
        Initialize the LabelFileProcessor with a folder path.

        :param folder_path: Path to the folder containing label files.
        """
        self.folder_path = folder_path

    def _process_file_with_value_mapping(self, file_path, value_mapping):
        """
        Modify specified values in each line of a file based on a mapping.

        :param file_path: Path to the label file.
        :param value_mapping: Dictionary mapping old values to new values.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Modify specified values in each line
        for i in range(len(lines)):
            values = lines[i].split(" ")  # Split line into individual values

            # Check if the first value is in the mapping dictionary
            if values[0] in value_mapping:
                new_value = value_mapping[values[0]]  # Get the new value from the mapping
                values[0] = new_value  # Update the value

            lines[i] = ' '.join(values)  # Reconstruct the line

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            file.writelines(lines)

    def _process_file_with_index(self, file_path, indices_to_keep):
        """
        Filter lines in a file based on the specified indices.

        :param file_path: Path to the label file.
        :param indices_to_keep: List of indices to retain.
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter lines based on the specified indices
        lines_to_keep = [line for line in lines if line.startswith(tuple(f"{index} " for index in indices_to_keep))]

        # Check if there are any lines to keep
        if lines_to_keep:
            with open(file_path, 'w') as file:
                file.writelines(lines_to_keep)  # Write retained lines back to the file
        else:
            os.remove(file_path)  # Delete the file if no lines are retained

    def update_label_folder_with_value_mapping(self, value_mapping):
        """
        Update label files in the folder by modifying specified values based on a mapping.

        :param value_mapping: Dictionary mapping old values to new values.
        """
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.folder_path, file_name)
                self._process_file_with_value_mapping(file_path, value_mapping)

    def update_label_folder_with_index(self, indices_to_keep):
        """
        Update label files in the folder by retaining only lines that match the specified indices.

        :param indices_to_keep: List of indices to retain.
        """
        for file_name in os.listdir(self.folder_path):
            if file_name.endswith(".txt"):
                file_path = os.path.join(self.folder_path, file_name)
                self._process_file_with_index(file_path, indices_to_keep)

# Example usage
if __name__ == "__main__":
    # Replace with the actual path to your label folder
    folder_path = r"folder_path"

    # Create an instance of the LabelFileProcessor
    processor = LabelFileProcessor(folder_path)

    # Define value mapping and indices to keep
    value_mapping = {'0': '1', '1': '2', '2': '3', '3': '4'}
    indices_to_keep = [0, 1, 2, 3]

    # Uncomment the desired method call based on your requirements
    processor.update_label_folder_with_value_mapping(value_mapping)
    processor.update_label_folder_with_index(indices_to_keep)
