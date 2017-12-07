//delete all the console logs, printing out for testing purpose
/*
$('#audio')[0].onplay = function(){
	var audioElement = $('#audio')[0];
	audioElement.addEventListener("loadedmetadata", function(_event) {
    var duration = audioElement.duration;
    console.log(duration);
	var height = $('.card-text').css('height');
	console.log(height);
	var speed = parseInt(height)/parseInt(duration);
	console.log(speed);
	$('.card-text').hide().slideDown(speed*1000);
	});
}
*/


$('.card-title').on('click', function(){
	var audioElement = $('#audio')[0];
	audioElement.currentTime = 0;
	audioElement.play();
    var duration = audioElement.duration;
    //console.log(duration);
    var $lyric = $(this).next().next();
	var $height = $lyric.css('height');
	var $speed = parseInt($height)/parseInt(duration);
	$(this).data('clicked', true);
	//change the speed to default, currently speeds it up to display small changes
	$.each($('.card-title'), function(){
		if($(this).data('clicked')){
			$(this).data('clicked', false);
			console.log("hello");
		}
	});
	$lyric.hide().slideDown($speed*10000);
});
