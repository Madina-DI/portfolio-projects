/* The developer portfolio is intentionally English-only.
   Russian and English remain available as separate CV and presentation files. */
(() => {
  document.documentElement.lang = "en";
  try { localStorage.removeItem("portfolio-language"); } catch {}
  document.querySelectorAll(".language-toggle").forEach(toggle => toggle.remove());
  document.querySelectorAll(".cv-link").forEach(link => {
    link.href = "docs/Madina_Developer_CV_EN.pdf";
  });
})();
