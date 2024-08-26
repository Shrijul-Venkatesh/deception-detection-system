import csv
import os


def feature_csv_writer(audio_file, reduced_features, label, csv_file):
    num_samples = reduced_features.shape[0]

    # Only use the first row of the reduced_features
    first_row = reduced_features[0, :]

    csv_data = []

    # Create a row for the first row of reduced_features
    row = [
        audio_file,
        first_row[0],
        first_row[1],
        first_row[2],
        first_row[3],
        first_row[4],
        label,
    ]
    csv_data.append(row)

    file_exists = os.path.isfile(csv_file)
    mode = "a" if file_exists else "w"

    with open(csv_file, mode=mode, newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            headers = [
                "file",
                "mfcc_1",
                "mfcc_2",
                "mfcc_3",
                "mfcc_4",
                "mfcc_5",
                "label",
            ]
            writer.writerow(headers)
        writer.writerows(csv_data)
