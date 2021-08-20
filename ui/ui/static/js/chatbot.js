var j = 0;

function create_new() {
  if (j == 0) {
    var optionText = ["option1", "option2", "option3"];
    for (var i = 0; i < optionText.length; i++) {
      var option = document.createElement("button");
      document.body.appendChild(option);
      option.innerHTML = optionText[i];
      option.id = optionText[i];
      option.className += "btn-main";

      option.id.onlick = function () {
        console.log("loop");
        second_set();
      };
    }
    return (j = 1);
  } else {
    document.body.removeChild(option);
    return (j = 0);
  }
}

function get_text() {
  var text_value = document.getElementById("text_data").value;

  console.log(text_value);
  if (text_value == "hello") {
    create_new();
  }
  if (text_value == "clear") {
    console.log(option);
    document.body.removeChild(option);
  }
}
