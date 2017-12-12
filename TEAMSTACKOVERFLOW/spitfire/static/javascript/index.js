$(function(){
  $("#follow-feed").hide();

  $("#indexDropDownMenu a").on('click', function(event){
    var selected = $(event.target).html();

    if(selected === "Following"){//selected to see Following
      $(event.target).html("Top");
      $(event.target).parent().prev().html("Following");
      $("#top-feed").hide();
      $("#follow-feed").show();
    } else if(selected === "Top"){ //selected to see Top
      $(event.target).html("Following");
      $(event.target).parent().prev().html("Top");
      $("#follow-feed").hide();
      $("#top-feed").show();
    }
  });

});
