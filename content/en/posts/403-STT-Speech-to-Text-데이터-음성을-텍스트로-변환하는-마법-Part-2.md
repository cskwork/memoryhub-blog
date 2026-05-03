---
title: "STT (Speech-to-Text) Data: The Magic of Converting Speech to Text - Part 2"
date: 2024-11-18T20:05:45+09:00
slug: "403-STT-Speech-to-Text-데이터-음성을-텍스트로-변환하는-마법-Part-2"
original_url: "https://memoryhub.tistory.com/403"
tistory_id: 403
draft: false
---

## 1. Detailed Step-by-Step Voice Collection Guide

### 1.1 Recording Environment Setup

```
1. Recording Space
- Soundproof/sound-absorbing professional studio
- Maintain background noise below 40dB
- Maintain appropriate humidity of 40-60%

2. Recording Equipment
- Professional condenser microphone (ex: Shure SM58, AKG C414)
- Audio interface (ex: Focusrite Scarlett)
- Pop filter required
```

### 1.2 Recording Specifications Details

```
1. Basic Settings
- Sampling rate: 44.1kHz or 48kHz
- Bit depth: 24bit
- File format: WAV (lossless)

2. Recording Level
- Average: -18dB ~ -12dB
- Peak: -6dB or below
```

## 2. Preprocessing Pipeline Details

### 2.1 Audio Preprocessing (Python Example)

```
import librosa
import numpy as np

def preprocess_audio(audio_path):
    # 1. Load audio
    audio, sr = librosa.load(audio_path, sr=16000)

    # 2. Remove silence
    audio_trim, _ = librosa.effects.trim(audio, top_db=20)

    # 3. Normalization
    audio_norm = librosa.util.normalize(audio_trim)

    # 4. Noise removal
    noise_reduced = apply_noise_reduction(audio_norm)

    # 5. Remove DC offset
    audio_no_dc = remove_dc_offset(noise_reduced)

    return audio_no_dc, sr
```

### 2.2 Text Preprocessing

```
def preprocess_text(text):
    # 1. Special character handling
    text = re.sub(r'[^\w\s]', '', text)

    # 2. Normalize number representation
    text = convert_numbers_to_words(text)

    # 3. Standardize case
    text = text.lower()

    # 4. Normalize spacing
    text = normalize_spacing(text)

    return text
```

## 3. Detailed Labeling Guide

### 3.1 Utterance Information Tagging

```
{
    "utterance_id": "UTT_001",
    "audio_path": "/data/audio/001.wav",
    "transcript": "Hello, nice to meet you",
    "speaker_info": {
        "speaker_id": "SPK_001",
        "gender": "female",
        "age_group": "20s",
        "dialect": "Seoul"
    },
    "recording_info": {
        "environment": "studio",
        "device": "Shure SM58",
        "sampling_rate": 44100,
        "bit_depth": 24
    },
    "timestamps": [
        {"word": "Hello", "start": 0.0, "end": 0.8},
        {"word": "nice", "start": 1.0, "end": 1.5}
    ],
    "metadata": {
        "emotion": "neutral",
        "noise_level": "clean",
        "quality_check": "passed"
    }
}
```

### 3.2 Quality Management Checklist

```
1. Voice Quality Check
□ No clipping
□ SNR 20dB or above
□ DC offset within ±0.001
□ Appropriate silence intervals

2. Transcription Accuracy Check
□ Spelling accuracy
□ Punctuation consistency
□ Numbers/symbols notation rules

3. Metadata Check
□ Speaker information completeness
□ Timestamp accuracy
□ Emotion/situation tag consistency
```

## 4. Detailed Data Augmentation Techniques

### 4.1 Time Domain Augmentation

```
def time_domain_augmentation(audio):
    augmented = []

    # 1. Time stretching
    stretch_rates = [0.8, 0.9, 1.1, 1.2]
    for rate in stretch_rates:
        aug_audio = librosa.effects.time_stretch(audio, rate=rate)
        augmented.append(aug_audio)

    # 2. Pitch shift
    pitch_steps = [-2, -1, 1, 2]
    for steps in pitch_steps:
        aug_audio = librosa.effects.pitch_shift(audio, sr=16000, n_steps=steps)
        augmented.append(aug_audio)

    return augmented
```

### 4.2 Frequency Domain Augmentation

```
def frequency_domain_augmentation(audio):
    # 1. Frequency masking
    mask_param = 50
    freq_mask = freq_mask_augment(audio, mask_param)

    # 2. Spectrogram augmentation
    spec_aug = spectrogram_augment(audio)

    return [freq_mask, spec_aug]
```

## 5. Dataset Splitting and Validation

### 5.1 Dataset Split Ratio

```
def split_dataset(data, split_ratio=(0.8, 0.1, 0.1)):
    """
    Split dataset into train/validation/test

    Split criteria:
    - Training data: 80%
    - Validation data: 10%
    - Test data: 10%
    """
    total = len(data)
    train_size = int(total * split_ratio[0])
    val_size = int(total * split_ratio[1])

    indices = np.random.permutation(total)

    return {
        'train': data[indices[:train_size]],
        'val': data[indices[train_size:train_size+val_size]],
        'test': data[indices[train_size+val_size:]]
    }
```

### 5.2 Cross-Validation Implementation

```
def cross_validation(data, n_folds=5):
    from sklearn.model_selection import KFold

    kf = KFold(n_splits=n_folds, shuffle=True)

    for fold, (train_idx, val_idx) in enumerate(kf.split(data)):
        train_data = data[train_idx]
        val_data = data[val_idx]

        yield fold, train_data, val_data
```

## 6. Data Format Conversion Utilities

### 6.1 Audio Format Conversion

```
def convert_audio_format(input_path, output_path, target_format='wav'):
    """
    Supported formats:
    - WAV
    - FLAC
    - MP3
    - OGG
    """
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=target_format)
```

### 6.2 Text Format Conversion

```
def convert_text_format(input_file, output_format='json'):
    if output_format == 'json':
        return to_json_format(input_file)
    elif output_format == 'csv':
        return to_csv_format(input_file)
    elif output_format == 'txt':
        return to_txt_format(input_file)
```

## Conclusion

We've now covered the detailed processing steps and implementation methods for STT data. In actual projects, you can use these techniques in combination and optimize them as needed!

---

References:

1. [Deep Speech: Scaling up end-to-end speech recognition](https://arxiv.org/abs/1412.5567)
2. [ESPnet: End-to-End Speech Processing Toolkit](https://github.com/espnet/espnet)
3. [Librosa Documentation](https://librosa.org/doc/latest/index.html)
4. [WebRTC Voice Activity Detector](https://github.com/wiseman/py-webrtcvad)
5. [Audio Data Augmentation Guidelines](https://arxiv.org/abs/2001.04295)
