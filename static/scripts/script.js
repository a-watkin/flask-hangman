jQuery(document).ready(function($) {
  $.noConflict();

  // holds the JSON from the backend
  let currentState;

  function checkGameState() {
    if (currentState["game_won"] === true) {
      console.log("game over", currentState["score"]);
      $("#input-area").empty();
      $("#input-area").append(`<h1>Congrats you won.</h1>
        <form method="POST">
          <div class="form-group">
            <label for="exampleInputEmail1">Name</label>
            <input name="username" type="text" class="form-control" placeholder="Enter name">
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Score</label>
            <input name="score" class="form-control" value="${
              currentState["score"]
            }">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      `);
    } else if (currentState["guesses"] <= 0) {
      console.log("out of guesses");
      $("#input-area").empty();
      $("#input-area").append(`<h1>Out of guesses, you lost.</h1>
      <button class="btn btn-primary" onClick="window.location.reload()">Try again?</button>
      `);
    }
  }

  function updateInputArea(data) {
    $("#input-area").empty();
    currentState = data;
    displayWord = data["display_word"];

    for (i = 0; i < displayWord.length; i++) {
      if (displayWord[i] !== "_") {
        $("#input-area").append(`
            <th>
            <h1 class="display-word text-center">${displayWord[i]}</h1>
            <input value="${
              displayWord[i]
            }" class="table-input text-center" id="text-input-${i}" maxlength="1" type="text" />
            </th>
            `);
      } else {
        $("#input-area").append(`
            <th>
            <h1 class="display-word text-center">${displayWord[i]}</h1>
            <input class="table-input text-center" id="text-input-${i}" maxlength="1" type="text" />
            </th>
            `);
      }
    }

    checkGameState();
  }

  function getDisplayWord() {
    fetch("/hangman/guess-word", {})
      .then(res => res.json())
      .then(result => {
        updateInputArea(result);
      });
  }

  function sendData(data) {
    console.log("sending data ", data);
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
        currentState = result;
        checkGameState;
        console.log("data from server ", result);
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
    // currentState["display_word"] = getDisplayValue();

    // send the data
    sendData(currentState);
    event.preventDefault();
  }

  $("#make-guess").click(onClick);

  getDisplayWord();
});
