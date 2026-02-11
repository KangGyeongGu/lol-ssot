## 0. 작업 양식
신규 에러 코드를 추가할 때는 아래 항목을 반드시 기입한다.

```
[코드]
- CODE_NAME

[의미]
- 언제 발생하는가

[HTTP 상태 코드]
- 4xx/5xx

[details.context]
- 포함해야 하는 필드

[영향 범위]
- 관련 엔드포인트
```

---
## 1. 문서 목적
- REST API 표준 에러 포맷과 에러 코드 정의.
- 프론트엔드는 HTTP 상태 코드가 아니라 `error.code`로 분기한다.
- `error.message`는 로그용이며 UI 노출 금지.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

---
## 2. 에러 Envelope
```json
{
  "error": {
    "code": "STRING_ENUM",
    "message": "로그용 설명",
    "details": {}
  },
  "meta": {
    "requestId": "string",
    "serverTime": "2026-01-26T12:34:56Z"
  }
}
```

### 2.1 검증 오류 상세
스키마/필드 검증 실패 시:
```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "...",
    "details": {
      "fieldErrors": [
        { "field": "roomName", "reason": "required" }
      ]
    }
  },
  "meta": { "requestId": "...", "serverTime": "..." }
}
```

---
## 3. HTTP 상태 코드 매핑
| 상태 | 의미 |
|---|---|
| 400 | 요청 검증 실패 |
| 401 | 인증 실패 |
| 403 | 권한 없음 |
| 404 | 리소스 없음 |
| 409 | 상태 충돌 |
| 429 | 요청 제한 |
| 500 | 서버 오류 |

---
## 4. 에러 코드
### 4.1 인증 / 권한
- UNAUTHORIZED
- FORBIDDEN
- NOT_HOST
- KICKED_USER

### 4.2 전역 상태
- ACTIVE_GAME_EXISTS
- INVALID_STAGE_ACTION
- GAME_ALREADY_FINISHED

### 4.3 Room
- ROOM_NOT_FOUND
- ROOM_FULL
- PLAYER_NOT_IN_ROOM
- INVALID_PLAYER_STATE

### 4.4 Game
- GAME_NOT_FOUND

### 4.5 Ban / Pick / Shop
- DUPLICATED_BAN
- DUPLICATED_PICK
- SHOP_PURCHASE_ALREADY_SUBMITTED
- DUPLICATED_ITEM
- DUPLICATED_SPELL
- INSUFFICIENT_COIN
- MAX_ITEM_LIMIT
- MAX_SPELL_LIMIT
- MAX_ITEM_QUANTITY
- MAX_SPELL_QUANTITY

### 4.6 Submission
- SUBMISSION_REJECTED
- INVALID_LANGUAGE

### 4.7 검증 / 서버
- VALIDATION_FAILED
- RATE_LIMITED
- INTERNAL_ERROR

---
## 5. 고정 원칙
- 코드 이름은 변경/삭제하지 않는다.
- 신규 코드 추가 시 반드시 본 문서를 갱신한다.
