![Banner](https://raw.githubusercontent.com/JonahWhaler/llm-agent-toolkit/main/images/repo-banner.jpeg)

# LLM Agent Toolkit: Modular Components for AI Workflows
LLM Agent Toolkit provides minimal, modular interfaces for core components in LLM-based applications. Simplify workflows with stateless interaction, embedding encoders, memory management, tool integration, and data loaders, designed for compatibility and scalability. It prioritizes simplicity and modularity by proposing minimal wrappers designed to work across common tools, discouraging direct access to underlying technologies. Specific implementations and examples will be documented separately in a Cookbook (planned).

PyPI: ![PyPI Downloads](https://static.pepy.tech/badge/llm-agent-toolkit)

## Attention!!!
Using this toolkit simplifies integration by providing unified and modular interfaces across platforms. Many configurations are intentionally kept at their default settings to prioritize ease of use. However, most of these components are extensible through abstract classes, allowing developers to define their own desired configurations for greater flexibility. While this approach enhances consistency and reduces complexity, advanced customization may require extending the provided abstractions. 

For developers requiring full-range customization or access to the latest features, it is recommended to consider using native libraries like `ollama` and `openai` directly.

# Table of Contents
- [LLM Agent Toolkit: Modular Components for AI Workflows](#llm-agent-toolkit-modular-components-for-ai-workflows)
  - [Attention!!!](#attention)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Fundamental Components](#fundamental-components)
  - [Core:](#core)
  - [Encoder:](#encoder)
  - [Memory:](#memory)
  - [Tool:](#tool)
  - [Loader:](#loader)
  - [Chunkers:](#chunkers)
- [Planned Feature](#planned-feature)
- [License](#license)

# Installation
  `
  pip install llm-agent-toolkit
  `

# Fundamental Components
## Core: 

A stateless chat completion interface to interact with the LLM.

**Purpose**: Serves as the central execution layer that abstracts interaction with the underlying LLM model.

**Features**:
* Supports Text-to-Text and Image-to-Text.
* Enables iterative executions for multi-step workflows.
* Facilitates tool invocation as part of the workflow.
* Support models from OpenAI and Ollama

## Encoder:
A standardized wrapper for embedding models.

**Purpose**: Provides a minimal API to transform text into embeddings, usable with any common embedding model.

**Features**:
* Abstracts away model-specific details (e.g., dimensionality, framework differences).
* Allows flexible integration with downstream components like Memory or retrieval mechanisms.
* Support OpenAI, Ollama and Transformers.
* Support asynchronous operation.

## Memory: 
Offers essential context retention capabilities.

**Purpose**: Allows efficient context management without hardcoding database or memory solutions.

**Types**:
1. *Short-term Memory*:
    * Maintains recent interactions for session-based context.
2. *Vector Memory*:
    * Combines embedding and storage for retrieval-augmented workflows.
    * Includes optional metadata management for filtering results.
    * Support Faiss and Chroma
3. *Async Vector Memory*:
    * Same as Vector Memory with async support.

## Tool:
A unified interface for augmenting the LLM's functionality.

**Purpose**: Provides a lightweight abstraction for tool integration, accommodating both simple and complex tools.

**Features**:
* *Simple Tools*: Lazy wrappers for functions or basic utilities.
* *Complex Tools*: Abstract class for external APIs or multi-step operations.

## Loader:
Responsible for converting raw data into text.

**Purpose**: Handles preprocessing and content extraction from diverse formats.

**Features**:
* Covering limited type of documents, images, and audio files.

## Chunkers:
Utility to split long text into chunks.

**Features**:
* **Basic**: 
  * *FixedCharacterChunker*: Split text into fixed-size character chunks with optional overlapping.
  * *FixedGroupChunker*: Splits text into K chunks. Supporting two levels, `word` and `character`, default is `character`.
* **Semantic**:
  * *SemanticChunker*: Split text into semantically coherent chunks.
  * *SimulatedAnnealingSemanticChunker*: Enhanced with Simulated Annealing optimization technique.

# Planned Feature
- A Cookbook with detailed implementation examples.

# License
This project is licensed under the GNU General Public License v3.0 License. See the [LICENSE](LICENSE) file for details.
