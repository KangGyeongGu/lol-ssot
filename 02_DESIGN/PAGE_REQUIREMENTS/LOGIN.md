## 목적
- WELCOME(로그인) 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/WELCOME.md]]
- [[03_API/PAGE_MAP/SIGNUP.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

## Required Data
- auth result: result code (OK/SIGNUP_REQUIRED)
- active game snapshot (pageRoute, stage) when available
- error code (auth failure)

## Required States
- idle
- loading (oauth/login)
- signup required
- error (auth)

## Interactions
- 로그인 실패 시 알림을 표시한다(error.code: VALIDATION_FAILED, RATE_LIMITED, INTERNAL_ERROR).
- 회원가입 실패 시 알림을 표시한다(error.code: VALIDATION_FAILED, RATE_LIMITED, INTERNAL_ERROR).
- 알림 문구는 서버 `error.code` 기준으로 프론트엔드에서 관리한다.

## Prohibited
- 로그인 결과 없이 다음 화면 이동
