jQuery(document).ready(function($) {
  $.noConflict();

  // holds the JSON from the backend
  let currentState;

  function getDisplayWord() {
    fetch("/hangman/guess-word", {})
      .then(res => res.json())
      .then(result => {
        displayWord = result["display_word"];
        console.log(result);
        currentState = result;
        console.log(currentState);
        // $("#disaply-word").append(result["display_word"].join(" "));

        for (i = 0; i < displayWord.length; i++) {
          console.log("what");
          $("#input-area").append(`
          <th>
          <h1 class="text-center">${displayWord[i]}</h1>
          <input class="table-input text-center" id="text-input-${i}" maxlength="1" type="text" />
          </th>
          `);
        }
      });
  }

  function updateInputArea(data) {
    $("#input-area").empty();
    displayWord = data["display_word"];

    for (i = 0; i < displayWord.length; i++) {
      console.log("what");
      $("#input-area").append(`
          <th>
          <h1 class="text-center">${displayWord[i]}</h1>
          <input class="table-input text-center" id="text-input-${i}" maxlength="1" type="text" />
          </th>
          `);
    }
  }

  function sendData(data) {
    fetch("/hangman/check-guess", {
      method: "POST",
      credentials: "include",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .catch(error => console.error(error))
      .then(res => res.json())
      .then(result => {
        updateInputArea(result);
        console.log("please?", result);
      });
  }

  function onClick(event) {
    var guessAttempt = $(".table-input")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();

    // update the object with the guess
    currentState["current_guess"] = guessAttempt;
    // send the data
    sendData(currentState);

    event.preventDefault();
  }

  $("#make-guess").click(onClick);

  getDisplayWord();
});
