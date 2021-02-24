let sendMessage = () => {
    let number = document.getElementById("number").value;
    let message = document.getElementById("message").value;

    data = {
        number: number,
        message: message
    }

    fetch('/api/sendMessage', {
        method: 'POST',
        headers: {'Content-Type': 'application/json', 'Accept': 'application/json'},
        body: JSON.stringify(data)
    }).then(response => {
        if (response.status === 200) {
            document.getElementById("form").reset();
            alert("Your message has been sent!")
        }
    })
};