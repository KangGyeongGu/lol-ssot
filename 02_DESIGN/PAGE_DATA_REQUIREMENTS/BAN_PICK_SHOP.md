## 목적
- BAN/PICK/SHOP 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/BAN_PICK_SHOP.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]

## Required Data
- game state: stage, remainingMs, coin, inventory
- algorithms catalog (ban/pick 대상)
- items catalog: itemId, name, price, duration, iconKey
- spells catalog: spellId, name, price, duration, iconKey
- room chat messages (channel=INGAME, roomId)

## Required States
- loading (initial)
- stage transition (BAN/PICK/SHOP)
- submit pending
- error (REST/WS)

## Prohibited
- 남은 시간 없이 단계 진행 표시
