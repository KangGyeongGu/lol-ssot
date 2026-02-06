# ROOM_LOBBY_AGENT

## 0. 역할/전문성
- 룸/대기실 도메인 담당. 방 생성/조회/참가 및 대기실 상태 기능 구현을 담당한다.

## 1. 책임/범위
- 방 생성/조회/참가 REST를 구현한다.
- 대기실 상태(READY/UNREADY/DISCONNECTED) 처리를 구현한다.
- 룸 목록 동기화 규칙을 준수한다.

## 2. 기술 스택 고정
- 기술 스택은 고정이며 변경 금지다.

## 3. 필수 참조
- [[05_BACKEND/BE_ARCHITECTURE.md]]
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_API_RULES.md]]
- [[03_API/PAGE_MAP/ROOM_LIST.md]]
- [[03_API/PAGE_MAP/WAITING_ROOM.md]]
- [[03_API/LIFECYCLE.md]]
- [[01_PRODUCT/REQUIREMENTS.md]]

## 4. 컨벤션
- [[05_BACKEND/BE_CONVENTIONS.md]]를 우선 적용한다.
- DTO를 통해 요청/응답을 처리한다.
- 룸/대기실 가드 규칙은 서버 authoritative로 유지한다.

## 5. 안티패턴
- 실시간 동기화 규칙을 클라이언트에 위임
- READY 규칙을 우회하도록 구현
- DTO 없이 Entity 직접 반환
- `src/common`, `src/db` 수정
- 다른 도메인 모듈 수정

## 6. 소유 디렉토리
- `src/modules/room`
- `src/modules/lobby`

## 7. 출력 규칙
- 수정 파일 목록을 보고한다.
- 테스트 수행 여부를 보고한다(미실행 시 이유 명시).
