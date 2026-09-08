# Generative AI Architectures for Enterprise Applications

### Integrating S/LLMs into EShop Customer Support

---

## Table of Contents

0. [AI Foundations — AI, ML, DL & Types of AI](#0-ai-foundations--ai-ml-dl--types-of-ai)
1. [Course Overview](#1-course-overview)
2. [Large Language Models (LLMs)](#2-large-language-models-llms)
3. [Prompt Engineering](#3-prompt-engineering)
4. [Retrieval-Augmented Generation (RAG)](#4-retrieval-augmented-generation-rag)
5. [Fine-Tuning](#5-fine-tuning)
6. [Vector Databases & Semantic Search](#6-vector-databases--semantic-search)
7. [EShop Support Architecture](#7-eshop-support-architecture)
8. [Choosing the Right Approach](#8-choosing-the-right-approach)

---

## 0. AI Foundations — AI, ML, DL & Types of AI

### The Big Picture

```
Artificial Intelligence (AI)
│
└── Machine Learning (ML)           ← learns from data
    │
    └── Deep Learning (DL)          ← learns using neural networks
        │
        ├── Generative AI (GenAI)   ← creates new content
        └── Reinforcement Learning  ← learns by trial and reward
```

---

### What is Artificial Intelligence (AI)?

**AI** is the broad field of building machines that can perform tasks that normally require human intelligence — reasoning, learning, understanding language, recognising images, making decisions.

| Example                  | AI Capability Used            |
| ------------------------ | ----------------------------- |
| Gmail spam filter        | Classification                |
| Google Maps route        | Search + Optimisation         |
| Face ID unlock           | Computer Vision               |
| Siri / Alexa             | NLP + Speech Recognition      |
| Chess engine (Stockfish) | Search + Rule-based reasoning |
| ChatGPT                  | Language Generation (GenAI)   |

---

### What is Machine Learning (ML)?

**ML** is a subset of AI where the system **learns patterns from data** rather than following hand-written rules.

```
Traditional Programming:   Rules + Data  → Output
Machine Learning:          Data + Output → Rules (learned automatically)
```

#### Types of ML

| Type                       | How it learns                         | Example                                  |
| -------------------------- | ------------------------------------- | ---------------------------------------- |
| **Supervised Learning**    | From labeled input→output pairs       | Email spam detection, price prediction   |
| **Unsupervised Learning**  | Finds hidden patterns, no labels      | Customer segmentation, anomaly detection |
| **Semi-Supervised**        | Mix of labeled + unlabeled data       | Image classification with few labels     |
| **Reinforcement Learning** | Agent earns rewards by taking actions | Game playing (AlphaGo), robotics         |
| **Self-Supervised**        | Labels generated from the data itself | LLM pre-training (predict next word)     |

#### Common ML Algorithms

```
Linear/Logistic Regression   → simple predictions, classification
Decision Trees / Random Forest → structured/tabular data
SVM (Support Vector Machine) → binary classification
K-Means                      → clustering
XGBoost / LightGBM           → tabular data competitions, industry workhorse
Neural Networks              → complex patterns, images, text, audio
```

---

### What is Deep Learning (DL)?

**DL** is a subset of ML that uses **multi-layer neural networks** (inspired by the human brain) to automatically learn hierarchical representations from raw data.

```
Input Layer → [Hidden Layer 1] → [Hidden Layer 2] → ... → Output Layer
              (detects edges)    (detects shapes)           (detects "cat")
```

| When to use ML           | When to use DL                   |
| ------------------------ | -------------------------------- |
| Structured/tabular data  | Images, audio, video, raw text   |
| Small to medium datasets | Very large datasets              |
| Needs interpretability   | Black-box accuracy is acceptable |
| Limited compute          | GPU/TPU available                |

#### Key Deep Learning Architectures

| Architecture        | Full Name                          | Used For                                    |
| ------------------- | ---------------------------------- | ------------------------------------------- |
| **CNN**             | Convolutional Neural Network       | Images, video                               |
| **RNN / LSTM**      | Recurrent / Long Short-Term Memory | Sequential data, old NLP                    |
| **Transformer**     | —                                  | Text, images, audio (modern standard)       |
| **GAN**             | Generative Adversarial Network     | Image generation, deepfakes                 |
| **VAE**             | Variational Autoencoder            | Image/data generation                       |
| **Diffusion Model** | —                                  | Image generation (Stable Diffusion, DALL·E) |

---

### Deep Dive — Types of AI Models

#### Transformer

The **Transformer** (2017, "Attention is All You Need") is the architecture behind virtually every modern LLM and GenAI model. It replaced RNNs by processing all tokens in parallel using a mechanism called **self-attention**.

```
How a Transformer reads "The customer wants a refund because the item was broken":

Self-Attention asks:
  "broken"  → strongly attends to → "item" and "refund"
  "refund"  → strongly attends to → "customer" and "wants"

This lets the model understand relationships across the whole sentence at once,
not just left-to-right like old RNNs.
```

**Architecture:**

```
Input Text
    │
    ▼
[Token Embeddings + Positional Encoding]
    │
    ▼
┌──────────────────────────────────┐
│     Transformer Block (×N)       │
│                                  │
│  [Multi-Head Self-Attention]     │  ← "which words relate to which?"
│           │                      │
│  [Add & Norm]                    │
│           │                      │
│  [Feed-Forward Network]          │  ← "process each position"
│           │                      │
│  [Add & Norm]                    │
└──────────────────────────────────┘
    │
    ▼
[Output Head]  →  next token / classification / embedding
```

**Variants:**

| Variant             | Direction            | Used For                   | Examples             |
| ------------------- | -------------------- | -------------------------- | -------------------- |
| **Encoder-only**    | Reads full input     | Classification, embeddings | BERT, RoBERTa        |
| **Decoder-only**    | Generates left→right | Text generation (LLMs)     | GPT-4, Llama, Claude |
| **Encoder-Decoder** | Reads then generates | Translation, summarization | T5, BART             |

**Used in:** ChatGPT, Claude, Gemini, GitHub Copilot, DALL·E, Whisper, BERT

---

#### GAN — Generative Adversarial Network

A **GAN** (2014, Ian Goodfellow) trains two neural networks against each other in a game:

```
                    ┌─────────────┐
Random Noise ──────►│  GENERATOR  │──► Fake Image
                    └─────────────┘
                           │
                           ▼ (fake image)
                    ┌─────────────┐
  Real Images ─────►│DISCRIMINATOR│──► Real or Fake?
                    └─────────────┘
                           │
                    Feedback to both
```

- **Generator** tries to produce images so realistic the Discriminator can't tell them apart
- **Discriminator** tries to correctly label real vs fake
- They train together — the Generator gets better until its output is indistinguishable from real

**Real-world examples:**

| Application                  | GAN Use                                                 |
| ---------------------------- | ------------------------------------------------------- |
| **Deepfakes**                | Face-swap video generation                              |
| **StyleGAN**                 | Photorealistic human faces (thispersondoesnotexist.com) |
| **Image-to-Image (Pix2Pix)** | Sketch → photo, satellite → map                         |
| **Data augmentation**        | Generate synthetic training data                        |
| **Super resolution**         | Upscale low-res images                                  |

**Limitation:** GANs are notoriously hard to train — they can suffer from **mode collapse** (only generating a few types of outputs) or training instability.

---

#### VAE — Variational Autoencoder

A **VAE** learns a compressed **latent representation** of data and can generate new samples by sampling from that space.

```
                   ENCODER                    DECODER
                ┌───────────┐               ┌───────────┐
Input Image ───►│           │──► z (latent ►│           │──► Reconstructed
                │  Compress │    vector)    │  Expand   │    / Generated Image
                └───────────┘               └───────────┘
                      │                          ▲
                      └─── sample from ─────────-┘
                           Normal distribution
                           (enables generation)
```

**Key difference from a plain Autoencoder:**

- A regular autoencoder just compresses and decompresses — no generation
- A VAE forces the latent space to follow a **smooth probability distribution**, so you can **sample new points** and decode them into new, valid outputs

**Real-world examples:**

| Application                  | VAE Use                                                 |
| ---------------------------- | ------------------------------------------------------- |
| **Image generation**         | Generate new faces, digits, objects                     |
| **Anomaly detection**        | Reconstruct normal data; flag high reconstruction error |
| **Drug discovery**           | Generate new molecular structures                       |
| **Data imputation**          | Fill in missing values in datasets                      |
| **Latent space exploration** | Interpolate between two images smoothly                 |

---

#### Diffusion Model

**Diffusion models** (the backbone of Stable Diffusion, DALL·E 3, Midjourney) work by learning to **reverse a noise-adding process**.

```
FORWARD PROCESS (training — add noise step by step):
  [Real Image] → [Slightly Noisy] → [More Noisy] → ... → [Pure Noise]

REVERSE PROCESS (inference — denoise step by step):
  [Pure Noise] → [Less Noisy] → [Less Noisy] → ... → [Generated Image]
                 ▲
         Neural network predicts
         "what noise was added?"
         at each step
```

**Why diffusion beats GANs for images:**

- More stable training (no adversarial game)
- Higher quality and diversity
- Can be guided by text prompts (via CLIP embeddings)

**Real-world examples:**

| Model                | Output                            |
| -------------------- | --------------------------------- |
| **DALL·E 3**         | Text → photorealistic images      |
| **Stable Diffusion** | Text/image → images (open source) |
| **Midjourney**       | Text → artistic images            |
| **Sora**             | Text → video clips                |
| **AudioLDM**         | Text → audio / music              |

---

#### CNN — Convolutional Neural Network

**CNNs** are designed specifically for **grid-like data** (images, video). Instead of connecting every neuron to every pixel (too expensive), they use small **filters that slide across the image** to detect local features.

```
Input Image (28×28)
    │
    ▼
[Conv Layer 1]  →  detects edges, corners
    │
    ▼
[Conv Layer 2]  →  detects shapes (eyes, wheels)
    │
    ▼
[Conv Layer 3]  →  detects high-level features (faces, cars)
    │
    ▼
[Flatten + Dense Layer]
    │
    ▼
Output: "cat" / "dog" / "damaged product"
```

**Real-world examples:**

| Application           | CNN Use                                       |
| --------------------- | --------------------------------------------- |
| **Face ID**           | Face detection + recognition                  |
| **Medical imaging**   | Tumour detection in X-rays/MRIs               |
| **Self-driving cars** | Pedestrian and lane detection                 |
| **EShop**             | Damaged product detection from customer photo |
| **OCR**               | Reading text from scanned documents           |

---

#### RNN / LSTM (Legacy — largely replaced by Transformers)

**RNNs** process sequences **one token at a time**, maintaining a hidden state that carries memory forward. **LSTMs** added gates to control what to remember vs forget.

```
"My order"  →  [RNN] → hidden state h1
"My order is"  → [RNN] → hidden state h2
"My order is late" → [RNN] → hidden state h3 → Output
```

**Limitation:** Can't remember long sequences well (vanishing gradient). Transformers solved this with attention, which is why RNNs are largely obsolete for NLP.

**Still used in:** Time-series forecasting, some audio processing, lightweight edge models

---

### Model Architecture Summary

```
Image Tasks
├── CNN                  → Classification, detection, segmentation
├── GAN                  → Image generation, style transfer, deepfakes
├── VAE                  → Image generation, anomaly detection
└── Diffusion Model      → High-quality image/video generation (SOTA)

Text Tasks
├── Transformer (Encoder)       → BERT — classification, embeddings, search
├── Transformer (Decoder / LLM) → GPT, Llama — text generation, chat, code
└── Transformer (Enc-Dec)       → T5, BART — translation, summarization

Audio Tasks
├── CNN + RNN            → Speech recognition (old)
├── Transformer (Whisper)→ Speech-to-text (modern)
└── Diffusion (AudioLDM) → Text-to-audio generation

Multimodal
└── Transformer (vision + text) → GPT-4o, Gemini, CLIP
```

---

### Types of AI — By Capability

| Type                 | Description                                   | Status           | Example                                     |
| -------------------- | --------------------------------------------- | ---------------- | ------------------------------------------- |
| **ANI** — Narrow AI  | Excels at one specific task                   | ✅ Exists today  | Chess engine, spam filter, face recognition |
| **AGI** — General AI | Matches human-level reasoning across any task | 🔬 Research goal | Not yet achieved                            |
| **ASI** — Super AI   | Surpasses human intelligence in all domains   | 🔮 Theoretical   | Hypothetical future                         |

> Everything we use today — including ChatGPT — is **ANI** (Narrow AI), even though it feels broad.

---

### Types of AI — By Approach

#### 1. Traditional / Rule-Based AI

Hard-coded logic, decision trees, expert systems. No learning from data.

```python
# Traditional AI — rule-based ticket classifier
def classify_ticket(text: str) -> str:
    if "payment" in text or "charge" in text:
        return "billing"
    elif "delivery" in text or "shipping" in text:
        return "shipping"
    elif "return" in text or "refund" in text:
        return "returns"
    return "general"
```

- **Pro:** Fully explainable, no data needed
- **Con:** Brittle — breaks on anything not in the rules
- **Used in:** Early chatbots (ELIZA), rule engines, decision support systems

---

#### 2. Classical Machine Learning AI

Learns from labeled data using statistical algorithms (not neural networks).

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Train a ticket classifier on historical labeled data
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(ticket_texts)

model = LogisticRegression()
model.fit(X_train, ticket_labels)

# Predict
X_new = vectorizer.transform(["My payment was charged twice"])
print(model.predict(X_new))   # ['billing']
```

- **Pro:** Fast, interpretable, works well on tabular data
- **Con:** Needs feature engineering, struggles with nuance
- **Used in:** Fraud detection, credit scoring, recommendation systems

---

#### 3. Generative AI (GenAI)

AI that **creates new content** — text, images, audio, code, video — by learning patterns from massive datasets.

```
Discriminative AI:  Input → Label  (is this a cat? yes/no)
Generative AI:      Prompt → New Content  (write me a poem about cats)
```

| Model Type     | Creates              | Examples                             |
| -------------- | -------------------- | ------------------------------------ |
| **LLM**        | Text, code           | ChatGPT, Claude, Gemini, Llama       |
| **Image Gen**  | Images               | DALL·E, Stable Diffusion, Midjourney |
| **Audio Gen**  | Speech, music        | ElevenLabs, Suno, Whisper            |
| **Video Gen**  | Video clips          | Sora, Runway, Pika                   |
| **Multimodal** | Text + Image + Audio | GPT-4o, Gemini 1.5 Pro               |
| **Code Gen**   | Source code          | GitHub Copilot, CodeLlama            |

```python
# Generative AI — same task as above, but LLM understands nuance
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user",
               "content": "Classify this: 'I got charged 3 times but nothing arrived yet!'"}]
)
# Understands this is BOTH billing AND shipping — nuanced!
```

---

#### 4. Agentic AI

AI systems that don't just respond to a single prompt — they **plan, take actions, use tools, and loop** until a goal is completed autonomously.

```
Traditional LLM:   User prompts → LLM responds → Done

Agentic AI:        Goal given → Agent plans → Executes tools → Observes result
                             ↑_______________ loops until goal achieved __________|
```

**Core components of an AI Agent:**

```
┌─────────────────────────────────────────┐
│               AI AGENT                 │
│                                         │
│  [Brain / LLM]  ← thinks and decides   │
│       │                                 │
│  [Memory]       ← short + long term     │
│       │                                 │
│  [Tools]        ← search, code, APIs    │
│       │                                 │
│  [Planner]      ← breaks goals to steps │
└─────────────────────────────────────────┘
```

**Example — Agentic EShop Support:**

```python
# Agent goal: "Resolve ticket #5521 — customer was double charged"
#
# Agent autonomously:
# 1. Looks up order #5521 in the database (tool: query_db)
# 2. Confirms duplicate charge via payment API (tool: check_payments)
# 3. Issues refund (tool: process_refund)
# 4. Sends confirmation email (tool: send_email)
# 5. Closes ticket (tool: update_ticket)
# → All without human input
```

Popular agentic frameworks: **LangChain**, **LangGraph**, **AutoGen**, **CrewAI**, **OpenAI Assistants API**

---

#### 5. Multimodal AI

AI that understands and generates across **multiple modalities** (text, image, audio, video) simultaneously.

| Model             | Modalities                   |
| ----------------- | ---------------------------- |
| GPT-4o            | Text + Image + Audio         |
| Gemini 1.5 Pro    | Text + Image + Audio + Video |
| Claude 3.5 Sonnet | Text + Image                 |
| Whisper           | Audio → Text                 |
| DALL·E 3          | Text → Image                 |

```python
# GPT-4o reading an image of a damaged product
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text",  "text": "Is this product damaged? Classify the ticket."},
            {"type": "image_url", "image_url": {"url": "https://..."}}
        ]
    }]
)
```

---

### Summary — AI Landscape at a Glance

```
AI
├── Traditional / Rule-Based AI    → Expert systems, decision trees, ELIZA chatbot
├── Machine Learning (ML)
│   ├── Classical ML               → Fraud detection, spam filter, price prediction
│   └── Deep Learning (DL)
│       ├── Computer Vision        → Face ID, medical imaging, self-driving
│       ├── NLP (old)              → RNNs, LSTM, BERT
│       └── Generative AI (GenAI)
│           ├── LLMs               → ChatGPT, Claude, Llama — text & code
│           ├── Image Gen          → DALL·E, Stable Diffusion — images
│           ├── Audio / Video Gen  → ElevenLabs, Sora — audio/video
│           └── Agentic AI         → AutoGen, LangGraph — autonomous agents
└── Multimodal AI                  → GPT-4o, Gemini — cross-modal understanding
```

---

## 1. Course Overview

This tutorial walks you through designing **Generative AI Architectures** by integrating AI-powered Small and Large Language Models (S/LLMs) into a real-world **EShop Customer Support Enterprise Application**.

### What You Will Build

A complete AI-powered EShop support system with capabilities like:

| Capability         | Description                                     |
| ------------------ | ----------------------------------------------- |
| Classification     | Auto-tag support tickets by category            |
| Sentiment Analysis | Detect customer frustration in real time        |
| Summarization      | Summarize long ticket threads                   |
| Q&A Chat           | Answer customer questions from a knowledge base |
| Semantic Search    | Find relevant support docs using embeddings     |
| Code Generation    | Auto-generate response templates                |

### LLM Augmentation Flow

The core framework used throughout this course:

```
User Query
    │
    ▼
[Prompt Engineering]  ──► Shape the query with context and instructions
    │
    ▼
[RAG]                 ──► Inject relevant knowledge from your own data
    │
    ▼
[Fine-Tuning]         ──► Model already trained on your domain data
    │
    ▼
[LLM Response]        ──► Accurate, grounded, context-aware answer
```

---

## 2. Large Language Models (LLMs)

### How LLMs Work

LLMs are transformer-based neural networks trained on massive text corpora. They predict the next token based on all previous tokens, enabling text generation, reasoning, and summarization.

```
Input Tokens → Tokenizer → Transformer Layers → Output Tokens → Decoded Text
```

Key concepts:

- **Context window** — maximum tokens the model can process at once
- **Temperature** — controls randomness (0 = deterministic, 1 = creative)
- **Top-p / Top-k** — sampling strategies for output diversity

### Popular Models

| Type | Model             | Provider   | Best For                   |
| ---- | ----------------- | ---------- | -------------------------- |
| LLM  | GPT-4o            | OpenAI     | General, complex reasoning |
| LLM  | Claude 3.5        | Anthropic  | Long context, analysis     |
| LLM  | Gemini 1.5 Pro    | Google     | Multimodal, large context  |
| LLM  | Llama 3           | Meta       | Open-source, self-hosting  |
| LLM  | Mistral / Mixtral | Mistral AI | Fast, efficient            |
| LLM  | Grok              | xAI        | Real-time web data         |
| SLM  | GPT-4o mini       | OpenAI     | Cost-efficient, fast       |
| SLM  | Llama 3.2 mini    | Meta       | Edge / local inference     |
| SLM  | Gemma             | Google     | Lightweight, open          |
| SLM  | Phi-3.5           | Microsoft  | Small, high quality        |

### Core LLM Capabilities

```
Text Generation     → Write product descriptions, email replies
Summarization       → Condense long ticket threads
Q&A                 → Answer questions from a knowledge base
Classification      → Label ticket type: Billing / Shipping / Returns
Sentiment Analysis  → Detect: Positive / Neutral / Negative / Frustrated
Embedding Search    → Find semantically similar documents
Code Generation     → Generate API snippets, scripts
```

### Calling OpenAI Chat Completions (Python)

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful EShop support agent."},
        {"role": "user",   "content": "My order #12345 hasn't arrived. What do I do?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

### Running LLMs Locally with Ollama

```bash
# Install Ollama
brew install ollama          # macOS

# Pull and run a model
ollama pull llama3.2
ollama pull gemma

# Start local server
ollama serve

# Chat in terminal
ollama run llama3.2
```

```python
# Call local Ollama via OpenAI-compatible API
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Summarize this support ticket: ..."}]
)
```

### Function Calling & Structured Output

```python
import json

tools = [{
    "type": "function",
    "function": {
        "name": "classify_ticket",
        "description": "Classify a support ticket into a category",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "enum": ["billing", "shipping", "returns", "technical", "general"]
                },
                "priority": {
                    "type": "string",
                    "enum": ["low", "medium", "high", "urgent"]
                }
            },
            "required": ["category", "priority"]
        }
    }
}]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "My payment was charged twice!"}],
    tools=tools,
    tool_choice="auto"
)

