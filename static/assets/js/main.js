

(function ($) {
  "use strict";

  // ==========================================
  //      Start Document Ready function
  // ==========================================
  $(document).ready(function () {

  // =============== 01. Header Hide Js Click On Body Js Start =========
  $('.header-button').on('click', function() {
    $('.body-overlay').toggleClass('show')
  }); 
  $('.body-overlay').on('click', function() {
    $('.header-button').trigger('click')
    $(this).removeClass('show');
  }); 
  // =============== Header Hide Click On Body Js End =========
  
   //  ===============================02. category sidebar js Start =============================== 
    $('.header-category').on('click', function() {
      $('.category').toggleClass('show-sidebar');
      
      $('.sidebar-overlay').toggleClass('show');
   });
   
    $('.close-sidebar, .sidebar-overlay').on('click', function() {
        $('.category').removeClass('show-sidebar')
        $('.sidebar-overlay').removeClass('show')
    });
   //  =============================== category Sidebar js End =============================== 

  //  ===================================03. Card Delete Js Start Here ===========================
  $('.delete-icon').on('click', function() {
    $(this).closest('tr').addClass('d-none')
  }); 
  //  =================================== Card Delete Js End Here ===========================
   
    // ===========================04. Main header category js start here ===========================================
    $('.header-category-two__item').on('click', function() {
      $('.category-two').toggleClass('show-sidebar');

      $('.sidebar-overlay').toggleClass('show');
   });
   
    $('.close-sidebar, .sidebar-overlay').on('click', function() {
        $('.category-two').removeClass('show-sidebar')
        $('.sidebar-overlay').removeClass('show')
    });

    $('.has-dropdown').on('click', function(){
      $(this).find(".category-dropdown").slideToggle(300); 
    });
    // =========================== Main header category js End here ===========================================

    // ======================05. category two js Start ===================================
    $('.category-menu-two__link').on('click', function(){
      $(this).toggleClass('rotate')
    });
    // category js 
    $('.category-menu__link').on('click', function(){
      $(this).toggleClass('show-one')
    });
    // category js 
    // ==========================category two js End ===================================

    //  ==========================06. category rotate js Start ========================== 
    $('.has-dropdown-two').on('click', function(){
      $(this).find(".category-dropdown-two").slideToggle(300); 
    });
    //  ========================== category rotate js End ========================== 

    // ============================07. product sidebar js start ====================
    $('.product-sidebar-filter__button').on('click', function() {
      $('.left-sidebar').addClass('show-product-sidebar')
      $('.sidebar-overlay').addClass('show')
    });
  
    $('.close-sidebar, .sidebar-overlay').on('click', function() {
      $('.left-sidebar').removeClass('show-product-sidebar')
      $('.sidebar-overlay').removeClass('show')
    });
   // =========================== product sidebar js end here ===========================================
   
    //  ===========================================08. product-item icon js =========================================== 
    $('.product-item__icon-style').on('click', function() {
      $(this).toggleClass('wishlisted')
    }); 
  // ===========================================09. color variant js =========================================== 
    $('.color-variant-list > li').on('click', function() {
        $(this).addClass('active').siblings().removeClass('active');
    })
  // =========================================== color variant js end =========================================== 

  // ==========================10. Countdown Js Start Here =================================
    $('#countdown-container').ClassyCountdown({
      theme: "white", 
      
      // end time
      now: $.now(), 
      end: $.now() + 28988645600,

      
      // whether to display the days/hours/minutes/seconds labels.
      labels: true,
      
      // object that specifies different language phrases for says/hours/minutes/seconds as well as specific CSS styles.
      labelsOptions: {
        lang: {
          days: 'Days',
          hours: 'Hours',
          minutes: 'Minutes',
          seconds: 'Seconds'
        },
        style: 'font-size: 16px;'
      },
      
      // custom style for the countdown
      style: {
        element: '',
        labels: false,
        days: {
          gauge: {
            thickness: 0.07,
            bgColor: 'rgba(127, 77, 79, 0.2)',
            fgColor: 'rgba(127, 77, 79, 1)',
            lineCap: 'butt'
          },
          textCSS: ''
        },
        hours: {
          gauge: {
            thickness: 0.07,
            bgColor: 'rgba(127, 77, 79, 0.2)',
            fgColor: 'rgba(127, 77, 79, 1)',
            lineCap: 'butt'
          },
          textCSS: ''
        },
        minutes: {
          gauge: {
            thickness: 0.07,
            bgColor: 'rgba(127, 77, 79, 0.2)',
            fgColor: 'rgba(127, 77, 79, 1)',
            lineCap: 'butt'
          },
          textCSS: ''
        },
        seconds: {
          gauge: {
            thickness: 0.07,
            bgColor: 'rgba(127, 77, 79, 0.2)',
            fgColor: 'rgba(127, 77, 79, 1)',
            lineCap: 'butt'
          },
          textCSS: ''
        }
      },
      
      // callback that is fired when the countdown reaches 0.
      onEndCallback: function() {}
      
    });
  // ========================== Countdown Js End Here =================================

    // =========================11. Slick Slider Js Start ==============
    $('.testimonial-slick-slider').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      speed: 1500,
      asNavFor: '.testimonials-thumb-slider',
      dots: true,
      fade:true,
      pauseOnHover: true,
      arrows: false,
      prevArrow: '<button type="button" class="slick-prev"><i class="fas fa-long-arrow-alt-right"></i></button>',
      nextArrow: '<button type="button" class="slick-next"><i class="fas fa-long-arrow-alt-left"></i></button>',
      responsive: [
          {
            breakpoint: 1199,
            settings: {
              arrows: false,
              slidesToShow: 1,
              dots: true,
            }
          },
          {
            breakpoint: 991,
            settings: {
              arrows: false,
              slidesToShow: 1
            }
          },
          {
            breakpoint: 767,
            settings: {
              arrows: false,
              slidesToShow: 1
            }
          }
        ]
    });
    // testimonial thumb slider
    $('.testimonials-thumb-slider').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      asNavFor: '.testimonial-slick-slider',
      arrows: false,
      dots: false,
      fade:true,
      focusOnSelect: true,
      autoplay: true,
      speed: 1500,
      autoplaySpeed: 2000,
    });
    // =============================12. slick slider two =========================
   
    $('.testimonial-two-slick-slider').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      asNavFor: '.testimonial-two-thumb',
      speed: 1500,
      dots: false,
      pauseOnHover: true,
      arrows: true,
      fade: true,
      prevArrow: '<button type="button" class="slick-prev"><i class="las la-angle-right"></i></button>',
      nextArrow: '<button type="button" class="slick-next"><i class="las la-angle-left"></i></button>',
      responsive: [
          {
            breakpoint: 1199,
            settings: {
              arrows: true,
              slidesToShow: 1,
              dots: false,
            }
          },
          {
            breakpoint: 991,
            settings: {
              arrows: true,
              slidesToShow: 1
            }
          },
          {
            breakpoint: 767,
            settings: {
              arrows: true,
              slidesToShow: 1
            }
          }
        ]
    });
    $('.testimonial-two-thumb').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      asNavFor: '.testimonial-two-slick-slider',
      arrows: false,
      dots: false,
      fade:true,
      focusOnSelect: true,
      autoplay: true,
      speed: 1500,
      autoplaySpeed: 2000,
    });
  // ===============================13. latest blog slider js======================
    $('.latest-blog-slider').slick({
      slidesToShow: 2,
      slidesToScroll: 1,
      // autoplay: true,
      autoplaySpeed: 2000,
      speed: 1500,
      dots: false,
      pauseOnHover: true,
      arrows: true,
      prevArrow: '<button type="button" class="slick-prev"><i class="las la-angle-left"></i></button>',
      nextArrow: '<button type="button" class="slick-next"><i class="las la-angle-right"></i></button>',
      responsive: [
          {
            breakpoint: 1199,
            settings: {
              arrows: true,
              slidesToShow: 1,
              dots: false,
            }
          },
          {
            breakpoint: 991,
            settings: {
              arrows: true,
              slidesToShow: 1
            }
          },
          {
            breakpoint: 767,
            settings: {
              arrows: true,
              slidesToShow: 1
            }
          },
          {
            breakpoint: 424,
            settings: {
              arrows: false,
              dots:true,
              slidesToShow: 1
            }
          }
        ]
    });
  // ========================= Slick Slider Js End ===================
  // ========================14. tooltip js start here ==================
   const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
   const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
  //======================== tooltip end here =======================
      // ==================15. password Show Hide Js Start ==========
      $(".toggle-password").on('click', function() {
        $(this).toggleClass(" fa-eye-slash");
        var input = $($(this).attr("id"));
        if (input.attr("type") == "password") {
        input.attr("type", "text");
        } else {
        input.attr("type", "password");
        }
      });
    // =============== Password Show Hide Js End =================

  // =========================16. Sidebar Gallery magnific Popup Icon Js Start =====================
  $('.gallery-popup').magnificPopup({
    type: 'image',
    gallery:{
      enabled:true
    }
  });
