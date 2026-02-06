# Project Verification Report & Improvement Plan
**Date:** 2026-02-06
**Scope:** `src` directory, compared against `04_FRONTEND` design documents.

---

## 1. Compliance Verification

### 1.1 Architecture & Directory Structure
| Item | Status | Observation |
|---|---|---|
| `src/shared/ui` | **MISSING** | `FE_ARCHITECTURE.md` mandates `src/shared/ui` for common UI components. Currently missing. |
| `src/pages` | PASS | Route-based structure is followed. |
| `src/stores` | PASS | Pinia stores (`useRoomStore.ts`) follow the Single Source of Truth pattern. |
| `src/api` | PASS | API/Mock separation is clear. |
| `src/widgets` | WARN | `widgets` exists but `shared/ui` is missing, leading to ambiguity. |

### 1.2 Design & Styling Rules
| Item | Status | Observation |
|---|---|---|
| SCSS Usage | PASS | Scoped SCSS used correctly in `WaittingRoomPage.vue`. |
| Token Usage | **FAIL** | `WaittingRoomPage.vue` uses hardcoded alpha values (e.g., `rgba(18, 16, 30, 0.85)`), ignoring the token `0.78` or strict token mapping. `MainPage.vue` uses hardcoded pixel values (`120px`) alongside tokens. |
| Scale Rules | PASS | `WaitingRoomPage` correctly uses `vw/vh` and `clamp()` for 16:9 scaling. |
| Grid Layout | PASS | `WaitingRoomPage` correctly implements the 2x3 grid as per latest mockup. |

### 1.3 Coding Conventions
| Item | Status | Observation |
|---|---|---|
| TypeScript | PASS | No implicit `any` found. Types are imported from `dtos`. |
| Script Setup | PASS | Used correctly. |
| Comments | WARN | Some comments (e.g., in mocks or logic) may be redundant or "AI-style" rather than "collaboration-style". |

### 1.4 Component Reuse
| Item | Status | Observation |
|---|---|---|
| Common UI | **FAIL** | `WaitingRoomPage` implements its own `badge`, `action-btn` styles. These are candidates for `BaseBadge` and `BaseButton` in `shared/ui`. |

---

## 2. Improvement Plan

**Strategy:** Refactor progressively without breaking current functionality.

### Phase 1: Architecture Correction
1.  **Create `src/shared/ui`**: Initialize directory.
2.  **Extract Components**:
    *   Move `badge` styles from `WaitingRoomPage` -> `src/shared/ui/BaseBadge.vue`.
    *   Move `action-btn` styles from `WaitingRoomPage` -> `src/shared/ui/BaseButton.vue`.
    *   Ensure `BaseButton` supports variants (`primary`, `secondary`, `outline`).

### Phase 2: Strict Styling
1.  **Token Standardization**:
    *   Replace `rgba(18, 16, 30, 0.85)` with proper token usage (e.g., `rgba(var(--color-bg-panel-rgb), var(--opacity-panel))`) or strictly use defined opacity tokens.
    *   Fix `MainPage` padding to use consistent spacing tokens or percentage-based layout for responsiveness.
2.  **Common Layout**:
    *   Ensure `scaling-container` logic can be reused if needed (currently page-specific is fine, but verify).

### Phase 3: Code Cleanup
1.  **Comment Audit**: Remove "Step 1...", "Step 2..." AI-generated comments unless strictly necessary for flow understanding. Use JSDoc for complex logic.
2.  **Lint Fixes**: Ensure `mockRegistry` and other potential TS strict mode issues are resolved.
