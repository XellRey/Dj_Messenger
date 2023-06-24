var cnt_list = document.getElementById("contacts_list");
var cnt_btn = document.getElementById("contacts_btn");
let isOpenC = false;

cnt_btn.onclick = function() {
  if (isOpenC == false) {
    cnt_list.style.display = "block";
    isOpenC = true;
  } else {
    cnt_list.style.display = "none";
    isOpenC = false;
  }
};
