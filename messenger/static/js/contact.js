//Contact_list
var cnt_list = document.getElementById("contacts_list");
var cnt_btn = document.getElementById("contacts_btn");
let isOpen = false;

cnt_btn.onclick = function() {
  if (isOpen == false) {
    cnt_list.style.display = "block";
    isOpen = true;
  } else {
    cnt_list.style.display = "none";
    isOpen = false;
  }
};
