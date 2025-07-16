from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime 
#search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.
    
    run,
    description="Search the web for information",    
)
#wikipedia tool 
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_max_tokens=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

#custom tool
def save_to_txt(data: str, filename: str ="response_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f" ---Resarch Output --- \nTimestamp: {timestamp}\n\n{data}\n\n "
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
        
    return f"Data successfully saved to {filename}"    
save_tool =Tool(
    name = "save_txt_to_file",
    func = save_to_txt,
    description = "Save structured resarch data to text file."
   )

   