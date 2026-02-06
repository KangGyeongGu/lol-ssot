# OPENAPI (REST)

## 0. 작업 양식
엔드포인트/스키마 추가 시 아래 절차를 따른다.

```
[변경 목적]
- 왜 필요한가

[스키마 변경]
- 추가/수정 스키마 명

[엔드포인트 변경]
- METHOD /path
- 요청/응답 스키마
- 가능한 에러 코드

[동기화 체크]
- CONVENTIONS.md
- AUTH_GUARDS.md
- ERROR_MODEL.md
- API_SUMMARY.md
```

---
## 1. 문서 목적
이 문서는 League Of Algo Logic 프로젝트의 REST API 계약을 정의한다.
본 문서는 REST API에 대한 **단일 진실(Single Source of Truth)** 이며,
실시간(WebSocket/STOMP) 계약은 포함하지 않는다.

## 관련 문서
- [[03_API/CONTRACT/REST/API_SUMMARY.md]]
- [[03_API/CONTRACT/REST/CONVENTIONS.md]]
- [[03_API/CONTRACT/REST/AUTH_GUARDS.md]]
- [[03_API/CONTRACT/REST/ERROR_MODEL.md]]

---

openapi: 3.0.3
info:
  title: League Of Algo Logic REST API
  version: "1.0.0"
servers:
  - url: /api/v1

security:
  - BearerAuth: []

tags:
  - name: Auth
  - name: Users
  - name: Rooms
  - name: Games
  - name: Catalog
  - name: Stats

