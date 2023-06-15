

function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    let form = document.getElementById("send_msg")



    function sendChat(e){
        e.preventDefault()
        let chatMessage= document.getElementById("msg_body").value
        console.log(chatMessage)

        const data = { msg: chatMessage };

        let url = "{% url 'sent_msg' userid %}"

fetch(url, {
  method: 'POST', // or 'PUT'
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
  body: JSON.stringify(data),
})
.then(response => response.json())
.then(data => {
  console.log('Success:', data);
  let chat_body = document.getElementById('send_message_body')
  let chatMessageBox = document.createElement("div")
  chatMessageBox.classList.add("message_object")
  chatMessageBox.innerText = data
  chat_body.append(chatMessageBox)
  document.getElementById("send_msg").value=""
})
.catch((error) => {
  console.error('Error:', error);
});


    }

counter = 0
setInterval(receiveMessages, 2000)


function receiveMessages(){


    let url = "{% url 'rec_msg' userid %}"

        fetch(url)
        .then(response => response.json())
        .then(data => {
        console.log('Success:', data);



        if(data.length == 0){}

        else{

            let lastMsg = data[data.length-1]

            if(counter == data.length){
                console.log("there is no new chat")
            }
            else{
                let chat_body = document.getElementById('send_message_body')
                let chatMessageBox = document.createElement("div")
                chatMessageBox.classList.add("message_object_friend")
                chatMessageBox.innerText = lastMsg
                chat_body.append(chatMessageBox)
                document.getElementById("send_msg").value=""
                console.log()
            }
        }
        counter = data.length

        })
        .catch((error) => {
        console.error('Error:', error);
        });

}
