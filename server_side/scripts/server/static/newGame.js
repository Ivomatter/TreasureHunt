const usernameInput = document.getElementById('username');
const joinButton = document.getElementById('joinButton');
const createButton = document.getElementById('createButton');

usernameInput.addEventListener('input', () => {
    if (usernameInput.value.trim() !== '') {
        joinButton.disabled = false;
        createButton.disabled = false;
    } else {
        joinButton.disabled = true;
        createButton.disabled = true;
    }
});

function newGame(event) {
    console.log(usernameInput);

    fetch("/create_game", {
        method: "POST",
        headers: { "Content-Type": "application/json; charset=UTF-8" },
        body: JSON.stringify({ request: 'create_game', user: usernameInput })
    })
        .then(response => response.json())
        .then((data) => {
            console.log(data);
            window.location.href = "/r1";
        })
        .catch((errdata) => {
            console.log(errdata);
        });
}

function newGameJS() {
    const loginButton = document.getElementById("createButton");
    loginButton.addEventListener("click", newGame);
}

newGameJS();