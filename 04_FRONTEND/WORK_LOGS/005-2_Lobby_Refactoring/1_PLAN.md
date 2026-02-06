# [005-2] Lobby UI Refactoring Plan

## 1. Goal
Refactor the Lobby layer to match the premium Cyberpunk aesthetic of the provided mockups (`2. 메인페이지`, `2-2. 방리스트 조회 페이지`).
The current MVP implementation is deemed "insufficient/plain".

## 2. Design Analysis
### A. Main Hub (`/main`) - "2. 메인페이지.png"
- **Layout**: 3-Row Structure (Header / Body / Bottom Chat).
- **Body**:
  - **Left/Center**: Large Hero Banner ("Global Algorithm Championship") + 2 Action Cards (Create Match / Find Match).
  - **Right**: Ranking Sidebar (Most Banned/Picked, Top Players List).
- **Footer**: Global Chat Widget (Fixed height).

### B. Battle Rooms (`/lobby`) - "2-2. 방리스트 조회 페이지.png"
- **Header**: "Battle Rooms" Title with Back Button.
- **Filter Bar**: Create Button, Dropdowns (Languages, Types, Filter), Refresh, Search Input.
- **Room Grid**: Cyberpunk styled cards with "Join" button inside.
- **Pagination**: Numbered pagination at bottom.

## 3. Implementation Steps
1. **Asset & Style Setup**: Ensure `Oxanium` font is applied for headers. Define clear glassmorphism mixins if not present.
2. **Main Hub Components**:
   - `HeroBanner.vue`
   - `RankingSidebar.vue` (Static data for UI)
   - `GlobalChatWidget.vue` (UI only)
3. **Lobby (Room List) Components**:
   - `RoomFilterBar.vue`
   - `RoomCard.vue` (Visual overhaul)
4. **Router Update**:
   - `/main`: Main Hub
   - `/lobby`: Room List (New route)

## 4. Execution Order
1. Rename/Refactor `MainPage` to `HubPage`.
2. Create `LobbyPage` for Room List.
3. Apply rigorous styling using `tokens.scss`.
