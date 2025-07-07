🧠 Research Assistant AI-Agent

This is a command-line based AI research assistant that uses large language models and tool integration to generate structured research responses. 
It combines natural language understanding with Wikipedia search, web search, and output-saving functionality to assist users in compiling information 
efficiently.

🛠 Tech Stack

- **Python**
- **LangChain** – Agent orchestration and prompt handling
- **Claude 3.5 Sonnet** (via `langchain-anthropic`) – LLM backend
- **Pydantic** – Structured output parsing
- **Wikipedia API** – For encyclopedia-based search
- **DuckDuckGo Search** – For web-based information lookup
- **dotenv** – For managing API keys securely

📌 Features
1.Uses LangChain’s agent system
2.Supports tool calling: Wikipedia, DuckDuckGo, Save-to-File
3.Uses Claude 3.5 Sonnet (Anthropic) as the LLM
4.Parses output into structured format (topic, summary, sources, tools_used)
5.Saves results with timestamp to response_output.txt





