import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import gradio as gr

# Load base model and tokenizer
base_model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, "lora_finetuned_model")
model.eval()

# Generate function
def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=200,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Gradio UI
gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="LoRA Fine-tuned GPT-2",
    description="Ask anything: quotes, poems, or chat prompts."
).launch()
