import sys
import typer
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.live import Live
from typing import Optional, List

from playbooks.core.loader import load
from playbooks.core.runtime import RuntimeConfig, SingleThreadedPlaybooksRuntime
from dotenv import load_dotenv
load_dotenv()

app = typer.Typer()
console = Console()

def print_markdown(text: str):
    """Print text as markdown using rich"""
    md = Markdown(text)
    console.print(md)

def print_streaming_markdown(stream_iterator):
    """Print streaming markdown content"""
    content = ""
    with Live(Markdown(content), refresh_per_second=10) as live:
        for chunk in stream_iterator:
            content += chunk
            live.update(Markdown(content))

@app.command()
def chat(
    playbook_paths: List[str] = typer.Argument(
        ...,
        help="One or more paths to playbook files. Supports glob patterns"
    ),
    llm: str = typer.Option(
        None,
        help="LLM provider to use (openai, anthropic, vertexai)"
    ),
    model: str = typer.Option(
        None,
        help="Model name for the selected LLM"
    ),
    api_key: Optional[str] = typer.Option(
        None,
        help="API key for the selected LLM"
    ),
    stream: bool = typer.Option(
        False,
        help="Enable streaming output from LLM"
    )
):
    """Start an interactive chat session using the specified playbooks and LLM"""
    
    try:
        # Load playbooks
        playbook_paths = playbook_paths[1:]
        combined_playbooks = load(playbook_paths)
        
        # Initialize runtime with selected LLM
        config = RuntimeConfig(
            model=model,
            api_key=api_key
        )
        runtime = SingleThreadedPlaybooksRuntime(config)
        
        # Start chat loop
        while True:
            user_input = Prompt.ask("\n[blue]User[/blue]")
            if user_input.lower() in ["exit", "quit"]:
                break
                
            try:
                console.print("\n[yellow]Agent: [/yellow]")
                if stream:
                    response_stream = runtime.stream(combined_playbooks, user_input=user_input)
                    print_streaming_markdown(response_stream)
                else:
                    response = runtime.run(combined_playbooks, user_input=user_input)
                    print_markdown(response)
            except Exception as e:
                console.print(f"\n[red]Error:[/red] {str(e)}")
                
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/yellow]")

def main():
    app()

if __name__ == "__main__":
    main()