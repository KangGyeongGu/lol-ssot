# ECONOMY

## 0. 문서 목적
- 이 문서는 코인/경험치/보상 및 티어/경험치 구간을 정의한다.
- 경제/진행(Progression) 정책의 단일 진실이다.
- 게임 진행 규칙/판정/채점은 GAME_RULES를 따른다.

## 관련 문서
- [[01_PRODUCT/GAME_RULES.md]]
- [[01_PRODUCT/CATALOG.md]]
---
## 1. 보상 규칙 (RANKED)
- NORMAL 게임은 코인/경험치 보상이 없다.
- 보상은 게임 종료 시점에 산정되며, 결과는 사용자 게임 결과 기록에 반영한다.
- 기준값:
  - base_coin = 1000
  - base_exp = 25.0
- 결과 계수:
  - WIN = 1.0
  - DRAW = 0.8
  - LOSE = 0.6
- 순위 보너스:
  - 1위: +200 coin, +10.0 exp
  - 2위: +100 coin, +5.0 exp
- 정답 제출 보너스:
  - solved = true: +100 coin, +7.5 exp
- 이탈 처리:
  - state = LEFT 인 경우 coin_delta = 0, exp_delta = 0
- 계산식:
  - coin_delta = floor(base_coin * result_multiplier + rank_bonus_coin + solved_bonus_coin)
  - exp_delta = base_exp * result_multiplier + rank_bonus_exp + solved_bonus_exp
- 무승부일 경우 모든 참가자의 result는 DRAW로 기록한다.
### 1.1 초기 코인
- 신규 가입 시 초기 코인 1000을 지급한다.
---
## 2. 랭킹 / 티어 규칙
### 2.1 티어 산정 기준
- 티어는 USER.score에 의해 결정된다.
- 티어는 score 기반 파생값이며, 저장은 캐시용이다.
### 2.2 티어 구간
| 티어 | Division | 점수 범위 |
|---|---|---|
| Iron | - | 0 ~ 299 |
| Bronze | V / IV / III / II / I | 300 ~ 799 |
| Silver | V / IV / III / II / I | 800 ~ 1299 |
| Gold | V / IV / III / II / I | 1300 ~ 1799 |
| Platinum | V / IV / III / II / I | 1800 ~ 2299 |
| Diamond | V / IV / III / II / I | 2300 ~ 2799 |
| Master | - | 2800 ~ 2999 |
| Grandmaster | - | 3000 ~ 3199 |
| Challenger | - | 3200 이상 |
### 2.3 Division 구간 규칙
- Bronze ~ Diamond는 100점 단위로 5개 구간으로 나눈다.
  - 예: Bronze
    - V: 300~399
    - IV: 400~499
    - III: 500~599
    - II: 600~699
    - I: 700~799
- Master 이상은 Division이 없다.
---
## 3. 경험치(Exp) 규칙
### 3.1 기본 원칙
- 경험치는 USER.exp로 누적 관리한다.
- 경험치는 RANKED 게임에서만 지급된다.
- NORMAL 게임은 경험치 보상이 없다.
### 3.2 레벨 구간(경험치 구간)
- 레벨은 경험치 구간의 파생값이며, 별도 저장하지 않는다.
- 레벨업 필요 경험치:
  - `exp_to_next_level(L) = 1000 + 200 * (L - 1)`
- 누적 경험치(레벨 도달 기준):
  - `total_exp_to_reach(L) = (L - 1) * (1000 + 100 * (L - 2))`
