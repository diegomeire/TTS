
This is a fork of https://github.com/coqui-ai/TTS
<<<<<<< HEAD

______________________________________________________________________

## <img src="https://raw.githubusercontent.com/coqui-ai/TTS/main/images/coqui-log-green-TTS.png" height="56"/>
______________________________________________________________________

## <img src="Screenshot_01.jpg" height="56"/>


This adds an improved server.py, where you can refer to a local wav file for voice cloning either running XTTS or Vits:





______________________________________________________________________
Please refer to the original repository for more information


## 🐸Coqui.ai News
- 📣 ⓍTTSv2 is here with 16 languages and better performance across the board.
- 📣 ⓍTTS fine-tuning code is out. Check the [example recipes](https://github.com/coqui-ai/TTS/tree/dev/recipes/ljspeech).
- 📣 ⓍTTS can now stream with <200ms latency.
- 📣 ⓍTTS, our production TTS model that can speak 13 languages, is released [Blog Post](https://coqui.ai/blog/tts/open_xtts), [Demo](https://huggingface.co/spaces/coqui/xtts), [Docs](https://tts.readthedocs.io/en/dev/models/xtts.html)
- 📣 [🐶Bark](https://github.com/suno-ai/bark) is now available for inference with unconstrained voice cloning. [Docs](https://tts.readthedocs.io/en/dev/models/bark.html)
- 📣 You can use [~1100 Fairseq models](https://github.com/facebookresearch/fairseq/tree/main/examples/mms) with 🐸TTS.
- 📣 🐸TTS now supports 🐢Tortoise with faster inference. [Docs](https://tts.readthedocs.io/en/dev/models/tortoise.html)
=======
>>>>>>> eb2b8bf47b0d83f3df1737a63c3d16a62c325f1a

______________________________________________________________________

<div align="center">
<img src="Screenshot_01.jpg" height="480"/>
</div>

______________________________________________________________________

## Description
This adds an improved server.py, where you can refer to a local wav file for voice cloning either running XTTS or Vits.


## Installation

To run this, you must clone from this repo and install TTS from here as it changes some of the code related to the server

```bash
git clone https://github.com/diegomeire/TTS
pip install -e .  # Select the relevant extras
```


## Running


### XTTS server 
#### using CPU
```
cd /TTS/server
python server.py --model_name="tts_models/multilingual/multi-dataset/xtts_v2" --show_details=True  --use_cuda=False
```
#### using GPU
```
cd /TTS/server
python server.py --model_name="tts_models/multilingual/multi-dataset/xtts_v2" --show_details=True  --use_cuda=True
```

### VITS server 
#### using CPU
```
cd /TTS/server
python server.py --model_name="tts_models/en/vctk/vits" --show_details=True --use_cuda=False
```
#### using GPU
```
cd /TTS/server
python server.py --model_name="tts_models/en/vctk/vits" --show_details=True --use_cuda=True
```

### Adding a custom model
Edit the hidden file `.models.json`  and add your entry like:

```
        "mark": {
                    "description": "VITS End2End TTS model trained on VCTK dataset with 109 different speakers with EN accent.",
                    "github_rls_url": [
                    	"https://github.com/diegomeire/PebbleAndFriends/blob/main/TTS_Models/tts_models--en--vctk--mark/config.json",
                    	"https://github.com/diegomeire/PebbleAndFriends/blob/main/TTS_Models/tts_models--en--vctk--mark/speaker_ids.json"	
                    	"https://github.com/diegomeire/PebbleAndFriends/blob/main/TTS_Models/tts_models--en--vctk--mark/model_file.pth",
                    ],
                    "default_vocoder": null,
                    "commit": "3900448",
                    "author": "Diego Meire",
                    "license": "apache 2.0",
                    "contact": "egolge@coqui.ai"
          },
```
In this case, I'm adding this entry to `tts_models/en/vctk`. This will make the server download these files when the call is made:
`python server.py --model_name="tts_models/en/vctk/mark" --show_details=True --use_cuda=True` 

If the download fails, you can find the location where the models are downloaded to and copy the files manually there. The folder, in this case, is  created with the name `tts_models--en-vctk--mark`. When you find the folder, you can copy the files listed on the json file entry there. 
On the Mac, the folder is `/Users/{username}/Library/Application\ Support/tts/{folder}`
On Windows, the folder is `c:\Users\{user}\AppData\Local\tts`





______________________________________________________________________
Please refer to the original repository for more information