tool_call = response.choices[0].message.tool_calls[0]
result = json.loads(tool_call.function.arguments)
print(result)
# {"category": "billing", "priority": "urgent"}
```

---

## 3. Prompt Engineering

### The 3-Step Design Loop

```
1. ITERATE   → Write a draft prompt, test it
2. EVALUATE  → Does the output match expectations?
3. TEMPLATIZE → Extract variables, make it reusable
```

### Advanced Prompting Techniques

#### Zero-Shot

No examples — rely on the model's training.

```
Classify this support message into one of: billing, shipping, returns, technical.

Message: "I got the wrong item in my order."
Category:
```

#### One-Shot

Provide a single example.

```
Classify support messages.

Example:
Message: "My payment failed." → Category: billing

Now classify:
Message: "Package arrived damaged." → Category:
```

#### Few-Shot

Provide multiple examples to guide the pattern.

```
Message: "I was charged twice."           → billing
Message: "My order is 5 days late."       → shipping
Message: "I want to send this back."      → returns
Message: "App keeps crashing on login."   → technical

Message: "Can I change my delivery address?" →
```

#### Chain-of-Thought (CoT)

Ask the model to reason step-by-step before answering.

```
A customer says: "I ordered two items but only one arrived and I was charged for both."

Think step by step:
1. What is the customer's main issue?
2. What department handles this?
3. What is the urgency?

