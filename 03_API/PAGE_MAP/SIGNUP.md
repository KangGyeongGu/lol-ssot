## 목적
- WELCOME 위 SIGNUP 오버레이(추가 정보 입력) 상태의 회원가입 REST 매핑을 정의한다.

## 관련 문서
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

---
## 1. 사용자 액션 → REST
| 사용자 액션 | 메서드 | 엔드포인트 | 비고 |
|---|---|---|---|
| 회원가입 완료 제출 | POST | /auth/signup | signupToken, nickname, language 전달 |
| 가입 완료 후 복귀 판단 | GET | /users/me/active-game | null이면 MAIN, 값이 있으면 stage/pageRoute로 자동 이동 |

---
## 2. 주요 검증/에러
| 엔드포인트 | 상태 코드 | 의미 |
|---|---|---|
| /auth/signup | 400 | 닉네임/언어/토큰 검증 실패 |
