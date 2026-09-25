(() => {
  const aside = document.querySelector(".hero-aside");
  const copy = aside?.querySelector(".vision-copy");
  const photo = aside?.querySelector(".profile-avatar");
  if (!aside || !copy || !photo) return;

  const aspectRatio = Number(photo.getAttribute("width")) / Number(photo.getAttribute("height"));
  if (!Number.isFinite(aspectRatio) || aspectRatio <= 0) return;

  let pendingFrame = 0;

  function fitPhoto() {
    aside.classList.remove("hero-aside-stacked");
    aside.style.removeProperty("grid-template-columns");

    const availableWidth = aside.getBoundingClientRect().width;
    const gap = parseFloat(getComputedStyle(aside).columnGap) || 0;
    const maximumWidth = Math.min(240, (availableWidth - gap) * 0.34);
    const minimumWidth = Math.min(88, maximumWidth);
    const extraHeight = 24;
    let fittedWidth = null;

    for (let width = minimumWidth; width <= maximumWidth; width += 4) {
      aside.style.gridTemplateColumns = `${width}px minmax(0, 1fr)`;
      if (width / aspectRatio >= copy.getBoundingClientRect().height + extraHeight) {
        fittedWidth = width;
        break;
      }
    }

    if (fittedWidth === null) {
      aside.style.gridTemplateColumns = `${maximumWidth}px minmax(0, 1fr)`;
      if (maximumWidth / aspectRatio >= copy.getBoundingClientRect().height + extraHeight) {
        fittedWidth = maximumWidth;
      }
    }

    if (fittedWidth === null) {
      aside.style.removeProperty("grid-template-columns");
      aside.classList.add("hero-aside-stacked");
    } else {
      aside.style.gridTemplateColumns = `${fittedWidth}px minmax(0, 1fr)`;
    }
  }

  function scheduleFit() {
    if (pendingFrame) return;
    pendingFrame = requestAnimationFrame(() => {
      pendingFrame = 0;
      fitPhoto();
    });
  }

  const observer = new ResizeObserver(scheduleFit);
  observer.observe(aside);
  observer.observe(copy);
  window.addEventListener("resize", scheduleFit);
  document.fonts?.ready.then(scheduleFit);
  scheduleFit();
})();
