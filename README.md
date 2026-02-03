<h1>📄 Chat with PDF using RAG (Groq + LangChain)</h1>

<p>
A simple and efficient <b>Retrieval-Augmented Generation (RAG)</b> application that allows users to upload a PDF and ask questions about its content.
The app retrieves relevant document chunks using embeddings and generates answers using a powerful LLM via the <b>Groq API</b>.
</p>

<hr/>

<h2>🚀 Features</h2>
<ul>
  <li>Upload any PDF and ask questions</li>
  <li>Semantic search using vector embeddings</li>
  <li>True RAG (no full document dumping)</li>
  <li>Fast inference using Groq LLM API</li>
  <li>Clean and minimal codebase</li>
</ul>

<hr/>

<h2>🧠 Tech Stack</h2>
<ul>
  <li><b>LLM</b>: Groq (<code>llama-3.3-70b-versatile</code>)</li>
  <li><b>Embeddings</b>: <code>BAAI/bge-base-en-v1.5</code></li>
  <li><b>Vector Store</b>: FAISS</li>
  <li><b>Framework</b>: LangChain</li>
  <li><b>Frontend</b>: Streamlit</li>
  <li><b>Deployment</b>: Hugging Face Spaces</li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>

<pre>
rag-app/
├── app.py
├── requirements.txt
└── README.md
</pre>

<hr/>

<h2>⚙️ Setup Instructions (Local)</h2>

<h3>1️⃣ Clone the repository</h3>
<pre>
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
</pre>

<h3>2️⃣ Create and activate virtual environment</h3>
<pre>
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
</pre>

<h3>3️⃣ Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>4️⃣ Set environment variables</h3>

<p>Create a <code>.env</code> file in the project root:</p>

<pre>
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
</pre>

<h3>5️⃣ Run the app</h3>
<pre>
streamlit run app.py
</pre>

<hr/>

<h2>🌐 Deploy on Hugging Face Spaces</h2>
<ol>
  <li>Create a new <b>Streamlit Space</b></li>
  <li>Upload <code>app.py</code>, <code>requirements.txt</code>, and <code>README.md</code></li>
  <li>Go to <b>Settings → Secrets</b></li>
  <li>Add:
    <ul>
      <li><code>GROQ_API_KEY</code></li>
      <li><code>HF_TOKEN</code></li>
    </ul>
  </li>
  <li>Click <b>Deploy</b></li>
</ol>

<hr/>

<h2>🧩 How RAG Works</h2>

<ol>
  <li>PDF is loaded and split into chunks</li>
  <li>Chunks are converted into embeddings</li>
  <li>Embeddings are stored in FAISS vector store</li>
  <li>User query retrieves top-k relevant chunks</li>
  <li>Retrieved context is passed to the LLM</li>
  <li>LLM answers using <b>only retrieved context</b></li>
</ol>

<hr/>

<h2>⚠️ Limitations</h2>
<ul>
  <li>Vector store is rebuilt per PDF upload</li>
  <li>No chat history</li>
  <li>CPU-only embeddings</li>
</ul>

<hr/>

<h2>🛠 Future Improvements</h2>
<ul>
  <li>Cache vector store per PDF</li>
  <li>Add chat history</li>
  <li>Show source citations</li>
  <li>Multi-PDF support</li>
  <li>Streaming responses</li>
</ul>

<hr/>

<h2>📜 License</h2>
<p>MIT License</p>

<hr/>

<h2>⭐ Support</h2>
<p>If you like this project, give it a ⭐ on GitHub!</p>
