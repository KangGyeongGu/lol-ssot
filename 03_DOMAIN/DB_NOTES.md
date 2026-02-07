# DB_NOTES

## 0. 목적
- DATA_MODEL.md를 보조하는 성능/설계 이유 문서.
- 단일 진실은 DATA_MODEL.md이다.

## 관련 문서
- [[03_DOMAIN/DATA_MODEL.md]]

---
## 1. 인덱스 전략
### 1.1 USER
- unique: kakao_id
- unique: nickname
- index: score DESC (랭킹 조회)
- index: active_game_id (복귀 조회)

### 1.2 ROOM
- index: (game_type, language)
- index: room_name (검색)
- index: host_user_id

### 1.3 ROOM_PLAYER
- **활성 유니크 인덱스**: (room_id, user_id) WHERE left_at IS NULL
  - 부분 유니크 인덱스 필요(DB별 구현 상이)
- index: room_id (대기실 스냅샷)
- index: user_id (사용자 기준 조회)

### 1.4 ROOM_KICK
- unique: (room_id, user_id)
- index: room_id

### 1.5 ROOM_HOST_HISTORY
- index: room_id

### 1.6 GAME
- unique: room_id
- index: stage
- index: stage_deadline_at (타임아웃 처리)
  - ROOM은 단일 게임 세션 단위(ROOM당 GAME 최대 1건)로 운영한다.

### 1.7 GAME_PLAYER
- unique: (game_id, user_id)
- index: game_id
- index: (user_id, joined_at DESC) (전적 목록)
- index: state (접속 상태 조회)

### 1.8 GAME_BAN / GAME_PICK
- unique: (game_id, user_id)
- index: game_id
- index: (algorithm_id, created_at) (밴/픽 통계)

### 1.9 PURCHASE / USAGE / SUBMISSION
- PURCHASE: index (game_id, user_id)
- ITEM_USAGE: index (game_id, from_user_id), (game_id, to_user_id)
- SPELL_USAGE: index (game_id, user_id)
- SUBMISSION: index (game_id, submitted_at), (user_id, submitted_at)
- SUBMISSION: index (judge_status) (실패 원인 통계)

### 1.10 CATALOG
- index: is_active

### 1.11 CHAT_MESSAGE
- index: (channel_type, created_at DESC)
- index: room_id, created_at DESC
- index: sender_user_id, created_at DESC

---
## 2. 성능/운영 노트
- SUBMISSION.source_code는 용량이 커질 수 있으므로 분리 저장/압축 고려.
- 실시간 랭킹은 USER.score 기반 정렬이므로 캐시/정렬 최적화 필요.
- 밴/픽률 통계는 GAME_BAN/GAME_PICK 집계로 계산(배치/캐시 가능).
- SHOP 구매 검증은 GAME_ITEM_PURCHASE/GAME_SPELL_PURCHASE 합산으로 처리.
- CHAT_MESSAGE는 현재 무기한 보관(보관 정책 미적용)으로 가정한다.

---
## 3. 설계 이유
- ROOM.host_user_id를 단일 진실로 두어 중복/불일치 제거.
- ROOM_PLAYER는 left_at NULL을 활성 상태로 정의해 재입장/이력 보존.
- GAME_PLAYER.state로 접속/이탈을 추적해 재접속 검증을 단순화.
- 구매 시점 단가(unit_price) 저장으로 과거 재현 가능.

---
## 4. 캐시/DB 경계 원칙
### 4.1 DB에 최종 저장해야 하는 것 (persistent)
- 강퇴(ROOM_KICK), 밴/픽/구매/제출/사용 로그
- 점수/결과(GAME_PLAYER)
- 채팅 로그(CHAT_MESSAGE)
- active game 추적(USER.active_game_id)
- 재접속/감사/통계에 필요한 최소 기록

### 4.2 Redis에 두는 것 (ephemeral/derived)
- 타이핑 상태, 실시간 화면 스트림, 단계 남은 시간
- 실시간 연결 상태(heartbeat)
- UI 이벤트 기반 상태

### 4.3 운영 원칙
- 실시간 상태는 Redis가 단일 진실이다.
- 결과/이력/정산에 필요한 기록은 반드시 DB에 남긴다.
- Redis 상태는 게임 종료 시 DB 기록으로 귀결되어야 한다.

### 4.4 Write Policy
- 기본값: persistent는 write-through.
- 예외: ROOM, ROOM_PLAYER, GAME, GAME_PLAYER, GAME_BAN, GAME_PICK은 write-back(종료 시 DB 반영).
- 최종 기준은 DATA_MODEL.md의 Write Policy 매핑을 따른다.
