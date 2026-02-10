**목적**
- 컬러/타이포 토큰과 페이지 데이터 요구사항의 단일 진실(SSOT)을 정의한다.
- 레이아웃/컴포넌트 위치/사이즈/화면 구성은 범위에서 제외한다.

**범위**
- 포함: 컬러 시스템, 타이포 시스템, 페이지별 필수 데이터/상태
- 제외: 화면 레이아웃, UI 배치, 컴포넌트 위치/크기, 픽셀 기반 목업

**파일 구조**
```text
02_DESIGN/
  README.md # 이 문서
  COLOR_SYSTEM.md # 컬러 토큰 정의
  TYPOGRAPHY_SYSTEM.md # 폰트/웨이트/라인하이트 토큰 정의
  PAGE_DATA_REQUIREMENTS/
    BAN_PICK_SHOP.md # BAN/PICK/SHOP 페이지 필수 데이터/상태
    IN_GAME.md # IN_GAME 페이지 필수 데이터/상태
    LOGIN.md # LOGIN/WELCOME 페이지 필수 데이터/상태
    MAIN.md # MAIN 페이지 필수 데이터/상태
    MY_PAGE.md # MY_PAGE 페이지 필수 데이터/상태
    RESULT.md # RESULT 페이지 필수 데이터/상태
    ROOM_LIST.md # ROOM_LIST 상태 필수 데이터/상태
    WAITING_ROOM.md # WAITING_ROOM 페이지 필수 데이터/상태
```

**변경 원칙**
- 페이지 데이터 요구사항은 `03_API/PAGE_MAP/`과 일치해야 한다.
- 컬러/타이포 토큰 변경은 `02_DESIGN/`에서만 수행한다.
