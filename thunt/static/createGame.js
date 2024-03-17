const uploadedFiles = [];
durationInput = document.getElementById('duration');
treasureCountInput = document.getElementById('treasureCount');

function startGame(event) {
	user = localStorage.getItem('user');
	room = localStorage.getItem('room');

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

	fetch("/backend/start_game", {
		method: "POST",
		body: formData
	})
		.then(response => response.json())
		.then((data) => {
			window.location.href = "/start_game";
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
		imgContainer.prepend(img);
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
