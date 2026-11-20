[referencia=141fa255b5f5db2d score=0.048]
### Production-Ready Face Re-Aging for Visual Effects

Photorealistic digital re-aging of faces in video is becoming increasingly common in entertainment and advertising. But the predominant 2D painting workflow often requires frame-by-frame manual work that can take days to accomplish, even by skilled artists. Although research on facial image re-aging has attempted to automate and solve this problem, current techniques are of little practical use as they typically suffer from facial identity loss, poor resolution, and unstable results across subsequent video frames. In this paper, we present the first practical, fully-automatic and production-ready method for re-aging faces in video images. Our first key insight is in addressing the problem of collecting longitudinal training data for learning to re-age faces over extended periods of time, a task that is nearly impossible to accomplish for a large number of real people. We show how such a longitudinal dataset can be constructed by leveraging the current state-of-the-art in facial re-aging that, although failing on real images, does provide photoreal re-aging results on synthetic faces. Our second key insight is then to leverage such synthetic data and formulate facial re-aging as a practical image-to-image translation task that can be performed by training a well-understood U-Net architecture, without the need for more complex network designs. We demonstrate how the simple U-Net, surprisingly, allows us to advance the state of the art for re-aging real faces on video, with unprecedented temporal stability and preservation of facial identity across variable expressions, viewpoints, and lighting conditions. Finally, our new face re-aging network (FRAN) incorporates simple and intuitive mechanisms that provides artists with localized control and creative freedom to direct and fine-tune the re-aging effect, a feature that is largely important in real production pipelines and often overlooked in related research work.

---

[referencia=141fa255b5f5db2d score=0.008]
# **Production-Ready Face Re-Aging for Visual Effects**

### We demonstrate how the simple U-Net, surprisingly, allows us to advance the state of the art for re-aging real faces on video, with unprecedented temporal stability and preservation of facial identity across variable expressions, viewpoints, and lighting conditions.

**November 30, 2022 ACM SIGGRAPH Asia (2022)**


#### Authors

Gaspard Zoss (DisneyResearch|Studios)

Prashanth Chandran (DisneyResearch|Studios/ETH Joint PhD)

Eftychios Sifakis (DisneyResearch|Studios)

Markus Gross (DisneyResearch|Studios/ETH Zurich)

Paulo Gotardo (DisneyResearch|Studios)

Derek Bradley (DisneyResearch|Studios)

---

[referencia=b3be602ae28ce7ec score=0.005]
VALL-E is a language modeling approach for text-to-speech synthesis (TTS). Specifically, we train a neural codec language model (called VALL-E) using discrete codes derived from an off-the-shelf neural audio codec model, and regard TTS as a conditional language modeling task rather than continuous signal regression as in previous work. During the pre-training stage, we scale up the TTS training data to 60K hours of English speech which is hundreds of times larger than existing systems. VALL-E emerges in-context learning capabilities and can be used to **synthesize high-quality personalized speech with only a 3-second enrolled recording of an unseen speaker** as an acoustic prompt. Experiment results show that VALL-E significantly outperforms the state-of-the-art zero-shot TTS system in terms of speech naturalness and speaker similarity. In addition, we find VALL-E could preserve the speaker’s emotion and acoustic environment of the acoustic prompt in synthesis.

This page is for **research demonstration purposes** only.

## Model Overview

Unlike the previous pipeline (e.g., phoneme → mel-spectrogram → waveform), the pipeline of VALL-E is phoneme → discrete code → waveform. VALL-E generates the discrete audio codec codes based on phoneme and acoustic code prompts, corresponding to the target content and the speaker’s voice. VALL-E directly enables various speech synthesis applications, such as zero-shot TTS, speech editing, and content creation combined with other generative AI models like GPT.

---

[referencia=7bf9bf765e30299b score=0.004]
April 7, 2022

Posted by Tal Remez, Software Engineer, Google Research and Micheal Hassid, Software Engineer Intern, Google Research

Recent years have seen a tremendous increase in the creation and serving of video content to users across the world in a variety of languages and over numerous platforms. The process of creating high quality content can include several stages from video capturing and captioning to video and audio editing. In some cases dialogue is re-recorded (referred to as dialog replacement, post-sync or dubbing) in a studio in order to achieve high quality and replace original audio that might have been recorded in noisy conditions. However, the dialog replacement process can be difficult and tedious because the newly recorded audio needs to be well synced with the video, requiring several edits to match the exact timing of mouth movements.

