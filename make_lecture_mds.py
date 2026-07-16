import pandas as pd
import io
import os

if __name__ == "__main__":
    template = """---
type: {type}
date: {date}
title: "{title}"
instructor: {instructor}
hide_from_announcements: true
links: 
---
Readings:
"""
    data = '''date	topic	lecturer	type
2026-08-25	Introduction & Fundamentals	DI/FD	lecture
2026-08-27	Fundamentals: Learned Representations	FD	lecture
2026-09-01	Fundamentals: Autoregressive Language Modeling	FD	lecture
2026-09-03	Recurrent Neural Networks	DI	lecture
2026-09-08	Attention and Transformers	FD	lecture
2026-09-10	Tokenization and Decoding Algorithms	DI	lecture
2026-09-15	Pretraining	DI	lecture
2026-09-17	Scaling Laws and In-Context Learning	DI	lecture
2026-09-22	Fine-tuning and Distillation	DI	lecture
2026-09-24	Reasoning and Test-Time Scaling	DI	lecture
2026-09-29	Modeling I: Retrieval and RAG	FD	lecture
2026-10-01	String search	DI	lecture
2026-10-06	Multimodal models	guest	lecture
2026-10-08	Research Skills and Experimental Design	FD	lecture
2026-10-13	Midterm	DI/FD	exam
2026-10-15	🍂 Fall Break 🍂		noclass
2026-10-20	🍂 Fall Break 🍂		noclass
2026-10-22	Benchmarking and Evaluation Techniques	FD	lecture
2026-10-27	Diffusion and Flows	FD	lecture
2026-10-29	Reinforcement Learning I: Fundamentals	FD	lecture
2026-11-03	Reinforcement Learning II: Applications	FD	lecture
2026-11-05	Democracy Day		noclass
2026-11-10	Language Model-Based Agents	DI/FD	lecture
2026-11-12	Efficiency: Quantization, Parallelism, and Distributed Training	DI	lecture
2026-11-17	Looking at data	DI	lecture
2026-11-19	Mixture of Experts	DI	lecture
2026-11-24	Scaling Sequence Length	FD	lecture
2026-11-26	🦃 Thanksgiving 🦃		noclass
2026-12-01	Multilingual NLP	DI	lecture
2026-12-03	Poster Session	DI/FD	exam
'''

    df = pd.read_csv(io.StringIO(data), sep='\t')
    for idx, row in df.iterrows():
        print(row)
        text = template.format(
            date=row["date"],
            title=row["topic"],
            instructor=row["lecturer"],
            type=row["type"])
        filepath = os.path.join("_lectures", row["date"] + ".md")
        with open(filepath, "w") as f:
            f.write(text)

