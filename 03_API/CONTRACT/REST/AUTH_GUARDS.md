## 0. 작업 양식
가드 규칙 추가/수정 시 아래 양식으로 기록한다.

```
[가드 목적]
- 왜 필요한가

[적용 대상]
- 엔드포인트 / 조건 / 단계

[실패 응답]
- HTTP Status
- error.code
- details.context

[연관 문서 업데이트]
- OPENAPI.yaml.md
- ERROR_MODEL.md
- API_SUMMARY.md
```

---
## 1. 문서 목적
- REST API 인증/가드 규칙을 정의한다.
- 실시간(WebSocket/STOMP) 가드는 범위 밖이다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]

---
## 2. 인증 필수 규칙 (Global)
- 기본적으로 `/api/v1/**` 모든 요청은 인증이 필요하다.
- 예외(인증 불필요):
  - `POST /auth/kakao/login`
  - `POST /auth/signup`

인증 실패 처리:
- HTTP 401
- error.code = UNAUTHORIZED

---
## 3. Active Game 가드 (Global)
### 3.1 정의
Active Game: 사용자가 현재 참여 중이며 종료되지 않은 게임.

### 3.2 차단 동작
- 새로운 방 생성
- 다른 방 참가

### 3.3 실패 응답
- HTTP 409
- error.code = ACTIVE_GAME_EXISTS
- details.context.activeGameId 권장

---
## 4. 강퇴(Kick) 가드
- 강퇴된 사용자는 같은 방에 재입장 불가(게임 종료까지).
- 실패 응답:
  - HTTP 403
  - error.code = KICKED_USER
  - details.context.roomId 권장

---
## 5. 방장(Host) 권한 가드
### 5.1 방장 전용 기능
- 게임 시작
- 플레이어 강퇴

### 5.2 실패 응답
- HTTP 403
- error.code = NOT_HOST

---
## 6. 대기실 상태 가드
### 6.1 READY 규칙
- 모든 플레이어 READY 상태여야 게임 시작 가능.

### 6.2 실패 응답
- HTTP 409
- error.code = INVALID_PLAYER_STATE

---
## 7. 단계(Stage) 가드
명령은 허용된 stage에서만 가능하다.
- BAN → `/games/{gameId}/ban`
- PICK → `/games/{gameId}/pick`
- SHOP → `/games/{gameId}/shop/purchase`
- PLAY → `/games/{gameId}/submissions`

실패 응답:
- HTTP 409
- error.code = INVALID_STAGE_ACTION

---
## 8. 고정 원칙
- 서버가 단일 기준(authoritative)으로 가드를 판단한다.
- 프론트엔드는 가드를 추론하지 않고 응답에 반응한다.
