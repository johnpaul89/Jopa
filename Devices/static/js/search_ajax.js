$(function () {

  $('#search').keyup(function(){
    $.ajax({
      type: "POST",
      url: "/search/article",
      data: {
        'search_text' : $('#search').val(),
        'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
      },
      success: searchSuccess,
      datatype: 'html',
    });
  });
});
function searchSuccess(data, textStatus, jqXHR) {
  $("#search-results").html(data);
}
