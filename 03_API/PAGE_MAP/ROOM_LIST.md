## 목적
- MAIN 내부 ROOM_LIST 패널 상태의 방 탐색/참가 및 목록 동기화(REST/실시간)를 매핑한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]
- [[03_API/CONTRACT/REALTIME/TOPICS.md]]
- [[03_API/CONTRACT/REALTIME/EVENTS.md]]
- [[03_API/CONTRACT/REALTIME/CONVENTIONS.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 파라미터 | 목적 |
|---|---|---|---|
| GET | /rooms | roomName, language, gameType, cursor, limit | ROOM_LIST 패널 스냅샷 조회 (검색/필터/페이징 + listVersion) |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| 검색어/필터 변경 | GET | /rooms | query 변경값으로 재조회 |
| 다음 페이지 로드 | GET | /rooms | cursor 기반 추가 조회 |
| 업데이트 적용 버튼 클릭 | GET | /rooms | 누적 변경분(listVersion 차이) 최신화 |
| 방 참가 | POST | /rooms/{roomId}/join | 성공 시 WAITING_ROOM 진입 |

---
## 3. 실시간 구독
| 채널 | 이벤트 타입 | 목적 |
|---|---|---|
| /topic/rooms/list | ROOM_LIST_UPSERT | 방 생성/수정/상태 변화 반영 |
| /topic/rooms/list | ROOM_LIST_REMOVED | 방 삭제/목록 제외 반영 |

---
## 4. 동기화 규칙
- 현재 화면에 보이는 roomId의 상태 변화(대기중/게임중, 인원수, joinable)는 이벤트 수신 즉시 반영한다.
- 현재 페이지 범위 밖 변화는 리스트를 즉시 재배열하지 않고 업데이트 인디케이터 카운트만 증가시킨다.
- 업데이트 버튼 클릭 시 현재 필터/페이징 기준 `GET /rooms`를 재호출해 최신 목록을 적용한다.
- ROOM_LIST 체류 중 보정 재동기화로 20~30초 주기 `GET /rooms`를 권장한다.

---
## 5. 주요 에러 분기
| 엔드포인트 | 상태 코드 | 의미 |
|---|---|---|
| /rooms | 400/401 | 필터 파라미터 오류, 인증 실패 |
| /rooms/{roomId}/join | 403 | 강퇴된 사용자 재입장 차단 등 |
| /rooms/{roomId}/join | 404 | 대상 방 없음 |
| /rooms/{roomId}/join | 409 | 방 정원/상태 충돌, active game 존재 |
