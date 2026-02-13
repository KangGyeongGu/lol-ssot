## 0. 문서 목적
- 라우트/상태별로 반드시 참조해야 할 **페이지 데이터 요구사항** 문서를 매핑한다.
- 프론트 구현은 아래 매핑 문서를 **필수로 참조**해야 한다.

## 관련 문서
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/COLOR_SYSTEM.md]]
- [[02_DESIGN/TYPOGRAPHY_SYSTEM.md]]
- [[05_FRONTEND/SPEC/FE_ROUTING_RULES.md]]

---
## 1. 페이지 매핑 (Route → Data Requirements)
| Route | Data Requirements | 비고 |
|---|---|---|
| WELCOME | [[02_DESIGN/PAGE_REQUIREMENTS/LOGIN.md]] | 로그인/인증 진입
| MAIN | [[02_DESIGN/PAGE_REQUIREMENTS/MAIN.md]] | 메인 대시보드
| ROOM_LIST | [[02_DESIGN/PAGE_REQUIREMENTS/ROOM_LIST.md]] | MAIN 내 패널 상태
| WAITING_ROOM | [[02_DESIGN/PAGE_REQUIREMENTS/WAITING_ROOM.md]] | 대기실
| BAN_PICK_SHOP | [[02_DESIGN/PAGE_REQUIREMENTS/BAN_PICK_SHOP.md]] | 랭크 전용 단계
| IN_GAME | [[02_DESIGN/PAGE_REQUIREMENTS/IN_GAME.md]] | 인게임
| RESULT | [[02_DESIGN/PAGE_REQUIREMENTS/RESULT.md]] | 결과
| MY_PAGE | [[02_DESIGN/PAGE_REQUIREMENTS/MY_PAGE.md]] | 마이페이지

---
## 2. 적용 규칙
- 각 라우트/상태는 매핑된 데이터 요구사항 문서를 **필수로 참조**해야 한다.
- 데이터 요구사항에 없는 필드는 화면에 노출하지 않는다.
- 요구된 데이터/상태가 누락되면 해당 화면을 완료 상태로 표시하지 않는다.
