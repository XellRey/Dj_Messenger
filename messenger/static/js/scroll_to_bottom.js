const scrollButton = document.getElementById('scrollButton');
const chatContainer = document.getElementById('send_message_body');

function scrollToBottom() {
  const messages = chatContainer.querySelectorAll('.message_object, .message_object_friend');
  const lastMessage = messages[messages.length - 1];
  lastMessage.scrollIntoView();
}

function handleScroll() {
  const isScrolledToBottom = chatContainer.scrollHeight - chatContainer.clientHeight <= chatContainer.scrollTop + 1;
  if (isScrolledToBottom) {
    scrollButton.style.display = 'none';
  } else {
    scrollButton.style.display = 'block';
  }
}

scrollButton.addEventListener('click', scrollToBottom);
window.onload = scrollToBottom;
chatContainer.addEventListener('scroll', handleScroll);