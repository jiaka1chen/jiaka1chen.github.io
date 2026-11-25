(() => {
  const viewer = document.querySelector(".image-viewer");
  if (!viewer || typeof viewer.showModal !== "function") return;

  const frame = viewer.querySelector(".viewer-frame");
  for (const trigger of document.querySelectorAll(".image-trigger")) {
    trigger.setAttribute("aria-haspopup", "dialog");
    trigger.addEventListener("click", (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      const thumbnail = trigger.querySelector("img, video");
      const media = thumbnail.cloneNode(false);
      media.removeAttribute("class");
      media.removeAttribute("loading");
      if (media instanceof HTMLVideoElement) media.muted = true;
      frame.replaceChildren(media);
      const title = trigger.querySelector(".project-cover-title");
      if (title) frame.append(title.cloneNode(true));
      viewer.showModal();
    });
  }

  viewer.addEventListener("click", (event) => {
    if (event.target === viewer) viewer.close();
  });
  viewer.addEventListener("close", () => {
    frame.querySelector("video")?.pause();
    frame.replaceChildren();
  });
})();
