---
title: "? 개발자 필수 툴, Ripgrep(rg) 10가지 활용법 + macOS 설치 방법"
date: 2025-09-02T16:02:34+09:00
slug: "772-개발자-필수-툴-Ripgrep-rg-10가지-활용법-macOS-설치-방법"
original_url: "https://memoryhub.tistory.com/772"
tistory_id: 772
draft: false
categories: ["데브 옵스"]
tags: ["Linux"]
---

안녕하세요! ?

오늘은 많은 개발자들이 grep 대신 쓰기 시작한 \*\*Ripgrep(rg)\*\*에 대해 소개해드리려고 합니다.

특히 대규모 프로젝트에서 **빠른 코드 검색**이 필요할 때 정말 강력한 무기예요 ⚡

---

## **? Ripgrep이 뭐예요?**

- grep의 업그레이드 버전이라고 생각하시면 됩니다.
- **매우 빠른 속도**: grep보다 훨씬 빠르게 검색합니다.
- **스마트한 검색**: .gitignore를 자동으로 인식해서 불필요한 폴더는 무시합니다.
- **개발자 친화적**: 언어 타입, 확장자 필터링, 줄번호, 통계 등 기능이 기본 탑재되어 있습니다.

---

## **? macOS에서 Ripgrep 설치 방법**

맥에서는 기본으로 rg가 설치되어 있지 않습니다.

Homebrew를 통해 간단히 설치할 수 있어요 ?

```
# Homebrew가 설치되어 있다면 아래 명령어 실행
brew install ripgrep

# 설치 확인
rg --version
```

? rg --version이 정상적으로 출력되면 설치 완료!

---

## **? Ripgrep 10가지 실전 팁**

**번호****명령어****설명**

|  |  |  |
| --- | --- | --- |
| 1 | rg "BusinessException" | 현재 디렉토리 전체에서 문자열 검색 |
| 2 | rg -n "TODO" | **라인 번호**와 함께 검색 (기본값이지만 기억해두면 좋아요) |
| 3 | rg -i "error" | **대소문자 구분 없이** 검색 |
| 4 | rg -t java "UserService" | 특정 **언어 타입**만 검색 (예: Java 파일) |
| 5 | rg -g "\*.xml" "tchrId" | **특정 확장자**만 검색 |
| 6 | rg -g "!\*.min.js" "fetch(" | 특정 파일 제외 (예: minified JS 제외) |
| 7 | rg -C 3 "SQLException" | 검색 결과 주변의 **문맥 3줄**까지 출력 |
| 8 | rg -l "password" | 매칭된 **파일 이름만** 출력 |
| 9 | rg -v "DEBUG" | 매칭되지 않은 라인만 출력 (NOT 검색) |
| 10 | rg --stats "BusinessException" | 검색 후 **파일 수/매치 수 통계** 출력 |

---

## **?️ 파워 유저 꿀팁**

- rg --hidden "pattern" → 숨김 파일까지 검색 (.env 등)
- rg -uuu "pattern" → .gitignore 무시하고 전부 검색
- rg -w "id" → **단어 단위**로만 매칭
- rg -e "foo|bar" → **OR 조건** 검색 (foo 또는 bar)
- rg --json "pattern" → JSON 형식 출력 (IDE 연동 가능)

---

## **✅ 정리**

Ripgrep(rg)는 **빠르고, 똑똑하고, 개발자 친화적인 검색 도구**입니다.

특히 대규모 프로젝트에서 grep보다 훨씬 효율적으로 소스 코드를 탐색할 수 있어요.

? 한 줄 요약: **“macOS 개발자는 Homebrew로 Ripgrep 설치하고, 검색은 grep 대신 rg로!”**
