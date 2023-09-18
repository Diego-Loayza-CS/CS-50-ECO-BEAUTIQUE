let pos;

let divId = 'map';
const query = 'ecologic restaurant';
const radius = 1000;

window.onload = function () {
	initMap(divId);
};

function initMap(paramDiv) {
	const div = document.getElementById(paramDiv);
	if (!(navigator.geolocation)) {
		console.log('Geolocation is not supported by this browser.');
	}
	else {
		navigator.geolocation.getCurrentPosition(function (geolocation) {
			pos = {
				latitude: geolocation.coords.latitude,
				longitude: geolocation.coords.longitude
			};
			console.log(div);
			createMap(div, pos, query, radius);
		});
	}
}

function createMap(map, pos, query, radius) {
	const url = `/api/places?latitude=${pos.latitude}&longitude=${pos.longitude}&query=${query}&radius=${radius}`;

	fetch(url)
	.then(response => response.json())
	.then(data => {
		console.log(data);
		const resultsDiv = document.getElementById(map);
		resultsDiv.innerHTML = "";

		for (const place of data.results.items) {
			const title = place.title;
			const location = place.vicinity;
			const distance = place.distance;

			const titleElement = document.createElement("p");
			titleElement.textContent = `Title: ${title}`;

			const locationElement = document.createElement("p");
			locationElement.textContent = `Location: ${location}`;

			const distanceElement = document.createElement("p");
			distanceElement.textContent = `Distance: ${distance} m.`;

			resultsDiv.appendChild(titleElement);
			resultsDiv.appendChild(locationElement);
			resultsDiv.appendChild(distanceElement);
		}
	})
	.catch(error => {
		console.error("Error with query:", error);
	});
}
