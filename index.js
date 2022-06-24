var playerTurn = ["X", "O"];
var playerTurn = ["O", "X"];
var player = 0;
gameEnd = false;

var list = [];

window.addEventListener("DOMContentLoaded", () => {
  const tiles = Array.from(document.querySelectorAll(".boardTile"));

  console.log("TILE ARRAY", tiles);

  tiles.forEach((tile, index) => {
    tile.addEventListener("click", () => userAction(tile, index));
  });

  const playAgainButton = document.querySelector(".reset");
  playAgainButton.addEventListener("click", () => resetGame(tiles));
  // _____________________________________________
  const userAction = (tile, index) => {
    // console.log(tile.style);
    console.log(tile);
    console.log(player);
    var turn = "boardTilePlayer" + playerTurn[player];

    if (
      !tile.classList.contains("boardTilePlayerX") &&
      !tile.classList.contains("boardTilePlayerO")
    ) {
      tile.classList.add(turn);
      if (player == 0) {
        player = 1;
      } else if (player == 1) {
        player = 0;
      }
    }

    fetchData(index);
    recieveData();
    // let l = '{"UserMove": "6", "AIMove": 3, "GameEnded": "False" }';
    // let l = '{"UserMove": "1", "AIMove": "", "GameEnded": "False"}';
    // console.log(typeof l);
    // l = JSON.parse(l);
    // console.log(typeof l);
    // console.log(l["GameEnded"]);
    // console.log(`RESPONSE::::: ${}`);
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
      }),
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          alert("something is wrong");
        }
      })
      .then((jsonResponse) => {
        // Log the response data in the console
        // console.log(jsonResponse);
      })
      .catch((err) => console.error(err));
    console.log(
      "woah",
      JSON.stringify({
        UserMove: String(tileIndex + 1),
        AIMove: "",
        GameEnded: gameEnd,
      })
    );
    console.log(tileIndex);
  }

  async function recieveData() {
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
        console.log("type", typeof data);
        // document.getElementById("title").innerHTML = data;
        console.log(data[28]);
        // console.log("TWIII", tiles[data[28]]);
        // return data;
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
      });
    // document.getElementsByClassName("currentPlayer").innerText = "data";
    // data = data.json();
    // console.log(typeof data);
    // return data;

    // console.log("RESULT");
    // result = JSON.parse(data);
    // console.log(typeof result);

    // async function getDict() {
    //   const response = await fetch("http://127.0.0.1:5000/sender", {
    //     headers: {
    //       "Content-Type": "application/json",
    //       Accept: "application/json",
    //     },
    //   });
    //   const text = await response.text();
    //   // const text = await response.json();
    //   console.log(text);

    //   // console.log(JSON.parse(text));
    // }
  }

  // console.log("AH", userAction(tiles[3 + 1], 4));

  // async function fetchYER() {
  //   let response = await fetch("http://127.0.0.1:5000/sender");
  //   let data = await response.json();
  //   data = JSON.stringify(data);
  //   data = JSON.parse(data);
  //   console.log(data);
  //   return data.text;
  // }

  // while (!gameEnd) {
  //   console.log("User Select A Tile");
  // }
});