Then classify: category, priority, and recommended action.
```

#### Role-Based Prompting

```
You are a senior EShop customer support agent with 10 years of experience.
Your tone is empathetic, professional, and solution-focused.
You always acknowledge the customer's frustration before offering a resolution.

Customer message: "This is ridiculous, I've been waiting 3 weeks for my order!"

Write a response:
```

### EShop Prompt Templates

#### Ticket Classification Prompt

```python
CLASSIFICATION_PROMPT = """
You are an EShop support ticket classifier.

Classify the following ticket into exactly one category:
- billing    (payments, charges, invoices, refunds)
- shipping   (delivery, tracking, delays, lost packages)
- returns    (exchanges, return requests, damaged items)
- technical  (app issues, login, website errors)
- general    (anything else)

Respond with JSON only: {{"category": "...", "confidence": 0.0-1.0}}

Ticket: {ticket_text}
"""

def classify_ticket(ticket_text: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": CLASSIFICATION_PROMPT.format(ticket_text=ticket_text)
        }],
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)
```

#### Sentiment Analysis Prompt

```python
SENTIMENT_PROMPT = """
Analyze the sentiment of this customer support message.

Return JSON: {{
  "sentiment": "positive|neutral|negative|frustrated",
  "score": -1.0 to 1.0,
  "key_emotion": "brief description"
}}

Message: {message}
"""
```

#### Summarization Prompt

```python
SUMMARIZATION_PROMPT = """
Summarize this support ticket thread in 2-3 sentences for an agent handoff.
Include: main issue, any actions already taken, current status.

Ticket thread:
{ticket_thread}

Summary:
"""
```

---

## 4. Retrieval-Augmented Generation (RAG)

### Why RAG?

LLMs have a **knowledge cutoff** and don't know your private data. RAG solves this by retrieving relevant documents at query time and injecting them into the prompt.

```
Without RAG:  User asks about your return policy → LLM guesses
With RAG:     User asks → system retrieves your actual policy doc → LLM answers accurately
```

### RAG Architecture (3 Parts)

#### Part 1 — Ingestion (Offline)

```
Your Documents (PDFs, FAQs, policies)
    │
    ▼
