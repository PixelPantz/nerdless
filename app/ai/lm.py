from transformers import AutoModelForCausalLM, AutoTokenizer

from app.config import settings

checkpoint = fr"app/ai/models/toxic_ruDialoGPT" if settings.lm_mode == 'local' else settings.hf_model_name
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)


def model_generate(input):
    """Model generation function for running in asyncio executor"""
        
    inputs = tokenizer(input, return_tensors='pt')

    return model.generate(
        **inputs,
        top_k=10,
        top_p=0.95,
        num_beams=3,
        num_return_sequences=1,
        do_sample=True,
        no_repeat_ngram_size=2,
        temperature=0.7,
        repetition_penalty=1.2,
        length_penalty=1.0,
        eos_token_id=50257,
        max_new_tokens=48,
        pad_token_id=0
    )
