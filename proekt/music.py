from ctypes import*
bass = cdll.LoadLibrary('E:\pybass-master\lib\x86\libbass.so')

# init bass
bass.BASS_Init(-1, 44100, 0, 0, None)

# load sample
file = 'music.mp3'
sample = bass.BASS_SampleLoad(False, file, c_longlong(0), 0, 2, 0x20000)

# get channel
channel = bass.BASS_SampleGetChannel(sample, False)

# play
bass.BASS_ChannelPlay(channel, True)

# free sample and bass
bass.BASS_SampleFree(sample)
bass.BASS_Free()