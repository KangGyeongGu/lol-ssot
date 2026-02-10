**목적**
- REST/실시간 계약과 페이지 맵의 단일 진실(SSOT)을 정의한다.
- 프론트/백엔드 구현은 반드시 이 계약을 기준으로 한다.

**범위**
- 포함: OpenAPI, REST 규약, 실시간 규약, 페이지별 계약 매핑, 라이프사이클
- 제외: 구현 코드, DB 모델 세부 설계

**파일 구조**
```text
03_API/
  README.md # 이 문서
  LIFECYCLE.md # 로그인/복귀/게임 진행 흐름 기준
  CONTRACT/
    REST/
      API_SUMMARY.md # REST API 요약
      AUTH_GUARDS.md # 인증/인가 가드 규칙
      CONVENTIONS.md # REST 공통 규약
      ERROR_MODEL.md # 에러 모델 규칙
      OPENAPI.yaml.md # REST API 스키마(OpenAPI)
    REALTIME/
      COMMANDS.md # 커맨드 정의
      CONVENTIONS.md # 실시간 메시지 규약
      EVENTS.md # 이벤트 타입 정의
      TOPICS.md # 구독 토픽 정의
  PAGE_MAP/
    BAN_PICK_SHOP.md # BAN/PICK/SHOP 페이지 REST/WS 매핑
    IN_GAME.md # IN_GAME 페이지 REST/WS 매핑
    MAIN.md # MAIN 페이지 REST/WS 매핑
    MY_PAGE.md # MY_PAGE 페이지 REST 매핑
    RESULT.md # RESULT 페이지 REST/WS 매핑
    ROOM_LIST.md # ROOM_LIST 상태 REST/WS 매핑
    SIGNUP.md # SIGNUP 흐름 REST 매핑
    WAITING_ROOM.md # WAITING_ROOM 페이지 REST/WS 매핑
    WELCOME.md # WELCOME(로그인) REST 매핑
```

**변경 원칙**
- API 계약 변경은 `03_API/`에서 먼저 수정한다.
- 구현 문서는 이 계약을 재정의하지 않는다.
