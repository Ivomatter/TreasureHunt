const uploadedFiles = [];
durationInput = document.getElementById('duration');
treasureCountInput = document.getElementById('treasureCount');

console.log(localStorage.getItem('room'));

const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
});

function handleFileUpload(event) {
  const file = event.target.files[0];
  const imgContainer = document.querySelector('.imgContainer');

  const reader = new FileReader();
  reader.onload = function (e) {
    const img = document.createElement('img');
    img.src = e.target.result;
    img.alt = 'Image';
    imgContainer.appendChild(img);
  };

  reader.readAsDataURL(file);
//   console.log(reader.result);
    toBase64(file).then((data) => {
        console.log(data);
        uploadedFiles.push(data);
    });

//   console.log(file.toString());
//   uploadedFiles.push(file);
//   console.log(uploadedFiles);
}

function startGame(event) {
    user = localStorage.getItem('user');
    room = localStorage.getItem('room');

    fetch("/start_game", {
        method: "POST",
        headers: { "Content-Type": "application/json; charset=UTF-8" },
        body: JSON.stringify({ request: 'start_game', 
                               user: user,  
                               room: room, 
                               duration: durationInput.value,
                               treasure_count: treasureCountInput.value,
                               images: uploadedFiles})
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

function createJS() {
    const loginButton = document.getElementById("startButton");
    loginButton.addEventListener("click", startGame);
}

createJS();