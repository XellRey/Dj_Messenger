const messageInput = document.getElementById('message');
const submitButton = document.getElementById('submit');

submitButton.addEventListener('click', function(event) {
  const maxLength = 200;
  console.log("sadas");
  const currentLength = messageInput.value.length;
  console.log(currentLength);

if (currentLength > maxLength) {
    event.preventDefault();
    alert('фыфффвцфцф');
  }
});