import os
import requests
import pandas as pd
from tqdm import tqdm
import pyfiglet  # For attractive text

class ImageDownloader:
    def __init__(self, input_file_path, output_folder, prefix):
        """
        Initializes the ImageDownloader with the input file path, output folder, and user-defined prefix.

        :param input_file_path: Path to the input file containing URLs.
        :param output_folder: Path to the output folder where images will be saved.
        :param prefix: Prefix for the downloaded image files.
        """
        self.input_file_path = input_file_path
        self.output_folder = output_folder
        self.prefix = prefix  # Set the user-defined prefix
        self.urls = self._load_urls()

    def _load_urls(self):
        """
        Loads the URLs from an Excel or text file based on the file extension.

        :return: A list of URLs.
        """
        if self.input_file_path.endswith('.xlsx'):
            # Read URLs from the first column of an Excel file
            df = pd.read_excel(self.input_file_path)
            return df.iloc[:, 0].dropna().tolist()  # Drop NaN values and convert to list
        else:
            # Read URLs from a text file
            try:
                with open(self.input_file_path, 'r') as file:
                    return [line.strip() for line in file if line.strip()]  # Remove empty lines
            except FileNotFoundError:
                print(f"Error: The file {self.input_file_path} was not found.")
                return []

    def _create_output_folder(self):
        """
        Creates the output folder if it does not exist.
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder, exist_ok=True)
            print(f"Output folder '{self.output_folder}' created.")
        else:
            print(f"Output folder '{self.output_folder}' already exists.")

    def download_images(self):
        """
        Downloads images from the URLs and saves them in the output folder.
        """
        # Ensure the output folder exists
        self._create_output_folder()

        print("Downloading images, please wait...")

        # Download images with progress bar
        for i, url in enumerate(tqdm(self.urls, desc="Downloading images"), start=1):
            if url:  # Skip empty URLs
                try:
                    # Send a GET request to the URL
                    response = requests.get(url)
                    response.raise_for_status()  # Raise error for bad responses

                    # Get the file extension
                    _, extension = os.path.splitext(url)
                    extension = extension.lower()

                    # Save the image to the output folder with the user-defined prefix
                    image_path = os.path.join(self.output_folder, f'{self.prefix}_{i}{extension}')
                    with open(image_path, 'wb') as image_file:
                        image_file.write(response.content)

                except requests.exceptions.RequestException as e:
                    print(f"Error downloading image {i}: {e}")

        # After downloading all images, print completion message
        self._print_completion_message()

    def _print_completion_message(self):
        """
        Prints a completion message with a decorative ASCII art.
        """
        completion_message = pyfiglet.figlet_format("Download Complete!")
        print(completion_message)
        print(f"Images saved in directory: {self.output_folder}")

if __name__ == "__main__":
    # Provide the path to the input file (Excel or text) and the output folder
    input_file_path = r"BodyWashData.txt"  # Update with your file path
    output_folder = r"Output_Folder"  # Update with your desired output folder

    # Ask user for the prefix
    prefix = input("Enter the prefix for the image files: ")

    # Initialize the ImageDownloader and start the download process
    downloader = ImageDownloader(input_file_path, output_folder, prefix)
    downloader.download_images()
