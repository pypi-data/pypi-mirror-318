<h1 align="center">Mini LLM Flow - LLM Framework in 100 Lines</h1>

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Docs](https://img.shields.io/badge/docs-latest-blue)](https://zachary62.github.io/miniLLMFlow/)

A [100-line](minillmflow/__init__.py) minimalist LLM framework for agents, task decomposition, RAG, etc.

- Install via  ```pip install minillmflow```, or just copy the [source](minillmflow/__init__.py) (only 100 lines)

- **Pro tip:** Build LLM apps with LLMs assistants (ChatGPT, Claude, etc.)

  - Chat with [Mini LLM Flow Assistant](https://chatgpt.com/g/g-677464af36588191b9eba4901946557b-mini-llm-flow-assistant)
 
  - Use your own LLMs and provide contexts via [this prompt](assets/prompt)

Documentation: https://minillmflow.github.io/miniLLMFlow/

## Why Mini LLM Flow?

Mini LLM Flow is designed to be **the framework used by LLMs**. In the future, LLM projects will *self-programmed* by LLMs themselves: Users specify requirements, and LLMs will design, build, and maintain. Current LLMs are:

1. **👍 Good at Low-level Implementation:** LLMs can handle *LLM wrappers, tools, and prompts*, which don't require any framework. Current frameworks are often over-engineered, making them difficult for humans (and LLMs) to understand.

2. **👎 Bad at High-level Paradigms:** While paradigms like *MapReduce, task decomposition, and agents* are powerful, LLMs still struggle to design them elegantly. These high-level concepts should be emphasized in frameworks.

The ideal framework for LLMs should (1) **strip away low-level implementations**, and (2) **keep high-level paradigms** to program against. Hence, we provide this minimal (100-line) framework that allows LLMs to focus on what matters.  

Mini LLM Flow is also a **great learning resource**, as current frameworks abstract too much away.

<div align="center">
  <img src="/assets/minillmflow.jpg" width="400"/>
</div>

## Tutorial

- Documentation: https://minillmflow.github.io/miniLLMFlow/

- Beginner Tutorial: [Text summarization for Paul Graham Essay + QA agent](https://colab.research.google.com/github/zachary62/miniLLMFlow/blob/main/cookbook/demo.ipynb)

    - Have questions for this tutorial? Ask LLM assistants through [this prompt](https://chatgpt.com/share/676f16d2-7064-8000-b9d7-f6874346a6b5)
