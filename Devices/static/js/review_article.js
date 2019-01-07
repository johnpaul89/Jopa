$(document).ready(function(event){

  $('#delete').click(function(){
    return confirm("Are you sure you want to delete this article?");
  });

  $('.reply-btn').click(function(){
    $(this).parent().parent().next('.replied-comments').fadeToggle()
  });

  $(document).on('submit', '.review-comment-form', function(event){
   event.preventDefault();
   console.log($(this).serialize());
   $.ajax({
     type: 'POST',
     url: $(this).attr('action'),
     data: $(this).serialize(),
     dataType: 'json',
     success: function(response) {
       $('.main-review-comment-section').html(response['form']);
       $('textarea').val('');
       $('.reply-btn').click(function() {
         $(this).parent().parent().next('.replied-comments').fadeToggle();
         $('textarea').val('');
       });
     },
     error: function(rs, e) {
       console.log(rs.responseText);
     },
   });
 });

 $(document).on('submit', '.review-reply-form', function(event){
  event.preventDefault();
  console.log($(this).serialize());
  $.ajax({
    type: 'POST',
    url: $(this).attr('action'),
    data: $(this).serialize(),
    dataType: 'json',
    success: function(response) {
      $('.main-review-comment-section').html(response['form']);
      $('textarea').val('');
      $('.reply-btn').click(function() {
        $(this).parent().parent().next('.replied-comments').fadeToggle();
        $('textarea').val('');
      });
    },
    error: function(rs, e) {
      console.log(rs.responseText);
    },
  });
});


});
