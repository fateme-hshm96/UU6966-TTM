# https://huggingface.co/docs/transformers/perplexity
from transformers import AutoModelForSeq2SeqLM 
from transformers import T5TokenizerFast

from datasets import load_dataset

import torch
from tqdm import tqdm


device = "cuda"

model_id = "google/flan-t5-xl"
model = AutoModelForSeq2SeqLM.from_pretrained(model_id).to(device)
tokenizer = T5TokenizerFast.from_pretrained(model_id)

print("--> model loaded")

test = load_dataset("wikitext", "wikitext-2-raw-v1", split="test")

encodings = tokenizer("\n\n".join(test["text"]), return_tensors="pt")
# encodings = tokenizer("\n\n".join(test["text"]), max_length=1024, return_tensors="pt")

print("--> data loaded and encoded")

max_length = model.config.n_positions
stride = 512
seq_len = encodings.input_ids.size(1)

nlls = []
prev_end_loc = 0
for begin_loc in tqdm(range(0, seq_len, stride)):
    end_loc = min(begin_loc + max_length, seq_len)
    trg_len = end_loc - prev_end_loc  # may be different from stride on last loop
    input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)
    target_ids = input_ids.clone()
    target_ids[:, :-trg_len] = -100

    with torch.no_grad():
        outputs = model(input_ids, labels=target_ids)

        # loss is calculated using CrossEntropyLoss which averages over input tokens.
        # Multiply it with trg_len to get the summation instead of average.
        # We will take average over all the tokens to get the true average
        # in the last step of this example.
        neg_log_likelihood = outputs.loss * trg_len

    nlls.append(neg_log_likelihood)

    prev_end_loc = end_loc
    if end_loc == seq_len:
        break

ppl = torch.exp(torch.stack(nlls).sum() / end_loc)
print("PPL:", ppl)


# Strid=256:    tensor(3.0953, device='cuda:0')
# Strid=512:    tensor(1.0968, device='cuda:0')
# Strid=1024:   tensor(1.0953, device='cuda:0')
# Strid=2048:   tensor(1.0985, device='cuda:0')