[Text Chunking]          → Split into ~500 token chunks
    │
    ▼
[Embedding Model]        → Convert each chunk to a vector (e.g., 1536 dimensions)
    │
    ▼
[Vector Database]        → Store vectors + original text
```

```python
from openai import OpenAI
import chromadb

client = OpenAI(api_key="YOUR_API_KEY")
chroma = chromadb.Client()
collection = chroma.create_collection("eshop_support_docs")

def ingest_document(doc_id: str, text: str):
    # Chunk the text
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    for i, chunk in enumerate(chunks):
        # Generate embedding
        embedding = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        ).data[0].embedding

        # Store in vector DB
        collection.add(
            ids=[f"{doc_id}_chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk]
        )
```

#### Part 2 — Retrieval (Online)

```
User Query
    │
    ▼
[Embed the query]        → Same embedding model as ingestion
    │
    ▼
[Vector Search]          → Find top-k most similar chunks
    │
    ▼
[Reranking]              → Re-score retrieved chunks by relevance
    │
    ▼
[Context Assembly]       → Combine top chunks into a context block
```

```python
def retrieve_context(query: str, top_k: int = 3) -> str:
    # Embed the query
    query_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    ).data[0].embedding

    # Search vector DB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    # Return combined context
    return "\n\n".join(results["documents"][0])
