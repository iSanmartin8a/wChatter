

function showRandomNumber() {
  var random_number = Math.floor(Math.random() * 11) + 1;
  document.getElementById("numberCard").innerHTML = random_number;

  var quotes = ["¡NUEVO TEMA!", "PREGUNTA", "ESTA ES DURA", "RESPONDE TU", "UFF", "NO SE YO", "TE TOCA A TI"];
  var random_quote = Math.floor(Math.random() * 6) + 1;
  document.getElementById("cardTitle").innerHTML = quotes[random_quote];

  var cat = document.querySelector('.cat');

  function setProperty(duration) {
    cat.style.setProperty('--animation-time', duration +'s');
  }
  
  function changeAnimationTime() {
    var animationDuration = Math.random();
    setProperty(animationDuration);
  }
  
  setInterval(changeAnimationTime, 1000);
}