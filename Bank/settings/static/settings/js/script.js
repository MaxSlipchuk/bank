const darkModeToggle = document.getElementById('darkmode-toggle');
const customHeader = document.querySelector('.custom-header');

darkModeToggle.addEventListener('change', () => {
    console.log('Checkbox state changed');
    if (darkModeToggle.checked) {
        customHeader.style.backgroundColor = 'var(--header-bg-color-dark)';
    } else {
        customHeader.style.backgroundColor = 'var(--header-bg-color)';
    }
});