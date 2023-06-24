var user_edit_modal = document.getElementById("edit_block");
var btn = document.getElementById("edit_profile_btn");
let isOpenU = false;

btn.onclick = function() {
  if (isOpenU == false) {
    user_edit_modal.style.display = "block";
    isOpenU = true;
  } else {
    user_edit_modal.style.display = "none";
    isOpenU = false;
  }
};