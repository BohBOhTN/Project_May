# 🧘 Bien-Être Test Application

Welcome to the **Bien-Être Test Application**, a web-based tool to assess users' well-being through a series of questions. At the end of the test, users receive feedback based on their total score and can view nearby doctors if their score indicates a high risk of distress.

---

## 🚀 **Features**
- **Dynamic Questionnaire**: Users answer multiple-choice questions to calculate their well-being score.
- **Personalized Feedback**: Feedback is displayed based on the user's final score:
  - **0 - 10**: "Vous semblez bien gérer vos émotions et votre stress. Continuez !"
  - **11 - 20**: "Vous pourriez ressentir un certain stress ou des fluctuations émotionnelles, mais elles restent gérables. Pensez à des activités relaxantes."
  - **21 and above**: "Vous montrez des signes de stress ou de mal-être significatifs. Une discussion avec un professionnel est recommandée."
- **Find Nearby Doctors**: If the user's score exceeds 31, a "Check Near Doctor" button appears. This button prompts the user for GPS coordinates and provides a route to a nearby doctor using Google Maps.
- **Responsive Design**: The app is mobile-friendly and offers a clean, colorful user experience.

---

## 📋 **Installation Instructions**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/BohBOhTN/bien-etre-test.git
cd bien-etre-test
