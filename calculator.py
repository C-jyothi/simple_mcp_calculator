
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("My Calculator")

# Addition tool
@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


# Subtraction tool
@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first number."""
    return a - b


# Multiplication tool
@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


# Division tool
@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")

    return a / b


# Run the MCP server
if __name__ == "__main__":
    mcp.run()
