#!/usr/bin/env python3
"""
Direct runner for the market research flow.
This script directly imports and runs the market research flow for better debugging.
"""
import asyncio
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = Path(__file__).parent.absolute()
sys.path.append(str(project_root))

# Load environment variables
load_dotenv()

# Import the flow after setting up the path
from src.prefect.flows.research_flow import market_research_flow

async def main():
    """Run the market research flow with example parameters."""
    try:
        # Example parameters - you can modify these or make them command-line arguments
        symbol = "AAPL"  # Example stock symbol
        price_target = 200  # Example price target
        horizon = "3month"  # Can be "3month", "6month", or "12month"
        
        print(f"Starting market research for {symbol} with target ${price_target} in {horizon}")
        
        # Run the flow directly
        result = await market_research_flow(
            symbol=symbol,
            price_target=price_target,
            horizon=horizon
        )
        
        print(f"\nMarket research completed successfully!")
        print(f"Run ID: {result['run_id']}")
        print(f"Results have been saved and processed.")
        
        return 0
        
    except Exception as e:
        print(f"Error running market research: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
