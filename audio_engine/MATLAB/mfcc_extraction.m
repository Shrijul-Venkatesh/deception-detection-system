function mfccs = mfcc_extraction(audioFilePath)

if exist(audioFilePath, 'file')
    [y, fs] = audioread(audioFilePath);
    mfccs = mfcc(y, fs);
    
else
    disp(['File not found: ', audioFilePath]);
    mfccs = []; % Return an empty array if the file doesn't exist
end

end
