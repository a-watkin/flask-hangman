jQuery(document).ready(function($) {
  $.noConflict();

  fetch("http://127.0.0.1:5000/hangman/guess-word", {})
    .then(res => res.json())
    .then(result => {
      $("#disaply-word").append(result["display_word"].join(" "));
    });
});
