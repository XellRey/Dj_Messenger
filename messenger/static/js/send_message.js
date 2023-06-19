function checkTextLength() {
  var submitButton = document.getElementById("submit");

  var textArea = document.getElementById("id_message").value;
  var characterCount = textArea.length + (textArea.match(/\n/g) || []).length;

  if (characterCount < 200) {
    submitButton.classList.remove("inactive");
    submitButton.classList.add("active");
    submitButton.disabled = false;
  } else {
    submitButton.classList.remove("active");
    submitButton.classList.add("inactive");
    submitButton.disabled = true;
  }
}