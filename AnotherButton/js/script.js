let button = document.querySelector('button');
let p = document.querySelector('p');

button.addEventListener('click', function() {
    p.textContent = 'Я же просила!!!';
    button.textContent = 'НЕ НАЖИМАТЬ!!!';
    button.style.background = 'blue';
});