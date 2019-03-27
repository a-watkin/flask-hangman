jQuery(document).ready(function($) {
  $.noConflict();
  // Holds game state as JSON from the server.
  let currentState;

  function checkGameState() {
    // Prevents multiple forms from being generated.
    let allowAppend = $("#game-over").find("h1").length === 0;

    if (currentState["game_won"] === true && allowAppend) {
      $("#game-over").append(
        `
        <h1>Congrats you won!</h1>
        <form class="game-over-form text-center" method="POST">
          <div class="form-group">
            <label for="exampleInputEmail1">Name</label>
            <input
              name="username"
              type="text"
              class="form-control text-center form-input"
              placeholder="Enter name"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Score</label>
            <input name="score" class="form-control text-center form-input" 
            value="${currentState["score"]}" 
            readonly="true">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        `
      );
    } else if (currentState["guesses"] <= 0 && allowAppend) {
      $("#game-over").append(
        `
        <h1>Out of guesses, you lost.</h1>
        <button class="btn btn-primary" onClick="window.location.reload()">Try again?</button>
        `
      );
    }
  }

  function updateInputArea(data) {
    $("#input-area").empty();
    currentState = data;
    displayWord = data["display_word"];

    // Clear the input area.
    $("#display-word").empty();
    $("#input-area").empty();

    for (i = 0; i < displayWord.length; i++) {
      if (displayWord[i] !== "_") {
        $("#display-word").append(
          `
            <td class="text-center">
              <h1 class="display-word text-center">${displayWord[i]}</h1>
            </td>
          `
        );

        $("#input-area").append(
          `
            <td class="text-center">
              <input class="table-input text-center" id="text-input-${i}" maxlength="1" type="text"
              value="${displayWord[i]}"/>
            </td>
          `
        );
      } else {
        $("#display-word").append(
          `
            <td class="text-center">
              <h1 class="display-word text-center">${displayWord[i]}</h1>
            </td>
          `
        );

        $("#input-area").append(
          `
            <td class="text-center">
              <input class="table-input text-center" id="text-input-${i}" maxlength="1" type="text" />
            </td>
          `
        );
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
      });
  }

  function onClick(event) {
    var guessAttempt = $(".table-input")
      .map(function(idx, elem) {
        return $(elem).val();
      })
      .get();

    // Update the object with the guess.
    currentState["current_guess"] = guessAttempt;

    // Send the data.
    sendData(currentState);
    event.preventDefault();
  }

  $("#make-guess").click(onClick);

  getDisplayWord();
});
