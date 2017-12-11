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

  $("#lyrics-by").hide();

  $(".dropdown-menu a").click(function(event){
    var selected = $(event.target).html();

    if(selected === "Lyrics by"){//selected to see lyrics
      $(event.target).html("Tracks by");
      $(event.target).parent().prev().html("Lyrics by");
      $("#tracks-by").hide();
      $("#lyrics-by").show();
    } else if(selected === "Tracks by"){ //selected to see tracks
      $(event.target).html("Lyrics by");
      $(event.target).parent().prev().html("Tracks by");
      $("#lyrics-by").hide();
      $("#tracks-by").show();
    }
  });

  $("#follow-btn").click(function(event){
  var follow_btn = $(this);

  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });

  var artist_id = $(event.target).attr("artist-id");
  var state = $(event.target).html();

  if(state === "Follow"){
    $.post("/spitfire/profile/" + artist_id + "/follow", function(data){
      follow_btn.html("Following");
      follow_btn.removeClass("btn-primary");
      follow_btn.addClass("btn-outline-secondary");
      follow_btn.attr("follow-relationship-id", data);
    });
  } else if(state === "Following"){
    var follow_relationship_id = follow_btn.attr("follow-relationship-id");

    $.ajax({
      type: "delete",
      url: "/spitfire/profile/" + artist_id + "/follow",
      data: JSON.stringify({'relationship_id': follow_relationship_id}),
      contentType: 'application/x-www-form-urlencoded; charset=utf-8',
      success: function(data) {
        follow_btn.html("Follow");
        follow_btn.removeClass("btn-outline-secondary");
        follow_btn.addClass("btn-primary");
      }
    });
  }
});
});
