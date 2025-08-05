# py-sitegen

A custom static site generator built in Python that converts Markdown content into a fully functional static website. It processes Markdown files recursively, converts them to HTML using a custom parsing engine, and applies templates to generate a complete website with proper navigation and styling.

## Technologies/Libraries Used

- **Python 3** - Core programming language
- **Built-in Python modules**:
  - `os` and `pathlib` - File system operations and path handling
  - `shutil` - Directory copying and management
  - `re` - Regular expressions for Markdown parsing
  - `enum` - Enumeration classes for type definitions
- **Custom Markdown parser** - No external dependencies, built from scratch
- **HTML templating system** - Custom template replacement engine
- **Shell scripting** - Build automation with bash

## Main Features Implemented

### Core Static Site Generation
- **Recursive Markdown processing** - Automatically discovers and converts all `.md` files in nested directories
- **Custom Markdown parser** - Built-in support for:
  - Headers (H1-H6)
  - Bold and italic text formatting
  - Code blocks and inline code
  - Links and images
  - Ordered and unordered lists
  - Blockquotes
  - Paragraphs with proper line handling

### HTML Generation Engine
- **Node-based architecture** - Separate `TextNode` and `HTMLNode` classes for structured parsing
- **Template system** - Dynamic content injection with `{{ Title }}` and `{{ Content }}` placeholders
- **Path rewriting** - Automatic adjustment of asset paths for different deployment contexts (supports custom base paths)

### Build System
- **Static asset copying** - Automatically copies images and CSS from `static/` to output directory
- **Clean builds** - Removes existing output before regeneration
- **Test suite** - Comprehensive unit tests for all parsing components
- **GitHub Pages integration** - Configured for deployment with proper path handling

### Project Structure
- Organized source code with separation of concerns
- Modular design with separate files for text parsing, HTML generation, and block processing
- Template-based theming system
- Example content demonstrating all supported Markdown features