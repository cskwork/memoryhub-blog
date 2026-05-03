---
title: "STT(Speech-to-Text) 데이터: 음성을 텍스트로 변환하는 마법 ? - Part 2"
date: 2024-11-18T20:05:45+09:00
slug: "403-STT-Speech-to-Text-데이터-음성을-텍스트로-변환하는-마법-Part-2"
original_url: "https://memoryhub.tistory.com/403"
tistory_id: 403
draft: false
---

## 1. 데이터 수집 단계별 상세 가이드 ?

### 1.1 음성 녹음 환경 설정

```
1. 녹음 공간
- 방음/흡음 처리된 전문 스튜디오
- 배경 소음 40dB 이하 유지
- 적정 습도 40-60% 유지

2. 녹음 장비
- 전문 콘덴서 마이크 사용 (ex: Shure SM58, AKG C414)
- 오디오 인터페이스 (ex: Focusrite Scarlett)
- 팝 필터 필수
```

### 1.2 녹음 사양 상세

```
1. 기본 설정
- 샘플링 레이트: 44.1kHz 또는 48kHz
- 비트심도: 24bit
- 파일 포맷: WAV (무손실)

2. 녹음 레벨
- 평균 -18dB ~ -12dB
- 피크 -6dB 이하
```

## 2. 전처리 파이프라인 상세 ?

### 2.1 오디오 전처리 (Python 예시)

```
import librosa
import numpy as np

def preprocess_audio(audio_path):
    # 1. 오디오 로드
    audio, sr = librosa.load(audio_path, sr=16000)

    # 2. 무음 구간 제거
    audio_trim, _ = librosa.effects.trim(audio, top_db=20)

    # 3. 노멀라이제이션
    audio_norm = librosa.util.normalize(audio_trim)

    # 4. 노이즈 제거
    noise_reduced = apply_noise_reduction(audio_norm)

    # 5. DC offset 제거
    audio_no_dc = remove_dc_offset(noise_reduced)

    return audio_no_dc, sr
```

### 2.2 텍스트 전처리

```
def preprocess_text(text):
    # 1. 특수문자 처리
    text = re.sub(r'[^\w\s]', '', text)

    # 2. 숫자 표현 정규화
    text = convert_numbers_to_words(text)

    # 3. 대소문자 통일
    text = text.lower()

    # 4. 띄어쓰기 정규화
    text = normalize_spacing(text)

    return text
```

## 3. 레이블링 상세 가이드 ?️

### 3.1 발화 정보 태깅

```
{
    "utterance_id": "UTT_001",
    "audio_path": "/data/audio/001.wav",
    "transcript": "안녕하세요 반갑습니다",
    "speaker_info": {
        "speaker_id": "SPK_001",
        "gender": "female",
        "age_group": "20s",
        "dialect": "서울"
    },
    "recording_info": {
        "environment": "studio",
        "device": "Shure SM58",
        "sampling_rate": 44100,
        "bit_depth": 24
    },
    "timestamps": [
        {"word": "안녕하세요", "start": 0.0, "end": 1.2},
        {"word": "반갑습니다", "start": 1.4, "end": 2.5}
    ],
    "metadata": {
        "emotion": "neutral",
        "noise_level": "clean",
        "quality_check": "passed"
    }
}
```

### 3.2 품질 관리 체크리스트

```
1. 음성 품질 체크
□ 클리핑 없음
□ SNR 20dB 이상
□ DC offset ±0.001 이내
□ 무음구간 적절

2. 전사 정확도 체크
□ 철자 정확도
□ 문장부호 일관성
□ 숫자/기호 표기 규칙

3. 메타데이터 체크
□ 화자 정보 완전성
□ 타임스탬프 정확도
□ 감정/상황 태그 일관성
```

## 4. 데이터 증강 상세 기법 ?

### 4.1 시간 도메인 증강

```
def time_domain_augmentation(audio):
    augmented = []

    # 1. 시간 스트레칭
    stretch_rates = [0.8, 0.9, 1.1, 1.2]
    for rate in stretch_rates:
        aug_audio = librosa.effects.time_stretch(audio, rate=rate)
        augmented.append(aug_audio)

    # 2. 피치 시프트
    pitch_steps = [-2, -1, 1, 2]
    for steps in pitch_steps:
        aug_audio = librosa.effects.pitch_shift(audio, sr=16000, n_steps=steps)
        augmented.append(aug_audio)

    return augmented
```

### 4.2 주파수 도메인 증강

```
def frequency_domain_augmentation(audio):
    # 1. 주파수 마스킹
    mask_param = 50
    freq_mask = freq_mask_augment(audio, mask_param)

    # 2. 스펙트럼 증강
    spec_aug = spectrogram_augment(audio)

    return [freq_mask, spec_aug]
```

## 5. 데이터셋 분할 및 검증 ?

### 5.1 데이터셋 분할 비율

```
def split_dataset(data, split_ratio=(0.8, 0.1, 0.1)):
    """
    데이터셋을 학습/검증/테스트로 분할

    분할 기준:
    - 학습데이터: 80%
    - 검증데이터: 10%
    - 테스트데이터: 10%
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

### 5.2 교차 검증 구현

```
def cross_validation(data, n_folds=5):
    from sklearn.model_selection import KFold

    kf = KFold(n_splits=n_folds, shuffle=True)

    for fold, (train_idx, val_idx) in enumerate(kf.split(data)):
        train_data = data[train_idx]
        val_data = data[val_idx]

        yield fold, train_data, val_data
```

## 6. 데이터 포맷 변환 유틸리티 ?

### 6.1 오디오 포맷 변환

```
def convert_audio_format(input_path, output_path, target_format='wav'):
    """
    지원 포맷:
    - WAV
    - FLAC
    - MP3
    - OGG
    """
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format=target_format)
```

### 6.2 텍스트 포맷 변환

```
def convert_text_format(input_file, output_format='json'):
    if output_format == 'json':
        return to_json_format(input_file)
    elif output_format == 'csv':
        return to_csv_format(input_file)
    elif output_format == 'txt':
        return to_txt_format(input_file)
```

## 마치며 ?

이상으로 STT 데이터의 상세한 처리 과정과 구현 방법에 대해 알아보았습니다. 실제 프로젝트에서는 이러한 기술들을 상황에 맞게 조합하고 최적화하여 사용하시면 됩니다!

---

참고문헌:

1. [Deep Speech: Scaling up end-to-end speech recognition](https://arxiv.org/abs/1412.5567)
2. [ESPnet: End-to-End Speech Processing Toolkit](https://github.com/espnet/espnet)
3. [Librosa Documentation](https://librosa.org/doc/latest/index.html)
4. [WebRTC Voice Activity Detector](https://github.com/wiseman/py-webrtcvad)
5. [Audio Data Augmentation Guidelines](https://arxiv.org/abs/2001.04295)
