// User_description
var user_descrp_modal = document.getElementById("user_description_modal");

var btn = document.getElementById("user_description_modal_btn");

btn.onclick = function() {
  user_descrp_modal.style.display = "block";
}

window.onclick = function(event) {
  if (event.target == user_descrp_modal) {
    user_descrp_modal.style.display = "none";
  }
}




