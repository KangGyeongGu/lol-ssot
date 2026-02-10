## 목적
- MY_PAGE 화면(내정보/통계/전적)의 REST 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 목적 |
|---|---|---|
| GET | /users/me | 프로필(언어/티어/점수/경험치/레벨/진행도/코인) 조회 |
| GET | /users/me/stats | 승/패/무/승률 통계 조회 |
| GET | /users/me/matches | 전적 목록 첫 페이지 조회 |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 파라미터 |
|---|---|---|---|
| 전적 더보기(무한 스크롤/페이지네이션) | GET | /users/me/matches | cursor, limit |
| 새로고침 | GET | /users/me, /users/me/stats, /users/me/matches | 기본 스냅샷 재조회 |

---
## 3. 범위
- MY_PAGE 관련 실시간(WS) 전용 Topic/Command는 현재 계약 범위에 없다.
