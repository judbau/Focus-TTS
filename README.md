# Focus-TTS

This repository contains the questionnaire and the stimuli that were used in a listening test to investigate the effect of focus-sensitive prosody in synthetic speech.

## Background
The listening test was part of a study that was conducted for the Thesis project "Improving the naturalness of an end-to-end speech synthesis system with information structure". The study examines whether the naturalness of a synthetic voice that produces sequences of sentences is improved when the prosody of its sentences is modified so that it better matches the current context. For this purpose, we replicated an approach proposed by Latif et al. (2021) that uses control tags for prosody modification in end-to-end TTS systems. We used this approach to synthesize isolated sentences and paragraphs in English where prosody accords with the contextually induced focus types. We also trained a second TTS system that does not allow prosody control. In a subsequently conducted mean opinion score (MOS) study, isolated sentences and paragraphs achieve higher naturalness ratings when synthesized with the system that marks foci prosodically. This suggests that a more context-appropriate prosody can improve the naturalness of synthetic voices, not only when producing sequences of sentences but also when producing sentences in isolation. In addition, across the two systems, paragraphs receive lower ratings than isolated sentences. This strengthens the idea that the naturalness of a TTS system that has been evaluated on isolated sentences may decrease when the same system is used for the synthesis of larger texts or conversations This should be taken into account when designing and interpreting the evaluation of a TTS system.


## Producing the stimuli

The NVIDIA FastPitch implementation was used to train both models: https://github.com/NVIDIA/DeepLearningExamples/tree/master/PyTorch/SpeechSynthesis/FastPitch

A sigularity container was used for data pre-processing, training, and inference.

### Data
The 'prosody-control' dataset created by Latif et al. (2021) was used to train both models. The dataset was made publicly availble by the authors. It can be downloaded via https://download.europe.naverlabs.com/prosody-control/.

### Data preparation

The following steps were taken to prepare the dataset for training the **test model**:

- A metadata file was created that contains the name of all audio files together with their transcriptios. To create this file: 

  - All superfluous annotations (everything besides audio number and sentence type), and punctuation marks were removed
  - Control tags were added: '!' and a space before corrective foci, '?' and a space before questions
  - All letters were converted to lowercase
  - All transcriptions were duplicated

-> via create_metadata.py

- The WAV files were modified:
  - They were re-sampled to a frequency of 22050 Hz using convert_wavs_to_22050.py
  - They were converted to 16-bit WAV format using convert_to_16bits.sh
  - Silence before and after speech was removed with a threshold of 30dB using trim_silence.py

The same, prepared data was used to train the **baseline model**. However, before training the baseline model, the control tags were removed from the transcriptions. 

### Synthesis of the stimuli
The "Stimuli" directory contains the 24 stimuli that were synthesized for the listening test. They were synthesized using the sentences in "Text_input.pdf". The 12 stimuli in the subdirectory called "no_tag_model" were synthesized with the baseline model, i.e., with the model that was trained without control tags. Six isolated sentences and 6 paragraphs were synthesized with this model (see sub-subdirectories). The 12 stimuli in the subdirectory called "tags_model" were synthesized with the text model, i.e., with the model that was trained with tags marking foci and questions. With this model as well, 6 isolated sentences and 6 paragraphs were synthesized (see, again, sub-subdirectories). Paragraphs were synthesized in two steps: First, the two sentences of the paragraph were synthesized individually. Second, the two sentences were concatenated with a pause of 100 ms between them. The test model paragraphs were synthesized with tags that mark the narrow foci on the subject or the verb of the second sentence with the objective of inducing a narrow-focus intonation.

## Listening test
### Questionnaire
The file "Questionnaire.pdf" contains the questionnaire that was used for the listening test. It consits of an introduction, followed by the collection of demographic data, instructions to the listening test and the listening test (stimuli rating). The stimuli were presented to participants in random order. They were asked to rate each stimulus on a 9-point scale from bad to excellent.

### Text input
The file "Test_input.pdf" contains the lines of text that were used during inference (i.e., synthesis) of the stimuli. For the inference with the test model, the sign '!' was used as a tag to indicate to the model that a word carries a narrow corrective focus. 

## Bibliography
Latif, Siddique and Kim, Inyoung and Calapodescu, Ioan and Besacier, Laurent (2021) Controlling Prosody in End-to-End TTS: A Case Study on Contrastive Focus Generation. In: 25th Conference on Computational Natural Language Learning (CoNLL 2021), 10 Nov - 11 Nov 2021, Punta Cana, Dominican Republic. 
