---
title: "STT (Speech-to-Text) Data: The Magic of Converting Speech to Text"
date: 2024-11-18T20:03:41+09:00
slug: "402-STT-Speech-to-Text-데이터-음성을-텍스트로-변환하는-마법"
original_url: "https://memoryhub.tistory.com/402"
tistory_id: 402
draft: false
categories: ["Dev Concepts"]
tags: ["TA Business"]
---

Hello! Today, let's take a detailed look at STT data, the core of AI speech recognition.

## What is STT Data?

STT data is similar to how we learn a foreign language by looking at listening materials and scripts together!

- Pairs of audio files and their corresponding accurate text transcripts
- Used to train AI models to convert speech to text
- Includes diverse speakers, accents, and environmental noise

## Components of STT Data

### 1. Speech Data Characteristics

```
- Sampling rate: typically 16kHz or 44.1kHz
- Audio format: WAV, MP3, FLAC, etc.
- Channel: mono/stereo
- Bit depth: 16-bit, 24-bit, etc.
```

### 2. Text Data Characteristics

```
- Accurate transcription of speech content
- Time information (timestamps)
- Speaker information
- Emotion/context tags (optional)
```

## STT Data Construction Process

1. **Voice Collection**

   - Professional recording
   - Crowdsourcing
   - Real conversation/broadcast recording

2. **Preprocessing**

   ```
   # Audio preprocessing example
   audio = load_audio("sample.wav")
   processed_audio = preprocess_audio(audio)
   # - Noise removal
   # - Speech enhancement
   # - Sample rate normalization
   ```

3. **Labeling**

   ```
   {
     "audio_id": "001",
     "duration": "5.2",
     "text": "Hello, nice to meet you",
     "speaker_id": "SPK_001",
     "timestamp": {
       "start": "0.0",
       "end": "5.2"
     }
   }
   ```

## Major STT Datasets

### 1. Korean Datasets

- AIHub Korean Speech
- KsponSpeech
- zeroth-korean

### 2. English Datasets

- LibriSpeech
- Common Voice
- TIMIT

## Data Quality Standards ⭐

1. **Speech Quality**

   - SNR (Signal-to-Noise Ratio)
   - Speech clarity
   - Background noise level

2. **Transcription Quality**

   - Spelling accuracy
   - Punctuation consistency
   - Special character handling

3. **Diversity**

   - Speaker diversity
   - Dialects/accents
   - Domain coverage

## Data Augmentation Techniques

1. **Speech Augmentation**

   ```
   # Speech augmentation example
   augmented_audio = add_noise(audio, noise_level=0.1)
   augmented_audio = change_speed(audio, speed_factor=1.2)
   augmented_audio = pitch_shift(audio, steps=2)
   ```

2. **Environment Simulation**

   - Reverberation effects
   - Background noise addition
   - Channel distortion

## Important Considerations ⚠️

1. **Personal Information Protection**

   - Obtain speaker consent
   - Remove sensitive information
   - Anonymize data

2. **Quality Management**

   - Consistent guidelines
   - Cross-validation
   - Regular quality assessment

## Practical Use Cases

```
# STT dataset loading example
def load_stt_dataset(path):
    dataset = {
        'audio': [],
        'text': [],
        'metadata': []
    }
    # Data loading logic
    return dataset

# Data preprocessing pipeline
def preprocess_pipeline(dataset):
    # 1. Audio normalization
    # 2. Noise removal
    # 3. Special character handling
    return processed_dataset
```

## Conclusion

STT data is a critical element that determines the performance of speech recognition AI. Building and managing high-quality data is the first step to developing a successful STT system!

---

References:

1. [Speech Recognition: Data, Models, Languages - arXiv](https://arxiv.org/abs/2010.12750)
2. [AIHub Speech Data Construction Guidelines](https://aihub.or.kr/)
3. [Mozilla Common Voice Dataset](https://commonvoice.mozilla.org/)
4. [Kaldi Speech Recognition Toolkit](https://kaldi-asr.org/doc/data_prep.html)
5. [LibriSpeech ASR Corpus](http://www.openslr.org/12)
