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
      $.post("soundtrack/" + id + "/upvote", function(upvoteCount){
        $(event.target).html("▲ " + upvoteCount);
        $(event.target).prop("disabled", true);
      });
    } else{ //lyric upvote btn
      var id = $(event.target).attr("lyric-id");
      $.post("lyric/" + id + "/upvote", function(upvoteCount){
        $(event.target).html("▲ " + upvoteCount);
        $(event.target).prop("disabled", true);
      });
    }

    console.log(event);
  });
});
