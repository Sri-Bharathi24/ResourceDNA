# ResourceDNA
An AI sustainability tool that estimates the hidden water, energy and carbon footprint of AI queries.


# 🌱 ResourceDNA

### The Nutrition Label for AI

AI is becoming part of everyday life, but the resources used behind each AI interaction are mostly invisible to users.

**ResourceDNA** is a simple AI sustainability tool that estimates the environmental footprint of an AI query. It shows estimated **water usage, energy consumption, carbon emissions, and token processing** in an easy-to-understand nutrition-label format.

Instead of showing only technical numbers, ResourceDNA also converts the results into familiar comparisons, such as phone charging and water-bottle equivalents.

---

## 💡 Why ResourceDNA?

When we use an AI tool, we usually think about the answer we receive.

We don't normally think about:

* How much electricity was required?
* How much cooling water may have been used?
* What could be the associated carbon emissions?
* Does using a larger model always make sense for a simple task?

ResourceDNA was created to make these hidden resource costs easier to understand.

---

## 🚀 How It Works

The user:

1. Selects an AI model category.
2. Enters an AI prompt.
3. ResourceDNA estimates the number of tokens involved.
4. The system calculates estimated energy, water, and carbon usage.
5. The result is displayed as an **AI Nutrition Label**.
6. The user can also explore what the footprint could look like when the same query is repeated many times.

### Example

A user enters:

> Explain climate change to a beginner.

ResourceDNA produces an estimated label showing:

**💧 Water**
Estimated cooling water

**⚡ Energy**
Estimated inference energy

**🌍 Carbon**
Estimated CO₂e

**🔤 Tokens**
Estimated tokens processed

It also provides simple comparisons to make the numbers easier to understand.

---

## 🧠 Technology Used

* Python
* Streamlit
* HTML/CSS
* Mathematical estimation models
* Token estimation
* GitHub

---

## 📊 Resource Estimation

ResourceDNA currently uses model-level assumptions for different AI model categories.

The estimation considers:

* Estimated token count
* Energy required per 1,000 tokens
* Water associated with cooling
* Carbon intensity of electricity

The current prototype uses different resource profiles for small, mid-size, large frontier, and image-generation workloads.

---

## 🎯 Key Features

* AI-style interaction interface
* AI model selection
* Prompt-based footprint estimation
* Water, energy and carbon estimates
* Token estimation
* Easy-to-understand comparisons
* Daily usage simulation
* Explanation of how the estimates are calculated
* Responsive interface

---

## 🌍 Real-World Impact

ResourceDNA is designed to improve **awareness of AI's environmental footprint**.

The goal is not to discourage people from using AI.

Instead, it is to help users understand that digital services also depend on physical resources such as electricity, cooling infrastructure and water.

Making this information visible can encourage more thoughtful and resource-aware AI usage.

---

## ⚠️ Important Note

ResourceDNA provides **estimates, not direct measurements**.

Actual AI resource consumption can vary depending on:

* AI model and hardware
* AI provider
* Data-centre efficiency
* Cooling technology
* Geographic location
* Electricity grid mix
* Prompt and output length

Therefore, the values shown by ResourceDNA should be treated as indicative estimates rather than exact measurements.

---

## 🔮 Future Improvements

Possible future versions could include:

* Live model and provider data
* More accurate token counting
* Regional electricity and water factors
* More AI model categories
* Model-to-model resource comparison
* API-based real-time estimation
* Personal AI usage history
* Resource-efficient model recommendations

---

## 👨‍💻 Project

**ResourceDNA** was developed as an open-innovation project exploring the connection between **Artificial Intelligence and environmental sustainability**.

The project focuses on one simple question:

> **If we can see what AI gives us, can we also see what AI uses?**

---

## 📄 License

This project is created for educational, research, and hackathon purposes.