// ========================= Sidebar Gallery magnific Popup Icon Js End =====================

  // =========================17. Client Slider Js Start ===============
  $('.client-slider').slick({
    slidesToShow: 6,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
    pauseOnHover: true,
    speed: 2000 ,
    dots: false,
    arrows: false,
    prevArrow: '<button type="button" class="slick-prev"><i class="fas fa-long-arrow-alt-right"></i></button>',
    nextArrow: '<button type="button" class="slick-next"><i class="fas fa-long-arrow-alt-left"></i></button>',
    responsive: [
        {
          breakpoint: 1199,
          settings: {
            slidesToShow:6,
          }
        },
        {
          breakpoint: 991,
          settings: {
            slidesToShow: 5
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 3
          }
        },
        {
          breakpoint: 400,
          settings: {
            slidesToShow: 2
          }
        }
      ]
  });
// ========================= Client Slider Js End ===================

//========================18. product details slider js=========================
$('.product-details__thumb').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.product-details-gallery',
});

$('.product-details-gallery').slick({
slidesToShow: 4,
slidesToScroll: 1,
asNavFor: '.product-details__thumb',
dots: false,
arrows: false,
centerMode: false,
focusOnSelect: true,
 responsive: [
  {
    breakpoint: 1200,
    settings: {
      slidesToShow: 4,
      slidesToScroll: 1
    }
  },
  {
    breakpoint: 991,
    settings: {
      slidesToShow: 4,
      slidesToScroll: 1
    }
  },
  {
    breakpoint: 768,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 1
    }
  },
  {
    breakpoint: 676,
    settings: {
      slidesToShow: 3,
      slidesToScroll: 1
    }
  },
  {
    breakpoint: 460,
    settings: {
      slidesToShow: 2,
      slidesToScroll: 1
    }
  },
]
});
// ==========slider js end========
// =================19. Increament & Decreament Js Start ======
  const productQty = $(".product-qty");
  productQty.each(function () {
    const qtyIncrement = $(this).find(".product-qty__increment");
    const qtyDecrement = $(this).find(".product-qty__decrement");
    let qtyValue = $(this).find(".product-qty__value");
    qtyIncrement.on("click", function () {
      var oldValue = parseFloat(qtyValue.val());
      var newVal = oldValue + 1;
      qtyValue.val(newVal).trigger("change");
    });
    qtyDecrement.on("click", function () {
      var oldValue = parseFloat(qtyValue.val());
      if (oldValue <= 0) {
        var newVal = oldValue;
      } else {
        var newVal = oldValue - 1;
      }
      qtyValue.val(newVal).trigger("change");
    });
  });
  // ======================= Increament & Decreament Js End ====================

  // =========================20. Range Slider Ui Js Start =====================
  $( "#slider-range" ).slider({
    range: true,
    min: 0,
    max: 500,
    values: [ 75, 300 ],
    slide: function( event, ui ) {
      $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
    }
  });
  $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
    " - $" + $( "#slider-range" ).slider( "values", 1 ) );
  // ========================= Range Slider Ui Js End =====================
 
  });
  // ==========================================
  //      End Document Ready function
  // ==========================================

  // =========================21. Preloader Js Start =====================
    $(window).on("load", function(){
      $('.preloader').fadeOut(); 
    })
  // ========================= Preloader Js End =====================

    // =========================22. Header Sticky Js Start ==============
    $(window).on('scroll', function() {
      if ($(window).scrollTop() >= 200) {
        $('.header').addClass('fixed-header');
      }
      else {
          $('.header').removeClass('fixed-header');
      }
    }); 
    // =================== header-two js =======================
    $(window).on('scroll', function() {
      if ($(window).scrollTop() >= 200) {
        $('.header-two').addClass('fixed-header');
      }
      else {
          $('.header-two').removeClass('fixed-header');
      }
    }); 
    // ================= header-two js end ========================================

    // ================= main-header js start here ========================================
    $(window).on('scroll', function() {
      if ($(window).scrollTop() >= 200) {
        $('.main-header').addClass('fixed-header');
      }
      else {
          $('.main-header').removeClass('fixed-header');
      }
    }); 
    // ========================= Header Sticky Js End===================

    // ============23. magnific popup Start ======================================
    var videoItem = $(".video-play");
    if (videoItem) {
      videoItem.magnificPopup({
        type: "iframe",
      });
    };
   // ============ magnific popup End ======================================

    //============================24. Scroll To Top Icon Js Start =========
    var btn = $('.scroll-top');

    $(window).scroll(function() {
      if ($(window).scrollTop() > 300) {
        btn.addClass('show');
      } else {
        btn.removeClass('show');
      }
    });

    btn.on('click', function(e) {
      e.preventDefault();
      $('html, body').animate({scrollTop:0}, '300');
    });
//========================= Scroll To Top Icon Js End ======================


})(jQuery);