In “More than Words: In-the-Wild Visually-Driven Prosody for Text-to-Speech”, we present a proof-of-concept visually-driven text-to-speech model, called VDTTS, that automates the dialog replacement process. Given a text and the original video frames of the speaker, VDTTS is trained to generate the corresponding speech. As opposed to standard visual speech recognition models, which focus on the mouth region, we detect and crop full faces using MediaPipe to avoid potentially excluding information pertinent to the speaker’s delivery. This gives the VDTTS model enough information to generate speech that matches the video while also recovering aspects of prosody, such as timing and emotion. Despite not being explicitly trained to generate speech that is synchronized to the input video, the learned model still does so.

| Given a text and video frames of a speaker, VDTTS generates speech with prosody that matches the video signal. | 

The VDTTS model resembles Tacotron at its core and has four main components: (1) text and video encoders that process the inputs; (2) a multi-source attention mechanism that connects encoders to a decoder; (3) a spectrogram decoder that incorporates the speaker embedding (similarly to VoiceFilter), and produces mel-spectrograms (which are a form of compressed representation in the frequency domain); and (4) a frozen, pretrained neural vocoder that produces waveforms from the mel-spectrograms.

---

[referencia=7bf9bf765e30299b score=0.001]
| **Original** | **VDTTS** | **VDTTS video-only** | **TTS** | 

| **Original** displays the original video clip.**VDTTS** , displays the audio predicted using both the video frames and the text as input.**VDTTS video-only** displays audio predictions using video frames only.**TTS** displays audio predictions using text only.**Top transcript** : "of space for people to make their own judgments and to come to their own".**Bottom transcript** : "absolutely love dancing I have no dance experience whatsoever but as that". | 

We’ve measured the VDTTS model’s performance using the VoxCeleb2 dataset and compared it to TTS and the TTS with length hint (a TTS that receives the scene length) models. We demonstrate that VDTTS outperforms both models by large margins in most of the aspects we measured: higher sync-to-video quality (measured by SyncNet Distance) and better speech quality as measured by mel cepstral distance (MCD), and lower Gross Pitch Error (GPE), which measures the percentage of frames where pitch differed by more than 20% on frames for which voice was present on both the predicted and reference audio.

| SyncNet distance comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

| Mel cepstral distance comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

| Gross Pitch Error comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

One thing to note is that, intriguingly, VDTTS can produce video synchronized speech without any explicit losses or constraints to promote this, suggesting complexities such as synchronization losses or explicit modeling are unnecessary.

While this is a proof-of-concept demonstration, we believe that in the future, VDTTS can be upgraded to be used in scenarios where the input text differs from the original video signal. This kind of a model would be a valuable tool for tasks such as translation dubbing.

---

[referencia=b3be602ae28ce7ec score=0.001]
## Zero-shot TTS for LibriSpeech and VCTK dataset

- 
			Text Ground Truth Reconstruction (Encodec) Reconstruction (Vocos) Speaker Prompt (Prefix/Ref) Baseline Samples (YourTTS) VALL-E Samples 
 (Encodec)VALL-E Samples 
 (Vocos)They moved thereafter cautiously about the hut groping before and about them to find something to show that Warrenton had fulfilled his mission And lay me down in thy cold bed and leave my shining lot Number ten fresh nelly is waiting on you good night husband Yea his honourable worship is within but he hath a godly minister or two with him and likewise a leech Instead of shoes the old man wore boots with turnover tops and his blue coat had wide cuffs of gold braid The army found the people in poverty and left them in comparative wealth Thus did this humane and right minded father comfort his unhappy daughter and her mother embracing her again did all she could to soothe her feelings He was in deep converse with the clerk and entered the hall holding him by the arm

- 
			Text Ground Truth Reconstruction (Encodec) Reconstruction (Vocos) Speaker Prompt (3s_5s_10s) Baseline Samples (YourTTS) VALL-E Samples 
 (Encodec)VALL-E Samples 
 (Vocos)We have to reduce the number of plastic bags So what is the campaign about My life has changed a lot Nothing is yet confirmed I could hardly move for the next couple of days His son has been travelling with the Tartan Army for years Her husband was very concerned that it might be fatal We’ve made a couple of albums

