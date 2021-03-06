$(function(){
  function getCookie(c_name){
    if (document.cookie.length > 0){
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1){
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
  }

  $('.upvote-btn').on('click', function(event){
    var attr = $(this).attr('track-id');

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });

    if(typeof attr !== typeof undefined && attr !== false){//track upvote btn
      var id = $(event.target).attr("track-id");
      $.post("/spitfire/soundtrack/" + id + "/upvote", function(upvoteCount){
        $(event.target).html("▲ " + upvoteCount);
        $(event.target).prop("disabled", true);
      });
    } else{ //lyric upvote btn
      var id = $(event.target).attr("lyric-id");
      $.post("/spitfire/lyric/" + id + "/upvote", function(upvoteCount){
        $(event.target).html("▲ " + upvoteCount);
        $(event.target).prop("disabled", true);
      });
    }
    console.log(event);
  });

  $('.soundtrack-image').hover(function() {
    $(this).css('cursor','pointer');
  }, function() {
    $(this).css('cursor','auto');
  });

  $('.track-title').hover(function() {
    $(this).css('cursor','pointer');
  }, function() {
    $(this).css('cursor','auto');
  });

  $('.track-artist').hover(function() {
    $(this).css('cursor','pointer');
  }, function() {
    $(this).css('cursor','auto');
  });

  $('.soundtrack-image').on('click', function(event){
    var trackid = $(this).attr('track-id');
    window.location.replace("http://localhost:8000/spitfire/soundtrack/" + trackid);
  })

  $('.track-title').on('click', function(event){
    var trackid = $(this).attr('track-id');
    window.location.replace("http://localhost:8000/spitfire/soundtrack/" + trackid);
  })

  $('.track-artist').on('click', function(event){
    var artistid = $(this).attr('artist-id');
    window.location.replace("http://localhost:8000/spitfire/profile/" + artistid);
  })
});
