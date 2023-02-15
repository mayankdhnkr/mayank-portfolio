$(window).on("resize", function () {
  var win = $(this);
  if (win.width() > 1275) {
    $(".ribbonmainspacing").removeClass("justify-content-start");
    $(".ribbonmainspacing").addClass("justify-content-between");
    $(".ribbon-name").removeClass("order-2");
  } else {
    $(".ribbonmainspacing").removeClass("justify-content-between");
    $(".ribbonmainspacing").addClass("justify-content-start");
    $(".ribbon-name").addClass("order-2");

  }

  var win = $(this);
  if (win.width() > 580) {
    $(".res").removeClass("my-5");
    $(".folders").removeClass("my-2");
  } else {
    $(".res").addClass("my-5");
    $(".folders").addClass("my-2");
  }
});


// setInterval(function () {
//   var $webdev_icon = $("#webdev-icon");
//   if ($webdev_icon.is(":hover")) {
//     $("#webdev-icon").addClass("d-none");
//     $("#webdev-icon-colored").removeClass("d-none");
//   } 
//   else {
//     $("#webdev-icon").removeClass("d-none");
//     $("#webdev-icon-colored").addClass("d-none");
//   }
// }, 100);
