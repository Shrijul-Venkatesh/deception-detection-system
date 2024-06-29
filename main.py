import matlab.engine as Engine

engine = Engine.start_matlab()

matlab_functions_dir = r"./Deception_Detection_System/Audio_Engine/MATLAB"
engine.addpath(matlab_functions_dir, nargout=0)

audio_file_path = r"./Dataset/MU3D-Package/audio_set/BF001_1PT.mp3"

mfccs = engine.mfcc_extraction(audio_file_path)
mfccs = [list(row) for row in mfccs]

print(mfccs)


engine.quit()
