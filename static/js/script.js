let currentIndex = 1; // Start with the first question
const totalQuestions = 9; // Total number of questions
let responses = []; // Store user responses

// Load the first question
async function loadQuestion(index) {
  try {
    const response = await fetch(`/question/${index}`);
    if (response.ok) {
      const data = await response.json();
      document.getElementById('question-text').textContent = data.question;
      document.getElementById('progress').textContent = `${index} of ${totalQuestions}`;
    } else {
      showFinalScore();
    }
  } catch (error) {
    console.error('Error loading question:', error);
  }
}

// Handle user choice
async function handleChoice(value) {
  responses.push(parseInt(value, 10)); // Add the selected value to responses

  if (currentIndex < totalQuestions) {
    currentIndex++;
    loadQuestion(currentIndex); // Load the next question
  } else {
    showFinalScore();
  }
}

// Display the final score
async function showFinalScore() {
  const response = await fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ responses }),
  });
  const result = await response.json();
  document.querySelector('.grid').style.display = 'none';
  document.getElementById('progress').style.display = 'none';
  document.getElementById('score-result').style.display = 'block';
  document.getElementById('final-score').textContent = result.score;
}

// Add event listeners to option buttons
document.querySelectorAll('.option').forEach((button) => {
  button.addEventListener('click', (e) => {
    handleChoice(e.target.closest('.option').dataset.value);
  });
});

// Initialize the first question
loadQuestion(currentIndex);
