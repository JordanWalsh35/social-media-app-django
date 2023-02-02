document.querySelectorAll(".options-image").forEach(function(image) {
  image.addEventListener("click", function() {
  
    const postID = $(this).attr('id');
    // console.log(postID);
    document.querySelector("#post-dropdown-options-" + postID).classList.toggle("show");
  });
});
