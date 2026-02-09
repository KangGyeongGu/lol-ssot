# FE_REVIEW_AGENTS

## 0. 목적
- 프론트엔드 코드 리뷰/검증 전용 에이전트 시스템을 정의한다.
- 마스터 리뷰 에이전트가 계획 수립, 분해, 결과 수집, 수정 라운드 설계를 담당한다.
- 서브 에이전트는 영역별 정밀 리뷰 및 수정 작업을 수행한다.

## 1. 사용 원칙
- 단일 진실은 SSOT 문서이며 문서에 없는 규칙은 추정하지 않는다.
- 서브 에이전트는 지정된 소유 디렉토리만 수정한다.
- 리뷰는 기본적으로 읽기 전용이며, 수정은 마스터의 명시 지시가 있을 때만 수행한다.
- 동일 파일은 같은 라운드에서 한 에이전트만 수정한다.

## 2. 에이전트 구성
- FE_REVIEW_MASTER_AGENT.md: 리뷰 오케스트레이터(모델: opus)
- FE_REVIEW_APP_INFRA_AGENT.md: 앱 초기화/환경 설정(sonnet)
- FE_REVIEW_ROUTING_AGENT.md: 라우팅/가드(sonnet)
- FE_REVIEW_STATE_AGENT.md: 스토어/상태(sonnet)
- FE_REVIEW_API_AGENT.md: REST/DTO/엔티티(sonnet)
- FE_REVIEW_REALTIME_AGENT.md: WebSocket/STOMP(sonnet)
- FE_REVIEW_COMPONENT_AGENT.md: shared/ui, widgets, features UI(sonnet)
- FE_REVIEW_PAGE_AGENT.md: pages/페이지 전용 구성(sonnet)
- FE_REVIEW_STYLING_AGENT.md: 스타일/토큰/전역 스타일(sonnet)

## 3. 표준 워크플로우
1. 마스터가 범위/목표/대상 파일을 확정한다.
2. 마스터가 영역별 서브에이전트를 병렬 또는 순차로 배정한다.
3. 서브에이전트는 정밀 리뷰 보고서를 제출한다.
4. 마스터는 결과를 통합하고 중복/충돌을 정리한다.
5. 수정이 필요하면 라운드별 수정 계획을 작성해 재배정한다.
6. 수정 결과를 재검증하고 최종 요약을 출력한다.

## 4. 병렬/순차 기준
- 병렬: 소유 디렉토리가 겹치지 않고 의존성이 낮을 때.
- 순차: 공통 인터페이스/스토어/라우팅 등 영향 범위가 큰 경우.

## 5. 기본 결과 포맷
- Summary: 총 이슈 수 및 심각도 분포
- Findings: 심각도/파일/근거 문서/설명
- Fix Plan: 수정 항목/담당 에이전트/순서
- Tests: 수행/미수행 및 이유
