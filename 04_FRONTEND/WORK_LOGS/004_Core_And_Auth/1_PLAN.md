# [004] Core Infra & Auth Feature Plan

## 1. Goal
Implement the "Thin Core" infrastructure (API Client, Auth Token) and the first vertical feature "Authentication" (Login, Signup flow).

## 2. Requirements (Strict Adherence to Datasource)
- **Stack**: Vue 3, Pinia, Axios, SCSS (`FE_STACK.md`)
- **API Client**: Centralized in `src/api`, handle `error.code`, manage JWT (`FE_API_CLIENT.md`)
- **Routing**: Use UPPERCASE route names like `WELCOME`, `LOGIN` (`FE_ROUTING_RULES.md`)
- **State**: Auth state in Pinia, synced with LocalStorage/Token (`FE_STATE_RULES.md`)
- **Styling**: SCSS, Tokens from `src/styles/tokens.scss` (`FE_STYLING.md`)

## 3. Scope

### Phase 0: Thin Core
- [ ] Install `axios`
- [ ] `src/api/axios.ts`: Axios instance with Interceptors (Request: Inject Token, Response: Error Handling)
- [ ] `src/stores/auth.ts`: Pinia store for User/Token management

### Phase 1: Auth Feature
- [ ] `src/api/auth.ts`: Endpoints for `/auth/kakao/login`, `/auth/signup`, `/auth/refresh`
- [ ] `src/pages/auth/LoginPage.vue`: UI for Kakao Login (Redirect handling)
- [ ] `src/pages/auth/SignupPage.vue`: Additional info form (Nickname, Language)
- [ ] `src/pages/welcome/WelcomePage.vue`: Landing page
- [ ] `src/router/routes.ts`: Define routes (`WELCOME`, `LOGIN`, `SIGNUP`)

## 4. Verification
- **Automated**: Check for no TS errors.
- **Manual**:
    1. access `/welcome` -> Render success
    2. access `/login` -> Mock API call -> Store update -> Redirect