```

#### Part 3 — Generation (Online)

```python
RAG_PROMPT = """
You are an EShop customer support agent.
Use ONLY the context below to answer the customer's question.
If the answer is not in the context, say "I'll escalate this to a specialist."

Context:
{context}

Customer Question: {question}

Answer:
"""

def rag_answer(question: str) -> str:
    context = retrieve_context(question)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": RAG_PROMPT.format(context=context, question=question)
        }]
    )
    return response.choices[0].message.content
```

### End-to-End RAG Flow

```
Customer: "What is your return policy for electronics?"
    │
    ▼
Embed query → [0.23, -0.11, 0.87, ...]
    │
    ▼
Vector Search → Top 3 chunks from "returns_policy.pdf"
    │
    ▼
Context injected into prompt
    │
    ▼
LLM generates: "Electronics can be returned within 30 days with original packaging..."
```

---

## 5. Fine-Tuning

### What is Fine-Tuning?

Fine-tuning adapts a pre-trained LLM on your own labeled dataset so the model **internalizes** your domain knowledge, tone, and response style — without needing context injection at runtime.

### Fine-Tuning Methods

| Method                | Description                             | Cost      | Use When                      |
| --------------------- | --------------------------------------- | --------- | ----------------------------- |
| **Full Fine-Tuning**  | Retrain all model weights               | Very high | Large budget, max performance |
| **PEFT**              | Freeze most weights, tune small layers  | Medium    | Good balance                  |
| **LoRA**              | Add small trainable adapter matrices    | Low       | Most common in practice       |
| **Transfer Learning** | Start from a domain-specific checkpoint | Low       | Domain already exists         |

### LoRA — How It Works

```
Original weight matrix W  (frozen)
+
Small adapter matrices A × B  (trainable, rank r << original)
=
Effective fine-tuned behavior with minimal parameters
```

### Fine-Tuning Workflow

```
1. Collect labeled examples (input → ideal output)
2. Format as JSONL training file
3. Upload to fine-tuning service (e.g., OpenAI, Hugging Face)
4. Run training job
5. Evaluate on validation set
6. Deploy fine-tuned model
```

### Training Data Format (JSONL)

```jsonl
{"messages": [{"role": "system", "content": "You are an EShop support agent."}, {"role": "user", "content": "My order is late."}, {"role": "assistant", "content": "I'm sorry to hear that! Let me check your order status right away. Could you provide your order number?"}]}
{"messages": [{"role": "system", "content": "You are an EShop support agent."}, {"role": "user", "content": "I want a refund."}, {"role": "assistant", "content": "I understand your frustration. I'd be happy to help process a refund. Could you share your order ID and the reason for the return?"}]}
```

### Fine-Tuning with OpenAI API

```python
# 1. Upload training file
with open("eshop_training.jsonl", "rb") as f:
    training_file = client.files.create(file=f, purpose="fine-tune")

