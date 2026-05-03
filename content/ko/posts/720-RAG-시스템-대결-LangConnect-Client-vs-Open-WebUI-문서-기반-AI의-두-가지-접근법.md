---
title: "RAG 시스템 대결: LangConnect-Client vs Open WebUI - 문서 기반 AI의 두 가지 접근법"
date: 2025-07-08T22:40:58+09:00
slug: "720-RAG-시스템-대결-LangConnect-Client-vs-Open-WebUI-문서-기반-AI의-두-가지-접근법"
original_url: "https://memoryhub.tistory.com/720"
tistory_id: 720
draft: false
---

## 서론: AI가 문서를 읽고 답하는 시대

여러분이 수백 개의 기술 문서를 가지고 있다고 상상해보세요. 누군가 "우리 시스템에서 인증 오류를 해결하는 방법이 뭐야?"라고 물으면, AI가 관련 문서를 찾아 정확한 답변을 제공합니다. 이것이 바로 RAG(Retrieval-Augmented Generation)의 마법입니다.

오늘은 이러한 RAG 시스템을 구현하는 두 가지 인기 있는 오픈소스 프로젝트를 심층 비교해보겠습니다: **LangConnect-Client**와 **Open WebUI**. 각각의 아키텍처, 성능, 그리고 실제 사용 시나리오를 기술적으로 분석하여, 여러분의 프로젝트에 최적인 선택을 도와드리겠습니다.

## RAG란 무엇인가? 간단한 설명

RAG는 세 단계로 작동합니다:

```
# RAG의 기본 흐름
def rag_pipeline(user_question):
    # 1단계: 검색 (Retrieval)
    relevant_docs = vector_db.search(user_question)

    # 2단계: 증강 (Augmentation)
    context = format_context(relevant_docs)
    prompt = f"Context: {context}\nQuestion: {user_question}"

    # 3단계: 생성 (Generation)
    answer = llm.generate(prompt)
    return answer
```

이제 두 시스템이 이 과정을 어떻게 구현하는지 살펴보겠습니다.

## 1. 벡터 데이터베이스 아키텍처: 데이터 저장의 핵심

### LangConnect-Client: PostgreSQL + pgvector

LangConnect는 전통적인 관계형 데이터베이스인 PostgreSQL에 벡터 검색 기능을 추가한 pgvector 확장을 사용합니다.

```
-- LangConnect의 벡터 테이블 구조 예시
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    content TEXT,
    embedding vector(1536),  -- OpenAI 임베딩 차원
    metadata JSONB
);

-- 코사인 유사도 검색 쿼리
SELECT content, 1 - (embedding <=> query_embedding) as similarity
FROM documents
ORDER BY embedding <=> query_embedding
LIMIT 5;
```

**장점:**

- ACID 트랜잭션 보장
- 기존 PostgreSQL 인프라 활용 가능
- Supabase와 같은 관리형 서비스 지원

**단점:**

- 대규모 벡터 검색 시 성능 제한
- 특수 인덱스(IVF, HNSW) 설정 필요

### Open WebUI: ChromaDB

Open WebUI는 벡터 검색에 특화된 ChromaDB를 사용합니다.

```
# Open WebUI의 ChromaDB 설정 예시
import chromadb

# 로컬 ChromaDB 클라이언트 초기화
client = chromadb.PersistentClient(path="./chroma_db")

# 컬렉션 생성
collection = client.create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}  # 코사인 유사도 사용
)

# 문서 추가
collection.add(
    documents=["문서 내용..."],
    embeddings=[[0.1, 0.2, ...]],  # 임베딩 벡터
    metadatas=[{"source": "manual.pdf"}],
    ids=["doc1"]
)
```

**장점:**

- 인메모리 검색으로 빠른 속도
- 근사 최근접 이웃(ANN) 알고리즘 내장
- 벡터 검색에 최적화된 구조

**단점:**

- 관계형 데이터 처리 제한
- 대규모 배포 시 별도 서버 필요

## 2. 문서 처리 및 청킹 전략: 텍스트를 의미 있는 조각으로

### LangConnect-Client: 자동화된 단순함

