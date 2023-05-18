document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('search-form');
    const searchedCityInfo = document.getElementById('searched-city-info');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const cityInput = document.querySelector('input[name="city"]');
        const city = cityInput.value;
        const searchURL = '/search/';

        const response = await fetch(`${searchURL}?city=${city}`);
        const data = await response.json();

        if (response.ok) {
            const newSection = document.createElement('div');
            newSection.classList.add('row', 'justify-content-center');

            const cardCol = document.createElement('div');
            cardCol.classList.add('col-sm-2', 'd-flex', 'justify-content-center');

            const cardWrapper = document.createElement('div');
            cardWrapper.classList.add('weather-card-wrapper', 'mx-auto');

            const card = document.createElement('div');
            card.classList.add('searched-card');
            card.style.backgroundImage = `url('${data.background_image}')`;

            const cardBody = document.createElement('div');
            cardBody.classList.add('card-body');

            const cardTitle = document.createElement('h5');
            cardTitle.classList.add('card-title');
            cardTitle.textContent = data.city;

            const temperature = document.createElement('p');
            temperature.classList.add('card-text');
            temperature.textContent = `Temperature: ${data.temperature}°C`;

            const weather = document.createElement('p');
            weather.classList.add('card-text');
            weather.textContent = `Weather: ${data.description}`;

            const humidity = document.createElement('p');
            humidity.classList.add('card-text');
            humidity.textContent = `Humidity: ${data.humidity}%`;

            cardBody.appendChild(cardTitle);
            cardBody.appendChild(temperature);
            cardBody.appendChild(weather);
            cardBody.appendChild(humidity);

            card.appendChild(cardBody);
            cardWrapper.appendChild(card);
            cardCol.appendChild(cardWrapper);
            newSection.appendChild(cardCol);

            searchedCityInfo.innerHTML = '';
            searchedCityInfo.appendChild(newSection);

            if (data.last_10_records) {
                const recordsSection = document.createElement('div');
                recordsSection.classList.add('row', 'justify-content-center');

                const recordsCol = document.createElement('div');
                recordsCol.classList.add('col-sm-6');

                const recordsTitle = document.createElement('h5');
                recordsTitle.textContent = 'Last 10 Records';

                const recordsList = document.createElement('ul');
                recordsList.classList.add('list-group');

                for (const record of data.last_10_records) {
                    const listItem = document.createElement('li');
                    listItem.classList.add('list-group-item');

                    const dateTime = new Date(record.timestamp); // Convert timestamp to Date object
                    const formattedDateTime = dateTime.toLocaleString(); // Format the date and time

                    listItem.textContent = `Date: ${formattedDateTime}, Temperature: ${record.temperature}°C, Weather: ${record.description}, Humidity: ${record.humidity}%`;
                    recordsList.appendChild(listItem);
                }

                recordsCol.appendChild(recordsTitle);
                recordsCol.appendChild(recordsList);
                recordsSection.appendChild(recordsCol);

                searchedCityInfo.appendChild(recordsSection);
            }
        } else {
            const error_message = data.error || 'An error occurred. Please try again.';
            searchedCityInfo.innerHTML = `<p class="text-center text-danger">${error_message}</p>`;
        }
    });
});
