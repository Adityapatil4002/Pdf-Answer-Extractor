document.getElementById('pdf-upload-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent page reload
    
    const formData = new FormData(this);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const messageElem = document.getElementById('upload-message');
        if (data.error) {
            messageElem.textContent = data.error;
            messageElem.style.color = 'red';
        } else {
            messageElem.textContent = data.message;
            messageElem.style.color = 'green';

            // Show the question section
            document.getElementById('qa-section').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('ask-question-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent page reload
    
    const formData = new FormData(this);

    fetch('/ask', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const answerElem = document.getElementById('answer');
        if (data.error) {
            answerElem.textContent = data.error;
            answerElem.style.color = 'red';
        } else {
            answerElem.textContent = data.answer;
            answerElem.style.color = 'green';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
