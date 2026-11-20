[referencia=141fa255b5f5db2d score=0.016]
### Production-Ready Face Re-Aging for Visual Effects

Photorealistic digital re-aging of faces in video is becoming increasingly common in entertainment and advertising. But the predominant 2D painting workflow often requires frame-by-frame manual work that can take days to accomplish, even by skilled artists. Although research on facial image re-aging has attempted to automate and solve this problem, current techniques are of little practical use as they typically suffer from facial identity loss, poor resolution, and unstable results across subsequent video frames. In this paper, we present the first practical, fully-automatic and production-ready method for re-aging faces in video images. Our first key insight is in addressing the problem of collecting longitudinal training data for learning to re-age faces over extended periods of time, a task that is nearly impossible to accomplish for a large number of real people. We show how such a longitudinal dataset can be constructed by leveraging the current state-of-the-art in facial re-aging that, although failing on real images, does provide photoreal re-aging results on synthetic faces. Our second key insight is then to leverage such synthetic data and formulate facial re-aging as a practical image-to-image translation task that can be performed by training a well-understood U-Net architecture, without the need for more complex network designs. We demonstrate how the simple U-Net, surprisingly, allows us to advance the state of the art for re-aging real faces on video, with unprecedented temporal stability and preservation of facial identity across variable expressions, viewpoints, and lighting conditions. Finally, our new face re-aging network (FRAN) incorporates simple and intuitive mechanisms that provides artists with localized control and creative freedom to direct and fine-tune the re-aging effect, a feature that is largely important in real production pipelines and often overlooked in related research work.

---

[referencia=7bf9bf765e30299b score=0.015]
April 7, 2022

Posted by Tal Remez, Software Engineer, Google Research and Micheal Hassid, Software Engineer Intern, Google Research

Recent years have seen a tremendous increase in the creation and serving of video content to users across the world in a variety of languages and over numerous platforms. The process of creating high quality content can include several stages from video capturing and captioning to video and audio editing. In some cases dialogue is re-recorded (referred to as dialog replacement, post-sync or dubbing) in a studio in order to achieve high quality and replace original audio that might have been recorded in noisy conditions. However, the dialog replacement process can be difficult and tedious because the newly recorded audio needs to be well synced with the video, requiring several edits to match the exact timing of mouth movements.

In “More than Words: In-the-Wild Visually-Driven Prosody for Text-to-Speech”, we present a proof-of-concept visually-driven text-to-speech model, called VDTTS, that automates the dialog replacement process. Given a text and the original video frames of the speaker, VDTTS is trained to generate the corresponding speech. As opposed to standard visual speech recognition models, which focus on the mouth region, we detect and crop full faces using MediaPipe to avoid potentially excluding information pertinent to the speaker’s delivery. This gives the VDTTS model enough information to generate speech that matches the video while also recovering aspects of prosody, such as timing and emotion. Despite not being explicitly trained to generate speech that is synchronized to the input video, the learned model still does so.

| Given a text and video frames of a speaker, VDTTS generates speech with prosody that matches the video signal. | 

The VDTTS model resembles Tacotron at its core and has four main components: (1) text and video encoders that process the inputs; (2) a multi-source attention mechanism that connects encoders to a decoder; (3) a spectrogram decoder that incorporates the speaker embedding (similarly to VoiceFilter), and produces mel-spectrograms (which are a form of compressed representation in the frequency domain); and (4) a frozen, pretrained neural vocoder that produces waveforms from the mel-spectrograms.

---

[referencia=7bf9bf765e30299b score=0.005]
| **Original** | **VDTTS** | **VDTTS video-only** | **TTS** | 

| **Original** displays the original video clip.**VDTTS** , displays the audio predicted using both the video frames and the text as input.**VDTTS video-only** displays audio predictions using video frames only.**TTS** displays audio predictions using text only.**Top transcript** : "of space for people to make their own judgments and to come to their own".**Bottom transcript** : "absolutely love dancing I have no dance experience whatsoever but as that". | 

We’ve measured the VDTTS model’s performance using the VoxCeleb2 dataset and compared it to TTS and the TTS with length hint (a TTS that receives the scene length) models. We demonstrate that VDTTS outperforms both models by large margins in most of the aspects we measured: higher sync-to-video quality (measured by SyncNet Distance) and better speech quality as measured by mel cepstral distance (MCD), and lower Gross Pitch Error (GPE), which measures the percentage of frames where pitch differed by more than 20% on frames for which voice was present on both the predicted and reference audio.

| SyncNet distance comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

| Mel cepstral distance comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

| Gross Pitch Error comparison between VDTTS, TTS and the TTS with Length hint (a lower metric is better). | 

One thing to note is that, intriguingly, VDTTS can produce video synchronized speech without any explicit losses or constraints to promote this, suggesting complexities such as synchronization losses or explicit modeling are unnecessary.

While this is a proof-of-concept demonstration, we believe that in the future, VDTTS can be upgraded to be used in scenarios where the input text differs from the original video signal. This kind of a model would be a valuable tool for tasks such as translation dubbing.

---

[referencia=141fa255b5f5db2d score=0.003]
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

[referencia=7bf9bf765e30299b score=0.000]
| The overall architecture of VDTTS. Text and video encoders process the inputs and then a multisource attention mechanism connects these to a decoder that produces mel-spectrograms. A vocoder then produces waveforms from the mel-spectrograms to generate speech as an output. | 

We train VDTTS using video and text pairs from LSVSR in which the text corresponds to the exact words spoken by a person in a video. Throughout our testing, we have determined that VDTTS cannot generate arbitrary text, thus making it less prevalent for misuse (e.g., the generation of fake content).

To showcase the unique strength of VDTTS in this post, we have selected two inference examples from the VoxCeleb2 test dataset and compare the performance of VDTTS to a standard text-to-speech (TTS) model. In both examples, the video frames provide prosody and word timing clues, visual information that is not available to the TTS model.

In the first example, the speaker talks at a particular pace that can be seen as periodic gaps in the ground-truth mel-spectrogram (shown below). VDTTS preserves this characteristic and generates audio that is much closer to the ground-truth than the audio generated by standard TTS without access to the video.

Similarly, in the second example, the speaker takes long pauses between some of the words. These pauses are captured by VDTTS and are reflected in the video below, whereas the TTS does not capture this aspect of the speaker’s rhythm.

We also plot fundamental frequency (F0) charts to compare the pitch generated by each model to the ground-truth pitch. In both examples, the F0 curve of VDTTS fits the ground-truth much better than the TTS curve, both in the alignment of speech and silence, and also in how the pitch changes over time. See more original videos and VDTTS generated videos.

| We present two examples, (a) and (b), from the VoxCeleb2 test set. From top to bottom: input face images, ground-truth (GT) mel-spectrogram, mel-spectrogram output of VDTTS, mel-spectrogram output of a standard TTS model, and two plots showing the normalized F0 (normalized by mean non-zero pitch, i.e., mean is only over voiced periods) of VDTTS and TTS compared to the ground-truth signal. |

---

[referencia=7bf9bf765e30299b score=0.000]
*We would like to thank the co-authors of this research: Michelle Tadmor Ramanovich, Ye Jia, Brendan Shillingford, and Miaosen Wang. We are also grateful to the valued contributions, discussions, and feedback from Nadav Bar, Jay Tenenbaum, Zach Gleicher, Paul McCartney, Marco Tagliasacchi, and Yoni Tzafir.*