```
# LangConnect의 자동 청킹 프로세스 (추정)
class AutoChunker:
    def __init__(self, chunk_size=1000, overlap=100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_document(self, text):
        """문서를 자동으로 청크로 분할"""
        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]

            # 문장 경계에서 자르기
            if end < len(text):
                last_period = chunk.rfind('.')
                if last_period > 0:
                    end = start + last_period + 1
                    chunk = text[start:end]

            chunks.append({
                'content': chunk,
                'start': start,
                'end': end
            })

            start = end - self.overlap

        return chunks
```

### Open WebUI: 세밀한 제어

```
# Open WebUI의 설정 가능한 청킹
class ConfigurableChunker:
    def __init__(self, config):
        self.mode = config['mode']  # 'character' 또는 'token'
        self.chunk_size = config['chunk_size']  # 기본값: 500 토큰
        self.overlap = config['overlap']  # 기본값: 50 토큰

    def chunk_by_tokens(self, text, tokenizer):
        """토큰 기반 청킹 - 더 정확한 LLM 컨텍스트 관리"""
        tokens = tokenizer.encode(text)
        chunks = []

        for i in range(0, len(tokens), self.chunk_size - self.overlap):
            chunk_tokens = tokens[i:i + self.chunk_size]
            chunk_text = tokenizer.decode(chunk_tokens)

            chunks.append({
                'content': chunk_text,
                'token_count': len(chunk_tokens),
                'position': i
            })

        return chunks
```

**청킹 크기 선택 가이드:**

- **작은 청크 (300-500 토큰)**: 법률 문서, 기술 사양서
- **중간 청크 (500-800 토큰)**: 일반 문서, 매뉴얼
- **큰 청크 (800-1000 토큰)**: 내러티브 문서, 연구 논문

## 3. 임베딩 모델과 벡터 인덱싱: 의미를 숫자로

### LangConnect-Client: OpenAI의 힘

```
# OpenAI 임베딩 사용 예시
import openai

def get_embeddings(texts):
    """OpenAI의 text-embedding-ada-002 모델 사용"""
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=texts
    )

    # 1536차원 벡터 반환
    embeddings = [item['embedding'] for item in response['data']]
    return embeddings

# 장점: 최고 수준의 품질, 다국어 지원
# 단점: API 비용, 인터넷 연결 필요
```

### Open WebUI: 다양한 선택지

```
# Open WebUI의 유연한 임베딩 모델 선택
from sentence_transformers import SentenceTransformer

# 다양한 모델 옵션
models = {
    'fast': 'sentence-transformers/all-MiniLM-L6-v2',  # 384차원, 빠름
    'balanced': 'Snowflake/arctic-embed-l-v2.0',      # 1024차원, 균형
    'accurate': 'BAAI/bge-large-en-v1.5'              # 1024차원, 정확
}

# 모델 로드 및 사용
model = SentenceTransformer(models['balanced'])
embeddings = model.encode(texts, batch_size=32)

# GPU 가속 가능
if torch.cuda.is_available():
    model = model.to('cuda')
```

**임베딩 모델 비교:**

| 모델 | 차원 | 속도 | 정확도 | 메모리 |
| --- | --- | --- | --- | --- |
| MiniLM | 384 | 매우 빠름 | 중간 | 낮음 |
| Arctic Embed | 1024 | 빠름 | 높음 | 중간 |
| OpenAI Ada | 1536 | API 의존 | 매우 높음 | 없음 |

## 4. 검색 파이프라인: 똑똑한 문서 찾기

### LangConnect-Client: 하이브리드 검색

```
class LangConnectRetriever:
    def hybrid_search(self, query, alpha=0.5):
        """시맨틱 + 키워드 하이브리드 검색"""
        # 1. 벡터 유사도 검색
        vector_results = self.vector_search(query)

        # 2. 전문 검색 (Full-text search)
        keyword_results = self.keyword_search(query)

        # 3. 점수 결합
        combined_scores = {}
        for doc in vector_results:
            combined_scores[doc.id] = alpha * doc.score

        for doc in keyword_results:
            if doc.id in combined_scores:
                combined_scores[doc.id] += (1 - alpha) * doc.score
            else:
                combined_scores[doc.id] = (1 - alpha) * doc.score

        # 4. 상위 결과 반환
        return sorted(combined_scores.items(), 
                     key=lambda x: x[1], 
                     reverse=True)[:5]
```

