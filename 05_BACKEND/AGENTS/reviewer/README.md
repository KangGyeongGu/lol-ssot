# BE_REVIEW_AGENTS

## 0. 목적
- 백엔드 코드 리뷰/검증 전용 에이전트 시스템을 정의한다.
- 마스터 리뷰 에이전트가 계획 수립, 분해, 결과 통합, 수정 라운드 설계를 담당한다.
- 서브 에이전트는 도메인 영역별 정밀 리뷰와 수정 작업을 수행한다.

## 1. 사용 원칙
- 단일 진실은 SSOT 문서이며 문서에 없는 규칙은 추정하지 않는다.
- 서브 에이전트는 지정된 소유 디렉토리만 수정한다.
- 리뷰는 기본적으로 읽기 전용이며, 수정은 마스터의 명시 지시가 있을 때만 수행한다.
- 동일 파일은 같은 라운드에서 한 에이전트만 수정한다.
- 리뷰는 "계약 준수"뿐 아니라 "코드 품질"(정확성/동시성/보안/성능/안정성) 관점도 포함한다.

## 2. 에이전트 구성
- BE_REVIEW_MASTER_AGENT.md: 리뷰 오케스트레이터(모델: opus)
- BE_REVIEW_CORE_INFRA_AGENT.md: 서버 부트스트랩/공통/DB/상태(sonnet)
- BE_REVIEW_AUTH_USER_AGENT.md: 인증/유저(sonnet)
- BE_REVIEW_ROOM_LOBBY_AGENT.md: 방/로비(sonnet)
- BE_REVIEW_GAME_LIFECYCLE_AGENT.md: 게임 라이프사이클(sonnet)
- BE_REVIEW_BAN_PICK_SHOP_AGENT.md: 밴/픽/상점/인벤토리(sonnet)
- BE_REVIEW_REALTIME_CHAT_AGENT.md: 실시간/STOMP/채팅(sonnet)
- BE_REVIEW_STATS_RANKING_AGENT.md: 통계/랭킹(sonnet)

## 3. 표준 워크플로우
1. 마스터가 범위/목표/대상 파일을 확정한다.
2. 마스터가 영역별 서브에이전트를 병렬 또는 순차로 배정한다.
3. 서브에이전트는 정밀 리뷰 보고서를 제출한다.
4. 마스터는 결과를 통합하고 중복/충돌을 정리한다.
5. 수정이 필요하면 라운드별 수정 계획을 작성해 재배정한다.
6. 수정 결과를 재검증하고 최종 요약을 출력한다.

## 4. 병렬/순차 기준
- 병렬: 소유 디렉토리가 겹치지 않고 의존성이 낮을 때.
- 순차: 공통 인터페이스/도메인 상태/트랜잭션 경계가 겹칠 때.

## 5. 기본 결과 포맷
- Summary: 총 이슈 수 및 심각도 분포
- Findings: Type=Spec|CodeQuality, 심각도/파일/근거/설명
- Fix Plan: 수정 항목/담당 에이전트/순서
- Tests: 수행/미수행 및 이유
