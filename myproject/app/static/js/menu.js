var menu = document.getElementById('menu');
var btn = document.getElementById('menubtn');
var bg = document.getElementById('menu_bg');
var ct = document.getElementById('menu_contianer');
btn.addEventListener('click', () => {
    menu.classList.replace('opacity-0', 'opacity-100')
    // menu.classList.replace('z-[-8]', 'z-[102]')
    menu.classList.replace('max-h-[0]', 'max-h-[80vh]')
    bg.classList.replace('bg-transparent', 'bg-black')
    bg.classList.replace('opacity-0', 'opacity-80')
    bg.classList.replace('z-[-9]', 'z-[101]')
    ct.classList.replace('z-[-10]', 'z-[100]')
});

bg.addEventListener('click', () => {
    menu.classList.replace('opacity-100', 'opacity-0')
    // menu.classList.replace('z-[102]', 'z-[-8]')
    menu.classList.replace('max-h-[80vh]', 'max-h-[0]')
    bg.classList.replace('bg-black', 'bg-transparent')
    bg.classList.replace('opacity-80', 'opacity-0')
    bg.classList.replace('z-[101]', 'z-[-9]')
    ct.classList.replace('z-[100]', 'z-[-10]')
});

menu.addEventListener('click', () => {
    menu.classList.replace('opacity-100', 'opacity-0')
    // menu.classList.replace('z-[102]', 'z-[-8]')
    menu.classList.replace('max-h-[80vh]', 'max-h-[0]')
    bg.classList.replace('bg-black', 'bg-transparent')
    bg.classList.replace('opacity-80', 'opacity-0')
    bg.classList.replace('z-[101]', 'z-[-9]')
    ct.classList.replace('z-[100]', 'z-[-10]')
});

