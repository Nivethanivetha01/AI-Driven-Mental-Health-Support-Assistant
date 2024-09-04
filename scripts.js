// static/scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const resultSection = document.querySelector('.results');
    if (resultSection) {
        resultSection.style.opacity = 0;
        setTimeout(() => {
            resultSection.style.transition = 'opacity 1s ease-in';
            resultSection.style.opacity = 1;
        }, 100);
    }
});
