# League of Algo Logic SSOT
----

이 레포지토리는 프로젝트 전 과정(설계·명세·개발)의 단일 진실 공급원(SSOT) 역할의 중앙 명세 저장소입니다. 모든 명세 및 설계는 SSOT에서 중앙 관리하며, 각 작업 도메인에서의 독자적인 명세 변경 또는 명세 정합성에 위배되는 수정을 제한합니다. 각 작업 도메인은 이 SSOT를 기준으로만 작업을 수행합니다.

각 명세는 해당하는 단일 소스에만 작성합니다. 중복 내용을 관련 도메인의 여러 파일에 분산 중복 작성하는 대신, 각 명세 간 Obsidian 위키링크 참조 형식으로 파일 간 연관 및 의존성을 작성하여 명세 중복 및 불일치를 최소화하도록 운용합니다.

각 작업 도메인별 AI AGENT는 CLAUDE CODE SUB AGENTS 및 SKILLS 시스템을 사용합니다. 각 SUB AGENT는 SSOT 명세를 기반 지침으로 활용하므로 SSOT 문서 내에서 파일 참조 누락 또는 명세 중복 작성이 발생하지 않도록 주의합니다.

----
## 1. SSOT
### 1.1. SSOT STRUCTURE
```markdown
.
├── 01_PRODUCT/            요구사항, 유저 플로우, 정책
├── 02_DESIGN/             디자인 규칙/토큰/페이지 요구사항
├── 03_API/                REST/실시간 계약 및 페이지 맵
├── 04_DOMAIN/             데이터 모델 및 DB 규칙
├── 05_FRONTEND/           프론트엔드 컨벤션/패턴/설계
├── 06_BACKEND/            백엔드 컨벤션/패턴/설계
├── AGENTS/                AI AGENT 관련 설계 및 구현체
├── 11_LOL_WEB_MOCKUP_BEFORE/  과거 웹 목업
└── README.md              프로젝트 소개 및 사용 가이드
```

### 1.2. SSOT 명세 작성 원칙
- 프로젝트 구조·설계·명세·기능 변경/수정/삭제 등 모든 변경은 SSOT 문서에서 가장 먼저 수행되어야 합니다.
- 모든 명세는 각 단일 문서에만 작성되어야 하며, 여러 문서에 걸친 중복 작성을 허용하지 않습니다.
- 연관 문서 간 참조는 Obsidian 위키링크 형식으로 명시하며, 연관 기준은 각 명세 목적 일치 또는 작업 도메인 연관성 유무에 따라 판단합니다.

---
## 2. AI AGENT 가이드라인
> 모든 AI AGENT는 SSOT 명세 기반 지침을 바탕으로 작업을 수행하며, 명세 범위를 벗어난 llm의 자율적인 작업 영역이 발생하지 않도록 제한합니다.
### 2.1. 프로젝트 Submodule 연결
>`docs`는 **참조 전용**으로 사용되며, `docs`에 수정 작업이 발생하지 않도록 주의합니다.
1. 프로젝트 저장소에서 SSOT를 `docs`로 추가합니다.
```bash
git submodule add https://github.com/KangGyeongGu/lol-ssot.git docs
git submodule update --init --recursive
```
2. SSOT 갱신 시 submodule 또한 최신 버전으로 갱신합니다.
```bash
git submodule update --remote --merge
```
### 2.2. AGENTS & SKILLS 설계 및 구현 원칙
> AGENTS 및 SKILLS 구조 및 사용 가이드라인 관련 설명은 [README](AGENTS/CLAUDE/README)를 참조합니다.
1. 에이전트는 역할·제약·언어 규칙·참조 SSOT 문서 링크만 포함해야 합니다.
	- 에이전트 지침이 지나치게 비대해지지 않도록 주의합니다.
	- 사용자가 의도하지 않은 (llm 자율 추론) 작업이 발생하지 않도록, 하나의 에이전트의 작업 단위를 명확히 한정합니다.
2. SKILL은 workflows만 정의하며, frontmatter를 통해 작업을 위한 sub agent를 `fork()`하도록 설정합니다.
---
## 3. GIT CONVENTION
### 3.1. 커밋 컨벤션
> 메시지 형식은 `영역: 요약`을 사용합니다. 예: `docs: 서브에이전트 가이드 정비`

### 3.2. SSOT Partial Commit Convention
> Partial Review Agents & Skills 워크플로우를 위한 Git SSOT 커스텀 컨벤션을 사용합니다. 자세한 설명은 [README Partial Agents&Skills](AGENTS/CLAUDE/README#L323)를 참조합니다.
```markdown
ssot(<domain>): <action> <summary>
ssot: <action> <summary>
```
- `ssot(`로 시작하지 않으면 자동 감지 대상에서 제외합니다.
- `<domain>`은 선택 사항입니다. 생략 시 도메인 확인을 요청합니다.
- 다중 도메인은 `ssot(be-auth,be-redis): ...` 형식으로 표기합니다.
