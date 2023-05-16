$(document).ready(function() {
  // Fetch weather data from the backend API
  $.get("/home", function(data) {
    // Iterate over the weather data for each city
    for (var i = 0; i < data.length; i++) {
      var city = data[i];

      // Create a Bootstrap card for the city weather
      var card = $("<div>").addClass("card");

      // Add city name
      var cityName = $("<h3>").text(city.city);
      card.append(cityName);

      // Add weather description
      var description = $("<p>").text(city.description);
      card.append(description);

      // Add temperature
      var temperature = $("<p>").text("Temperature: " + city.temperature + "°C");
      card.append(temperature);

      // Add humidity
      var humidity = $("<p>").text("Humidity: " + city.humidity + "%");
      card.append(humidity);

      // Append the card to the weather container
      $("#weather-container").append(card);
    }
  });
});
