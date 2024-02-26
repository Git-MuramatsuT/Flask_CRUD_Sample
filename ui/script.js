async function fetchMessage(path) {
    const response = await fetch(path);
    if (!response.ok) {
        alert("something wrong! have you run the server yet?")
        return;
    }
    const message = await response.text();
    alert(message)
}