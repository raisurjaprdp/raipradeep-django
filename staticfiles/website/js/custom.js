// website/static/website/js/custom.js

// AOS init
AOS.init({ duration: 800, once: true });

// Typed.js for hero titles
new Typed('#typed', {
  strings: ['Freelance Developer.', 'Backend Specialist.', 'Problem Solver.'],
  typeSpeed: 50,
  backSpeed: 30,
  loop: true
});

// Smooth scroll
document.querySelectorAll('.nav-link[href^="#"]').forEach(el => {
  el.addEventListener('click', e => {
    e.preventDefault();
    document.querySelector(el.getAttribute('href')).scrollIntoView({ behavior: 'smooth' });
  });
});

// Dark/light theme toggle
const btn = document.getElementById('theme-toggle');
btn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  btn.innerHTML = document.body.classList.contains('dark') ? '<i class="fa-solid fa-sun"></i>' : '<i class="fa-solid fa-moon"></i>';
});
