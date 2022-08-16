# Focus-TTS

This repository contains the questionnaire and the stimuli that were used in a listening test to investigate the effect of focus-sensitive prosody on the naturalness of synthetic speech.

## Background
The listening test was part of a study that was conducted for the Thesis project "Improving the naturalness of an end-to-end speech synthesis system with information structure". The study examines whether the naturalness of a synthetic voice that produces sequences of sentences is improved when the prosody of its sentences is modified so that it better matches the current context. For this purpose, we replicated an approach proposed by Latif et al. (2021) that uses control tags for prosody modification in end-to-end TTS systems. We used this approach to synthesize isolated sentences and paragraphs in English where prosody accords with the contextually induced focus types. We also trained a second TTS system that does not allow prosody control. In a subsequently conducted mean opinion score (MOS) study, isolated sentences and paragraphs achieve higher naturalness ratings when synthesized with the system that marks foci prosodically. This suggests that a more context-appropriate prosody can improve the naturalness of synthetic voices, not only when producing sequences of sentences but also when producing sentences in isolation. In addition, across the two systems, paragraphs receive lower ratings than isolated sentences. This strengthens the idea that the naturalness of a TTS system that has been evaluated on isolated sentences may decrease when the same system is used for the synthesis of larger texts or conversations This should be taken into account when designing and interpreting the evaluation of a TTS system.


## Producing the stimuli

The NVIDIA FastPitch implementation was used to train both models: https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/SpeechSynthesis/FastPitch

A Singularity container was used for data pre-processing, training, and inference.

### Data
The 'prosody-control' dataset created by Latif et al. (2021) was used to train both models. The dataset was made publicly available by the authors. It can be downloaded via https://download.europe.naverlabs.com/prosody-control/.

### Dataset preparation

The following steps were taken to prepare the dataset for training the **test model**:

- A metadata file was created that contains the name of all audio files together with their transcriptions. To create this file: 

  - All superfluous annotations (everything besides audio number and sentence type) and punctuation marks were removed
  - Control tags were added: '!' and a space before corrective foci, '?' and a space before questions
  - All letters were converted to lowercase
  - All transcriptions were duplicated

The script create_metadata.py was used for these modifications.

- The WAV files were modified:
  - They were re-sampled to a frequency of 22050 Hz using convert_wavs_to_22050.py
  - They were converted to 16-bit WAV format using convert_wavs_to_16bits.sh
  - Silence before and after speech was removed with a threshold of 30dB using trim_silence.py

The same prepared data was used to train the **baseline model**. However, before training the baseline model, the control tags were removed from the transcriptions. 

### Pre-processing

The scripts prepare_dataset.py and prepare_dataset.sh from the NVIDIA FastPitch implementation were used to pre-process the data.

### Training

The scripts train.py and train.sh from the NVIDIA FastPitch implementation were used for training. The parameters were set in the train.sh file. The following parameters were used:

- number of GPUS = 1 
- batch size = 16
- grad accumulation = 16
- learning rate = 0.1
- AMP = false

Both models were trained for 400 epochs. You can download the resulting checkpoints here: 
- [baseline model (trained without tags)](https://drive.google.com/file/d/1yoTGj-3w1uT3RLGc1by9BoZOICqZl5HP/view?usp=sharing)
- [test model (trained with tags)](https://drive.google.com/file/d/1q90EQTHfJ8r6wrrWbgfRkodTU5WIaJoZ/view?usp=sharing)

### Synthesis
A pre-trained WaveGlow model (Prenger et al. 2019) was used as a vocoder. It was downloaded using the download_dataset.sh script of the NVIDIVA FastPitch implementation. It can also be downloaded [here](https://drive.google.com/file/d/1KjwqmUql_OydpimlWI6sBO9akuJ18-bV/view?usp=sharing). The scripts inference.py and inference_example.sh from the NVIDIA FastPitch implementation were used for inference. The file stimuli_no_tags.tsv was used for synthesis with the baseline model. The file stimuli_tags.tsv was used for synthesis with the test model. 

Paragraphs were synthesized in two steps: First, the two sentences of the paragraph were synthesized individually. Second, the two sentences were concatenated with a pause of 100 ms between them. The test model paragraphs were synthesized with tags that mark the narrow foci on the subject or the verb of the second sentence with the objective of inducing a narrow-focus intonation.

The "Stimuli" directory contains the 24 stimuli that were synthesized for the listening test. The subdirectory called "no_tags_model" contains the 12 stimuli that were synthesized with the baseline model. Six isolated sentences and 6 paragraphs were synthesized with this model (see sub-subdirectories). The subdirectory called "tags_model" contains the 12 stimuli that were synthesized with the test model. With this model, as well, 6 isolated sentences and 6 paragraphs were synthesized (see sub-subdirectories). 

## Listening test
### Questionnaire
The file "Questionnaire.pdf" contains the questionnaire that was used for the listening test. It consists of an introduction, followed by the collection of demographic data, instructions for the listening test, and the listening test (stimuli rating). The stimuli were presented to participants in random order. They were asked to rate each stimulus on a 9-point scale from bad to excellent.

## Bibliography
Latif, Siddique and Kim, Inyoung and Calapodescu, Ioan and Besacier, Laurent (2021) Controlling Prosody in End-to-End TTS: A Case Study on Contrastive Focus Generation. In: 25th Conference on Computational Natural Language Learning (CoNLL 2021), 10 Nov - 11 Nov 2021, Punta Cana, Dominican Republic. 

Prenger, Ryan, Rafael Valle, and Bryan Catanzaro (2019) Waveglow: A flow-based generative network for speech synthesis. In ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pages 3617–3621. IEEE.
