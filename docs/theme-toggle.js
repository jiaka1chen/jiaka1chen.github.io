(() => {
  const STORAGE_KEY = "themeMode";
  const AUTO = "auto";
  const DARK = "dark";
  const LIGHT = "light";

  function getSavedMode() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === AUTO || saved === LIGHT || saved === DARK) return saved;
    return AUTO;
  }

  function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
  }

  function systemTheme() {
    return window.matchMedia?.("(prefers-color-scheme: dark)")?.matches ? DARK : LIGHT;
  }

  // Apply early to minimize flash before DOMContentLoaded.
  // If user explicitly chose light/dark, respect it; otherwise follow system until Auto resolves.
  const earlyMode = getSavedMode();
  applyTheme(earlyMode === LIGHT || earlyMode === DARK ? earlyMode : systemTheme());

  function setToggleVisual(mode) {
    const btn = document.getElementById("theme-toggle");
    if (!btn) return;

    const icon = btn.querySelector("i");
    if (!icon) return;

    icon.classList.remove("bi-circle-half", "bi-sun", "bi-moon-stars");
    if (mode === AUTO) icon.classList.add("bi-circle-half");
    else if (mode === LIGHT) icon.classList.add("bi-sun");
    else icon.classList.add("bi-moon-stars");

    const label = mode === AUTO ? "Theme: Auto" : mode === LIGHT ? "Theme: Light" : "Theme: Dark";
    btn.setAttribute("aria-label", label);
    btn.setAttribute("title", label);
  }

  function fallbackNightByClock() {
    const h = new Date().getHours();
    return h >= 18 || h < 6;
  }

  async function resolveAutoTheme() {
    // No location permission prompts: use a simple local-time "sunset window" rule.
    applyTheme(fallbackNightByClock() ? DARK : LIGHT);
  }

  function applyMode(mode) {
    if (mode === LIGHT) applyTheme(LIGHT);
    else if (mode === DARK) applyTheme(DARK);
    else resolveAutoTheme();
  }

  function nextMode(mode) {
    if (mode === AUTO) return LIGHT;
    if (mode === LIGHT) return DARK;
    return AUTO;
  }

  function toggleMode() {
    const current = getSavedMode();
    const mode = nextMode(current);
    localStorage.setItem(STORAGE_KEY, mode);
    setToggleVisual(mode);
    applyMode(mode);
  }

  document.addEventListener("DOMContentLoaded", () => {
    const mode = getSavedMode();
    setToggleVisual(mode);
    applyMode(mode);

    const btn = document.getElementById("theme-toggle");
    if (btn) btn.addEventListener("click", toggleMode);

    const menuToggle = document.getElementById("menu-toggle");
    const nav = document.querySelector(".rail-nav");
    if (menuToggle && nav) {
      const isMobile = () => window.matchMedia?.("(max-width: 720px)")?.matches;
      const closeMenu = () => nav.classList.remove("open");

      menuToggle.addEventListener("click", () => {
        nav.classList.toggle("open");
      });

      nav.addEventListener("click", (event) => {
        if (!isMobile()) return;
        if (event.target.closest("a")) closeMenu();
      });

      document.addEventListener("click", (event) => {
        if (!isMobile() || !nav.classList.contains("open")) return;
        const target = event.target;
        if (target.closest(".rail-nav") || target.closest("#menu-toggle")) return;
        closeMenu();
      });
    }
  });
})();
