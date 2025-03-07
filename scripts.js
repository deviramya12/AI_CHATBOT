async function sendMessage() {
  const userInput = document.getElementById('user_input').value;
  const response = await fetch('/api/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ message: userInput })
  });
  const data = await response.json();

  // Update the #chatbot-body element with new message
  const chatbotBody = document.getElementById('chatbot-body');
  chatbotBody.innerHTML += `<div>User: ${userInput}</div><div>Bot: ${data.bot_response}</div>`;

  document.getElementById('user_input').value = '';
}
