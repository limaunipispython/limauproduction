'use strict';

$(document).ready(function(){
	$(".item").click(function(){
		$(this).toggleClass("item2");
	});
});

// this is for star rating system using jquery prototype
// $.fn.stars = function() {
// 	return $(this).each(function() {

// 		var rating = $(this).data("rating");

// 		var numStars = $(this).data("num-stars");

// 		var fullStar = new Array(Math.floor(rating + 1)).join('<i class="fa fa-star"></i>');

// 		var halfStar = ((rating%1) !== 0) ? '<i class="fa fa-star-half-empty"></i>': '';

// 		var noStar = new Array(Math.floor(numStars + 1 - rating)).join('<i class="fa fa-star-o"></i>');

// 		$(this).html(fullStar + halfStar + noStar);

// 	});
// }

$.fn.stars = function() {
	return $(this).each(function() {

		var rating = $(this).data("rating");

		var numStars = $(this).data("num-stars");

		var fullStar = new Array(Math.floor(rating + 1)).join('<i class="fa fa-star"></i>');

		var halfStar = ((rating%1) !== 0) ? '<i class="fa fa-star-half-empty"></i>': '';

		var noStar = new Array(Math.floor(numStars + 1 - rating)).join('<i class="fa fa-star-o"></i>');

		$(this).html(fullStar + halfStar + noStar);

	});
};	

$(document).ready(function(){
	$(".stars").stars();
})

//  $('body').on('ready','.contentgroup',function(){
// 	 $('star').stars(;)
//  });


// ------Threaded Comments Javascript

function show_reply_form(event) {
	var $this = $(this);
	var comment_id = $this.data('comment-id');

	$('#id_parent').val(comment_id);
	$('#form-comment').insertAfter($this.closest('.comment'));
};

function cancel_reply_form(event) {
	$('#id_comment').val('');
	$('#id_parent').val('');
	$('#form-comment').appendTo($('#wrap_write_comment'));
}

$.fn.ready(function() {
	$('.comment_reply_link').click(show_reply_form);
	$('#cancel_reply').click(cancel_reply_form);
})