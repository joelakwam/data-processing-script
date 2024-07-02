from utils import Utils

while True:
    print('-' * 100)
    print('Create a structured CSV file from a series of TXT files in a folder.')
    print('-' * 100)
    
    path_to_folder = input('\n> What is the path to the folder?\n Eg, "/Users/mac/Documents/Datasets/large-movie-review-dataset/train/pos"\n')
    sentiment = input('\n> What type of sentiment is in the files?\n Eg, "POSITIVE" or "NEGATIVE" \n')
    file_name = input('\n> Provide a name for the CSV file. Remember to add the .csv extension at the end of the file name. \nEg, "people.csv"\n')
    path_to_save_file = input('\n> Where do you want to save the file. Provide a full path to the location, please.\n Eg, "/Users/mac/Documents/" \n')
    
    Utils.create_structured_dataset(path_to_folder, sentiment, file_name, path_to_save_file)
    break
    
