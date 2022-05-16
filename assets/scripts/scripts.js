$('.ui.accordion').accordion();


function flip_me_left() {
    $('.shape').shape('flip back');
}
function flip_me_right() {
    $('.shape').shape('flip over');
}


function showhide(e, PrjctID) {
    var i, tablink, tabimgs;
    tabimgs = document.getElementsByClassName('PrjctPg');
    for (i = 0; i < tabimgs.length; i++) {
        tabimgs[i].classList.replace('visible', 'hidden');
    }
    tablink = document.getElementsByClassName('LinkHalf');
    for (i = 0; i < tablink.length; i++) {
        tablink[i].classList.remove('is-active');
    }
    document.getElementById(PrjctID).classList.replace('hidden', 'visible');
    e.currentTarget.className += ' is-active';
}
var elms = document.getElementsByClassName( 'splide' );
for ( var i = 0, len = elms.length; i < len; i++ ) {
    new Splide( elms[ i ] ).mount();
}


function project_images_modal() {
    $('.ui.modal').modal('show');
}