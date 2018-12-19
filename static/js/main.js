console.log('We in da house!')

$(document).ready(function () {
  $('.sidenav').sidenav();
  // console.log('hello');

  $('#hamburger, #crossBtn').on('click', openCloseMobileNav);

  function openCloseMobileNav() {
    $('#hamburger').toggleClass('.hamburger-icon')
    $('#crossBtn').toggleClass('hide');
    $('nav').toggleClass('small-nav');
    $('.menu').toggleClass('nav-btn-small');
  };

});