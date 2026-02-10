## 목적
- MY_PAGE 화면에 필요한 데이터/상태를 정의한다.

## 관련 문서
- [[03_API/PAGE_MAP/MY_PAGE.md]]
- [[03_API/CONTRACT/REST/OPENAPI.yaml.md]]

## Required Data
- profile: nickname, tier, score, level, exp, coin, language
- stats: win, lose, draw, winRate
- match history: matchId, gameType, result, roomTitle, finalPlayers, playedAt

## Required States
- loading (initial)
- empty match history
- error (REST)

## Prohibited
- matchId 없이 전적 항목 표시