### Open WebUI: 다단계 검색 파이프라인

```
class OpenWebUIRetriever:
    def advanced_retrieval(self, query, top_k=10):
        """2단계 검색 + 재순위화"""
        # 1단계: 초기 검색 (벡터 + BM25)
        candidates = []

        # 벡터 검색
        vector_results = self.vector_db.similarity_search(
            query, k=top_k * 2
        )
        candidates.extend(vector_results)

        # BM25 키워드 검색
        if self.enable_hybrid:
            bm25_results = self.bm25_search(query, k=top_k)
            candidates.extend(bm25_results)

        # 중복 제거
        seen = set()
        unique_candidates = []
        for doc in candidates:
            if doc.id not in seen:
                seen.add(doc.id)
                unique_candidates.append(doc)

        # 2단계: Cross-Encoder 재순위화
        if self.cross_encoder:
            pairs = [(query, doc.content) for doc in unique_candidates]
            scores = self.cross_encoder.predict(pairs)

            # 점수로 재정렬
            ranked_docs = sorted(
                zip(unique_candidates, scores),
                key=lambda x: x[1],
                reverse=True
            )

            # 관련성 임계값 적용
            filtered_docs = [
                doc for doc, score in ranked_docs 
                if score >= self.relevance_threshold
            ]

            return filtered_docs[:top_k]

        return unique_candidates[:top_k]
```

**Cross-Encoder의 효과:**

```
# Cross-Encoder 예시
from sentence_transformers import CrossEncoder

# 모델 로드
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# 재순위화 전후 비교
query = "Python에서 비동기 프로그래밍 방법"
documents = [
    "Python의 async/await 문법을 사용한 비동기 프로그래밍",  # 관련성 높음
    "Python은 프로그래밍 언어입니다",  # 관련성 낮음
    "JavaScript의 Promise와 async 함수",  # 부분적 관련
]

# 점수 계산
scores = cross_encoder.predict([(query, doc) for doc in documents])
# 결과: [0.95, 0.12, 0.45] - 첫 번째 문서가 가장 관련성 높음
```

## 5. 정확도와 효율성 분석

### 정확도 측면

**실험 결과 (가상 시나리오):**

```
# 100개 질문에 대한 정확도 테스트
test_results = {
    'LangConnect': {
        'precision@5': 0.82,  # 상위 5개 중 관련 문서 비율
        'recall@5': 0.75,     # 전체 관련 문서 중 찾은 비율
        'f1_score': 0.78
    },
    'OpenWebUI': {
        'precision@5': 0.91,  # Cross-Encoder 덕분에 더 높음
        'recall@5': 0.83,
        'f1_score': 0.87
    }
}
```

### 효율성 측면

```
# 성능 벤치마크
performance_metrics = {
    'LangConnect': {
        '문서_임베딩_시간': '~200ms/청크 (API 호출)',
        '검색_시간': '~50ms (로컬 DB)',
        '총_지연시간': '~250ms',
        '비용': '$0.0001/1K 토큰',
        'GPU_필요': False
    },
    'OpenWebUI': {
        '문서_임베딩_시간': '~20ms/청크 (GPU), ~100ms/청크 (CPU)',
        '검색_시간': '~30ms (ChromaDB)',
        '재순위화_시간': '~50ms',
        '총_지연시간': '~100ms (GPU), ~180ms (CPU)',
        '비용': '$0 (로컬 실행)',
        'GPU_필요': '선택사항 (성능 향상용)'
    }
}
```

## 6. 실전 가이드: 언제 무엇을 선택할까?

### LangConnect-Client를 선택해야 할 때:

```
# 이상적인 사용 케이스
use_cases_langconnect = {
    "빠른_프로토타이핑": "OpenAI API로 즉시 시작",
    "소규모_팀": "인프라 관리 부담 최소화",
    "고품질_임베딩": "OpenAI의 최신 모델 활용",
    "기존_PostgreSQL_사용": "현재 인프라와 통합"
}

# 구현 예시
def setup_langconnect():
    """LangConnect 빠른 설정"""
    # 1. 환경 변수 설정
    os.environ['OPENAI_API_KEY'] = 'your-key'
    os.environ['DATABASE_URL'] = 'postgresql://...'

    # 2. 서버 시작
    # docker-compose up -d

    # 3. 문서 업로드
    # 웹 UI 사용 또는 API 호출
```

