jQuery('document').ready(()=>{
    var scrollIndex = jQuery('#second-container').offset().top;

    

    jQuery(window).scroll(()=>{
        var scrollPos = jQuery(window).scrollTop();
     
        if(scrollPos>=60){
            jQuery('#second-container').css({
                'background-size' : 100 + 0.05*(scrollPos-500) + '%'
            })
        }

        if(scrollPos>=600){
            jQuery('#third-container').css({
                'background-size' : 100- 0.05* (scrollPos-900) + '%'
            });
        }
    });
});