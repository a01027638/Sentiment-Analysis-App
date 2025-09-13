import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load tokenizer and model (CPU only)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct",
    device_map="cpu",
    torch_dtype="auto"
)
# Zero-shot sentiment analysis
def zero_shot_sentiment(review):
    prompt = f"""Question: Is the following review positive or negative about the movie?
    Review: {review} Answer:"""

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    outputs = model(input_ids)
    final_logits = outputs.logits[0, -1]

    positive_id = tokenizer.encode("positive", add_special_tokens=False)[0]
    negative_id = tokenizer.encode("negative", add_special_tokens=False)[0]

    if final_logits[positive_id] > final_logits[negative_id]:
        return "Positive 😊"
    else:
        return "Negative 😞"

# Few-shot sentiment analysis
def few_shot_sentiment(review):
    prompt = f"""
Translate English to Sentiment

English: The movie was fantastic!
Sentiment: Positive

English: I was expecting something more complex,  I did not like it
Sentiment: Negative

English: Not a very good acting by the cast
Sentiment: Negative

English: I hated the film.
Sentiment: Negative

English: The plot was confusing but the acting was great.
Sentiment: Positive

English: The movie was too long and boring.
Sentiment: Negative

English: An absolute masterpiece with stunning visuals.
Sentiment: Positive

English: I didn't like it
Sentiment: Negative

English: The soundtrack was amazing, but the story felt weak.
Sentiment: Negative

English: Some scenes were dull, yet overall it left me inspired.
Sentiment: Positive

English: It wasn’t terrible, but I wouldn’t watch it again.
Sentiment: Negative

English: The first half was boring, but the ending was really moving.
Sentiment: Positive

English: The special effects were impressive, though the characters lacked depth.
Sentiment: Negative

English: I expected more, but it still had a few touching moments.
Sentiment: Positive

English: The pacing was uneven and dragged in places.
Sentiment: Negative

English: The cast delivered powerful performances that saved the movie.
Sentiment: Positive

English: The jokes were flat and predictable, I barely laughed.
Sentiment: Negative

English: Despite some flaws, it was overall a delightful experience.
Sentiment: Positive


English: {review}
Sentiment:
"""

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    output = model.generate(input_ids, max_new_tokens=10)
    sentiment = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    # Extract only the sentiment
    for line in sentiment.split("\n"):
        if "Sentiment:" in line:
            return line.split(":")[-1].strip()

    return sentiment

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Movie Review Sentiment Analysis", page_icon="🎥", layout="centered")
st.title("🎬 Movie Review Sentiment Analysis 🎭")

review = st.text_area("Enter your movie review:")

if st.button("Analyze Sentiment"):
    if review.strip():
        with st.spinner("Analyzing..."):
            zero_shot_result = zero_shot_sentiment(review)
            few_shot_result = few_shot_sentiment(review)

        st.subheader("🎯 Zero-shot Result")
        st.success(f"The sentiment of the review is: {zero_shot_result}")

        st.subheader("🔍 Few-shot Result")
        st.success(f"The sentiment of the review is: {few_shot_result}")
    else:
        st.warning("Please enter a review to analyze.")
