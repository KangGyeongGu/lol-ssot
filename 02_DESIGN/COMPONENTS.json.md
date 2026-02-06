# COMPONENTS

아래는 주요 컴포넌트 스타일 토큰 JSON이다.

```json
{
  "button": {
    "height": {"sm": 36, "md": 44, "lg": 52},
    "radius": "lg",
    "primary": {
      "bg": "color.accent.yellow",
      "text": "color.text.inverse",
      "border": "color.border.yellow",
      "glow": "glow.yellow"
    },
    "secondary": {
      "bg": "transparent",
      "text": "color.text.primary",
      "border": "color.border.cyan",
      "glow": "glow.cyan"
    },
    "danger": {
      "bg": "transparent",
      "text": "color.accent.red",
      "border": "color.accent.red",
      "glow": "glow.red"
    }
  },
  "primaryButton": {
    "base": "button.primary",
    "size": "lg"
  },
  "secondaryButton": {
    "base": "button.secondary",
    "size": "lg"
  },
  "outlineButton": {
    "base": "button.secondary",
    "size": "md"
  },
  "dangerButton": {
    "base": "button.danger",
    "size": "md"
  },
  "card": {
    "radius": "xl",
    "bg": "color.bg.panel",
    "border": "color.border.cyan",
    "shadow": "shadow.panel",
    "padding": 24
  },
  "heroCard": {
    "base": "card",
    "border": "color.border.yellow"
  },
  "statPanel": {
    "base": "card"
  },
  "settingsPanel": {
    "base": "card"
  },
  "problemCard": {
    "base": "card"
  },
  "modal": {
    "radius": "xl",
    "bg": "color.bg.panel",
    "border": "color.border.cyan",
    "shadow": "shadow.float",
    "maxWidth": 900
  },
  "input": {
    "height": 44,
    "radius": "md",
    "bg": "color.bg.panelStrong",
    "border": "color.border.cyan",
    "focusGlow": "glow.cyan"
  },
  "toggleButton": {
    "base": "tab",
    "height": 40
  },
  "chipButton": {
    "base": "chip"
  },
  "languageButton": {
    "base": "chip"
  },
  "tab": {
    "height": 44,
    "radius": "lg",
    "activeBorder": "color.border.yellow",
    "inactiveBorder": "color.border.subtle",
    "activeGlow": "glow.yellow"
  },
  "chip": {
    "height": 32,
    "radius": "md",
    "bg": "color.bg.panelStrong",
    "activeBorder": "color.border.magenta",
    "activeGlow": "glow.magenta"
  },
  "badge": {
    "height": 24,
    "radius": "md",
    "bg": "color.bg.panelStrong",
    "text": "color.text.primary"
  },
  "coinBadge": {
    "base": "badge"
  },
  "updateBadge": {
    "base": "badge"
  },
  "stageTabs": {
    "height": 56,
    "radius": "xl",
    "activeGlow": "glow.magenta"
  },
  "algorithmCard": {
    "width": 220,
    "height": 120,
    "radius": "lg",
    "border": "color.border.cyan",
    "activeBorder": "color.border.yellow"
  },
  "shopItemCard": {
    "base": "card"
  },
  "shopSpellCard": {
    "base": "card"
  },
  "playerCard": {
    "width": 420,
    "height": 100,
    "radius": "lg",
    "border": "color.border.cyan"
  },
  "lobbySlot": {
    "width": 360,
    "height": 140,
    "radius": "lg",
    "border": "color.border.cyan",
    "placeholderStyle": "dashed"
  },
  "rankingRow": {
    "height": 56,
    "radius": "md"
  },
  "inventorySlot": {
    "width": 64,
    "height": 64,
    "radius": "md",
    "badgeSize": 18
  },
  "webrtcTile": {
    "width": 260,
    "height": 140,
    "radius": "md",
    "border": "color.border.cyan"
  },
  "profileAvatar": {
    "size": 48,
    "border": "color.border.cyan"
  },
  "typingStatusBar": {
    "height": 40,
    "radius": "md",
    "bg": "color.bg.panelStrong",
    "border": "color.border.cyan"
  },
  "editorToolbar": {
    "height": 48,
    "radius": "md",
    "bg": "color.bg.panelStrong"
  },
  "resultDrawer": {
    "height": 220,
    "radius": "md",
    "bg": "color.bg.panelStrong"
  },
  "matchRow": {
    "height": 64,
    "radius": "md"
  },
  "paginationDots": {
    "base": "badge",
    "height": 20
  },
  "countdownTimer": {
    "font": "font.mono",
    "size": "2xl"
  },
  "statusChip": {
    "base": "chip"
  },
  "editor": {
    "base": "card"
  },
  "profileBar": {
    "base": "card"
  },
  "tabBar": {
    "base": "tab"
  },
  "accountCard": {
    "base": "card"
  },
  "tierCard": {
    "base": "card"
  },
  "heatmap": {
    "base": "card"
  },
  "radarChart": {
    "base": "card"
  },
  "headerCard": {
    "base": "card"
  },
  "resultRow": {
    "height": 120,
    "radius": "md"
  },
  "rewardChip": {
    "base": "chip"
  },
  "logoTitle": {
    "font": "font.display",
    "weight": 800
  },
  "subtitleText": {
    "font": "font.ui",
    "size": "md"
  },
  "helperText": {
    "font": "font.ui",
    "size": "sm"
  },
  "filterBar": {
    "base": "card"
  },
  "roomCard": {
    "base": "card"
  },
  "updateButton": {
    "base": "secondaryButton",
    "size": "sm"
  },
  "statRing": {
    "size": 120
  },
  "chat": {
    "bg": "color.bg.panel",
    "border": "color.border.yellow",
    "inputHeight": 40
  },
  "roomListSync": {
    "updateButtonHeight": 36,
    "updateButtonRadius": "md",
    "updateButtonBorder": "color.border.cyan",
    "updateButtonGlow": "glow.cyan",
    "highlightBorder": "color.border.yellow",
    "highlightGlow": "glow.yellow",
    "badgeSize": 20,
    "badgeBg": "color.accent.magenta",
    "badgeText": "color.text.inverse"
  }
}
```
