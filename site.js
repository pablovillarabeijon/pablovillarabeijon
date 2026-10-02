document.querySelectorAll('.map-carousel').forEach(carousel => {
  const slides = [...carousel.querySelectorAll('.carousel-slide')];
  let current = 0;
  function show(next) {
    current = (next + slides.length) % slides.length;
    slides.forEach((slide, index) => { slide.hidden = index !== current; });
    carousel.querySelector('[data-counter]').textContent = `${current + 1} / ${slides.length}`;
  }
  carousel.querySelector('[data-prev]').addEventListener('click', () => show(current - 1));
  carousel.querySelector('[data-next]').addEventListener('click', () => show(current + 1));
});
