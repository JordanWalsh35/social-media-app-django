document.querySelectorAll(".share-link").forEach(function(a) {
  a.addEventListener("click", function() {
    const url = this.dataset.url;
    navigator.clipboard.writeText(url).then(function() {
      console.log("Copied to clipboard!")
      alert("Copied to clipboard!")
    }, function(err) {
      console.error("Failed to copy: ", err)
    })
  })
})
