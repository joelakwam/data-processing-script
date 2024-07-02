import os
import glob
import csv


class Utils:
    
    @staticmethod
    def create_structured_dataset(
        path_to_folder, sentiment, file_name, path_to_save_file
    ):
        """
        - This method loops through TXT files in the provided folder, extracts the text and label if NEGATIVE or POSITIVE and saves it in a new CSV file.
        """

        reviews = []

        for file_path in glob.glob(os.path.join(path_to_folder, "*.txt")):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                review = [content, sentiment]
                reviews.append(review)

        csv_path = os.path.join(path_to_save_file, file_name)

        with open(csv_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(reviews)
            print(f"CSV file {file_name} has been created successfully!!!...")
