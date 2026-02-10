## 0. 작업 양식
아래 양식으로 변경 내용을 기록하고, 연관 문서를 함께 갱신한다.

```
[변경 목적]
- 무엇을 왜 바꾸는가

[변경 내용]
- 규칙/정책/포맷 변경 요약

[연관 문서 업데이트]
- OPENAPI.yaml.md
- ERROR_MODEL.md
- AUTH_GUARDS.md
- API_SUMMARY.md

[검토 체크리스트]
- 규칙 충돌 없음
- 예시 최신화
- OpenAPI/요약 동기화
```

---
## 1. 문서 목적
- LoL 프로젝트 REST API 전역 규칙을 정의한다.
- 이 문서 + OPENAPI.yaml.md가 REST 계약의 단일 진실이다.
- 실시간(WebSocket/STOMP)은 범위 밖이다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]
- [[03_API/CONTRACT/REST/AUTH_GUARDS.md]]

---
## 2. 기본 규칙
### 2.1 기본 경로
- 모든 REST API는 `/api/v1` prefix를 사용한다.

### 2.2 Content-Type
- Request: `application/json`
- Response: `application/json; charset=utf-8`

### 2.3 Time Format / Sync
- 모든 시간 값은 ISO-8601 UTC 문자열을 사용한다.
- `meta.serverTime`가 모든 타이머 동기화 기준이다.

### 2.4 Auth
- 원칙: `/api/v1/**`는 인증 필요
- 예외(인증 불필요):
  - `POST /auth/kakao/login`
  - `POST /auth/signup`

---
## 3. 네이밍 규칙
### 3.1 Resource Path
- 리소스는 복수형 명사: `/rooms`, `/games`, `/users`
- 소문자만 사용한다.
- 경로 세그먼트는 `kebab-case`를 허용하며(`active-game`, `algorithm-pick-ban-rates`), 카멜케이스는 금지한다.

### 3.2 Query Parameter
- query parameter는 `camelCase`를 사용한다.

---
## 4. HTTP 메서드 규칙
| 메서드 | 용도 |
|---|---|
| GET | 스냅샷 조회 |
| POST | 생성 또는 명령 |
| PATCH | 부분 상태 변경(드묾) |

- PUT / DELETE는 사용하지 않는다.

---
## 5. 응답 Envelope
### 5.1 Success
```json
{
  "data": {},
  "meta": {
    "requestId": "string",
    "serverTime": "2026-01-26T12:34:56Z"
  }
}
```

### 5.2 목록 + 커서 페이징
```json
{
  "data": {
    "items": [],
    "page": {
      "limit": 20,
      "nextCursor": "string|null"
    }
  },
  "meta": {
    "requestId": "string",
    "serverTime": "2026-01-26T12:34:56Z"
  }
}
```

### 5.3 Error
- ERROR_MODEL.md에 정의된 형식을 따른다.

### 5.4 Room List Version
- `GET /rooms` 응답(`PagedRoomList`)에는 `listVersion`을 포함한다.
- `listVersion`은 ROOM_LIST 실시간 델타 동기화 기준값으로 사용한다.

---
## 6. ID / 타입 규칙
- 모든 식별자는 문자열: `userId`, `roomId`, `gameId`, `algorithmId`, `itemId`, `spellId`.
- Enum은 UPPER_SNAKE_CASE 문자열을 사용한다.

---
## 7. 핵심 Enum
### 7.1 GameType
- `NORMAL`
- `RANKED`

### 7.2 PlayerState (Lobby)
- `READY`
- `UNREADY`
- `DISCONNECTED`

### 7.3 GameStage (Authoritative)
- `LOBBY` (대기실)
- `BAN`
- `PICK`
- `SHOP`
- `PLAY` (인게임)
- `FINISHED`

### 7.4 PageRoute (Frontend 매핑)
PageRoute는 프론트 라우팅 식별자이며, 상세 매핑은 PAGE_MAP에서 정의한다.
Active game 응답에는 `stage`와 `pageRoute`를 함께 제공한다.
PageRoute 값은 다음 3개만 사용한다.
- `WAITING_ROOM`
- `BAN_PICK_SHOP`
- `IN_GAME`
게임이 FINISHED로 종료되면 active game 응답은 null이며 결과 페이지로 강제 복귀하지 않는다.

---
## 8. 상태 코드 규칙
- 200 OK: 성공(명령 포함)
- 400: 요청 검증 실패
- 401: 인증 실패 (UNAUTHORIZED)
- 403: 권한 없음 (NOT_HOST, KICKED_USER)
- 404: 리소스 없음
- 409: 상태 충돌
- 429: 요청 제한 초과
- 500: 서버 내부 오류

---
## 9. 409 Conflict 규칙
아래 조건 중 하나라도 만족하면 409를 반환한다.
- active game 존재 상태에서 다른 방 생성/참가 시도
- stage 불일치 액션 요청
- 이미 종료된 게임에 액션 요청
- READY 규칙 위반

---
## 10. REST vs 실시간
- REST는 스냅샷 + 명령만 담당한다.
- 채팅/단계 전환 알림/아이템 효과는 실시간에서 정의한다.
