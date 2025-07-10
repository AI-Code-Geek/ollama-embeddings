## Running the Example

### Git Repository Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AI-Code-Geek/ollama-embeddings.git
   cd ollama-embeddings
   ```

2. **Install Python virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate Python virtual environment**:
   ```bash
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Install required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the example**:
   ```bash
   python embedding-model.py
   ```

## Conclusion

This guide demonstrates how embedding models power intelligent RAG systems by transforming text into meaningful vector representations. By leveraging local models through Ollama, you can build privacy-focused, cost-effective RAG systems that provide accurate responses based on your specific knowledge base.

The combination of embedding models and vector databases creates a powerful foundation for building intelligent applications that can understand and retrieve contextually relevant information, making AI responses more accurate and domain-specific.