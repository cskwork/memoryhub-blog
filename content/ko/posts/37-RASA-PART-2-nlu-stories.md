---
title: "RASA PART 2 nlu & stories"
date: 2020-11-23T12:57:06+09:00
slug: "37-RASA-PART-2-nlu-stories"
original_url: "https://memoryhub.tistory.com/37"
tistory_id: 37
draft: false
---

라사와 대화하는 형태는 story로 보관되고 생성된 story 기반으로 순차적으로 대화를 이끌어간다.

```
stories:
- story: search_venues #story 명칭
steps: #진행 단계
- intent: search_venues #사용자 질문
- action: action_search_venues # action_는 백앤드 액션을 실행하기 위한 사용자 정의 함수다.
- slot_was_set: #slot은 봇 메모리 즉 답변 보관용으로 사용 
- venues: [{"name": "Big Arena", "reviews": 4.5}]
```