### Open WebUI를 선택해야 할 때:

```
# 이상적인 사용 케이스
use_cases_openwebui = {
    "데이터_프라이버시": "모든 데이터 로컬 처리",
    "대규모_문서": "수만 개 문서 효율적 처리",
    "커스터마이징": "청킹, 임베딩, 검색 세밀 조정",
    "오프라인_운영": "인터넷 없이 작동"
}

# 최적화 설정 예시
optimization_config = {
    "embedding_model": "Snowflake/arctic-embed-l-v2.0",
    "chunk_size": 500,
    "chunk_overlap": 50,
    "top_k": 5,
    "relevance_threshold": 0.7,
    "enable_reranking": True,
    "cross_encoder_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"
}
```

## 7. 고급 팁과 최적화

### 문서 전처리 최적화

```
def preprocess_documents(docs):
    """문서 품질 향상을 위한 전처리"""
    processed = []

    for doc in docs:
        # 1. 메타데이터 추출
        metadata = extract_metadata(doc)

        # 2. 구조화된 콘텐츠 파싱
        if doc.type == 'pdf':
            sections = parse_pdf_structure(doc)
        elif doc.type == 'html':
            sections = parse_html_semantically(doc)

        # 3. 섹션별 청킹 (의미 단위 보존)
        for section in sections:
            chunks = smart_chunk(
                section.content,
                preserve_paragraphs=True,
                min_size=300,
                max_size=800
            )

            for chunk in chunks:
                processed.append({
                    'content': chunk,
                    'metadata': {
                        **metadata,
                        'section': section.title,
                        'position': chunk.position
                    }
                })

    return processed
```

### 하이브리드 시스템 구축

```
class HybridRAGSystem:
    """두 시스템의 장점 결합"""

    def __init__(self):
        # OpenAI 임베딩 + 로컬 재순위화
        self.embedder = OpenAIEmbeddings()
        self.reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        self.vector_db = ChromaDB()

    def search(self, query):
        # 1. 고품질 쿼리 임베딩 (OpenAI)
        query_embedding = self.embedder.embed(query)

        # 2. 빠른 로컬 검색 (ChromaDB)
        candidates = self.vector_db.search(query_embedding, k=20)

        # 3. 정밀 재순위화 (로컬 Cross-Encoder)
        reranked = self.reranker.rerank(query, candidates)

        return reranked[:5]
```

## 결론: 당신의 선택은?

두 시스템 모두 강력한 RAG 솔루션입니다. 선택의 핵심은 여러분의 우선순위입니다:

- **간단함과 빠른 시작**: LangConnect-Client
- **최대 성능과 커스터마이징**: Open WebUI

미래에는 이 두 접근법이 융합될 가능성이 높습니다. 클라우드 서비스의 편의성과 로컬 처리의 유연성을 결합한 하이브리드 시스템이 표준이 될 것입니다.

## 기술 용어집

**RAG (Retrieval-Augmented Generation)**

- 이전: AI가 모든 것을 외워야 했어요
- 지금: AI가 필요할 때 책을 찾아봐요
- 비유: 시험 볼 때 오픈북처럼!

**벡터 임베딩 (Vector Embedding)**

- 이전: 컴퓨터는 단어를 글자로만 봤어요
- 지금: 단어의 의미를 숫자로 표현해요
- 비유: 색깔을 RGB 숫자로 표현하는 것처럼!

**Cross-Encoder**

- 이전: 단순히 비슷해 보이는 것만 찾았어요
- 지금: 질문과 답변이 진짜 맞는지 다시 확인해요
- 비유: 친구가 숙제 검사해주는 것처럼!

**청킹 (Chunking)**

- 이전: 책 전체를 한 번에 읽어야 했어요
- 지금: 책을 페이지나 문단으로 나눠서 읽어요
- 비유: 피자를 조각으로 나누는 것처럼!

---

*이 포스트가 도움이 되셨나요? 여러분의 RAG 프로젝트 경험을 댓글로 공유해주세요!*
