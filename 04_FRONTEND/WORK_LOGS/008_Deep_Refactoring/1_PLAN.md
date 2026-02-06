# Deep Refactoring Plan: Full Frontend Codebase

## 1. Goal
Execute a comprehensive refactoring of the entire `src/pages` and `src/widgets` directories.
**Scope**: All Vue components in `04_FRONTEND`.
**Objective**: Architecture compliance, Strict Typing, and true Modularization.

## 2. Target Inventory
We will strictly audit and refactor the following modules:

### A. Pages (`src/pages`)
1.  **Auth Module** (`pages/auth/`)
    - `LoginPage.vue`: Extract generic form components if applicable. Check `any` usage in auth logic.
    - `SignupPage.vue`: Ensure validation logic is clean.
2.  **Main Module** (`pages/main/`)
    - `MainPage.vue`: Ensure layout shell is pure.
    - `panels/HubPanel.vue`: Check for logic leaks.
    - `panels/RoomListPanel.vue`: Ensure it uses `src/features/room` or `src/widgets` properly.
3.  **Room Module** (`pages/room/`)
    - `WaitingRoomPage.vue`: **Major Refactor**. Decompose into `PlayerSlot`, `ChatPanel`, `RoomSettings`.
4.  **User Module** (`pages/user/`)
    - `MyPage.vue`: Standardize layout tokens.

### B. Widgets (`src/widgets`)
1.  **Shared Widgets**
    - `RoomList.vue`: Ensure it's a "dumb" UI component or a "smart" business widget (decide and enforce).
    - `CreateRoomModal.vue`: Check for inline styles and form logic patterns.

## 3. Execution Plan

### Phase 1: Global Type Hygiene
- [ ] **Audit**: `grep` for `any` and `as string/number` across entire `src/`.
- [ ] **Fix**: Replace all occurrences with:
    - `src/api/dtos/*.types.ts`
    - `src/shared/types/*.ts`
    - Proper generic types for Events/Props.

### Phase 2: Core Components Extraction
- [ ] **Chat Feature** (`src/features/chat`)
    - Move chat logic from `WaitingRoomPage` => `useChatStore`.
    - Create `ChatPanel.vue`.
- [ ] **Room Features** (`src/features/room`)
    - Extract `PlayerSlot.vue` (Visual state machine).
    - Extract `RoomSettingsPanel.vue`.

### Phase 3: Page-by-Page Standards Enforcement
Iterate through each target ensuring:
- **No hardcoded text** (Move to `COPY_TEXT` or Constants).
- **No inline/local colors** (Use tokens).
- **No "Storytelling" comments** (Remove redundant comments).
- **Correct Layering** (Page -> Feature/Widget -> Shared UI).

#### Specific Tasks:
- [ ] Refactor `LoginPage.vue` & `SignupPage.vue`.
- [ ] Refactor `MainPage.vue` & Panels.
- [ ] Refactor `WaitingRoomPage.vue` (composition only).
- [ ] Refactor `MyPage.vue`.

## 4. Verification Guardrails
- [ ] **Strict Check**: `vue-tsc --noEmit`.
- [ ] **Component Size**: Pages should primarily composed of widgets/features, not raw HTML.
- [ ] **Console check**: No runtime validation warnings.
