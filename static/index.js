var playerTurn = ["X", "O"];
var playerTurn = ["O", "X"];
var player = 0;
gameEnd = false;

var winner = "";
var tieCheck = "";
var turnCount = 0;

window.addEventListener("DOMContentLoaded", () => {
  const tiles = Array.from(document.querySelectorAll(".boardTile"));
  document.getElementById("playerTitle").innerHTML = "PLAYER O'S TURN";
  console.log("TILE ARRAY", tiles);
  tiles.forEach((tile, index) => {
    tile.addEventListener("click", () => userAction(tile, index));
  });

  const playAgainButton = document.querySelector(".reset");
  playAgainButton.addEventListener("click", () => resetGame(tiles));
  // _____________________________________________
  const userAction = (tile, index) => {
    console.log(turnCount);

    turnCount++;

    if (winner == "X" || winner == "O") {
      return;
    }

    if (player == 1) {
      return;
    }

    console.log(tile);
    console.log(player);
    var turn = "boardTilePlayer" + playerTurn[player];

    if (
      !tile.classList.contains("boardTilePlayerX") &&
      !tile.classList.contains("boardTilePlayerO")
    ) {
      tile.classList.add(turn);
      if (player == 0) {
        document.getElementById("playerTitle").innerHTML =
          "PLAYER X'S TURN <br />";
        document.getElementById("pleaseWait").innerHTML = "PLEASE WAIT...";
        player = 1;
      } else if (player == 1) {
        document.getElementById("playerTitle").innerHTML = "PLAYER O'S TURN";
        document.getElementById("pleaseWait").innerHTML = "";
        player = 0;
      }
    }

    if (turnCount == 9) {
      console.log("CAUGHT");
      endGameCheck();
      return;
    }
    fetchData(index);
    recieveData();
  };

  const resetGame = (tiles) => {
    tiles.forEach((tile, index) => {
      tile.classList.remove("boardTilePlayerX");
      tile.classList.remove("boardTilePlayerO");
      player = 0;
    });
  };

  function fetchData(tileIndex) {
    fetch("http://127.0.0.1:5000/receiver", {
      method: "POST",
      headers: {
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
        "Content-type": "application/json",
        Accept: "application/json",
      },
      // Strigify the payload into JSON:
      // body: JSON.stringify(String(tileIndex)),
      body: JSON.stringify({
        UserMove: String(tileIndex + 1),
        AIMove: "",
        GameEnded: gameEnd,
        winner: "",
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          alert("something is wrong");
        }
      })
      .then((jsonResponse) => {})
      .catch((err) => console.error(err));
    console.log(
      "woah",
      JSON.stringify({
        UserMove: String(tileIndex + 1),
        AIMove: "",
        GameEnded: gameEnd,
        winner: "",
      })
    );
    console.log(tileIndex);
  }

  async function recieveData() {
    turnCount++;

    fetch("http://127.0.0.1:5000/sender", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // data = JSON.parse(data);
        console.log("data", data);
        console.log(data[28]);
        AIMove = parseInt(data[28]) - 1;
        var turn = "boardTilePlayer" + playerTurn[player];

        if (
          !tiles[AIMove].classList.contains("boardTilePlayerX") &&
          !tiles[AIMove].classList.contains("boardTilePlayerO")
        ) {
          tiles[AIMove].classList.add(turn);
          if (player == 0) {
            player = 1;
          } else if (player == 1) {
            player = 0;
          }
        }
        winner = data.substring(61, 64).trim();
        tieCheck = data.substring(62, 65).trim();
        console.log(data);
        console.log(winner);
        console.log(tieCheck);

        endGameCheck();
      });
  }

  function endGameCheck() {
    console.log(turnCount);
    if (winner == "X") {
      document.getElementById("playerTitle").innerHTML = "X WINS!";
      document.getElementById("pleaseWait").innerHTML = "";
    } else if (winner == "O") {
      document.getElementById("playerTitle").innerHTML = "O WINS!";
    } else if (turnCount == 9) {
      // } else if (tieCheck == "Tie") {
      console.log("WE OUT HERE");
      document.getElementById("playerTitle").innerHTML = "THE GAME IS A TIE!";
      document.getElementById("pleaseWait").innerHTML = "";
    } else {
      document.getElementById("playerTitle").innerHTML = "PLAYER O'S TURN";
      document.getElementById("pleaseWait").innerHTML = "";
    }
  }
});
