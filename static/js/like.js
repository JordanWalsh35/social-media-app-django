$('.like-form').submit(function(e){
  e.preventDefault()

  const post_id = $(this).attr('id')
  const likeButton = $(`.like-btn${post_id}`)
  const likeImage = likeButton.find("img")
  const url = $(this).attr('action')

  let res;
  const likes = $(`.like-count${post_id}`).text()
  const trimCount = parseInt(likes)

  $.ajax({
      type: 'POST',
      url: url,
      data: {
          'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
          'post_id':post_id,
      },
      success: function(response) {
          if(likeImage.attr("src").endsWith("heart-full.png")) {
              likeImage.attr("src", "/static/images/heart-empty.png")
              res = trimCount - 1
          } else {
              likeImage.attr("src", "/static/images/heart-full.png")
              res = trimCount + 1
          }

          $(`.like-count${post_id}`).html("<b>" + res + " likes" + "</b>")
      },
      error: function(response) {
          console.log('error', response)
      }
  })
});
