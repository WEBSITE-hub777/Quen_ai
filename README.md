# Quen AI

Quen AI ek multilingual text-first AI assistant hai jisme English, Hindi, aur Hinglish support hota hai. Is project ka goal hai ek smart conversational assistant banaana jo:

- English/Hindi/Hinglish mein baat kare
- coding help kare
- step-by-step explanation de
- future mein image tools support kare
  - text-to-image
  - image editing
  - image understanding

Is repo ko starter scaffold ke roop mein design kiya gaya hai. Isme:

- LoRA-based fine-tuning pipeline
- sample multilingual dataset
- FastAPI backend (future-ready)
- Streamlit chat UI for local testing
- training + inference instructions

## Project goals

1. Multilingual assistant
2. Coding tutor
3. Image related capabilities in future
4. Simple local-first setup

## Current status

- ✅ project structure ready
- ✅ sample training dataset ready
- ✅ LoRA fine-tuning script included
- ✅ local chat UI included
- ⏳ actual model training depends on GPU/data availability

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Future roadmap

- Add large Hindi/Hinglish instruction data
- Train LoRA model on domain data
- Add RAG for docs + code examples
- Add image tools (text-to-image, image edit, vision)
- Add API backend + deployment

## Suggested model stack

- Base LLM: Mistral-7B-Instruct or Llama-3.x instruction model
- Fine-tune: LoRA/PEFT
- UI: Streamlit
- API: FastAPI
- Vector search: FAISS / Weaviate (future)

## Training command

```bash
python train_lora.py \
  --model_name mistral-7b-instruct \
  --dataset data/sample_multilingual.jsonl \
  --output_dir outputs/quen_ai_lora \
  --epochs 3 \
  --batch_size 4
```

## Notes

Ye repo ek working starter project hai. Real-world quality aur performance ke liye Hindi/Hinglish data aur GPU compute zaroori hai.
