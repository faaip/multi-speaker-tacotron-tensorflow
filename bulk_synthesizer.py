# %%
from synthesizer import *
# %%
load_path = "/Users/au550101/Dropbox (Personal)/thesis/multi-speaker-tacotron-tensorflow/logs/_2019-04-12_18-02-51"
num_speakers = 1
synthesizer = Synthesizer()
synthesizer.load(load_path, 1, None)

# %%
