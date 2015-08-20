$('#likes').click(function(){
	var movieid;
	movieid = $(this).attr("data-movieid");
	$.get('/movie/like_movie', {movie_id: movieid}, function(data){
		$('#like_count').html(data);
		$('#likes').hide();
	});
});