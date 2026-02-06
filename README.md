# League of Algo Logic SSOT

League of Algo Logic 프로젝트의 **단일 진실(SSOT)** 저장소입니다. 제품/디자인/API/도메인/구현 규칙을 문서로 정의하며, AI 서브에이전트가 참조하는 기준입니다.

**Overview**
- 이 저장소는 **명세/규칙/패턴**을 정의합니다.
- 애플리케이션 코드 저장소가 아닙니다.
- 모든 문서는 Obsidian 위키링크로 연결됩니다.

**Scope**
- 포함: 제품 요구사항, 사용자 흐름, 디자인 규칙, API 계약, 데이터 모델, FE/BE 규칙, QA 기준
- 제외: 실제 서비스 코드, 배포 설정, 운영 스크립트

**Directory Tree**
```text
00_START/          작업 시작/결정 기록
01_PRODUCT/        요구사항, 유저 플로우, 정책
02_DESIGN/         디자인 규칙/토큰/페이지 레이아웃
03_API/            REST/실시간 계약 및 페이지 맵
03_DOMAIN/         데이터 모델 및 DB 규칙
04_FRONTEND/       프론트엔드 컨벤션/패턴/설계
05_BACKEND/        백엔드 컨벤션/패턴/에이전트 템플릿
06_QA/             테스트 및 품질 기준
CODEX_AGENTS/      검증용 에이전트 정의 및 로그
```

**Workflow**
- Obsidian에서 이 저장소를 열고 `00_START`부터 확인합니다.
- 변경은 항상 단일 진실 문서부터 수행합니다.

**Submodule Setup**
ai subagents 사용 시, 이 SSOT를 각 프로젝트에서 Git submodule로 연결해 사용합니다.

1. 프로젝트 저장소에서 SSOT를 `docs`로 추가합니다.
```bash
git submodule add https://github.com/KangGyeongGu/lol-ssot.git docs
git submodule update --init --recursive
```
2. SSOT 문서 업데이트가 필요하면 submodule을 갱신합니다.
```bash
git submodule update --remote --merge
```
3. `.claude/agents`에서 문서를 참조할 때는 `../docs/` 접두를 붙여 해석합니다.
4. `docs`는 **참조 전용**이며, 구현 코드 저장소에서 SSOT 문서를 직접 수정하지 않도록 주의합니다.

**AI Subagents**
- 서브에이전트는 이 SSOT를 **참조 전용**으로 사용합니다.
- 실제 실행 에이전트는 각 코드 레포의 `.claude/agents`에 둡니다.
- 프론트엔드 규칙은 `04_FRONTEND`, 백엔드 규칙은 `05_BACKEND`에 있습니다.

**Obsidian Rules**
- 모든 문서 참조는 obsidian 위키링크 형식을 사용합니다: `[[path/to/file.md]]`.
- 파생 문서는 단일 진실을 재정의하지 않고 링크만 둡니다.

**Change Policy**
- 제품/정책 변경: `01_PRODUCT`에서 먼저 수정
- 디자인 변경: `02_DESIGN`에서 먼저 수정
- API 변경: `03_API`에서 먼저 수정
- 도메인/DB 변경: `03_DOMAIN`에서 먼저 수정
- FE/BE 구현 규칙 변경: `04_FRONTEND`, `05_BACKEND`
