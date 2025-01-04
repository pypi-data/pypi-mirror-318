// atlaz/frontend/scripts/messageForm.js

// File form functionality
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

// Function to fetch saved credentials from backend
async function fetchSavedCredentials() {
    try {
        const response = await fetch('http://127.0.0.1:5050/api/get_credentials');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching saved credentials:', error);
        return {
            api_key: '',
            llm_provider: 'openai',
            model_choice: 'gpt-4'
        };
    }
}

// Function to load inputs from backend
async function loadInputsFromBackend() {
    const credentials = await fetchSavedCredentials();
    apiKeyInput.value = credentials.api_key || '';
    llmProviderDropdown.value = credentials.llm_provider || 'gemini';
    llmModelInput.value = credentials.model_choice || 'gpt-4';
    messageInput.value = localStorage.getItem('instruction') || ''; // Retain instruction from localStorage
}

// Function to save inputs to backend
async function saveInputsToBackend(payload) {
    try {
        const response = await fetch('http://127.0.0.1:5050/send_data', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error saving inputs to backend:', error);
        throw error;
    }
}

// Initialize inputs on page load based on version and backend data
document.addEventListener('DOMContentLoaded', async () => {
    const currentVersion = await fetchServerVersion();
    const storedVersion = localStorage.getItem('serverVersion');

    if (currentVersion) {
        if (storedVersion === currentVersion) {
            // Same version, load stored instruction from localStorage and credentials from backend
            await loadInputsFromBackend();
        } else {
            // Different version, clear stored instruction and update version
            localStorage.removeItem('instruction');
            localStorage.setItem('serverVersion', currentVersion);
            await loadInputsFromBackend();
        }
    } else {
        // If unable to fetch version, attempt to load credentials
        await loadInputsFromBackend();
    }
});

messageForm.addEventListener('submit', async function(event) {
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
        // Save instruction to localStorage
        localStorage.setItem('instruction', messageText.trim());
        try {
            // Send all data in a single request
            const data = await saveInputsToBackend(payload);
            console.log('Server response:', data);
            if (data.status === 'success') {
                alert('Data sent successfully!');
                messageInput.value = '';
                // Optionally clear instruction from localStorage after successful submission
                localStorage.removeItem('instruction');
            } else {
                alert('Error: ' + data.message);
            }
        } catch (err) {
            console.error('Error:', err);
            alert('An error occurred while sending the data.');
        }
    } else {
        alert('Please enter the API key, LLM model, and a message before sending.');
    }
});
