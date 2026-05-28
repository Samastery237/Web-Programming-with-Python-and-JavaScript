if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', '0');
}

function updateCounter() {
    let count = parseInt(localStorage.getItem('counter'), 10) + 1;
    localStorage.setItem('counter', count);
    document.getElementById('counter-heading').textContent = count;
    
    if (count % 10 === 0) {
        console.log(`Counter is at ${count}!`); 
    }
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('counter-heading').textContent = localStorage.getItem('counter');

    document.getElementById('increment-btn').addEventListener('click', updateCounter);
    setInterval(updateCounter, 1000);
});