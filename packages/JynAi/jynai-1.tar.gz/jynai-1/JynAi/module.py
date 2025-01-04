import requests, re
from bs4 import BeautifulSoup
from transformers import T5Tokenizer, T5ForConditionalGeneration
import time
t5_tokenizer = T5Tokenizer.from_pretrained('t5-small')
t5_model = T5ForConditionalGeneration.from_pretrained('t5-small')
def JynAi(question):
    i = 1
    sources = ["https://en.wikipedia.org/wiki/"]
    for base_url in sources:
        try:
            response = requests.get(f"{base_url}{question.replace(' ', '_')}", headers={"User-Agent": "Mozilla/5.0"});response.raise_for_status();content = " ".join([para.text for para in BeautifulSoup(response.text, 'html.parser').find_all('p') if len(para.text) > 50 and not any(re.search(pattern, para.text, re.IGNORECASE) for pattern in [r'copyright', r'all rights reserved', r'terms of use', r'privacy policy', r'this page does not currently exist'])])
            if content.strip():
                input_ids = t5_tokenizer.encode(f"summarize: {content}", return_tensors="pt", max_length=512, truncation=True)
                output_ids = t5_model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)
                return t5_tokenizer.decode(output_ids[0], skip_special_tokens=True)
        except requests.exceptions.RequestException:print(f"Attempt {i} failed.");i += 1;time.sleep(0.1)
    input_text = question;inputs = t5_tokenizer.encode(input_text, return_tensors="pt");outputs = t5_model.generate(inputs, max_length=150, num_beams=5, no_repeat_ngram_size=2, early_stopping=True);return t5_tokenizer.decode(outputs[0], skip_special_tokens=True)