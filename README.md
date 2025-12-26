

# Gemini AI Inference API

A simple **FastAPI**-based inference API using **Google Gemini API** for text generation.

This project demonstrates:

- Receiving text input
- Calling the Gemini LLM API
- Returning structured JSON output
- Handling failures (timeouts, retries, rate limits, server errors)
- Logging token usage (prompt, completion, total tokens)

## Example Request

Endpoint: `POST /infer`

**Request Body:**
```json
{
  "prompt": "what is AI"
}
```

## Example Response

```json
{
  "output": "Artificial Intelligence (AI) is a broad field of computer science that focuses on creating machines capable of performing tasks that typically require human intelligence. In simpler terms, it's about making computers 'think' and 'reason' like humans, or even exceed human capabilities in certain areas...",
  "tokens_used": {}
}
```

## Token Logging

All prompts, outputs, and API token usage are logged in `token_usage.log`. This helps track usage and debug issues.

```
2025-12-25 23:03:24,548 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent "HTTP/1.1 200 OK"
2025-12-25 23:03:24,633 - Prompt: what is ai
2025-12-25 23:03:24,633 - Output: Artificial Intelligence (AI) is a broad field of computer science that focuses on **creating machines capable of performing tasks that typically require human intelligence.**

In simpler terms, it's about making computers "think" and "reason" like humans, or even exceed human capabilities in certain areas.

Here's a breakdown of what that means:

1.  **Simulating Human Intelligence:** AI systems are designed to mimic cognitive functions that humans associate with intelligence, such as:
    *   **Learning:** Acquiring information and rules for using the information.
    *   **Reasoning:** Using rules to reach approximate or definite conclusions.
    *   **Problem-Solving:** Finding solutions to complex challenges.
    *   **Perception:** Interpreting sensory information (like images or speech).
    *   **Understanding Language:** Processing and generating human language (Natural Language Processing).
    *   **Decision-Making:** Choosing the best course of action from various options.
    *   **Creativity:** Generating new ideas or products (e.g., AI art, music).

2.  **How AI Works (in a nutshell):**
    *   **Data:** AI systems learn from vast amounts of data. This data helps them identify patterns, relationships, and rules.
    *   **Algorithms:** These are the sets of instructions and statistical models that the AI uses to process data, learn, make predictions, or take actions.
    *   **Learning (Machine Learning):** A core component of AI where systems automatically improve their performance over time without being explicitly programmed for every single scenario. Deep Learning, a subset of Machine Learning, uses neural networks inspired by the human brain.

3.  **Types of AI:**
    *   **Narrow AI (Weak AI):** This is the AI we have today. It's designed and trained for a specific task.
        *   *Examples:* Virtual assistants (Siri, Alexa), recommendation systems (Netflix, Amazon), spam filters, self-driving cars (only focused on driving), medical diagnosis tools.
    *   **General AI (Strong AI / AGI):** This is hypothetical AI that would possess human-level cognitive abilities across a wide range of tasks, similar to how a human can learn and apply intelligence to almost any problem. We are not there yet.
    *   **Superintelligence (ASI):** Hypothetical AI that would surpass human intelligence in every aspect, including creativity, general knowledge, and problem-solving. This is far in the future, if ever attainable.

4.  **Key Subfields of AI:**
    *   **Machine Learning (ML):** Teaching computers to learn from data.
    *   **Deep Learning (DL):** A subset of ML using artificial neural networks with many layers.
    *   **Natural Language Processing (NLP):** Enabling computers to understand, interpret, and generate human language.
    *   **Computer Vision (CV):** Enabling computers to "see" and interpret visual information from the world.
    *   **Robotics:** Designing and building robots that can perform tasks, often incorporating AI for perception, navigation, and decision-making.
    *   **Expert Systems:** Rule-based AI systems designed to emulate the decision-making ability of a human expert.
```
```
