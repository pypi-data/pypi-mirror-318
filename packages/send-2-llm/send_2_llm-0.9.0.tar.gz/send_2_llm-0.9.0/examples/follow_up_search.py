"""Example of using follow-up questions feature."""

import asyncio
from rich.console import Console
from rich.panel import Panel

from send_2_llm import LLMClient
from send_2_llm.config import load_config

console = Console()

async def main():
    """Run example."""
    # Show header
    console.print(Panel("[bold blue]Follow-up Questions Example[/bold blue]", border_style="blue"))
    
    # Get config
    config = load_config()
    
    # Create client
    async with LLMClient() as client:
        # Ask initial question
        question = "What are the main challenges in quantum computing?"
        console.print(f"\n[yellow]Initial question:[/yellow] {question}")
        
        response = await client.generate(
            question,
            web_search=True,
            return_citations=True,
            return_related_questions=True
        )
        
        # Show response
        console.print("\n[green]Response:[/green]")
        console.print(Panel(response.text, border_style="green"))
        
        # Show citations
        if response.metadata.citations:
            console.print("\n[blue]Citations:[/blue]")
            for citation in response.metadata.citations:
                console.print(f"- {citation}")
        
        # Show related questions
        if response.metadata.related_questions:
            console.print("\n[magenta]Related questions:[/magenta]")
            for q in response.metadata.related_questions:
                console.print(f"- {q}")

if __name__ == "__main__":
    asyncio.run(main()) 