console.log('We in da house!')

$(document).ready(function(){
  $('.sidenav').sidenav();
  // console.log('hello');

  $('#hamburger, #crossBtn, .menu-item').on('click', openCloseMobileNav);

  function openCloseMobileNav() {
    // console.log('click...!')
    $('#hamburger').toggleClass('hamburger-icon')
    $('#crossBtn').toggleClass('hide');
    $('nav').toggleClass('small-nav');
    $('.menu').toggleClass('nav-btn-small');
  };

});


// function openCloseMobileNav() {
//     $('.fa-bars').toggleClass('hamburger-icon');
//     $('.fa-times').toggleClass('close-icon');
//     $('.fa-times').toggleClass('hide');
//     //toggle dropdown
//     $('nav').toggleClass('small-screen-nav');
//     $('.nav-buttons').toggleClass('nav-buttons-small-screen');
//     $('#navImg').toggleClass('hide');
//   };