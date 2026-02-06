# BACKEND_AGENTS_TEMPLATES

## 0. 문서 목적
- 이 디렉토리는 Claude Code 서브에이전트 템플릿을 제공한다.
- 실제 실행 파일은 백엔드 레포의 `.claude/`에 복사한다.

## 관련 문서
- [[05_BACKEND/BE_AGENT_SPLIT.md]]
- [[05_BACKEND/BE_ARCHITECTURE.md]]
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_STACK.md]]
- [[05_BACKEND/BE_TEST_RULES.md]]

---
## 1. 사용 규칙
- 템플릿을 `.claude/`로 복사한 후, 참조 경로를 실제 환경에 맞게 조정한다.
- `LEAGUE_SPEC_ROOT` 절대 경로를 상단에 명시한다.
- 모든 에이전트는 본인의 소유 디렉토리만 수정한다.
- 기술 스택의 단일 진실은 [[05_BACKEND/BE_STACK.md]]이며 중복 정의하지 않는다.

---
## 2. 템플릿 필수 구성
- 역할/전문성 요약(예: DB 전문가, 실시간 전문가)
- 책임/범위(무엇을 담당하고 무엇을 담당하지 않는가)
- 기술 스택 고정(스택은 고정이고 변경 불가, 상세는 [[05_BACKEND/BE_STACK.md]] 참고)
- 필수 참조 목록(설계/계약 문서)
- 컨벤션(필수 규칙)
- 안티패턴/금지 사항
- 소유 디렉토리 범위
- 출력 규칙(수정 파일, 테스트 여부 보고)
