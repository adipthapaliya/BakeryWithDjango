jQuery(document).ready(function(){
  
    var navOffSet =jQuery("nav").offset().top;
    

    jQuery(window).scroll(function(){
        var scrollPos =jQuery(window).scrollTop();

        if(scrollPos>60){
            jQuery("nav").addClass("scrolling-active");
            jQuery("nav").removeClass("bg-transparent");            
        } else{
            jQuery("nav").removeClass("scrolling-active");
            jQuery("nav").addClass("bg-transparent");

        }  
    }); 

    jQuery("navbar-toggler").click(function(){
        alert('HI');
        jQuery("nav").removeClass("bg-transparent");
        jQuery("nav").addClass("bg-dark");

    }); 
});