# 2. Start fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=training_file.id,
    model="gpt-4o-mini",
    hyperparameters={"n_epochs": 3}
)

print(f"Job ID: {job.id}")

# 3. Use fine-tuned model
response = client.chat.completions.create(
    model=job.fine_tuned_model,   # e.g., "ft:gpt-4o-mini:org:eshop:abc123"
    messages=[{"role": "user", "content": "Track my order #99887"}]
)
```

---

## 6. Vector Databases & Semantic Search

### Core Concepts

| Concept                 | Description                                                |
| ----------------------- | ---------------------------------------------------------- |
| **Vector**              | A list of numbers representing meaning (e.g., 1536 floats) |
| **Embedding**           | The process of converting text → vector                    |
| **Semantic Similarity** | Two texts are "close" if their vectors are close           |
| **Vector Database**     | Database optimized to store and search vectors at scale    |

### Embedding Models

| Model                    | Provider  | Dimensions | Run Via        |
| ------------------------ | --------- | ---------- | -------------- |
| `text-embedding-3-small` | OpenAI    | 1536       | API            |
| `text-embedding-3-large` | OpenAI    | 3072       | API            |
| `all-minilm`             | Community | 384        | Ollama (local) |
| `nomic-embed-text`       | Nomic     | 768        | Ollama (local) |

### Similarity Metrics

**Cosine Similarity** — angle between two vectors (most common)
$$\text{similarity} = \frac{A \cdot B}{\|A\| \|B\|}$$

- Result: `-1` (opposite) to `1` (identical)
- Best for: comparing text semantics regardless of length

**Euclidean Distance** — straight-line distance between points
$$d = \sqrt{\sum_{i}(A_i - B_i)^2}$$

- Result: `0` (identical) to `∞`
- Best for: spatial/geometric similarity

### Vector Search Algorithms

| Algorithm   | Full Name                           | Speed        | Accuracy | Use When               |
| ----------- | ----------------------------------- | ------------ | -------- | ---------------------- |
| **kNN**     | k-Nearest Neighbors                 | Slow (exact) | 100%     | Small datasets         |
| **ANN**     | Approximate Nearest Neighbor (HNSW) | Fast         | ~95-99%  | Production scale       |
| **DiskANN** | Disk-based ANN                      | Very fast    | ~95%     | Billion-scale datasets |

### Popular Vector Databases

| Database            | Best For                         | Hosting             |
| ------------------- | -------------------------------- | ------------------- |
| **Chroma**          | Local dev, prototyping           | Self-hosted         |
| **Qdrant**          | High-performance, filtering      | Self-hosted / Cloud |
| **Pinecone**        | Fully managed, serverless        | Cloud               |
| **Weaviate**        | Hybrid search (vector + keyword) | Self-hosted / Cloud |
| **Milvus**          | Enterprise scale                 | Self-hosted / Cloud |
| **PgVector**        | Existing PostgreSQL users        | Self-hosted         |
| **Redis**           | Low-latency, caching layer       | Self-hosted / Cloud |
| **Azure AI Search** | Azure ecosystem                  | Azure Cloud         |

### Semantic Search Example with Chroma

```python
import chromadb
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
chroma = chromadb.PersistentClient(path="./eshop_vectordb")
collection = chroma.get_or_create_collection("support_kb")

