// function searchWeather() {
//     var country = encodeURIComponent(document.getElementById("location").value);
//     var url = `https://api.openweathermap.org/data/2.5/weather?q=${country}&appid=ad5afcb589e785b27686ccb6ed9ec57e&units=metric`;

//     fetch(url)
//     .then(response => response.json())
//     .then(data => {
//         var result = document.getElementById("weatherResult");
//         console.log(data.sys.country);
//         result.innerHTML = `
//             <h2>${data.name}, ${data.sys.country}</h2>
//             <p>Pressure: ${data.main.pressure} hPa</p>
//             <p>Coordinates: [${data.coord.lon}, ${data.coord.lat}]</p>
//             <p>Temperature: ${data.main.temp} °C</p>
//         `;
//     })
//     .catch(error => {
//         var result = document.getElementById("weatherResult");
//         console.log("error");
//         result.innerHTML = `<p>Error: ${error.message}</p>`;
//     });
// }


function showToast(message) {
    toastr.success(message);
}