components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

  schemas:
    Meta:
      type: object
      required: [requestId, serverTime]
      properties:
        requestId:
          type: string
        serverTime:
          type: string
          format: date-time

    SuccessEnvelope:
      type: object
      required: [data, meta]
      properties:
        data: {}
        meta:
          $ref: "#/components/schemas/Meta"

    ErrorEnvelope:
      type: object
      required: [error, meta]
      properties:
        error:
          type: object
          required: [code, message]
          properties:
            code:
              type: string
            message:
              type: string
            details:
              type: object
              additionalProperties: true
        meta:
          $ref: "#/components/schemas/Meta"

    PageCursor:
      type: object
      required: [limit, nextCursor]
      properties:
        limit:
          type: integer
        nextCursor:
          type: string
          nullable: true

    GameType:
      type: string
      enum: [NORMAL, RANKED]

    Language:
      type: string
      enum: [JAVA, PYTHON, CPP, JAVASCRIPT]

    PlayerState:
      type: string
      enum: [READY, UNREADY, DISCONNECTED]

    GameStage:
      type: string
      enum: [LOBBY, BAN, PICK, SHOP, PLAY, FINISHED]

    RoomStatus:
      type: string
      enum: [WAITING, IN_GAME]

    PageRoute:
      type: string
      enum: [WAITING_ROOM, BAN_PICK_SHOP, IN_GAME]

    MatchResult:
      type: string
      enum: [WIN, LOSE, DRAW]

    UserSummary:
      type: object
      required: [userId, nickname, tier, score]
      properties:
        userId:
          type: string
        nickname:
          type: string
        tier:
          type: string
        score:
          type: integer

    UserProfile:
      type: object
      required: [userId, nickname, language, tier, score, exp, coin]
      properties:
        userId:
          type: string
        nickname:
          type: string
        language:
          $ref: "#/components/schemas/Language"
        tier:
          type: string
        score:
          type: integer
        exp:
          type: number
          format: double
        coin:
          type: integer

    UserStats:
      type: object
      required: [games, wins, losses, draws, winRate]
      properties:
        games:
          type: integer
        wins:
          type: integer
        losses:
          type: integer
        draws:
          type: integer
        winRate:
          type: number

    MatchSummary:
      type: object
      required: [matchId, gameType, result, scoreDelta, playedAt]
      properties:
        matchId:
          type: string
        gameType:
          $ref: "#/components/schemas/GameType"
        result:
          $ref: "#/components/schemas/MatchResult"
        scoreDelta:
          type: integer
        playedAt:
          type: string
          format: date-time

    ActiveGame:
      type: object
      required: [gameId, roomId, stage, pageRoute, gameType]
      properties:
        gameId:
          type: string
        roomId:
          type: string
        stage:
          $ref: "#/components/schemas/GameStage"
          description: 진행 중 게임의 stage만 포함하며 FINISHED는 반환되지 않는다.
        pageRoute:
          $ref: "#/components/schemas/PageRoute"
          description: stage 기준 프론트 라우팅 식별자. FINISHED는 active game에 포함되지 않는다.
        gameType:
          $ref: "#/components/schemas/GameType"
        remainingMs:
          type: integer

    RoomSummary:
      type: object
      required: [roomId, roomName, gameType, language, maxPlayers, currentPlayers, roomStatus, joinable, updatedAt]
      properties:
        roomId:
          type: string
        roomName:
          type: string
        gameType:
          $ref: "#/components/schemas/GameType"
        language:
          $ref: "#/components/schemas/Language"
        maxPlayers:
          type: integer
          minimum: 2
          maximum: 6
        currentPlayers:
          type: integer
          minimum: 0
          maximum: 6
        roomStatus:
          $ref: "#/components/schemas/RoomStatus"
        joinable:
          type: boolean
          description: 현재 사용자 기준 참가 가능 여부
        updatedAt:
          type: string
          format: date-time

    RoomPlayer:
      type: object
      required: [user, state, isHost]
      properties:
        user:
          $ref: "#/components/schemas/UserSummary"
        state:
          $ref: "#/components/schemas/PlayerState"
        isHost:
          type: boolean

    RoomDetail:
      type: object
      required: [roomId, roomName, gameType, language, maxPlayers, players]
      properties:
        roomId:
          type: string
        roomName:
          type: string
        gameType:
          $ref: "#/components/schemas/GameType"
        language:
          $ref: "#/components/schemas/Language"
        maxPlayers:
          type: integer
        players:
          type: array
          items:
            $ref: "#/components/schemas/RoomPlayer"

    CreateRoomRequest:
      type: object
      required: [roomName, gameType, language, maxPlayers]
      properties:
        roomName:
          type: string
          minLength: 1
          maxLength: 30
        gameType:
          $ref: "#/components/schemas/GameType"
        language:
          $ref: "#/components/schemas/Language"
        maxPlayers:
          type: integer
          minimum: 2
          maximum: 6

    KickRequest:
      type: object
      required: [targetUserId]
      properties:
        targetUserId:
          type: string

    GamePlayer:
      type: object
      required: [userId, nickname, score]
      properties:
        userId:
          type: string
        nickname:
          type: string
        score:
          type: integer

    InventoryItem:
      type: object
      required: [itemId, quantity]
      properties:
        itemId:
          type: string
        quantity:
          type: integer

    InventorySpell:
      type: object
      required: [spellId, quantity]
      properties:
        spellId:
          type: string
        quantity:
          type: integer

    Inventory:
      type: object
      required: [items, spells]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/InventoryItem"
        spells:
          type: array
          items:
            $ref: "#/components/schemas/InventorySpell"

    GameState:
      type: object
      required: [gameId, roomId, gameType, stage, remainingMs, coin]
      properties:
        gameId:
          type: string
        roomId:
          type: string
        gameType:
          $ref: "#/components/schemas/GameType"
        stage:
          $ref: "#/components/schemas/GameStage"
        remainingMs:
          type: integer
        players:
          type: array
          items:
            $ref: "#/components/schemas/GamePlayer"
        coin:
          type: integer
        inventory:
          $ref: "#/components/schemas/Inventory"

    BanPickRequest:
      type: object
      required: [algorithmId]
      properties:
        algorithmId:
          type: string

    ShopItemRequest:
      type: object
      required: [itemId, quantity]
      properties:
        itemId:
          type: string
        quantity:
          type: integer

    ShopSpellRequest:
      type: object
      required: [spellId, quantity]
      properties:
        spellId:
          type: string
        quantity:
          type: integer

    SubmissionRequest:
      type: object
      required: [language, sourceCode]
      properties:
        language:
          $ref: "#/components/schemas/Language"
        sourceCode:
          type: string

    LoginRequest:
      type: object
      required: [authorizationCode]
      properties:
        authorizationCode:
          type: string

    AuthTokens:
      type: object
      required: [accessToken, refreshToken]
      properties:
        accessToken:
          type: string
        refreshToken:
          type: string

    LoginResponse:
      type: object
      required: [result]
      properties:
        result:
          type: string
          enum: [OK, SIGNUP_REQUIRED]
        accessToken:
          type: string
        refreshToken:
          type: string
        signupToken:
          type: string
        user:
          $ref: "#/components/schemas/UserSummary"

    SignupRequest:
      type: object
      required: [signupToken, nickname, language]
      properties:
        signupToken:
          type: string
        nickname:
          type: string
          minLength: 1
          maxLength: 20
        language:
          $ref: "#/components/schemas/Language"

    SignupResponse:
      type: object
      required: [accessToken, refreshToken, user]
      properties:
        accessToken:
          type: string
        refreshToken:
          type: string
        user:
          $ref: "#/components/schemas/UserSummary"

    AlgorithmSummary:
      type: object
      required: [algorithmId, name]
      properties:
        algorithmId:
          type: string
        name:
          type: string

    ItemSummary:
      type: object
      required: [itemId, name, price, durationSec]
      properties:
        itemId:
          type: string
        name:
          type: string
        description:
          type: string
          nullable: true
        durationSec:
          type: integer
          minimum: 1
        price:
          type: integer

    SpellSummary:
      type: object
      required: [spellId, name, price, durationSec]
      properties:
        spellId:
          type: string
        name:
          type: string
        description:
          type: string
          nullable: true
        durationSec:
          type: integer
          minimum: 1
        price:
          type: integer

    PlayerRanking:
      type: object
      required: [rank, userId, nickname, score, tier]
      properties:
        rank:
          type: integer
        userId:
          type: string
        nickname:
          type: string
        score:
          type: integer
        tier:
          type: string

    AlgorithmPickBanRate:
      type: object
      required: [algorithmId, name, pickRate, banRate]
      properties:
        algorithmId:
          type: string
        name:
          type: string
        pickRate:
          type: number
        banRate:
          type: number

    PagedRoomList:
      type: object
      required: [items, page, listVersion]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/RoomSummary"
        page:
          $ref: "#/components/schemas/PageCursor"
        listVersion:
          type: integer
          format: int64
          description: 방 목록 스냅샷 버전 (ROOM_LIST 실시간 동기화 기준)

    PagedMatchList:
      type: object
      required: [items, page]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/MatchSummary"
        page:
          $ref: "#/components/schemas/PageCursor"

    ListOfAlgorithms:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/AlgorithmSummary"

    ListOfItems:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/ItemSummary"

    ListOfSpells:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/SpellSummary"

    ListOfPlayerRankings:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/PlayerRanking"

    ListOfAlgorithmPickBanRates:
      type: object
      required: [items]
      properties:
        items:
          type: array
          items:
            $ref: "#/components/schemas/AlgorithmPickBanRate"

