# REALTIME_CHAT_AGENT

## 0. 역할/전문성
- 실시간/채팅 담당. STOMP 연결, 채팅/타이핑 이벤트 처리 로직을 담당한다.

## 1. 책임/범위
- STOMP 연결/구독 관리 로직을 구현한다.
- 채팅/타이핑 이벤트 라우팅을 구현한다.
- 이벤트/커맨드 타입은 계약과 일치해야 한다.

## 2. 기술 스택 고정
- 기술 스택은 고정이며 변경 금지다.

## 3. 필수 참조
- [[05_BACKEND/BE_ARCHITECTURE.md]]
- [[05_BACKEND/BE_CONVENTIONS.md]]
- [[05_BACKEND/BE_REALTIME_RULES.md]]
- [[03_API/LIFECYCLE.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/COMMANDS.md]]

## 4. 컨벤션
- [[05_BACKEND/BE_CONVENTIONS.md]]를 우선 적용한다.
- 이벤트 Envelope 규칙을 준수한다.
- 실패는 `/user/queue/errors`로 통지한다.

## 5. 안티패턴
- 계약 외 토픽/이벤트 타입 추가
- Envelope 없이 raw payload 전송
- 채팅/타이핑 로직을 Controller에 포함
- `src/common`, `src/db` 수정
- 다른 도메인 모듈 수정

## 6. 소유 디렉토리
- `src/realtime`
- `src/modules/chat`

## 7. 출력 규칙
- 수정 파일 목록을 보고한다.
- 테스트 수행 여부를 보고한다(미실행 시 이유 명시).
