## 0. 문서 목적
- 이 문서는 코인/경험치/보상 및 티어/경험치 구간을 정의한다.
- 경제/진행(Progression) 정책의 단일 진실이다.
- 게임 진행 규칙/판정/채점은 GAME_RULES를 따른다.

## 관련 문서
- [[01_PRODUCT/GAME_RULES.md]]
- [[01_PRODUCT/CATALOG.md]]
---
## 1. 보상 규칙
### 1.1 모드별 보상 적용
- RANKED: 점수(score) 변동 + 코인/경험치 보상
- NORMAL: 경험치 보상만 지급 (점수/코인 변동 없음)

### 1.2 기준값
- base_coin = 1000
- base_exp = 25.0

### 1.3 모드 배수
- mode_multiplier:
  - RANKED = 1.0
  - NORMAL = 0.6

### 1.4 결과 계수
- WIN = 1.0
- DRAW = 0.8
- LOSE = 0.6

### 1.5 순위 보너스 (NORMAL/RANKED 동일, mode_multiplier로 스케일)
- 1위: +200 coin, +10.0 exp
- 2위: +100 coin, +5.0 exp

### 1.6 정답 제출 보너스
- solved = true: +100 coin, +7.5 exp

### 1.7 이탈 처리
- state = LEFT 인 경우 coin_delta = 0, exp_delta = 0
- score_delta는 RANKED 기준 별도 패널티 적용

### 1.8 계산식
- coin_delta (RANKED만):
  - coin_delta = floor(base_coin * result_multiplier + rank_bonus_coin + solved_bonus_coin)
- exp_delta (NORMAL/RANKED):
  - exp_delta = mode_multiplier * (base_exp * result_multiplier + rank_bonus_exp + solved_bonus_exp)
- 무승부일 경우 모든 참가자의 result는 DRAW로 기록한다.

### 1.9 초기 코인
- 신규 가입 시 초기 코인 1000을 지급한다.
---
## 2. 랭킹 점수(Score) 규칙 (RANKED)
### 2.1 기본 원칙
- score는 랭킹 점수이며 USER.score로 누적 관리한다.
- score >= 0
- score 변동은 RANKED 게임에서만 발생한다. NORMAL은 score_delta = 0
- tier는 score 기반 파생값이며, 저장은 캐시용이다.
- 신규 가입 초기 score = 0 (Iron)

### 2.2 게임 내 순위 산정
- rank_in_game은 final_score_value 내림차순으로 결정한다.
- 동점은 동순위로 처리한다.
- LEFT는 최하위로 간주한다.

### 2.3 Elo 계산(다인전, 정규화 포함)
- 내부 레이팅: R = score + 1000
- N = 게임 참가자 수(LEFT 포함)
- E_ij = 1 / (1 + 10^((R_j - R_i)/400))
- S_ij = 1 (i가 j보다 상위)
- S_ij = 0.5 (동순위)
- S_ij = 0 (하위)
- E_i = Σ E_ij
- S_i = Σ S_ij
- raw_delta = K * (S_i - E_i) / (N - 1)
- score_delta = round(raw_delta)
- score_after = max(0, score_before + score_delta)

### 2.4 소프트 배치(K 값)
- 첫 N게임(기본 10): K = 40
- 이후: K = 24
- 소프트 배치는 내부 보정이며 사용자에게 별도 노출하지 않는다.

### 2.5 안정화 규칙
- 적용 순서: raw_delta 계산 → LEFT 패널티 → 클램프 → score_after
- LEFT 패널티: score_delta -= 20
- 클램프 범위: score_delta는 -50 ~ +50으로 제한한다.
---
## 3. 랭킹 / 티어 규칙
### 3.1 티어 산정 기준
- 티어는 USER.score에 의해 결정된다.
- 티어는 score 기반 파생값이며, 저장은 캐시용이다.
### 3.2 티어 구간
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
### 3.3 Division 구간 규칙
- Bronze ~ Diamond는 100점 단위로 5개 구간으로 나눈다.
  - 예: Bronze
    - V: 300~399
    - IV: 400~499
    - III: 500~599
    - II: 600~699
    - I: 700~799
- Master 이상은 Division이 없다.
---
## 4. 경험치(Exp) 규칙
### 4.1 기본 원칙
- 경험치는 USER.exp로 누적 관리한다.
- 경험치는 NORMAL/RANKED 모두 지급한다.
- 경험치는 감소하지 않는다.
- 레벨은 경험치 구간의 파생값이며, 별도 저장하지 않는다.
- UI/API 제공 파생값:
  - level
  - exp_in_level
  - exp_to_next
  - exp_progress

### 4.2 레벨 구간(경험치 구간)
- 레벨업 필요 경험치:
  - `exp_to_next_level(L) = 1000 + 200 * (L - 1)`
- 누적 경험치(레벨 도달 기준):
  - `total_exp_to_reach(L) = (L - 1) * (1000 + 100 * (L - 2))`
- 파생값 계산:
  - `level = max L where total_exp_to_reach(L) <= exp_total`
  - `exp_in_level = exp_total - total_exp_to_reach(level)`
  - `exp_to_next = exp_to_next_level(level)`
  - `exp_progress = exp_in_level / exp_to_next`