def embed(text: str) -> list[float]:
    return client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

# Add documents
docs = [
    "Our return policy allows returns within 30 days of purchase.",
    "Shipping typically takes 3-5 business days.",
    "Contact billing@eshop.com for invoice disputes."
]

for i, doc in enumerate(docs):
    collection.add(ids=[str(i)], embeddings=[embed(doc)], documents=[doc])

# Search
query = "How long do I have to return something?"
results = collection.query(query_embeddings=[embed(query)], n_results=1)
print(results["documents"][0][0])
# "Our return policy allows returns within 30 days of purchase."
```

---

## 7. EShop Support Architecture

### Full Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                   EShop Customer Portal                 │
│              (React / Next.js Frontend)                 │
└──────────────────────────┬──────────────────────────────┘
                           │ HTTP/REST
┌──────────────────────────▼──────────────────────────────┐
│              EShop Support API (.NET / Node.js)         │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────────┐  │
│  │ Ticket      │  │  RAG Chat   │  │  Fine-Tuned    │  │
│  │ Classifier  │  │  Service    │  │  Response Gen  │  │
│  └──────┬──────┘  └──────┬──────┘  └───────┬────────┘  │
└─────────┼────────────────┼─────────────────┼───────────┘
          │                │                 │
          ▼                ▼                 ▼
┌─────────────────┐  ┌──────────────┐  ┌────────────────┐
│  OpenAI / LLM   │  │  Vector DB   │  │  Fine-Tuned    │
│  (GPT-4o, etc.) │  │  (Qdrant /   │  │  Model         │
│                 │  │   PgVector)  │  │  (ft:gpt-4o)   │
└─────────────────┘  └──────────────┘  └────────────────┘
```

