from vad import VoiceActivityDetector


def includes_speech(file):
    v = VoiceActivityDetector(file)
    raw_detection = v.detect_speech()
    return v.includes_speech(raw_detection, thresh=3)


if __name__ == "__main__":
    filenames = ['wav-sample.wav']
    classification = includes_speech(filenames[0])
    print(classification)
