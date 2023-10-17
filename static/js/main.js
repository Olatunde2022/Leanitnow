
// Variables
const faqs = document.querySelectorAll('.faq')
const menu = document.querySelector('.nav__menu');
const menuBtn = document.querySelector('#open-menu-btn');
const closeBtn = document.querySelector('#close-menu-btn');


// Change navbar style on scrow
window.addEventListener('scroll', ()=>{
    document.querySelector('nav').classList.toggle('window-scroll', window.scrollY >50)
})

// // Show/hide faq answer

faqs.forEach(faq =>{
    faq.addEventListener('click',()=>{
        faq.classList.toggle('open');
        // change icon
        const icon = faq.querySelector('.faqs__icon i');
        if (icon.className === 'uil uil-plus'){
            icon.className = "uil uil-minus"
        } else{
            icon.className = "uil uil-plus"
        }
    })
})



document.addEventListener("DOMContentLoaded", function() { 
    // get the the span element
    const yrSpan = document.querySelector('.curr_year');
    // get the current year
    const currentYr = new Date().getFullYear();
    // set the year span element's text to the current year
    yrSpan.textContent = currentYr;
        });
// To show/hide menu


menuBtn.addEventListener('click', ()=>{
    menu.style.display = "flex";
    closeBtn.style.display = "inline-block";
    menuBtn.style.display = "none";
})

const closeNav =  () => {
    menu.style.display = "none";
    closeBtn.style.display = "none";
    menuBtn.style.display = "inline-block";
}

closeBtn.addEventListener('click', closeNav)