## 목적
- BAN/PICK/SHOP 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/BAN_PICK_SHOP.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- game state: stage, remainingMs, coin, inventory
- finalBanAlgorithmId (PICK 단계 선택 불가 처리용)
- finalAlgorithmId (최종 PICK 결과, SHOP 이후 참고)
- algorithms catalog (ban/pick 대상)
- items catalog: itemId, name, price, duration, iconKey
- spells catalog: spellId, name, price, duration, iconKey
- room chat messages (channel=INGAME, roomId)

## Required States
- loading (initial)
- stage transition (BAN/PICK/SHOP)
- submit pending
- purchase completed (재구매 불가 UI)
- error (REST/WS)

## Interactions
- GAME_BAN_SUBMITTED / GAME_PICK_SUBMITTED 수신 시 해당 플레이어 슬롯 테두리를 선택 완료 강조로 표시한다.
- 미선택 상태 플레이어 슬롯은 옅은 테두리로 표시한다.
- 단계 전환 시 선택 완료 강조 상태는 초기화한다.
- GAME_BAN_FINALIZED 수신 이후 PICK 단계에서 최종 BAN 알고리즘을 선택 불가 처리한다(별도 알림 없음).
- BAN/PICK 제출 실패 시 알림 컴포넌트로 사유를 표시한다(error.code: DUPLICATED_BAN, DUPLICATED_PICK, INVALID_STAGE_ACTION, GAME_ALREADY_FINISHED, GAME_NOT_FOUND, VALIDATION_FAILED, UNAUTHORIZED).
- SHOP 구매 성공 후 구매 UI는 비활성화한다(본인 구매 성공 기준, 재구매 불가).
- SHOP 재요청 또는 구매 실패 시 알림 컴포넌트로 사유를 표시한다(error.code: SHOP_PURCHASE_ALREADY_SUBMITTED, INSUFFICIENT_COIN, MAX_ITEM_LIMIT, MAX_SPELL_LIMIT, MAX_ITEM_QUANTITY, MAX_SPELL_QUANTITY, DUPLICATED_ITEM, DUPLICATED_SPELL, INVALID_STAGE_ACTION, GAME_ALREADY_FINISHED, GAME_NOT_FOUND, VALIDATION_FAILED, UNAUTHORIZED).
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- 남은 시간 없이 단계 진행 표시
