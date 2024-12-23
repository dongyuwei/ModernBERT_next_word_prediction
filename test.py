from transformers import AutoTokenizer, AutoModelForMaskedLM

model_id = "answerdotai/ModernBERT-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

text = "The capital of France is [MASK]."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)

# To get predictions for the mask:
masked_index = inputs["input_ids"][0].tolist().index(tokenizer.mask_token_id)
predicted_token_id = outputs.logits[0, masked_index].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id)
print("Predicted token:", predicted_token)
# Predicted token:  Paris

text2 = "What If I [MASK] you,"
inputs2 = tokenizer(text2, return_tensors="pt")
outputs2 = model(**inputs2)

# To get predictions for the mask:
masked_index2 = inputs2["input_ids"][0].tolist().index(tokenizer.mask_token_id)
predicted_token_id2 = outputs2.logits[0, masked_index2].argmax(axis=-1)
predicted_token2 = tokenizer.decode(predicted_token_id2)
print("Predicted token:", predicted_token2)
