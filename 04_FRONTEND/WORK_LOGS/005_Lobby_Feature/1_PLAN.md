# [005] Lobby & Room Feature Plan

## 1. Goal
Implement the main activity area (Lobby) and Room management system (Create/Join/List).

## 2. Requirements
- **Lobby UI**: Main navigation, User profile summary (`UserSummary` from store)
- **Room List**: Fetch active rooms via API (WebSocket listing is moved to Realtime Phase, initial verify via HTTP list)
- **Room Actions**: Create room modal, Join room flow
- **My Page**: Detailed user statistics

## 3. Scope

### API Layer
- [ ] `src/api/room.ts`: `getRooms()`, `createRoom()`, `joinRoom()`
- [ ] `src/api/dtos/room.ts`: `RoomSummary`, `CreateRoomRequest`

### Store Layer
- [ ] `src/stores/useRoomStore.ts`: Manage room list state

### UI Layer
- [ ] `src/pages/main/MainPage.vue`: The Lobby Dashboard
- [ ] `src/widgets/RoomList.vue`: Grid/List view of rooms
- [ ] `src/widgets/CreateRoomModal.vue`: Modal form
- [ ] `src/pages/user/MyPage.vue`: Profile view

## 4. Verification
- **Manual**: Check Main Page rendering after simulated login. Click "Create Room" -> API call.
