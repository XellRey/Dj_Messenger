var blocklist_edit_modal = document.getElementById("blocklist_block");
var btn = document.getElementById("blocklist_btn");
let isOpenBL = false;

btn.onclick = function() {
  if (isOpenBL == false) {
    blocklist_edit_modal.style.display = "block";
    isOpenBL = true;
  } else {
    blocklist_edit_modal.style.display = "none";
    isOpenBL = false;
  }
};