### Microservices with LLMs and VectorDBs as Backing Services

```
EShop Microservices
├── ticket-service          → CRUD for support tickets
├── classification-service  → LLM-powered auto-tagging
├── rag-chat-service        → RAG Q&A for customers
├── sentiment-service       → Real-time sentiment on messages
├── embedding-service       → Document ingestion + vector storage
└── notification-service    → Auto-response generation

Backing Services
├── OpenAI API              → LLM inference
├── Qdrant / PgVector       → Vector storage
├── PostgreSQL              → Ticket and user data
└── Azure AI Search         → Hybrid search (keyword + semantic)
```

### Using Azure Cloud AI Services

```python
# Azure OpenAI
from openai import AzureOpenAI

azure_client = AzureOpenAI(
    api_key="YOUR_AZURE_OPENAI_KEY",
    api_version="2024-02-01",
    azure_endpoint="https://YOUR_RESOURCE.openai.azure.com"
)

response = azure_client.chat.completions.create(
    model="gpt-4o",           # your deployment name
    messages=[{"role": "user", "content": "Classify this ticket: ..."}]
)
```

```python
# Azure AI Search (vector + keyword hybrid)
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

search_client = SearchClient(
    endpoint="https://YOUR_SEARCH.search.windows.net",
    index_name="eshop-support-docs",
    credential=AzureKeyCredential("YOUR_SEARCH_KEY")
)

results = search_client.search(
    search_text="return policy",
    vector_queries=[{
        "vector": embed("return policy"),
        "k_nearest_neighbors": 3,
        "fields": "content_vector"
    }]
)
```

---

## 8. Choosing the Right Approach

### Decision Guide

```
Do you have domain-specific data and budget for training?
    YES → Fine-Tuning (bakes knowledge into the model)
    NO  ↓

Do you have a private knowledge base (FAQs, policies, docs)?
    YES → RAG (retrieves at query time, always up-to-date)
    NO  ↓

Can you solve it with better instructions alone?
    YES → Prompt Engineering (fastest, cheapest)
```

### Comparison Table

| Factor                    | Prompt Engineering                | RAG                       | Fine-Tuning                |
| ------------------------- | --------------------------------- | ------------------------- | -------------------------- |
| **Setup cost**            | Very low                          | Medium                    | High                       |
| **Speed**                 | Fast                              | Medium (retrieval step)   | Fast (after training)      |
| **Knowledge freshness**   | Static (model knowledge)          | Always up-to-date         | Snapshot at training time  |
| **Private data support**  | No                                | Yes                       | Yes                        |
| **Consistency of output** | Medium                            | Medium-High               | High                       |
| **Best for**              | Quick prototyping, standard tasks | Knowledge bases, Q&A      | Custom tone, domain jargon |
| **EShop use case**        | Classification, summarization     | Policy Q&A, ticket search | Custom agent persona       |

### Recommended Stack for EShop Support

```
Layer 1 — Prompt Engineering
    ✅ Ticket classification
    ✅ Sentiment analysis
    ✅ Summarization for agent handoff

Layer 2 — RAG
    ✅ Customer-facing Q&A chatbot
    ✅ "Find similar tickets" feature
    ✅ Knowledge base search

Layer 3 — Fine-Tuning
    ✅ Custom response tone and brand voice
    ✅ Domain-specific terminology (SKUs, policies)
    ✅ High-volume, repetitive tasks needing consistency
```

---

## Quick Reference

```python
# Minimal RAG pipeline in ~20 lines
from openai import OpenAI
import chromadb

client = OpenAI(api_key="YOUR_KEY")
db = chromadb.Client().get_or_create_collection("docs")

def embed(t): return client.embeddings.create(model="text-embedding-3-small", input=t).data[0].embedding
def add(id, text): db.add(ids=[id], embeddings=[embed(text)], documents=[text])
def search(q, k=3): return "\n".join(db.query(query_embeddings=[embed(q)], n_results=k)["documents"][0])

def ask(question):
    context = search(question)
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}]
    )
    return res.choices[0].message.content

# Usage
add("policy1", "Returns accepted within 30 days with receipt.")
print(ask("Can I return something I bought 2 weeks ago?"))
```

---

_Tutorial based on: "Design Generative AI Architectures — Integrating AI-Powered S/LLMs into EShop Support Enterprise Applications"_
