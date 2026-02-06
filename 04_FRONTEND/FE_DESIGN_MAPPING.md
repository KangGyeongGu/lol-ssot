# FE_DESIGN_MAPPING

## 0. 문서 목적
- 라우트/상태별로 반드시 참조해야 할 디자인 문서를 매핑한다.
- 프론트 구현은 아래 매핑 문서를 **필수로 참조**해야 한다.

## 관련 문서
- [[01_PRODUCT/USER_FLOWS.md]]
- [[02_DESIGN/DESIGN_RULES.md]]
- [[02_DESIGN/LAYOUT_RULES.md]]
- [[02_DESIGN/TOKENS.json.md]]
- [[02_DESIGN/COMPONENTS.json.md]]
- [[04_FRONTEND/FE_ROUTING_RULES.md]]

---
## 1. 페이지 매핑 (Route → Design Page)
| Route | Design Page | 비고 |
|---|---|---|
| WELCOME | [[02_DESIGN/PAGES/LOGIN.md]] | 로그인 화면
| MAIN | [[02_DESIGN/PAGES/MAIN.md]] | 메인 대시보드
| WAITING_ROOM | [[02_DESIGN/PAGES/WAITING_ROOM.md]] | 대기실
| BAN_PICK_SHOP | [[02_DESIGN/PAGES/BAN_PICK_SHOP.md]] | 랭크 전용 단계
| IN_GAME | [[02_DESIGN/PAGES/IN_GAME.md]] | 인게임
| RESULT | [[02_DESIGN/PAGES/RESULT.md]] | 결과
| MY_PAGE | [[02_DESIGN/PAGES/MY_PAGE.md]] | 마이페이지

---
## 2. 오버레이/패널 매핑
| 상태 | Design Doc | 적용 범위 |
|---|---|---|
| SIGNUP Overlay | [[02_DESIGN/OVERLAYS/SIGNUP_MODAL.md]] | WELCOME 위 오버레이
| ROOM_CREATE Modal | [[02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md]] | MAIN에서 방 생성 클릭 시
| ROOM_LIST Panel | [[02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md]] | MAIN 헤더 하단 교체 상태

---
## 3. 적용 규칙
- 각 라우트/상태는 매핑된 디자인 문서를 **필수로 참조**해야 한다.
- 레이아웃 좌표/구성 요소는 디자인 문서 기준을 따른다.
- 디자인 문서에 없는 UI 임의 추가 금지.
