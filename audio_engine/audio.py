import os
import matlab.engine as Engine
import numpy as np
from sklearn.decomposition import PCA

from write_to_csv import feature_csv_writer


def flatten_to_2d(array):
    """Flatten a multi-dimensional array to 2D."""
    return array.reshape((array.shape[0], -1))


def extract_target_features(mfccs):
    mfccs = np.array(mfccs)

    # Extract energy and pitch features
    energy_features = mfccs[:, 0]
    pitch_features = mfccs[:, 2:14]

    # Combine energy and pitch features
    combined_features = np.hstack((energy_features[:, np.newaxis], pitch_features))

    # Flatten if necessary to ensure 2D
    if len(combined_features.shape) != 2:
        combined_features = flatten_to_2d(combined_features)

    return combined_features


def perform_pca(features, n_components=5):
    # Ensure features is 2D
    if len(features.shape) != 2:
        raise ValueError(f"features should be 2D, but has shape {features.shape}")

    pca = PCA(n_components=n_components)
    reduced_features = pca.fit_transform(features)
    return reduced_features, pca


def process_audio_files(audio_dir, n_components=5):
    engine = Engine.start_matlab()

    matlab_functions_dir = "./audio_engine/MATLAB"
    engine.addpath(matlab_functions_dir, nargout=0)

    audio_files = [f for f in os.listdir(audio_dir) if f.endswith(".mp3")]

    for audio_file in audio_files:
        csv_file = "mfcc_features.csv"

        audio_file_path = os.path.join(audio_dir, audio_file)

        # Extract MFCCs using MATLAB function
        mfccs = engine.mfcc_extraction(audio_file_path)
        mfccs = [list(row) for row in mfccs]

        features = extract_target_features(mfccs)

        # Perform PCA on the extracted features
        reduced_features, pca_model = perform_pca(features, n_components)

        # Print the shape of the final PCA-reduced features and a sample
        print(f"File: {audio_file}")
        print(f"Final set of PCA-transformed features shape: {reduced_features.shape}")
        print(f"Sample of PCA-transformed features:\n{reduced_features[:5]}")

        if "T" in audio_file:
            label = 1
        elif "L" in audio_file:
            label = 0

        feature_csv_writer(audio_file, reduced_features, label, csv_file)

    engine.quit()


# Example usage
audio_dir = "D:/Personal/Capstone/Phase 2/MU3D-Package/audio_set"
final_features = process_audio_files(audio_dir, n_components=5)
