function mfccs = mfcc_extraction(audioFilePath)
[y, fs] = audioread(audioFilePath);
mfccs = mfcc(y, fs);
end
