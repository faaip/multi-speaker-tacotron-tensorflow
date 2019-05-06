# %%
from tqdm import tnrange, tqdm_notebook
import glob
from synthesizer import *
import os
# %%
load_path = "/Users/au550101/Dropbox (Personal)/thesis/multi-speaker-tacotron-tensorflow/logs/_2019-05-02_15-01-25/"
num_speakers = 1
synthesizer = Synthesizer()
synthesizer.load(load_path, 1, None)


# %%
text = ["This is a test. Let's speak English."]  # must be in list
text = "/Users/au550101/uni/master_thesis/tts/multi-speaker-tacotron-tensorflow/txt.done.data.txt"
speaker_id = [0]
sample_path = "/Users/au550101/Dropbox (Personal)/thesis/multi-speaker-tacotron-tensorflow/samples/"
step_no = sorted(glob(os.path.join(load_path, "model*")))
sample_path = '{:}{:}/{:}/'.format(sample_path, load_path.split(
    '/')[-2], get_most_recent_checkpoint(load_path).split('-')[-1])
print(sample_path)
# %%
# make samples path
if not os.path.exists(sample_path):
    os.makedirs(sample_path)

# check if text is a file
if os.path.isfile(text):
    text = [line.rstrip('\n') for line in open(text)]

# %%
for t in tqdm(text):
    audio = synthesizer.synthesize(
        texts=t,
        base_path=sample_path,
        speaker_ids=speaker_id,
        attention_trim=False,
        isKorean=False)[0]

# %%
