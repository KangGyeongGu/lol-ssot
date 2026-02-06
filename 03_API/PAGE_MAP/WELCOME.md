# PAGE_MAP_WELCOME

## 목적
- WELCOME(로그인) 화면의 인증 진입 REST 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

---
## 1. 진입 시 REST
| 메서드 | 엔드포인트 | 목적 |
|---|---|---|
| GET | /users/me/active-game | 이미 로그인된 세션의 복귀 여부 확인 (필요 시) |

---
## 2. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| 카카오 로그인 제출 | POST | /auth/kakao/login | authorizationCode 전달 |
| 로그인 성공(기존 회원) 후 복귀 판단 | GET | /users/me/active-game | null이면 MAIN, 값이 있으면 stage/pageRoute로 자동 이동 |

---
## 3. 응답 분기
| API | 분기 기준 | 다음 화면 |
|---|---|---|
| POST /auth/kakao/login | data.result=OK | active-game 조회 후 MAIN 또는 게임 페이지 |
| POST /auth/kakao/login | data.result=SIGNUP_REQUIRED | WELCOME + SIGNUP 오버레이 |
