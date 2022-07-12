const cupcake = document.querySelector('.cupcake');
const cake = document.querySelector('.cake');
const dounot = document.querySelector('.dounot');
const cookies = document.querySelector('.cookies');
const desert = document.querySelector('.desert');

    document.querySelector('.cake-video').classList.add("display-none");
    document.querySelector('.cake-item').classList.add("display-none");
    document.querySelector('.dounot-video').classList.add("display-none");
    document.querySelector('.dounot-item').classList.add("display-none");
    document.querySelector('.cookies-video').classList.add("display-none");
    document.querySelector('.cookies-item').classList.add("display-none");
    document.querySelector('.desert-video').classList.add("display-none");
    document.querySelector('.desert-item').classList.add("display-none");
    document.querySelector('.cupcake-video').classList.add("display-none");
    document.querySelector('.cupcake-item').classList.add("display-none");


    document.querySelector('.cake-video').classList.remove("display-none");
    document.querySelector('.cake-item').classList.remove("display-none");

cupcake.addEventListener('click',()=>{
    document.querySelector('.cake-video').classList.add("display-none");
    document.querySelector('.cake-item').classList.add("display-none");
    document.querySelector('.dounot-video').classList.add("display-none");
    document.querySelector('.dounot-item').classList.add("display-none");
    document.querySelector('.cookies-video').classList.add("display-none");
    document.querySelector('.cookies-item').classList.add("display-none");
    document.querySelector('.desert-video').classList.add("display-none");
    document.querySelector('.desert-item').classList.add("display-none");

    cake.classList.remove('active-menu');
    dounot.classList.remove('active-menu');
    cookies.classList.remove('active-menu');
    desert.classList.remove('active-menu');

    cupcake.classList.add('active-menu');

    


    document.querySelector('.cupcake-video').classList.remove("display-none");
    document.querySelector('.cupcake-item').classList.remove("display-none");
    

});

cake.addEventListener('click',()=>{
    document.querySelector('.cupcake-video').classList.add("display-none");
    document.querySelector('.cupcake-item').classList.add("display-none");
    document.querySelector('.dounot-video').classList.add("display-none");
    document.querySelector('.dounot-item').classList.add("display-none");
    document.querySelector('.cookies-video').classList.add("display-none");
    document.querySelector('.cookies-item').classList.add("display-none");
    document.querySelector('.desert-video').classList.add("display-none");
    document.querySelector('.desert-item').classList.add("display-none");
    cupcake.classList.remove('active-menu');
    dounot.classList.remove('active-menu');
    cookies.classList.remove('active-menu');
    desert.classList.remove('active-menu');

    cake.classList.add('active-menu');

    document.querySelector('.cake-video').classList.remove("display-none");
    document.querySelector('.cake-item').classList.remove("display-none");
    

});
dounot.addEventListener('click',()=>{
    document.querySelector('.cake-video').classList.add("display-none");
    document.querySelector('.cake-item').classList.add("display-none");
    document.querySelector('.cupcake-video').classList.add("display-none");
    document.querySelector('.cupcake-item').classList.add("display-none");
    document.querySelector('.cookies-video').classList.add("display-none");
    document.querySelector('.cookies-item').classList.add("display-none");
    document.querySelector('.desert-video').classList.add("display-none");
    document.querySelector('.desert-item').classList.add("display-none");
    cake.classList.remove('active-menu');
    cupcake.classList.remove('active-menu');
    cookies.classList.remove('active-menu');
    desert.classList.remove('active-menu');

    dounot.classList.add('active-menu');

    document.querySelector('.dounot-video').classList.remove("display-none");
    document.querySelector('.dounot-item').classList.remove("display-none");
    

});
cookies.addEventListener('click',()=>{
    document.querySelector('.cake-video').classList.add("display-none");
    document.querySelector('.cake-item').classList.add("display-none");
    document.querySelector('.dounot-video').classList.add("display-none");
    document.querySelector('.dounot-item').classList.add("display-none");
    document.querySelector('.cupcake-video').classList.add("display-none");
    document.querySelector('.cupcake-item').classList.add("display-none");
    document.querySelector('.desert-video').classList.add("display-none");
    document.querySelector('.desert-item').classList.add("display-none");
    cake.classList.remove('active-menu');
    dounot.classList.remove('active-menu');
    cupcake.classList.remove('active-menu');
    desert.classList.remove('active-menu');

    cookies.classList.add('active-menu');

    document.querySelector('.cookies-video').classList.remove("display-none");
    document.querySelector('.cookies-item').classList.remove("display-none");
    

});
desert.addEventListener('click',()=>{
    document.querySelector('.cake-video').classList.add("display-none");
    document.querySelector('.cake-item').classList.add("display-none");
    document.querySelector('.dounot-video').classList.add("display-none");
    document.querySelector('.dounot-item').classList.add("display-none");
    document.querySelector('.cookies-video').classList.add("display-none");
    document.querySelector('.cookies-item').classList.add("display-none");
    document.querySelector('.cupcake-video').classList.add("display-none");
    document.querySelector('.cupcake-item').classList.add("display-none");
    cake.classList.remove('active-menu');
    dounot.classList.remove('active-menu');
    cookies.classList.remove('active-menu');
    cupcake.classList.remove('active-menu');

    desert.classList.add('active-menu');

    document.querySelector('.desert-video').classList.remove("display-none");
    document.querySelector('.desert-item').classList.remove("display-none");
    

});