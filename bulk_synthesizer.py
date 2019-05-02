# %%
from synthesizer import *
# %%
load_path = "/Users/au550101/Dropbox (Personal)/thesis/multi-speaker-tacotron-tensorflow/logs/_2019-04-12_18-02-51"
num_speakers = 1
synthesizer = Synthesizer()
synthesizer.load(load_path, 1, None)

# %%
parser = argparse.ArgumentParser()
parser.add_argument('--load_path', default=load_path)
parser.add_argument('--sample_path', default="samples")
parser.add_argument('--text', default="This is a test. Let's speak English.")
parser.add_argument('--num_speakers', default=1, type=int)
parser.add_argument('--speaker_id', default=0, type=int)
parser.add_argument('--checkpoint_step', default=None, type=int)
parser.add_argument('--is_korean', default=False, type=str2bool)
config = parser.parse_args()
# %%
text = "This is a test. Let's speak English."
speaker_id = [0]
sample_path = "samples"
# %%
audio = synthesizer.synthesize(
    texts=text,
    base_path=sample_path,
    speaker_ids=speaker_id,
    attention_trim=False,
    isKorean=False)[0]


# %%
