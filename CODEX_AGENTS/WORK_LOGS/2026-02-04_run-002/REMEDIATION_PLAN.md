# 2026-02-04_run-002 실패 항목 수정 설계안

## 0. 목적
- 기준 로그: `PRODUCT_VALIDATOR.md`, `DESIGN_VALIDATOR.md`, `API_VALIDATOR.md`, `DOMAIN_VALIDATOR.md`, `CROSS_CHECKER.md`
- 목표: 다음 검증 실행에서 FAIL 항목 0건
- 범위: 문서 정합성 수정(정책 신규 확장 금지, 기존 합의 정리/정규화 중심)

## 1. 선결정(수정 시작 전 동결)
1. 페이지 모델은 `MAIN + 상태(ROOM_LIST panel)` 구조를 유지한다.
2. `SIGNUP`은 독립 라우트가 아니라 `WELCOME` 위 오버레이 상태로 통일한다.
3. active-game 기반 `PageRoute`는 `WAITING_ROOM`, `BAN_PICK_SHOP`, `IN_GAME`만 사용한다.
4. `RESULT`는 `GAME_FINISHED` 이벤트 기반 진입만 허용하고 재접속 자동복귀는 금지한다.
5. 로그인 수단은 카카오 OAuth 단일 지원으로 통일한다.
6. ROOM 채팅 범위는 `WAITING_ROOM ~ IN_GAME` 공용으로 통일한다.

