"""
Hello World Demo
================

This is a simple Python script to demonstrate basic programming concepts.
Students can modify this file to practice making commits!
"""

def greet(name="World"):
    """
    A simple greeting function.
    
    Args:
        name (str): The name to greet. Defaults to "World".
    
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Main function to demonstrate the greeting."""
    print(greet())
    print(greet("Students"))
    print(greet("GitHub Learners"))
    
    # Try adding your own greeting below!
    # print(greet("Your Name"))


if __name__ == "__main__":
    main()
