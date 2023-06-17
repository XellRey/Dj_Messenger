
var user_edit_modal = document.getElementById("edit_block");
var btn = document.getElementById("edit_profile_btn");
let isOpen = false;

btn.onclick = function() {
  if (isOpen == false) {
    user_edit_modal.style.display = "block";
    isOpen = true;
  } else {
    user_edit_modal.style.display = "none";
    isOpen = false;
  }
};