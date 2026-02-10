## 0. 작업 양식
새 엔드포인트 추가 시 아래 양식을 유지한다.

```
[기능]
- 한 줄 요약

[메서드 / 엔드포인트]
- METHOD /path

[설명]
- 스냅샷인지 명령인지
- 주요 입력 파라미터
- 주요 에러 코드
```

---
## 1. 문서 목적
- REST 엔드포인트를 사람이 빠르게 이해/검토하기 위한 요약 문서.
- 정확한 계약과 스키마는 OPENAPI.yaml.md가 단일 진실이다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

---
## 2. Auth
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 카카오 로그인 | POST | /auth/kakao/login | 인가코드 전달, 회원이면 로그인 |
| 회원가입 완료 | POST | /auth/signup | 닉네임/주언어 입력 후 계정 생성 |
| 로그아웃 | POST | /auth/logout | 세션/refresh 무효화 |

---
## 3. Users
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 내 정보 조회 | GET | /users/me | 프로필(언어/티어/점수/경험치/레벨/진행도/코인) |
| active game 조회 | GET | /users/me/active-game | 복귀 판단용 |
| 내 통계 조회 | GET | /users/me/stats | 마이페이지 통계 |
| 전적 목록 조회 | GET | /users/me/matches | 커서 기반 페이징 |

---
## 4. Rooms (Lobby)
| 기능      | 메서드  | 엔드포인트                   | 설명                                          |
| ------- | ---- | ----------------------- | ------------------------------------------- |
| 방 목록 조회 | GET  | /rooms                  | 검색/필터/페이징 + roomStatus/joinable/listVersion |
| 방 생성    | POST | /rooms                  | NORMAL / RANKED                             |
| 방 상세 조회 | GET  | /rooms/{roomId}         | 대기실 스냅샷                                     |
| 방 참가    | POST | /rooms/{roomId}/join    | 인원/가드 검증                                    |
| 방 나가기   | POST | /rooms/{roomId}/leave   | 명령형 처리                                      |
| READY   | POST | /rooms/{roomId}/ready   | 준비 상태 전환                                    |
| UNREADY | POST | /rooms/{roomId}/unready | 준비 상태 전환                                    |
| 게임 시작   | POST | /rooms/{roomId}/start   | 방장 전용                                       |
| 플레이어 강퇴 | POST | /rooms/{roomId}/kick    | 방장 전용                                       |

---
## 5. Games
### 5.1 Game State
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 게임 상태 조회 | GET | /games/{gameId}/state | stage, remainingMs 등 |

### 5.2 Ranked Commands
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 밴 제출 | POST | /games/{gameId}/ban | body: algorithmId |
| 픽 제출 | POST | /games/{gameId}/pick | body: algorithmId |
| SHOP 일괄 구매 | POST | /games/{gameId}/shop/purchase | body: items[], spells[] |

### 5.3 Play
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 코드 제출 | POST | /games/{gameId}/submissions | body: language, sourceCode |

---
## 6. Catalog (Static Data)
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 알고리즘 목록 | GET | /catalog/algorithms | 밴/픽 선택 리스트 |
| 아이템 목록 | GET | /catalog/items | 상점 아이템(설명/가격/지속시간) |
| 스펠 목록 | GET | /catalog/spells | 상점 스펠(설명/가격/지속시간) |

---
## 7. Stats (Main)
| 기능 | 메서드 | 엔드포인트 | 설명 |
|---|---|---|---|
| 실시간 플레이어 점수 랭킹 | GET | /stats/realtime/player-rankings | 랭킹 스냅샷 |
| 실시간 알고리즘 밴/픽률 | GET | /stats/realtime/algorithm-pick-ban-rates | 밴/픽 비율 |

---
## 8. 비고
- 채팅/단계 전환 알림은 WebSocket에서 정의한다.
- REST는 스냅샷 + 명령만 담당한다.
