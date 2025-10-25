"""
Main entry point for Hello World Test Agent

Usage:
    python src/main.py
    python src/main.py --name "Your Name"
"""

import argparse
import logging
from agents.hello_world_agent import HelloWorldAgent


def setup_logging(verbose: bool = False):
    """Configure logging settings"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    """Main execution function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Cursor AI Hello World Test Agent'
    )
    parser.add_argument(
        '--name',
        type=str,
        default='World',
        help='Name to greet (default: World)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    parser.add_argument(
        '--info',
        action='store_true',
        help='Show agent information'
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    # Initialize agent
    logger.info("Starting Hello World Test Agent")
    agent = HelloWorldAgent()
    
    # Show agent info if requested
    if args.info:
        info = agent.get_agent_info()
        print("\n=== Agent Information ===")
        for key, value in info.items():
            print(f"{key.capitalize()}: {value}")
        print("========================\n")
    
    # Execute agent
    result = agent.execute(args.name)
    print(f"\n{result}\n")
    
    logger.info("Agent execution completed")


if __name__ == "__main__":
    main()
