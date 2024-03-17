const uploadedFiles = [];
durationInput = document.getElementById('duration');
treasureCountInput = document.getElementById('treasureCount');

const user = localStorage.getItem('user');
const room = localStorage.getItem('room');

document.querySelector('#game-id-label').innerText = `Room ${room}`;

function startGame(event) {
	// Creating new FormData instance
	let formData = new FormData();
	formData.append("request", 'start_game');
	formData.append("user", user);
	formData.append("room", room);
	formData.append("duration", durationInput.value);
	formData.append("treasure_count", treasureCountInput.value);

	// Append files to formData
	for (let index = 0; index < uploadedFiles.length; index++) {
		formData.append("file" + index, uploadedFiles[index]);
	}

	fetch("/start_game", {
		method: "POST",
		body: formData
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

	//Saving the actual File object
	uploadedFiles.push(file);
}

function createJS() {
	const loginButton = document.getElementById("startButton");
	loginButton.addEventListener("click", startGame);
}

createJS();
