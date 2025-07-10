# embedding-model.py
import ollama
import chromadb

# ANSI color codes for terminal formatting
class Colors:
    HEADER = '\033[95m'      # Magenta
    BLUE = '\033[94m'        # Blue
    CYAN = '\033[96m'        # Cyan
    GREEN = '\033[92m'       # Green
    YELLOW = '\033[93m'      # Yellow
    RED = '\033[91m'         # Red
    BOLD = '\033[1m'         # Bold
    UNDERLINE = '\033[4m'    # Underline
    END = '\033[0m'          # Reset to default

# Sample documents for the knowledge base
documents = [
    "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "Java is a widely used, object-oriented programming language and computing platform first released in 1995.",
    "Java and Python are both popular, high-level programming languages, but they have different strengths and weaknesses."
]

print(Colors.BOLD + Colors.HEADER + "=" * 80)
print("AICodeGeek🚀 RAG SYSTEM - RETRIEVAL AUGMENTED GENERATION")
print("=" * 80 + Colors.END)

# Initialize ChromaDB client and create collection
client = chromadb.Client()
collection = client.create_collection(name="docs")

print(f"\n{Colors.BLUE}📚 Building Knowledge Base...{Colors.END}")
print(Colors.BLUE + "-" * 40 + Colors.END)

# Store each document in a vector embedding database
for i, d in enumerate(documents):
    print(f"   Processing document {i+1}: {d[:50]}...")
    response = ollama.embed(model="mxbai-embed-large", input=d)
    # Extract the first (and only) embedding from the response
    embeddings = response["embeddings"][0]
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings],
        documents=[d]
    )

print(f"✅ Successfully indexed {len(documents)} documents!")

# User query
prompt = "What is python?"

print(f"\n❓ User Query: '{prompt}'")
print("-" * 40)

# Generate an embedding for the input and retrieve the most relevant doc
print("🔍 Searching knowledge base...")
response = ollama.embed(
    model="mxbai-embed-large",
    input=prompt
)

# Extract the first embedding and pass it correctly
query_embedding = response["embeddings"][0]
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

# Get the most relevant document
data = results['documents'][0][0]
print(f"📄 Most relevant document found:")
print(f"   → {data}")

# Generate a response combining the prompt and data we retrieved
print(f"\n🤖 Generating AI response using llama3.2...")
output = ollama.generate(
    model="llama3.2",
    prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
)

# Display the final response in a nice format with colors
print("\n" + Colors.CYAN + "=" * 80)
print("💬 AI RESPONSE")
print("=" * 80 + Colors.END)
print()

# Format the response with proper line breaks and indentation
response_text = output['response'].strip()

# Split into paragraphs for better readability
paragraphs = response_text.split('\n\n')
for paragraph in paragraphs:
    if paragraph.strip():
        # Wrap long lines for better readability
        words = paragraph.strip().split()
        line = ""
        for word in words:
            if len(line + word) > 75:
                print(f"{Colors.GREEN}   {line}{Colors.END}")
                line = word + " "
            else:
                line += word + " "
        if line.strip():
            print(f"{Colors.GREEN}   {line.strip()}{Colors.END}")
        print()

print(Colors.CYAN + "=" * 80)
print("✨ RAG Process Complete!")
print("=" * 80 + Colors.END)