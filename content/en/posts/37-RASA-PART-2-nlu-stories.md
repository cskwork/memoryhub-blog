---
title: "RASA PART 2 nlu & stories"
date: 2020-11-23T12:57:06+09:00
slug: "37-RASA-PART-2-nlu-stories"
original_url: "https://memoryhub.tistory.com/37"
tistory_id: 37
draft: false
---

The way conversations with Rasa are managed is stored as stories, and conversations are sequentially guided based on the generated stories.

```
stories:
- story: search_venues #story name
steps: #progression steps
- intent: search_venues #user query
- action: action_search_venues # action_ is a custom function for executing backend actions
- slot_was_set: #slot is used as bot memory i.e. for storing responses
- venues: [{"name": "Big Arena", "reviews": 4.5}]
```
