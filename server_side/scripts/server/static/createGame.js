const uploadedFiles = [];
durationInput = document.getElementById('duration');
treasureCountInput = document.getElementById('treasureCount');

console.log(localStorage.getItem('room'));

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

  uploadedFiles.push(file);
  console.log(uploadedFiles);
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
                               duration: durationInput.xvalue,
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