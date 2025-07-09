# LoRA Fine-Tuned GPT-2: Quotes, Poems & Conversations Generator

This project fine-tunes OpenAI’s GPT-2 using the [LoRA (Low-Rank Adaptation)](https://arxiv.org/abs/2106.09685) technique on a curated dataset of:

-  Human-like conversations (Ubuntu Dialogue Corpus)
-  Motivational quotes
-  English poems

The final model is lightweight (~7MB adapter) and runs efficiently on CPUs/GPUs — deployable as a web app using [Gradio](https://gradio.app).

---

##  Features

-  Fine-tuned using **PEFT (LoRA)** for fast, memory-efficient training
-  Generates realistic dialogues, motivational lines, and poetic verses
-  Uses GPT-2 as the base model
-  Web interface powered by **Gradio**
-  Easy to deploy on **Hugging Face Spaces** or **AWS EC2**

---

##  Model Training Summary

-  **Base model:** GPT-2 (`117M`)
-  **LoRA adapters:** Trained using PEFT on ~700MB+ combined dataset
-  **Datasets:**
  - Ubuntu Dialogue Corpus (chats)
  - Motivational Quotes (Hugging Face)
  - Poems Dataset

---

##  Project Structure

my-lora-gpt2-app/
- app.py # Gradio web interface
- requirements.txt # Python dependencies
- lora_finetuned_model/ # LoRA adapter and tokenizer files



## Credits

Transformers by Hugging Face
PEFT: Parameter Efficient Fine-Tuning

## 📊 Datasets

### 1. Ubuntu Dialogue Corpus  
-  [GitHub – rkadlec/ubuntu-ranking-dataset-creator](https://github.com/rkadlec/ubuntu-ranking-dataset-creator)  
-  Multi-turn, technical human conversations  
-  Used for training conversational ability

### 2. Motivational Quotes Dataset  
-  [Hugging Face – `asuender/motivational-quotes`](https://huggingface.co/datasets/asuender/motivational-quotes)  
-  Short, inspirational quotes with authors  
-  Used for stylistic and emotional depth

### 3. Poems Dataset  
-  Public domain (Poetry Foundation, Gutenberg, etc.)  
-  Poem title, author, and verses  
-  Used to teach rhythm, creativity, and structure

##  Run Locally

```bash
git clone https://github.com/<your-username>/lora-gpt2-app.git
cd lora-gpt2-app
pip install -r requirements.txt
python app.py
```
## About Me
  Satyam Kurum
- Aspiring Data Scientist | ML Developer | 2025 NITK Surathkal Graduate
- Passionate about GenAI, NLP, and creative machine learning apps

- You're free to use, modify, and distribute it with attribution.





