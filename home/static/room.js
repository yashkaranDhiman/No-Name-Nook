setInterval(receiveMessages,200)

function receiveMessages() {
    let inpform = document.getElementById("inpform");

    inpform.addEventListener("submit", (event) => {
        event.preventDefault();
        let room_id = Number(document.getElementById("room").innerText);
        let theText = document.getElementById("text").value;
        let csrftoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
        let data = {
            "msg": theText
        };
        let url = `/${room_id}/add_message/`;

        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            console.log("success:", data);
            let message_box = document.getElementById("messages");
            let new_message = document.createElement("div");
            new_message.classList.add("message");

            let message_content = document.createElement("h2");
            message_content.innerText = data.content;
            let message_time = document.createElement("h5");
            message_time.innerText = data.time;

            new_message.append(message_content);
            new_message.append(message_time);

            message_box.append(new_message);
            document.getElementById("text").value = "";
        })
        .catch(err => {
            console.error("Error:", err);
        });
    });
}