## Synthesis of diversity

- 
			Text Speaker Prompt VALL-E Sample1 VALL-E Sample2 Because we do not need it. I must do something about it. He has not been named. Number ten, fresh nelly is waiting on you, good night husband.

## Acoustic environment maintenance

- 
			Text Ground Truth Reconstruction (Encodec) Reconstruction (Vocos) Speaker Prompt (3-second) Baseline Samples (YourTTS) VALL-E Samples 
 (Encodec)VALL-E Samples 
 (Vocos)Yeah really Well they were saying it was snowing in southern Florida yesterday I think it’s like you know um more convenient too Everything is run by computer but you got to know how to think before you can do a computer Then out in LA you guys got a whole other ballgame with California to worry about

---

[referencia=7bf9bf765e30299b score=0.001]
*We would like to thank the co-authors of this research: Michelle Tadmor Ramanovich, Ye Jia, Brendan Shillingford, and Miaosen Wang. We are also grateful to the valued contributions, discussions, and feedback from Nadav Bar, Jay Tenenbaum, Zach Gleicher, Paul McCartney, Marco Tagliasacchi, and Yoni Tzafir.*

---

[referencia=b3be602ae28ce7ec score=0.000]
## Speaker emotion maintenance

- 
			Text Emotion Speaker Prompt (3-second) Baseline Samples (YourTTS) VALL-E Samples 
 (Encodec)VALL-E Samples 
 (Vocos)We have to reduce the number of plastic bags. Anger Sleepy Neutral Amused Disgusted

## Ethics Statement

VALL-E could synthesize speech that maintains speaker identity and could be used for educational learning, entertainment, journalistic, self-authored content, accessibility features, interactive voice response systems, translation, chatbot, and so on. While VALL-E can speak in a voice like the voice talent, the similarity, and naturalness depend on the length and quality of the speech prompt, the background noise, as well as other factors. It may carry potential risks in the misuse of the model, such as spoofing voice identification or impersonating a specific speaker. We conducted the experiments under the assumption that the user agrees to be the target speaker in speech synthesis. If the model is generalized to unseen speakers in the real world, it should include a protocol to ensure that the speaker approves the use of their voice and a synthesized speech detection model. If you suspect that VALL-E is being used in a manner that is abusive or illegal or infringes on your rights or the rights of other people, you can report it at the Report Abuse Portal.

---

[referencia=7bf9bf765e30299b score=0.000]
| The overall architecture of VDTTS. Text and video encoders process the inputs and then a multisource attention mechanism connects these to a decoder that produces mel-spectrograms. A vocoder then produces waveforms from the mel-spectrograms to generate speech as an output. | 

We train VDTTS using video and text pairs from LSVSR in which the text corresponds to the exact words spoken by a person in a video. Throughout our testing, we have determined that VDTTS cannot generate arbitrary text, thus making it less prevalent for misuse (e.g., the generation of fake content).

To showcase the unique strength of VDTTS in this post, we have selected two inference examples from the VoxCeleb2 test dataset and compare the performance of VDTTS to a standard text-to-speech (TTS) model. In both examples, the video frames provide prosody and word timing clues, visual information that is not available to the TTS model.

In the first example, the speaker talks at a particular pace that can be seen as periodic gaps in the ground-truth mel-spectrogram (shown below). VDTTS preserves this characteristic and generates audio that is much closer to the ground-truth than the audio generated by standard TTS without access to the video.

Similarly, in the second example, the speaker takes long pauses between some of the words. These pauses are captured by VDTTS and are reflected in the video below, whereas the TTS does not capture this aspect of the speaker’s rhythm.

We also plot fundamental frequency (F0) charts to compare the pitch generated by each model to the ground-truth pitch. In both examples, the F0 curve of VDTTS fits the ground-truth much better than the TTS curve, both in the alignment of speech and silence, and also in how the pitch changes over time. See more original videos and VDTTS generated videos.

| We present two examples, (a) and (b), from the VoxCeleb2 test set. From top to bottom: input face images, ground-truth (GT) mel-spectrogram, mel-spectrogram output of VDTTS, mel-spectrogram output of a standard TTS model, and two plots showing the normalized F0 (normalized by mean non-zero pitch, i.e., mean is only over voiced periods) of VDTTS and TTS compared to the ground-truth signal. |