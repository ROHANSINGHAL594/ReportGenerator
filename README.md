# 🤖 Report Generation Agent

This project implements a report generation agent using an orchestrator pattern. The agent leverages large language models (LLMs) like Groq and OpenAI to generate reports based on user input. The application is built with Streamlit, providing a user-friendly web interface.

## ✨ Features

-   **🤖 Dual LLM Support:** Seamlessly switch between Groq and OpenAI models for report generation.
-   **- 📈 Agentic Workflow:** Utilizes a graph-based agentic workflow for robust and modular report creation.
-   **- 🖥️ Streamlit UI:** An intuitive and easy-to-use web interface for user interaction.
-   **- 🔒 Secure API Key Handling:** Safely manages API keys using Streamlit's session state.

## 🚀 How it Works

The application follows these steps to generate a report:

1.  **✍️ User Input:** The user provides a topic or a query for the report through the Streamlit interface.
2.  **🤖 LLM Selection:** The user selects their preferred LLM (Groq or OpenAI) and provides the corresponding API key.
3.  **- 📈 Agentic Orchestration:** A `GraphBuilder` class constructs a computational graph using the `langgraph` library. This graph defines the workflow for the report generation process.
4.  **- 🧠 Node-Based Execution:** The graph consists of several nodes, including:
    *   `orchestor`: The main orchestrator that directs the flow of the generation process.
    *   `llm_call`: A node that interacts with the selected LLM to process the user's query.
    *   `synth`: A node that synthesizes the information and generates the final report.
5.  **- 📝 Report Generation:** The agent traverses the graph, executing the nodes in the defined order to generate the report.
6.  **- 💻 Display Results:** The final report is displayed on the Streamlit interface for the user to view.

## 🛠️ Installation

1.  **- Clone the repository:**
    ```bash
    git clone https://github.com/ROHANSINGHAL594/ReportGenerator.git
    cd ReportGenerator
    ```
2.  **- Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **- ▶️ Run the application:**
    ```bash
    streamlit run app.py
    ```
2.  **- 🤖 Select LLM:** Choose between "Groq" and "OpenAi" from the sidebar.
3.  **- 🔑 Enter API Key:** Provide the API key for the selected LLM.
4.  **- 💬 Enter your message:** Type your report topic or query in the chat input box.
5.  **- 👀 View the report:** The generated report will be displayed on the screen.

## 📂 Project Structure

```
├── app.py
├── requirements.txt
└── src
    └── reportgen
        ├── graphs
        │   └── graph_builder.py
        ├── llms
        │   ├── groqllm.py
        │   └── openaillm.py
        ├── main.py
        ├── nodes
        │   └── nodes.py
        ├── states
        │   └── state.py
        └── ui
            ├── streamlitui
            │   ├── display.py
            │   └── loadui.py
            └── uiconfig.py
```

