let button = document.querySelector('button');
let p = document.querySelector('p');
let a = document.querySelector('a');


button.addEventListener('click', function() {
    p.textContent = 'Я ЖЕ ПРОСИЛА...';
    p.style.fontSize = '3em';
    button.style.visibility = 'hidden';
    a.style.visibility = 'visible';
});

a.addEventListener('click', function() {
    p.textContent = ('Вот поэтому-то мы с тобой и не можем оставаться друзьями!...');
    $('a').hide(3000);
    $('p.textContent').show(3000);
});