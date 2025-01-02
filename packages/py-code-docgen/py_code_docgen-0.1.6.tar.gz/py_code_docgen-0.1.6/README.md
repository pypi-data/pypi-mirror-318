# DocGen - Beautiful Documentation Generator

A powerful documentation generator that creates beautiful markdown documentation from source code.

## Features 🌟

- 📝 Interactive wizard mode for easy configuration
- 🌳 Project tree visualization
- 📚 Table of contents with customizable formats
- 🔍 Collapsible sections for better organization
- 📊 File statistics and line counts
- ⚡ Fast project reports
- 🎨 Syntax highlighting for multiple languages
- 📋 Line numbers in code blocks
- 🔗 Clickable navigation links
- 🎯 Customizable output formats
- 🔄 CLI command generation for repeatable documentation
- 🎯 Fast project reports for quick insights

## Requirements 🛠️

- Python 3.7 or higher
- Works on Windows, macOS, and Linux

## Installation 📦

You can install DocGen directly from PyPI:

```bash
pip install py-code-docgen
```

For development installation:

```bash
git clone https://github.com/ci-psy/DocGen.git
cd docgen
pip install -r requirements.txt
```

## Quick Start 🚀

1. Interactive Mode (Recommended):
```bash
py-code-docgen -i
```

2. Command Line Usage:
```bash
py-code-docgen [project_dir] -o output.md --include "py,js,cpp"
```

3. View Help and Options:
```bash
py-code-docgen --help
```

## Command Line Options 🎮

```
usage: py-code-docgen [-h] [-i] [--fast-report] [-o OUTPUT] [--include INCLUDE]
                      [--show SHOW] [--show-all] [--no-collapsible]
                      [--collapsible-level {all,main,subsections,none}]
                      [--minimal] [--line-numbers] [--no-summary] [--no-tree]
                      [--no-file-info] [--no-line-count] [--no-file-stats]
                      [--no-timestamps] [--no-sizes] [--no-toc]
                      [--toc-format {full,name_ext,name}] [--no-toc-anchors]
                      [--toc-anchor-style {simple,full_path}] [--path-info]
                      [--chunk-size CHUNK_SIZE]
                      [project_dir]
```

## Interactive Wizard Features 🧙‍♂️

The interactive wizard (`-i` flag) provides a user-friendly way to configure your documentation:

1. **Optional Fast Report**: Get a quick overview of your project before proceeding
2. **Step-by-Step Configuration**: Guided setup for all documentation options
3. **CLI Command Generation**: After configuration, you can view the equivalent CLI command to:
   - Save it for future use
   - Automate documentation generation
   - Share your exact configuration with others

Example of generated CLI command:
```bash
py-code-docgen "my_project" -o "docs.md" --include "py,js" --toc-format full --collapsible-level main --line-numbers
```

## Examples 📋

Generate documentation with default settings:
```bash
py-code-docgen .
```

Generate minimal documentation for Python files:
```bash
py-code-docgen --include py --no-toc --minimal
```

Generate documentation with full paths and main section collapsing:
```bash
py-code-docgen --include cpp --toc-format full --collapsible-level main
```

Generate a quick project report:
```bash
py-code-docgen --fast-report
```

## Output Customization 🎨

### TOC Formats
- Full paths: `dir/subdir/file.ext`
- Name with extension: `file.ext`
- Just name: `file`

### Collapsible Sections
- All sections
- Main sections only
- Subsections only
- None (disabled)

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author ✨

Created by Cosmo Inclan

## Acknowledgments 🙏

Special thanks to all contributors and users of DocGen!