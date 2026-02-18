document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent default form submission

    const form = event.target;
    const formData = new FormData(form);

    fetch('/submit-form', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display success message
        const responseContainer = document.getElementById('form-response');
        responseContainer.innerHTML = `<p style="color: green;">${data.message}</p>`;

        // Optionally reset the form
        form.reset();
    })
    .catch(error => {
        // Handle errors
        const responseContainer = document.getElementById('form-response');
        responseContainer.innerHTML = `<p style="color: red;">Something went wrong. Please try again later.</p>`;
    });
});
