$(function(){
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
});
