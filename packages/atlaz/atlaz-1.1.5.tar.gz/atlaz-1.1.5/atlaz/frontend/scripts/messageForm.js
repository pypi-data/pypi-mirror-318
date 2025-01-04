// Message form functionality
const messageForm = document.getElementById('message-form');
const messageInput = document.getElementById('message-input');
const apiKeyInput = document.getElementById('api-key-input');
const llmProviderDropdown = document.getElementById('llm-provider-dropdown');
const llmModelInput = document.getElementById('llm-model-input'); // New input

// Function to fetch server version
async function fetchServerVersion() {
    try {
        const response = await fetch('http://127.0.0.1:5050/api/version');
        const data = await response.json();
        return data.version;
    } catch (error) {
        console.error('Error fetching server version:', error);
        return null;
    }
}

// Function to load inputs from localStorage
function loadInputs() {
    apiKeyInput.value = localStorage.getItem('apiKey') || '';
    llmProviderDropdown.value = localStorage.getItem('llmProvider') || 'gemini';
    llmModelInput.value = localStorage.getItem('llmModel') || '';
    messageInput.value = localStorage.getItem('instruction') || '';
}

// Function to save inputs to localStorage
function saveInputs() {
    localStorage.setItem('apiKey', apiKeyInput.value.trim());
    localStorage.setItem('llmProvider', llmProviderDropdown.value);
    localStorage.setItem('llmModel', llmModelInput.value.trim());
    localStorage.setItem('instruction', messageInput.value.trim());
}

// Function to clear stored inputs
function clearStoredInputs() {
    localStorage.removeItem('apiKey');
    localStorage.removeItem('llmProvider');
    localStorage.removeItem('llmModel');
    localStorage.removeItem('instruction');
}

// Initialize inputs on page load based on version
document.addEventListener('DOMContentLoaded', async () => {
    const currentVersion = await fetchServerVersion();
    const storedVersion = localStorage.getItem('serverVersion');

    if (currentVersion) {
        if (storedVersion === currentVersion) {
            // Same version, load stored inputs
            loadInputs();
        } else {
            // Different version, clear stored inputs and update version
            clearStoredInputs();
            localStorage.setItem('serverVersion', currentVersion);
        }
    }
});

messageForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const messageText = messageInput.value.trim();
    const apiKey = apiKeyInput.value.trim();
    const llmProvider = llmProviderDropdown.value;
    const llmModel = llmModelInput.value.trim(); // Capture LLM model

    // Gather selected directories
    const selectedPaths = gatherSelectedPaths(); // Function from directoryTree.js

    if (messageText !== '' && llmModel !== '' && apiKey !== '') { // Ensure all fields are provided
        // Log to the console (optional)
        console.log('messageText:', messageText);
        console.log('apiKey:', apiKey);
        console.log('llmProvider:', llmProvider);
        console.log('llmModel:', llmModel); // Log LLM model
        console.log('Selected Paths:', selectedPaths); // Log selected directories

        // Prepare the payload with all necessary data
        const payload = {
            api_key: apiKey,
            llm_model: llmModel,
            llm_provider: llmProvider,
            message: messageText,
            selected_files: selectedPaths
        };

        // Save inputs to localStorage
        saveInputs();

        // Send all data in a single request
        fetch('http://127.0.0.1:5050/send_data', { // Updated endpoint
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response:', data);
            if (data.status === 'success') {
                alert('Data sent successfully!');
                messageInput.value = '';
                // Optionally clear instruction from localStorage after successful submission
                localStorage.removeItem('instruction');
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(err => {
            console.error('Error:', err);
            alert('An error occurred while sending the data.');
        });
    } else {
        alert('Please enter the API key, LLM model, and a message before sending.');
    }
});
