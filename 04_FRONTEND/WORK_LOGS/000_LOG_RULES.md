# WORK_LOGS 운용 설계안

## 1. 개요
프로젝트 개발 내역을 체계적으로 기록하고, AI 인터랙션 세션이 종료되어도 문맥을 유지하기 위한 로그 시스템 설계입니다.

## 2. 디렉토리 구조
작업 로그는 `04_frontend/WORK_LOGS/` 하위에 저장하며, 각 작업 단위별로 **별도의 디렉토리**를 생성하여 격리합니다.

```
04_frontend/
└── WORK_LOGS/
    ├── 000_INDEX.md                    # [Index] 전체 작업 목록 및 상태 요약
    ├── 000_LOG_RULES.md                # [Rule] 로그 작성 규칙 (본 문서)
    │
    ├── 001_Project_Initialization/     # [Unit] 작업 단위 디렉토리
    │   ├── 1_PLAN.md                   # - 구현 계획 (Plan)
    │   ├── 2_TASK.md                   # - 작업 체크리스트 (Current Status)
    │   └── 3_REPORT.md                 # - 완료 보고 및 검증 결과 (Result)
    │
    └── 002_Auth_Feature/               # 순차적 넘버링으로 정렬
        ├── 1_PLAN.md
        └── ...
```

## 3. 파일 명명 및 역할 규칙

### 3.1. 작업 디렉토리 (`XXX_Description`)
- **형식**: `[순번 3자리]_[간략한_작업명]`
  - 예: `001_Setup`, `002_LoginUI`, `003_Refactor_Router`
- **목적**: 파일 탐색기에서 시간 순서대로 정렬되어 히스토리 파악 용이.

### 3.2. 내부 관리 파일
각 작업 디렉토리 내부에는 다음 3가지 파일을 표준으로 둡니다.

| 파일명 | 역할 | 매핑되는 AI Artifact |
|---|---|---|
| **1_PLAN.md** | 작업 목표, 변경 범위, 검증 계획 | `implementation_plan.md` |
| **2_TASK.md** | 상세 체크리스트, 진행 상황 마킹 | `task.md` |
| **3_REPORT.md** | 작업 결과, 트러블슈팅, 스크린샷 | `walkthrough.md` |

> **참고**: 필요 시 `4_CONTEXT.md` 등을 추가하여 프롬프트 컨텍스트나 참고 자료를 저장할 수 있습니다.

## 4. 인덱스 관리 (`000_INDEX.md`)
새로운 작업을 시작하거나 완료할 때마다 루트의 인덱스 파일을 업데이트하여 전체 현황을 한눈에 파악합니다.

**예시:**
```markdown
## Work Log Index

| ID | 작업명 | 상태 | 생성일 | 완료일 |
|---|---|---|---|---|
| 001 | Frontend Feasibility Analysis | ✅ Done | 2024-02-05 | 2024-02-05 |
| 002 | Project Scaffolding | 🚧 In Progress | 2024-02-05 | - |
```

## 5. 워크플로우 제안
1. **작업 시작**: `WORK_LOGS`에 다음 순번 디렉토리 생성 (예: `002_Scaffolding`)
2. **계획 수립**: `1_PLAN.md` 작성 및 사용자 승인
3. **진행**: `2_TASK.md` 체크리스트 업데이트하며 코딩 진행
4. **완료**: `3_REPORT.md` 작성 후 `000_INDEX.md` 업데이트

---
이 설계안대로 진행할 경우, 현재 진행했던 **타당성 검토(Feasibility Analysis)** 작업부터 `001_Feasibility_Check` 디렉토리로 마이그레이션하여 기록을 시작하게 됩니다.
