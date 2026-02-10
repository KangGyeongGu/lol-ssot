**목적**
- Claude Code 서브에이전트 정의의 단일 진실(SSOT)을 제공한다.
- 실제 실행 파일은 각 코드 레포의 `.claude/agents`로 복사하여 사용한다.

**범위**
- 포함: FE/BE Dev/Review 에이전트 템플릿
- 제외: 실제 코드 실행 결과/로그

**디렉토리 구조**
```text
07_AGENTS/
  README.md # 이 문서
  FRONTEND/
    DEV/
      MASTER_AGENT.md # FE Dev Master 오케스트레이션
      API_AGENT.md # API 연동/DTO 매핑
      STATE_AGENT.md # 상태 관리/스토어 규칙
      ROUTING_AGENT.md # 라우팅/가드 규칙
      REALTIME_AGENT.md # 실시간/소켓 규칙
      PERF_RELIABILITY_AGENT.md # 성능/안정성 개선
    REVIEW/
      MASTER_AGENT.md # FE Review Master 오케스트레이션
      API_REVIEW_AGENT.md # API 연동 리뷰
      STATE_REVIEW_AGENT.md # 상태 관리 리뷰
      ROUTING_REVIEW_AGENT.md # 라우팅/가드 리뷰
      REALTIME_REVIEW_AGENT.md # 실시간 리뷰
      QUALITY_REVIEW_AGENT.md # 품질/회귀/성능 리뷰
  BACKEND/
    DEV/
      MASTER_AGENT.md # BE Dev Master 오케스트레이션
      AUTH_USER_AGENT.md # 인증/유저 도메인
      ROOM_LOBBY_AGENT.md # 방/로비 도메인
      GAME_LIFECYCLE_AGENT.md # 게임 라이프사이클
      BAN_PICK_SHOP_AGENT.md # 밴/픽/상점 도메인
      REALTIME_CHAT_AGENT.md # 실시간/채팅
      CORE_INFRA_AGENT.md # 코어 인프라/공통
      REDIS_AGENT.md # Redis/캐시/퍼브섭
    REVIEW/
      MASTER_AGENT.md # BE Review Master 오케스트레이션
      AUTH_USER_REVIEW_AGENT.md # 인증/유저 도메인 리뷰
      ROOM_LOBBY_REVIEW_AGENT.md # 방/로비 도메인 리뷰
      GAME_LIFECYCLE_REVIEW_AGENT.md # 게임 라이프사이클 리뷰
      BAN_PICK_SHOP_REVIEW_AGENT.md # 밴/픽/상점 리뷰
      REALTIME_CHAT_REVIEW_AGENT.md # 실시간/채팅 리뷰
      CORE_INFRA_REVIEW_AGENT.md # 코어 인프라 리뷰
      REDIS_REVIEW_AGENT.md # Redis/캐시 리뷰
      JPA_DB_REVIEW_AGENT.md # JPA/DB 성능 리뷰
```

**사용 원칙**
- Dev/Review는 분리 운용한다.
- Master는 오케스트레이션만 수행한다.
