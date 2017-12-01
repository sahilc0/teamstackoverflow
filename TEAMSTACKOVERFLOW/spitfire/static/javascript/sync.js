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
	//audioElement.addEventListener("loadedmetadata", function(_event) {
    var duration = audioElement.duration;
    console.log(duration);
    var lyric = $(this).next().next();
	var height = lyric.css('height');
	console.log(height);
	var speed = parseInt(height)/parseInt(duration);
	console.log(speed);
	lyric.hide().slideDown(speed*1000);
});
