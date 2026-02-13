**목적**
- 프론트엔드 구현 규칙/패턴/컨벤션의 단일 진실(SSOT)을 정의한다.
- UI 레이아웃/시각 디자인 자체는 범위에서 제외한다.

**범위**
- 포함: 명세 정합성 기준(SPEC), 코드 품질 기준(QUALITY), 디자인/메시지 참조 문서
- 제외: 화면 레이아웃/컴포넌트 배치, 디자인 목업

**파일 구조**
```text
05_FRONTEND/
  README.md # 이 문서
  REVIEW_REFERENCE_MAP.md # 도메인별 SSOT/QUALITY 참조 맵
  SPEC/ # FE 정합성(명세) 기준
    FE_ARCHITECTURE.md # 레이어 경계/모듈 책임 규칙
    FE_API_CLIENT.md # REST 호출/에러 처리 규칙
    FE_STATE_RULES.md # 상태 분리/스토어 구조 규칙
    FE_ROUTING_RULES.md # 라우팅/가드/전환 규칙
    FE_REALTIME_RULES.md # 실시간 구독/연결 규칙
    RULE_INDEX.md # FE-S-* 룰 ID 인덱스
  QUALITY/ # FE 코드 품질 기준
    FE_CONVENTIONS.md # 네이밍/구조/유닛 규칙
    FE_COMPONENT_RULES.md # 컴포넌트 API 설계 품질 규칙
    FE_STYLING.md # --gu 스케일/토큰 적용 규칙
    FE_STACK.md # 프론트 기술 스택 고정값
    ANTI_PATTERNS.md # 금지 패턴 목록
  FE_DESIGN_MAPPING.md # 라우트→페이지 데이터 요구사항 매핑
  FE_NOTIFICATION_MESSAGES.md # UX 메시지/알림 문구 정책
  VIBE_SNIPPETS.md # 스타일 적용 예시 스니펫
```

**관련 SSOT**
- 디자인 토큰/페이지 데이터 요구사항: `02_DESIGN/`
- API 계약/페이지 맵: `03_API/`
- 제품 요구사항/카피: `01_PRODUCT/`

**변경 원칙**
- 프론트 구현 규칙 변경은 `05_FRONTEND/`에서만 정의한다.
