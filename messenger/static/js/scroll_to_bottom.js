
const scrollButton = document.getElementById('scrollButton');
function scrollToBottom() {
  const messages = document.querySelectorAll('.message_object, .message_object_friend');
  const lastMessage = messages[messages.length - 1];
  lastMessage.scrollIntoView();

}

scrollButton.addEventListener('click', scrollToBottom);
window.onload = scrollToBottom;
