**목적**
- 강제 파이프라인(스킬 기반) 설계의 초안 패키지를 보관한다.
- 실제 운영 전 검증/실험 용도로 사용한다.

**범위**
- 포함: 리뷰 마스터/서브에이전트 지침, 스킬 정의
- 제외: 실제 코드 변경

**디렉토리 구조**
```text
AGENTS/CLAUDE/
  README.md # 이 문서
  AGENTS/
    BACKEND/REVIEW/
      MASTER_AGENT.md # BE Review Master 지침
      AUTH_USER_REVIEW_AGENT.md # 인증/유저 리뷰 지침
      ROOM_LOBBY_REVIEW_AGENT.md # 방/로비 리뷰 지침
      GAME_LIFECYCLE_REVIEW_AGENT.md # 게임 라이프사이클 리뷰 지침
      BAN_PICK_SHOP_REVIEW_AGENT.md # 밴/픽/상점 리뷰 지침
      REALTIME_CHAT_REVIEW_AGENT.md # 실시간/채팅 리뷰 지침
      CORE_INFRA_REVIEW_AGENT.md # 코어 인프라 리뷰 지침
      REDIS_REVIEW_AGENT.md # Redis/캐시 리뷰 지침
      JPA_DB_REVIEW_AGENT.md # JPA/DB 성능 리뷰 지침
    BACKEND/DEV/
      BE_DEV_MASTER_AGENT.md # BE Dev Master 지침
      BE_DEV_AUTH_USER_AGENT.md # 인증/유저 Dev 지침
      BE_DEV_ROOM_LOBBY_AGENT.md # 방/로비 Dev 지침
      BE_DEV_GAME_LIFECYCLE_AGENT.md # 게임 라이프사이클 Dev 지침
      BE_DEV_BAN_PICK_SHOP_AGENT.md # 밴/픽/상점 Dev 지침
      BE_DEV_REALTIME_CHAT_AGENT.md # 실시간/채팅 Dev 지침
      BE_DEV_REDIS_AGENT.md # Redis Dev 지침
      BE_DEV_JPA_DB_AGENT.md # JPA/DB Dev 지침
      BE_DEV_CORE_INFRA_AGENT.md # 코어 인프라 Dev 지침
    FRONTEND/REVIEW/
      MASTER_AGENT.md # FE Review Master 지침
      API_REVIEW_AGENT.md # API 연동 리뷰 지침
      STATE_REVIEW_AGENT.md # 상태 관리 리뷰 지침
      ROUTING_REVIEW_AGENT.md # 라우팅 리뷰 지침
      REALTIME_REVIEW_AGENT.md # 실시간 리뷰 지침
      QUALITY_REVIEW_AGENT.md # 품질/성능 리뷰 지침
    FRONTEND/DEV/
      FE_DEV_MASTER_AGENT.md # FE Dev Master 지침
      FE_DEV_API_AGENT.md # API Dev 지침
      FE_DEV_STATE_AGENT.md # 상태 Dev 지침
      FE_DEV_ROUTING_AGENT.md # 라우팅 Dev 지침
      FE_DEV_REALTIME_AGENT.md # 실시간 Dev 지침
      FE_DEV_QUALITY_AGENT.md # 품질/성능 Dev 지침
  SKILLS/
    BACKEND/REVIEW/
      be-review/ # BE 리뷰 파이프라인 진입점
      be-review-auth-user/ # 인증/유저 리뷰 스킬
      be-review-room-lobby/ # 방/로비 리뷰 스킬
      be-review-game-lifecycle/ # 게임 라이프사이클 리뷰 스킬
      be-review-ban-pick-shop/ # 밴/픽/상점 리뷰 스킬
      be-review-realtime/ # 실시간 리뷰 스킬
      be-review-redis/ # Redis 리뷰 스킬
      be-review-jpa-db/ # JPA/DB 성능 리뷰 스킬
      be-review-core-infra/ # 코어 인프라 리뷰 스킬
    BACKEND/DEV/
      be-dev/ # BE Dev 파이프라인 진입점
      be-dev-auth-user/ # 인증/유저 Dev 스킬
      be-dev-room-lobby/ # 방/로비 Dev 스킬
      be-dev-game-lifecycle/ # 게임 라이프사이클 Dev 스킬
      be-dev-ban-pick-shop/ # 밴/픽/상점 Dev 스킬
      be-dev-realtime/ # 실시간 Dev 스킬
      be-dev-redis/ # Redis Dev 스킬
      be-dev-jpa-db/ # JPA/DB Dev 스킬
      be-dev-core-infra/ # 코어 인프라 Dev 스킬
    FRONTEND/REVIEW/
      fe-review/ # FE 리뷰 파이프라인 진입점
      fe-review-api/ # API 리뷰 스킬
      fe-review-state/ # 상태 관리 리뷰 스킬
      fe-review-routing/ # 라우팅 리뷰 스킬
      fe-review-realtime/ # 실시간 리뷰 스킬
      fe-review-quality/ # 품질/성능 리뷰 스킬
    FRONTEND/DEV/
      fe-dev/ # FE Dev 파이프라인 진입점
      fe-dev-api/ # API Dev 스킬
      fe-dev-state/ # 상태 Dev 스킬
      fe-dev-routing/ # 라우팅 Dev 스킬
      fe-dev-realtime/ # 실시간 Dev 스킬
      fe-dev-quality/ # 품질/성능 Dev 스킬
```

**운영 원칙**
- 이 디렉토리는 실험/검증 목적이며, 운영 규칙은 `AGENTS/CLAUDE/`를 기준으로 한다.

**산출물 경로**
- 리뷰/개발 산출물은 SSOT 밖의 `.claude/reports/`에만 작성한다.
