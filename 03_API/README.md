# 03_API

## 0. 작업 양식
API 명세 변경 시 아래 순서로 진행한다.

```
1) 01_PRODUCT 요구사항 확인
2) REST 계약 갱신 (OPENAPI.yaml.md)
3) 규약/가드/에러/요약 문서 동기화
4) 문서 간 불일치 체크
```

---
## 1. 목적
- 이 디렉토리는 LoL 프로젝트의 API 계약을 정의한다.
- AI 에이전트가 빠르게 참조할 수 있도록 단일 진실과 보조 문서를 분리한다.

---
## 2. 문서 구조
- `LIFECYCLE.md`: REST/실시간 연결·구독·해제·호출 타이밍 정의
- `CONTRACT/REST/OPENAPI.yaml.md`: REST 계약의 단일 진실
- `CONTRACT/REST/CONVENTIONS.md`: REST 공통 규칙
- `CONTRACT/REST/AUTH_GUARDS.md`: 인증/가드 규칙
- `CONTRACT/REST/ERROR_MODEL.md`: 에러 포맷 및 코드
- `CONTRACT/REST/API_SUMMARY.md`: 사람용 요약

---
## 3. 동기화 체크리스트
- OPENAPI.yaml.md와 API_SUMMARY.md의 엔드포인트가 일치하는가
- CONVENTIONS.md의 규칙이 OPENAPI에 반영되었는가
- AUTH_GUARDS.md의 가드가 요약/스키마에 드러나는가
- ERROR_MODEL.md의 코드가 실제 응답에 사용되는가
