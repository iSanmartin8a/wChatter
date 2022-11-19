

function showRandomNumber() {
  var random_number = Math.floor(Math.random() * 11) + 1;
  document.getElementById("numberCard").innerHTML = random_number;

  var quotes = ["NEW THEME!", "QUESTION", "THAT'S TOUGH"];
  var random_quote = Math.floor(Math.random() * 3);
  document.getElementById("cardTitle").innerHTML = quotes[random_quote];

}