# 04_FRONTEND

## 0. 문서 목적
- Vite + Vue 프론트엔드 개발 시 **지켜야 하는 코드 패턴/컨벤션/설계 규칙**을 정의한다.
- 단일 진실(제품/디자인/API)은 다른 디렉토리에 있으며, 본 문서는 **재작성하지 않고 링크로 참조**한다.
- AI 서브에이전트가 구현 시 참조할 **프론트 규칙집**으로 사용한다.

## 관련 문서
- [[01_PRODUCT/REQUIREMENTS.md]]
- [[01_PRODUCT/USER_FLOWS.md]]
- [[01_PRODUCT/COPY_TEXT.md]]
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[02_DESIGN/TOKENS.json.md]]
- [[02_DESIGN/COMPONENTS.json.md]]
- [[03_API/README.md]]
- [[03_API/LIFECYCLE.md]]

---
## 1. 단일 진실 (재정의 금지)
- 기능/정책/흐름: [[01_PRODUCT/REQUIREMENTS.md]], [[01_PRODUCT/USER_FLOWS.md]]
- UI 문구: [[01_PRODUCT/COPY_TEXT.md]]
- 레이아웃/스타일: [[02_DESIGN/DESIGN_RULES.md]], [[02_DESIGN/LAYOUT_RULES.md]], [[02_DESIGN/TOKENS.json.md]], [[02_DESIGN/COMPONENTS.json.md]]
- API 계약/실시간 규약: [[03_API/CONTRACT/REST/OPENAPI.yaml.md]], [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]], [[03_API/CONTRACT/REALTIME/TOPICS.md]], [[03_API/CONTRACT/REALTIME/EVENTS.md]], [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

---
## 2. 문서 구조
- `FE_STACK.md`: 기술 스택/런타임/환경 변수 이름 규칙
- `FE_CONVENTIONS.md`: 네이밍/파일 구조/코딩 컨벤션
- `FE_ARCHITECTURE.md`: 모듈 경계/레이어 책임 분리 규칙
- `FE_ROUTING_RULES.md`: 라우팅/가드/전환 구현 패턴
- `FE_STATE_RULES.md`: 상태 분리/스토어 구조/동기화 패턴
- `FE_API_CLIENT.md`: REST 호출 구조/에러 분기 규칙
- `FE_REALTIME_RULES.md`: 실시간 연결/구독 관리 패턴
- `FE_STYLING.md`: 토큰/16:9 스케일/스타일 적용 규칙
- `FE_COMPONENT_RULES.md`: 컴포넌트 API/props/slots 규칙
- `FE_DESIGN_MAPPING.md`: 라우트/상태별 디자인 문서 매핑
- `VIBE_SNIPPETS.md`: 스타일/레이아웃 예시 스니펫 모음
- `ANTI_PATTERNS.md`: 금지 구현 패턴

---
## 3. 변경 원칙
- 정책/흐름 변경은 01_PRODUCT에서 먼저 수정한다.
- 디자인 변경은 02_DESIGN에서 먼저 수정한다.
- API 변경은 03_API에서 먼저 수정한다.
- 프론트 구현 방식 변경은 04_FRONTEND에서만 정의한다.

---
## 4. 환경 변수 목록
| 이름 | 목적 |
|---|---|
| VITE_API_BASE_URL | REST API 기본 경로 |
| VITE_WS_BASE_URL | WebSocket 기본 경로 |
