$(window).load(function () {

    $(".hexagon").hover(function(){
      $('.hexagon').stop().animate({ "margin-left": '46%' }, {queue: false});
    });
          $(".hexagon").mouseleave(function(){
            $('.hexagon').stop().animate({ "margin-left": '50%' }, {queue: false});
          });
              $(".hexagon2").hover(function(){
                $('.hexagon2').stop().animate({ "margin-left": '60%' }, {queue: false});
              });
                    $(".hexagon2").mouseleave(function(){
                      $('.hexagon2').stop().animate({ "margin-left": '56%' }, {queue: false});
                    });


});
