# [003] Reflect SCSS Update Plan

## 1. Goal Description
Migrate the project's styling system from plain CSS to SCSS/Sass in accordance with the updated `FE_STACK.md` and `FE_STYLING.md`.

## 2. Updated Requirements
- **Stack**: Sass (dart-sass)
- **Convention**:
    - Global styles must reside in `src/styles/*.scss`.
    - Components must use `<style scoped lang="scss">`.
    - `tokens.json` should be generated as `tokens.scss` (Variable format: `$token-name` or CSS variables in SCSS).
    - *Note*: `FE_STYLING.md` still mentions "Tokens are mapped to CSS Variables". So we will keep CSS variables (`--color-bg`) but define them in a `.scss` file, or simply rename `main.css` to `main.scss` and ensure the build chain supports it. The key requirement is **"Styling file extension must be .scss"**.

## 3. Scope
- [ ] Install `sass` (`sass-embedded` or `sass`)
- [ ] Rename `src/styles/tokens.css` -> `src/styles/tokens.scss`
- [ ] Rename `src/styles/main.css` -> `src/styles/main.scss`
- [ ] Update `src/main.ts` import
- [ ] Update `scripts/generate-tokens.js` to output `.scss` file (content can still be `:root { --var: ... }` as valid SCSS, but file extension must match conventions).
- [ ] Verify `App.vue` uses `lang="scss"`.

## 4. Verification Plan
- [ ] **Automated**: `npm run dev` should pass without errors.
- [ ] **Manual**: Check browser DevTools to ensure styles are applied correctly.