paths:
  /auth/kakao/login:
    post:
      tags: [Auth]
      summary: 카카오 로그인
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/LoginRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/LoginResponse"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /auth/signup:
    post:
      tags: [Auth]
      summary: 카카오 로그인 이후 회원가입
      security: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/SignupRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/SignupResponse"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /auth/logout:
    post:
      tags: [Auth]
      summary: 로그아웃
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/SuccessEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /users/me:
    get:
      tags: [Users]
      summary: 내 프로필 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/UserProfile"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /users/me/active-game:
    get:
      tags: [Users]
      summary: active game 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        oneOf:
                          - $ref: "#/components/schemas/ActiveGame"
                          - type: "null"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /users/me/stats:
    get:
      tags: [Users]
      summary: 내 통계 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/UserStats"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /users/me/matches:
    get:
      tags: [Users]
      summary: 전적 목록 조회
      parameters:
        - name: cursor
          in: query
          schema:
            type: string
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/PagedMatchList"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms:
    get:
      tags: [Rooms]
      summary: 방 목록 조회
      parameters:
        - name: roomName
          in: query
          schema:
            type: string
        - name: language
          in: query
          schema:
            $ref: "#/components/schemas/Language"
        - name: gameType
          in: query
          schema:
            $ref: "#/components/schemas/GameType"
        - name: cursor
          in: query
          schema:
            type: string
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/PagedRoomList"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

    post:
      tags: [Rooms]
      summary: 방 생성
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/CreateRoomRequest"
      responses:
        "200":
          description: 생성됨
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 진행 중 게임 존재
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}:
    get:
      tags: [Rooms]
      summary: 방 상세 조회
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/join:
    post:
      tags: [Rooms]
      summary: 방 참가
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "403":
          description: 권한 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/leave:
    post:
      tags: [Rooms]
      summary: 방 나가기
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/SuccessEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/ready:
    post:
      tags: [Rooms]
      summary: READY 설정
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/unready:
    post:
      tags: [Rooms]
      summary: UNREADY 설정
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/start:
    post:
      tags: [Rooms]
      summary: 게임 시작
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ActiveGame"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "403":
          description: 권한 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /rooms/{roomId}/kick:
    post:
      tags: [Rooms]
      summary: 플레이어 강퇴
      parameters:
        - name: roomId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/KickRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/RoomDetail"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "403":
          description: 권한 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/state:
    get:
      tags: [Games]
      summary: 게임 상태 조회
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/ban:
    post:
      tags: [Games]
      summary: 밴 제출
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/BanPickRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/pick:
    post:
      tags: [Games]
      summary: 픽 제출
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/BanPickRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/shop/items:
    post:
      tags: [Games]
      summary: 아이템 구매
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ShopItemRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/shop/spells:
    post:
      tags: [Games]
      summary: 스펠 구매
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/ShopSpellRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /games/{gameId}/submissions:
    post:
      tags: [Games]
      summary: 코드 제출
      parameters:
        - name: gameId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/SubmissionRequest"
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/GameState"
        "400":
          description: 잘못된 요청
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "404":
          description: 리소스 없음
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "409":
          description: 상태 충돌
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /catalog/algorithms:
    get:
      tags: [Catalog]
      summary: 알고리즘 목록 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ListOfAlgorithms"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /catalog/items:
    get:
      tags: [Catalog]
      summary: 아이템 목록 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ListOfItems"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /catalog/spells:
    get:
      tags: [Catalog]
      summary: 스펠 목록 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ListOfSpells"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /stats/realtime/player-rankings:
    get:
      tags: [Stats]
      summary: 실시간 플레이어 랭킹 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ListOfPlayerRankings"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

  /stats/realtime/algorithm-pick-ban-rates:
    get:
      tags: [Stats]
      summary: 실시간 알고리즘 밴/픽률 조회
      responses:
        "200":
          description: 성공
          content:
            application/json:
              schema:
                allOf:
                  - $ref: "#/components/schemas/SuccessEnvelope"
                  - type: object
                    properties:
                      data:
                        $ref: "#/components/schemas/ListOfAlgorithmPickBanRates"
        "401":
          description: 인증 실패
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "429":
          description: 요청 제한
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"
        "500":
          description: 서버 오류
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ErrorEnvelope"

---

## 고정 원칙
- 본 문서는 REST API 계약의 단일 진실이다.
- 실시간 이벤트/채팅/타이핑/아이템 효과는 WebSocket 계약에서 정의한다.
