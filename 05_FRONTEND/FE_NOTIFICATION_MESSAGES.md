## 목적
- 알림 컴포넌트에서 사용하는 메시지 키와 한국어 문구를 단일 문서로 정의한다.
- 에러 알림은 `ERROR.<CODE>` 키를 사용한다.
- 이벤트/시스템 알림은 `NOTICE.*` 키를 사용한다.

## 관련 문서
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]

---
## 1. 기본 규칙
- 모든 알림은 `messageKey`로 렌더링한다.
- `messageKey`는 문서에 정의된 값만 사용한다.
- 미정의 키 수신 시 `ERROR.UNKNOWN`을 사용한다.

---
## 2. ERROR 매핑 (error.code → messageKey → ko)
| error.code                      | messageKey                            | ko                          |
| ------------------------------- | ------------------------------------- | --------------------------- |
| UNAUTHORIZED                    | ERROR.UNAUTHORIZED                    | 로그인이 필요합니다.                 |
| FORBIDDEN                       | ERROR.FORBIDDEN                       | 권한이 없습니다.                   |
| NOT_HOST                        | ERROR.NOT_HOST                        | 방장만 사용할 수 있습니다.             |
| KICKED_USER                     | ERROR.KICKED_USER                     | 강퇴되어 해당 방에 입장할 수 없습니다.      |
| ACTIVE_GAME_EXISTS              | ERROR.ACTIVE_GAME_EXISTS              | 이미 진행 중인 게임이 있습니다.          |
| INVALID_STAGE_ACTION            | ERROR.INVALID_STAGE_ACTION            | 현재 단계에서는 사용할 수 없습니다.        |
| GAME_ALREADY_FINISHED           | ERROR.GAME_ALREADY_FINISHED           | 이미 종료된 게임입니다.               |
| ROOM_NOT_FOUND                  | ERROR.ROOM_NOT_FOUND                  | 방을 찾을 수 없습니다.               |
| ROOM_FULL                       | ERROR.ROOM_FULL                       | 방이 가득 찼습니다.                 |
| PLAYER_NOT_IN_ROOM              | ERROR.PLAYER_NOT_IN_ROOM              | 해당 방의 플레이어가 아닙니다.           |
| INVALID_PLAYER_STATE            | ERROR.INVALID_PLAYER_STATE            | 현재 상태에서는 사용할 수 없습니다.        |
| GAME_NOT_FOUND                  | ERROR.GAME_NOT_FOUND                  | 게임을 찾을 수 없습니다.              |
| DUPLICATED_BAN                  | ERROR.DUPLICATED_BAN                  | 이미 밴을 제출했습니다.               |
| DUPLICATED_PICK                 | ERROR.DUPLICATED_PICK                 | 이미 픽을 제출했습니다.               |
| SHOP_PURCHASE_ALREADY_SUBMITTED | ERROR.SHOP_PURCHASE_ALREADY_SUBMITTED | 이미 구매를 완료했습니다.              |
| DUPLICATED_ITEM                 | ERROR.DUPLICATED_ITEM                 | 동일 아이템이 중복되었습니다.            |
| DUPLICATED_SPELL                | ERROR.DUPLICATED_SPELL                | 동일 스펠이 중복되었습니다.             |
| INSUFFICIENT_COIN               | ERROR.INSUFFICIENT_COIN               | 코인이 부족합니다.                  |
| MAX_ITEM_LIMIT                  | ERROR.MAX_ITEM_LIMIT                  | 아이템 종류 최대 수량을 초과했습니다.       |
| MAX_SPELL_LIMIT                 | ERROR.MAX_SPELL_LIMIT                 | 스펠 종류 최대 수량을 초과했습니다.        |
| MAX_ITEM_QUANTITY               | ERROR.MAX_ITEM_QUANTITY               | 아이템 개별 수량 제한을 초과했습니다.       |
| MAX_SPELL_QUANTITY              | ERROR.MAX_SPELL_QUANTITY              | 스펠 개별 수량 제한을 초과했습니다.        |
| SUBMISSION_REJECTED             | ERROR.SUBMISSION_REJECTED             | 제출이 거부되었습니다.                |
| INVALID_LANGUAGE                | ERROR.INVALID_LANGUAGE                | 지원하지 않는 언어입니다.              |
| VALIDATION_FAILED               | ERROR.VALIDATION_FAILED               | 입력값이 올바르지 않습니다.             |
| RATE_LIMITED                    | ERROR.RATE_LIMITED                    | 요청이 너무 많습니다. 잠시 후 다시 시도하세요. |
| INTERNAL_ERROR                  | ERROR.INTERNAL_ERROR                  | 서버 오류가 발생했습니다.              |
| UNKNOWN                         | ERROR.UNKNOWN                         | 알 수 없는 오류가 발생했습니다.          |

---
## 3. NOTICE 매핑 (이벤트 → messageKey → ko)
| trigger | messageKey | ko |
|---|---|---|
| ROOM_HOST_CHANGED (reason=MANUAL, toUserId=me) | NOTICE.HOST_TRANSFERRED | 방장을 위임받았습니다. |
| ROOM_HOST_CHANGED (reason=SYSTEM/LEAVE, toUserId=me) | NOTICE.HOST_ASSIGNED | 방장으로 지정되었습니다. |
| ROOM_KICKED | NOTICE.KICKED | 방에서 강퇴되었습니다. |