## 2. 수정 백로그 (우선순위 순)
| ID | 우선순위 | 실패 근거 | 수정 파일 | 수정 작업 설계 | 완료 기준 |
|---|---|---|---|---|---|
| A-01 | P0 | Cross-check 1, 2 | `01_PRODUCT/USER_FLOWS.md`, `03_API/LIFECYCLE.md`, `03_API/PAGE_MAP/ROOM_LIST.md`, `03_API/PAGE_MAP/MAIN.md` | ROOM_LIST를 독립 페이지가 아닌 MAIN 내부 패널 상태로 문구 통일 | PRODUCT/API/DESIGN에서 ROOM_LIST 표현이 동일(패널 상태) |
| A-02 | P0 | Cross-check 1, 3 | `01_PRODUCT/USER_FLOWS.md`, `03_API/PAGE_MAP/SIGNUP.md`, `02_DESIGN/OVERLAYS/SIGNUP_MODAL.md` | SIGNUP을 “페이지”에서 “WELCOME 오버레이 상태”로 통일 | SIGNUP page vs modal 모순 문구 제거 |
| A-03 | P0 | API FAIL 3, Cross-check 1 | `03_API/CONTRACT/REST/OPENAPI.yaml.md`, `03_API/CONTRACT/REST/CONVENTIONS.md`, `03_API/PAGE_MAP/RESULT.md` | `PageRoute` enum에서 `RESULT` 제거, active-game 설명과 라우트 정의 일치화 | OpenAPI/CONVENTIONS/PAGE_MAP 간 FINISHED 규칙 충돌 없음 |
| A-04 | P0 | Cross-check 3 | `02_DESIGN/PAGES/LOGIN.md` | 구글 로그인 버튼/문구 제거, 카카오 단일 CTA로 정리 | 디자인 로그인 수단이 REQUIREMENTS와 일치 |
| B-01 | P0 | Design FAIL 1 | `02_DESIGN/PAGES/MAIN.md`, `02_DESIGN/SECTIONS/ROOM_LIST_PANEL.md` | ROOM_LIST panel 좌표를 MAIN 교체영역(`y=10.2%`) 기준으로 재정렬 | 헤더/패널 좌표가 “헤더 하단” 설명과 수치 모두 일치 |
| B-02 | P0 | Design FAIL 2 | `02_DESIGN/OVERLAYS/ROOM_CREATE_MODAL.md`, `02_DESIGN/LAYOUT_RULES.md` | 모달 폭을 `<=900px`로 조정(예: 900px), 내부 요소 비율 재계산 | ROOM_CREATE modal 폭이 전역 모달 규칙 위반 없음 |
| B-03 | P1 | Design FAIL 4 | `02_DESIGN/PAGES/BAN_PICK_SHOP.md`, `02_DESIGN/PAGES/IN_GAME.md`, `02_DESIGN/COMPONENTS.json.md` | `stageTabs.height=56`, `editorToolbar.height=48`와 페이지 ref(px) 수치 일치화 | 컴포넌트 spec과 페이지 레이아웃 px 불일치 0건 |
| B-04 | P1 | Design FAIL 3 | `02_DESIGN/COMPONENTS.json.md`, `02_DESIGN/TOKENS.json.md`, `02_DESIGN/PAGES/*.md`, `02_DESIGN/OVERLAYS/*.md` | 컴포넌트 명칭을 canonical(`modal`, `input`, `chat`)로 통일, 토큰 경로를 단일 네임스페이스(`color.*`)로 정규화 | 별칭 혼재/토큰 루트 분리 문제 제거 |
| B-05 | P1 | Cross-check 3 | `02_DESIGN/PAGES/IN_GAME.md`, `02_DESIGN/PAGES/RESULT.md` | IN_GAME에 타이핑 상태 바/방 채팅 영역 명시 추가, RESULT CTA를 `메인/마이페이지`로 교정 | 제품 흐름 필수 요소와 디자인 명세가 일치 |
| C-01 | P0 | API FAIL 1 | `03_API/CONTRACT/REST/OPENAPI.yaml.md` | 모든 REST operation에 `429`, `500` 응답 정의 추가(공통 response component 권장) | 상태 코드 규칙 문서와 OpenAPI 응답 코드 집합 일치 |
| C-02 | P0 | API FAIL 2, Cross-check 2 | `03_API/CONTRACT/REALTIME/TOPICS.md`, `03_API/LIFECYCLE.md` | `/topic/rooms/{roomId}/chat` 범위를 `ROOM`으로 교정, WAITING~IN_GAME 설명과 표기 통일 | Topic 표/설명/라이프사이클 간 범위 충돌 제거 |
| C-03 | P1 | Cross-check 2 | `03_API/CONTRACT/REALTIME/TOPICS.md`, `03_API/PAGE_MAP/RESULT.md` | RESULT 단계 game topic 구독 정책을 단일화(권장: RESULT 추가 구독 없음, 진입 직후 해제) | RESULT 구독 정책 상충 문장 0건 |
| D-01 | P1 | Product FAIL 1 | `01_PRODUCT/REQUIREMENTS.md`, `01_PRODUCT/USER_FLOWS.md`, `01_PRODUCT/COPY_TEXT.md` | 채팅/마이페이지를 요구사항에 정식 편입하거나(권장) USER_FLOWS/COPY_TEXT에서 제거 중 하나로 통일 | REQUIREMENTS와 USER_FLOWS 기능 집합 차이 제거 |
| D-02 | P1 | Product FAIL 2 | `01_PRODUCT/GAME_RULES.md` | 점수 산정 규칙 적용 대상을 RANKED로 명시하고 NORMAL 무변동과 충돌 제거 | NORMAL 점수 규칙 모순 제거 |
| D-03 | P1 | Product FAIL 3 | `01_PRODUCT/GAME_RULES.md`, `01_PRODUCT/ECONOMY.md` | 필드명/저장 포맷 등 구현 상세를 정책 문구로 추상화 | PRODUCT 문서의 구현 의존 표현 제거 |
| D-04 | P1 | Product FAIL 4 | `01_PRODUCT/USER_FLOWS.md` | “정책 판단 미포함” 원칙과 실제 서술을 맞추도록 문구 재정의(결과 분기만 유지) | 문서 목적과 본문 서술의 자기모순 제거 |
| E-01 | P1 | Domain FAIL 1 | `03_DOMAIN/DB_NOTES.md` | USAGE 인덱스를 실제 스키마 기준으로 분리(`ITEM_USAGE`: from/to, `SPELL_USAGE`: user) | 인덱스 설명과 데이터모델 필드 일치 |
| E-02 | P1 | Domain FAIL 2, 3 | `03_DOMAIN/DATA_MODEL.md` | `ROOM_KICK`, `ROOM_HOST_HISTORY`의 USER 관계를 명시하고 ITEM/SPELL usage 관계 문구 분리 | 관계 정의 누락/용어 모호성 제거 |
| F-01 | P2 | Summary UNKNOWN | `CODEX_AGENTS/scripts/run_all_validators.sh` 또는 validator 출력 템플릿 | Summary 파서가 `Overall:` 외 표현도 인식하거나 validator 출력을 공통 포맷으로 강제 | `SUMMARY.md`에서 UNKNOWN 없이 PASS/FAIL 집계 |

## 3. 실행 순서
1. P0 항목(A-01~A-04, B-01~B-02, C-01~C-02) 먼저 처리한다.
2. P1 항목(B-03~E-02)으로 세부 정합성/표현 품질을 정리한다.
3. P2 항목(F-01)로 자동 집계 안정성을 보정한다.
4. 전체 validator 재실행 후 FAIL 잔여 항목만 재수정한다.

## 4. 검증 체크리스트
1. `01_PRODUCT`에서 요구 기능 집합과 `USER_FLOWS` 페이지/상태 집합이 동일하다.
2. `02_DESIGN`의 좌표/크기/컴포넌트 명칭이 `LAYOUT_RULES`/`COMPONENTS`와 일치한다.
3. `03_API`의 enum/응답코드/topic 범위가 계약 문서끼리 충돌하지 않는다.
4. `03_DOMAIN`의 인덱스/관계 정의가 데이터모델 필드와 1:1 대응된다.
5. `CROSS_CHECKER`에서 용어/페이지 모델/결과 구독 정책 충돌이 재발하지 않는다.

## 5. 재검증 명령
```bash
CODEX_AGENTS/scripts/run_all_validators.sh --mode date --sandbox read-only
```

