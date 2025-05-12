from datasets import load_dataset
ragbench = {}

# Thought: this is semi-useful, well distributed datasets, GPT generated Q/As, similar to my co-op, but scoring is in question
# Ref: https://huggingface.co/datasets/rungalileo/ragbench
for dataset in ['covidqa']: #select topic here, ['covidqa', 'cuad', 'delucionqa', 'emanual', 'expertqa', 'finqa', 'hagrid', 'hotpotqa', 'msmarco', 'pubmedqa', 'tatqa', 'techqa']:
    full_dataset = load_dataset("rungalileo/ragbench", dataset, split="test")
    sample_50 = ragbench.select(range(50))
    ragbench[dataset] = sample_50
