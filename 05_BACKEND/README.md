# 05_BACKEND

## 0. 문서 목적
- 백엔드 설계/코드 패턴/컨벤션을 정의한다.
- 단일 진실(제품/도메인/API 계약)은 다른 디렉토리에 있으며, 본 문서는 재작성하지 않는다.
- Claude Code 서브에이전트 템플릿을 포함하되, 실제 실행 파일은 백엔드 레포의 `.claude/`에 복사한다.

## 관련 문서
- [[01_PRODUCT/REQUIREMENTS.md]]
- [[01_PRODUCT/GAME_RULES.md]]
- [[01_PRODUCT/ECONOMY.md]]
- [[01_PRODUCT/CATALOG.md]]
- [[05_BACKEND/BE_STACK.md]]
- [[03_DOMAIN/DATA_MODEL.md]]
- [[03_DOMAIN/DB_NOTES.md]]
- [[03_API/README.md]]
- [[03_API/LIFECYCLE.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]
- [[03_API/CONTRACT/REST/AUTH_GUARDS.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 1. 문서 구조
- BE_STACK.md: 백엔드 기술 스택 고정값
- BE_ARCHITECTURE.md: 모듈 경계/레이어 책임 분리 규칙
- BE_CONVENTIONS.md: 네이밍/폴더/코딩 컨벤션
- BE_API_RULES.md: REST 계약 구현 규칙
- BE_REALTIME_RULES.md: 실시간(STOMP) 구현 규칙
- BE_DATA_MODEL_RULES.md: 데이터 모델/DB 규칙
- BE_TEST_RULES.md: 테스트 케이스/전략 규칙
- BE_AGENT_SPLIT.md: 병렬 서브에이전트 분할 기준
- AGENTS/README.md: 서브에이전트 템플릿 사용 규칙
- AGENTS/*.md: 역할별 서브에이전트 템플릿

---
## 2. 단일 진실 (재정의 금지)
- 기능/정책/규칙: [[01_PRODUCT/REQUIREMENTS.md]], [[01_PRODUCT/GAME_RULES.md]]
- 경제/카탈로그: [[01_PRODUCT/ECONOMY.md]], [[01_PRODUCT/CATALOG.md]]
- 도메인/DB: [[03_DOMAIN/DATA_MODEL.md]], [[03_DOMAIN/DB_NOTES.md]]
- API/실시간 계약: [[03_API/CONTRACT/REST/OPENAPI.yaml.md]], [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- 기술 스택: [[05_BACKEND/BE_STACK.md]]

---
## 3. 변경 원칙
- 정책/규칙 변경은 01_PRODUCT에서 먼저 수정한다.
- 도메인/DB 변경은 03_DOMAIN에서 먼저 수정한다.
- API/실시간 계약 변경은 03_API에서 먼저 수정한다.
- 백엔드 구현 패턴 변경은 05_BACKEND에서만 정의한다.
