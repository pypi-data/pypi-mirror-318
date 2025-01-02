#!/usr/bin/env python3
import os
import datetime
import sys
import argparse
from pathlib import Path
from typing import Set, List, Dict, Optional, NamedTuple, Callable
from dataclasses import dataclass

# ANSI escape codes for color and styling
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

#
# -----------------------------
#   Data Classes & Helpers
# -----------------------------
#

class DocumentationOptions(NamedTuple):
    """Store user preferences for documentation generation."""
    project_dir: str
    output_file: str
    include_extensions: str
    show_extensions: str
    show_all: bool
    show_file_info: bool
    show_tree: bool
    show_line_count: bool
    show_file_stats: bool
    show_timestamps: bool
    show_sizes: bool
    show_summary: bool
    use_collapsible: bool
    collapsible_level: str  # 'all', 'main', 'subsections', or 'none'
    use_minimal_format: bool
    show_line_numbers: bool
    show_toc: bool
    toc_format: str
    use_toc_anchors: bool
    toc_anchor_style: str
    show_path_info: bool
    chunk_size: int

@dataclass
class FileInfo:
    """Store information about a file."""
    path: str
    size: int
    last_modified: float
    line_count: Optional[int] = None

def get_file_number(path: str) -> float:
    try:
        return int(''.join(filter(str.isdigit, os.path.basename(path))))
    except ValueError:
        return float('inf')

def parse_extensions(ext_string: str) -> Set[str]:
    """Interpret 'all' or '*' as 'include everything' (empty set)."""
    if not ext_string:
        return set()
    if ext_string.lower() in ['all', '*']:
        return set()
    parts = [x.strip() for x in ext_string.split(',')]
    return {'.' + p.lstrip('.') for p in parts}

def should_process_file(filename: str, include_extensions: Set[str]) -> bool:
    if not include_extensions:  # empty => all
        return True
    return any(filename.endswith(ext) for ext in include_extensions)

def format_path(path: str, format_type: str) -> str:
    """Format a path for references."""
    if format_type == 'full':
        return path
    elif format_type == 'name_ext':
        return os.path.basename(path)
    else:  # 'name'
        return os.path.splitext(os.path.basename(path))[0]

def format_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"

def format_time(timestamp: float) -> str:
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

#
# -----------------------------
#   Line Numbering & Chunks
# -----------------------------
#

def add_line_numbers(code: str, start_line: int = 1) -> str:
    """
    Add line numbers to code, starting from 'start_line'.
    """
    lines = code.splitlines()
    total_lines = start_line + len(lines) - 1
    width = len(str(total_lines))
    return "\n".join(
        f"{(i + start_line):{width}} │ {line}"
        for i, line in enumerate(lines)
    )

def chunked_file_reader(file_path: str, chunk_size: int = 200) -> List[str]:
    """
    Read a file in 'chunk_size'-line increments.
    """
    chunks = []
    buffer = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                buffer.append(line)
                if len(buffer) >= chunk_size:
                    chunks.append(''.join(buffer))
                    buffer = []
        if buffer:
            chunks.append(''.join(buffer))
    except Exception:
        pass
    return chunks

def get_anchor_link(file_path: str, style: str) -> str:
    """Generate an anchor link from file path."""
    if style == 'simple':
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        return base_name.lower().replace(' ', '-').replace('_', '-')
    else:
        path_no_ext = os.path.splitext(file_path)[0]
        return path_no_ext.lower().replace(' ', '-').replace('_', '-').replace('/', '-')

#
# -----------------------------
#   Analyzer & Fast Report
# -----------------------------
#

class FileCache:
    """Optional cache so we don't re-read the same file repeatedly."""
    def __init__(self):
        self._cache: Dict[str, FileInfo] = {}

    def get(self, path: str) -> Optional[FileInfo]:
        return self._cache.get(os.path.abspath(path))

    def set(self, path: str, info: FileInfo):
        self._cache[os.path.abspath(path)] = info

class ProjectAnalyzer:
    """Analyze project structure and files."""
    TEXT_EXTENSIONS = {
        '.txt', '.md', '.swift', '.metal', '.py', '.js', '.html',
        '.css', '.json', '.xml', '.yaml', '.yml', '.cpp', '.h', '.c',
        '.ts'
    }

    def __init__(self, project_dir: str, file_cache: Optional[FileCache] = None):
        self.project_dir = os.path.abspath(project_dir)
        self.file_cache = file_cache or FileCache()
        self.stats: Dict[str, int] = {}
        self.total_lines = 0
        self.file_count = 0

    def is_text_file(self, file_path: str) -> bool:
        ext = os.path.splitext(file_path)[1].lower()
        return ext in self.TEXT_EXTENSIONS

    def analyze_project(self) -> Dict[str, int]:
        """
        Walk the directory and build:
          - stats (extension -> count)
          - file_count
          - total_lines for recognized text files
        """
        for root, _, files in os.walk(self.project_dir):
            for fname in files:
                ext = os.path.splitext(fname)[1].lower()
                self.stats[ext] = self.stats.get(ext, 0) + 1
                self.file_count += 1

                full_path = os.path.join(root, fname)
                if self.is_text_file(full_path):
                    self.get_file_info(full_path)

        return self.stats

    def get_file_info(self, file_path: str) -> FileInfo:
        cached = self.file_cache.get(file_path)
        if cached:
            return cached

        p = Path(file_path)
        try:
            st = p.stat()
            fi = FileInfo(
                path=str(p),
                size=st.st_size,
                last_modified=st.st_mtime
            )
        except FileNotFoundError:
            fi = FileInfo(path=str(p), size=0, last_modified=0)

        if self.is_text_file(str(p)):
            try:
                with open(p, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    fi.line_count = len(lines)
                    self.total_lines += len(lines)
            except Exception:
                pass

        self.file_cache.set(file_path, fi)
        return fi

def print_fast_report(project_dir: str):
    """Produce a quick summary of the project."""
    proj = ProjectAnalyzer(project_dir)
    proj.analyze_project()

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"{CYAN}\n=== FAST REPORT for {project_dir} ==={RESET}")
    print(f"Generated on {now}")
    print(f"Directory: {project_dir}")
    print(f"Total Files: {proj.file_count}")
    print(f"Total Lines (approx): {proj.total_lines}")
    print("\nExtension Distribution:")
    for ext, count in sorted(proj.stats.items()):
        print(f"  {ext or '(no ext)'}: {count}")
    print()

#
# -----------------------------
#   Directory Tree & Renderer
# -----------------------------
#

def generate_tree(directory: str,
                  show_extensions: Set[str] = None,
                  prefix: str = "",
                  is_last: bool = True,
                  ignore_hidden: bool = True) -> List[str]:
    output = []
    path_dir = Path(directory)
    try:
        items = list(path_dir.iterdir())
    except PermissionError:
        return output

    if ignore_hidden:
        items = [item for item in items if not item.name.startswith('.')]

    if show_extensions:
        filtered = []
        for item in items:
            if item.is_file():
                if any(item.name.endswith(ext) for ext in show_extensions):
                    filtered.append(item)
            else:
                match_found = False
                for r, _, fs in os.walk(item):
                    if any(f.endswith(tuple(show_extensions)) for f in fs):
                        match_found = True
                        break
                if match_found:
                    filtered.append(item)
        items = filtered

    items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    for i, item in enumerate(items):
        is_last_item = (i == len(items) - 1)
        current_prefix = prefix + ("└── " if is_last_item else "├── ") if prefix else ""

        if item.is_dir():
            output.append(f"{current_prefix}{item.name}/")
            deeper_prefix = prefix + ("    " if is_last_item else "│   ")
            output.extend(generate_tree(item, show_extensions, deeper_prefix, is_last_item, ignore_hidden))
        else:
            output.append(f"{current_prefix}{item.name}")

    return output

def write_section(file_obj,
                  title: str,
                  content_func: Callable[[], None],
                  options: DocumentationOptions,
                  initial_state: str = "open",
                  is_subsection: bool = True):
    """Write a (potentially collapsible) section to the output file."""
    should_collapse = (
        options.use_collapsible and
        options.collapsible_level != 'none' and
        (
            options.collapsible_level == 'all' or
            (options.collapsible_level == 'main' and not is_subsection) or
            (options.collapsible_level == 'subsections' and is_subsection)
        )
    )

    if should_collapse:
        file_obj.write(f"<details {initial_state}>\n<summary>{title}</summary>\n\n")
        content_func()
        file_obj.write("\n</details>\n\n")
    elif options.use_minimal_format:
        file_obj.write(f"{title}:\n")
        content_func()
        file_obj.write("\n")
    else:
        file_obj.write(f"## {title}\n\n")
        content_func()
        file_obj.write("\n")

def get_language_for_extension(extension: str) -> str:
    languages = {
        '.swift': 'swift',
        '.metal': 'metal',
        '.py': 'python',
        '.md': 'markdown',
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.sh': 'bash',
        '.cpp': 'cpp',
        '.h': 'cpp',
        '.c': 'c',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.html': 'html',
        '.css': 'css',
    }
    return languages.get(extension, '')

def create_markdown(project_dir: str,
                    output_file: str,
                    include_extensions: Set[str],
                    show_extensions: Optional[Set[str]],
                    options: DocumentationOptions):
    """
    Main function that renders the markdown file.
    """
    project_dir = os.path.abspath(project_dir)
    if not os.path.isdir(project_dir):
        raise ValueError(f"Directory not found: {project_dir}")

    analyzer = ProjectAnalyzer(project_dir)
    analyzer.analyze_project()

    files_to_process: List[str] = []
    for root, dirs, files in os.walk(project_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for filename in files:
            if should_process_file(filename, include_extensions):
                full_path = os.path.join(root, filename)
                rel_path = os.path.relpath(full_path, project_dir)
                files_to_process.append(rel_path)

    if not files_to_process:
        print(f"Warning: No files matching {include_extensions} found in {project_dir}")
        return

    files_to_process.sort(key=lambda x: (x.count(os.sep), get_file_number(x), x))

    out_path = Path(output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, 'w', encoding='utf-8') as out_file:
        # Document Header
        if options.use_minimal_format:
            out_file.write("# Project Code Documentation\n")
        else:
            out_file.write("# Project Code Documentation\n\n")

        # Summary
        if options.show_summary:
            def write_summary():
                now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                if options.use_minimal_format:
                    out_file.write(f"Generated: {now_str}\n")
                    out_file.write(f"Directory: {project_dir}\n")
                    out_file.write(f"File Types: {', '.join(sorted(include_extensions))}\n")
                    if options.show_file_stats:
                        out_file.write(f"Files: {analyzer.file_count}\n")
                        if options.show_line_count:
                            out_file.write(f"Lines: {analyzer.total_lines:,}\n")
                else:
                    out_file.write(f"- **Generated on:** {now_str}\n")
                    out_file.write(f"- **Project Directory:** {project_dir}\n")
                    out_file.write(f"- **Included File Types:** {', '.join(sorted(include_extensions))}\n")

                    if options.show_file_stats:
                        out_file.write(f"- **Total Files:** {analyzer.file_count}\n")
                        if options.show_line_count:
                            out_file.write(f"- **Total Lines of Code:** {analyzer.total_lines:,}\n")

                        out_file.write("\n### File Type Distribution\n\n")
                        out_file.write("| Extension | Count |\n|-----------|-------|\n")
                        for ext, cnt in sorted(analyzer.stats.items()):
                            if ext:
                                out_file.write(f"| {ext} | {cnt} |\n")

            write_section(out_file, "Project Information", write_summary, options)

        # Tree
        if options.show_tree:
            def write_tree():
                tree_lines = generate_tree(project_dir, show_extensions)
                out_file.write("```\n")
                out_file.write("\n".join(tree_lines))
                out_file.write("\n```\n")

            write_section(out_file, "Project Tree", write_tree, options)

        # TOC
        if options.show_toc:
            def write_toc():
                for i, rel_path in enumerate(files_to_process, start=1):
                    finfo = analyzer.get_file_info(os.path.join(project_dir, rel_path))
                    display_path = format_path(rel_path, options.toc_format)
                    extras = []
                    if options.show_sizes:
                        extras.append(format_size(finfo.size))
                    if options.show_line_count and finfo.line_count:
                        extras.append(f"{finfo.line_count:,} lines")

                    if options.use_toc_anchors:  # We only add anchor if anchors & TOC are used
                        anchor = get_anchor_link(rel_path, options.toc_anchor_style)
                        out_file.write(f"{i}. [{display_path}](#{anchor})")
                    else:
                        out_file.write(f"{i}. {display_path}")

                    if extras:
                        out_file.write(f" ({', '.join(extras)})")
                    out_file.write("\n")

            write_section(out_file, "Table of Contents", write_toc, options)
            if not options.use_minimal_format:
                out_file.write("---\n\n")

        # File Sections
        for i, rel_path in enumerate(files_to_process, start=1):
            full_path = os.path.join(project_dir, rel_path)
            finfo = analyzer.get_file_info(full_path)
            display_path = format_path(rel_path, options.toc_format)

            main_collapse = (
                options.use_collapsible and
                options.collapsible_level != 'none' and
                (
                    options.collapsible_level == 'all' or
                    options.collapsible_level == 'main'
                )
            )

            # Only add an anchor if show_toc + use_toc_anchors are both True
            if options.show_toc and options.use_toc_anchors:
                anchor = get_anchor_link(rel_path, options.toc_anchor_style)
            else:
                anchor = ""

            # Section heading
            if main_collapse:
                out_file.write(f'<details open>\n<summary style="font-size: 1.5em; font-weight: bold;">{i}. {display_path}</summary>\n\n')
                if anchor:
                    out_file.write(f'<a id="{anchor}"></a>\n\n')
            else:
                if anchor:
                    out_file.write(f"## {i}. {display_path} <a id=\"{anchor}\"></a>\n\n")
                else:
                    out_file.write(f"## {i}. {display_path}\n\n")

            # File info
            if options.show_file_info:
                def write_file_info():
                    if options.use_minimal_format:
                        if options.show_sizes:
                            out_file.write(f"Size: {format_size(finfo.size)}\n")
                        if options.show_timestamps:
                            out_file.write(f"Modified: {format_time(finfo.last_modified)}\n")
                        if options.show_line_count and finfo.line_count:
                            out_file.write(f"Lines: {finfo.line_count:,}\n")
                        if options.show_path_info and options.toc_format != 'full':
                            out_file.write(f"Path: {rel_path}\n")
                    else:
                        if options.show_sizes:
                            out_file.write(f"- **Size:** {format_size(finfo.size)}\n")
                        if options.show_timestamps:
                            out_file.write(f"- **Last Modified:** {format_time(finfo.last_modified)}\n")
                        if options.show_line_count and finfo.line_count:
                            out_file.write(f"- **Lines of Code:** {finfo.line_count:,}\n")
                        if options.show_path_info and options.toc_format != 'full':
                            out_file.write(f"- **Full Path:** {rel_path}\n")

                write_section(out_file, "File Information", write_file_info, options)

            # File contents
            def write_contents():
                extension = os.path.splitext(rel_path)[1].lower()
                language = get_language_for_extension(extension)
                chunks = chunked_file_reader(full_path, options.chunk_size)
                if not chunks:
                    out_file.write("```\n(No content or unreadable file)\n```\n")
                    return

                line_offset = 1
                for chunk_data in chunks:
                    out_file.write(f"```{language}\n")
                    if options.show_line_numbers:
                        lines_in_chunk = len(chunk_data.splitlines())
                        chunk_data = add_line_numbers(chunk_data, start_line=line_offset)
                        line_offset += lines_in_chunk
                    out_file.write(chunk_data)
                    out_file.write("\n```\n\n")

            write_section(out_file, "File Contents", write_contents, options)

            if main_collapse:
                out_file.write("</details>\n\n")

            if not options.use_minimal_format:
                out_file.write("---\n\n")

    print(f"{GREEN}Documentation generated successfully in {output_file}{RESET}")

#
# -----------------------------
#   Modern Interactive Wizard
# -----------------------------
#

def get_yes_no_input(prompt: str, default: bool = True) -> bool:
    default_str = "Y/n" if default else "y/N"
    response = input(f"{prompt} [{default_str}]: ").strip().lower()
    if not response:
        return default
    return response[0] == 'y'

def interactive_mode() -> DocumentationOptions:
    """Wizard for collecting user settings, with optional fast report at step 0."""
    print(f"{CYAN}╔════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║          {BOLD}📁 Project Documentation Wizard{RESET}{CYAN}            ║{RESET}")
    print(f"{CYAN}╚════════════════════════════════════════════════════╝{RESET}\n")

    # Step 0: Fast Report
    print(f"{BOLD}STEP 0:{RESET} {MAGENTA}Optional Fast Report{RESET}")
    do_fast_report = get_yes_no_input("  Would you like to see a fast project report first?")
    if do_fast_report:
        while True:
            project_dir_temp = input(f"  📂 Enter directory for fast report (or '.' for current): ").strip() or '.'
            if os.path.isdir(project_dir_temp):
                print_fast_report(project_dir_temp)
                break
            print(f"  {YELLOW}❌ Directory not found. Please try again.{RESET}")

        cont = get_yes_no_input("  Fast report generated. Continue to full wizard?", default=True)
        if not cont:
            print(f"{YELLOW}Exiting after fast report.{RESET}")
            sys.exit(0)
        print()

    # Step 1: Project Directory
    print(f"{BOLD}STEP 1:{RESET} {MAGENTA}Project Directory Setup{RESET}")
    while True:
        project_dir = input(f"  📂 Enter project directory (or '.' for current): ").strip() or '.'
        if os.path.isdir(project_dir):
            break
        print(f"  {YELLOW}❌ Directory not found. Please try again.{RESET}")
    print()

    # Analyze
    print(f"{MAGENTA}Analyzing project structure...{RESET}")
    analyzer = ProjectAnalyzer(project_dir)
    stats = analyzer.analyze_project()
    print(f"  Found file types in {GREEN}{project_dir}{RESET}:")
    for ext, count in sorted(stats.items()):
        if ext:
            print(f"    {ext}: {count} files")
    print()

    # Step 2: File Types
    print(f"{BOLD}STEP 2:{RESET} {MAGENTA}Choose File Types to Include{RESET}")
    print(f"  Enter a comma-separated list (e.g. 'swift,md') or 'all'")
    include = input("  Extensions > ").strip() or '*'
    print()

    # Step 3: Display Options
    print(f"{BOLD}STEP 3:{RESET} {MAGENTA}Display Options{RESET}")
    show_tree = get_yes_no_input("  Include project tree diagram?")
    show_toc = get_yes_no_input("  Include a table of contents?", default=True)
    if show_toc:
        print(f"\n  How should files be labeled in the TOC?")
        print("    1. Full paths (dir/subdir/file.ext)")
        print("    2. Filename with extension (file.ext)")
        print("    3. Just filename (file)")
        toc_choice = input("  Choice > ").strip()
        toc_format = {
            '1': 'full',
            '2': 'name_ext',
            '3': 'name'
        }.get(toc_choice, 'name_ext')

        use_toc_anchors = get_yes_no_input("  Include clickable links in TOC?", default=True)
        if use_toc_anchors:
            print(f"\n  How should TOC links be formatted?")
            print("    1. Simple (just filename)")
            print("    2. Full path-based anchors")
            anchor_choice = input("  Choice > ").strip()
            toc_anchor_style = 'simple' if anchor_choice == '1' else 'full_path'
        else:
            toc_anchor_style = 'simple'
    else:
        toc_format = 'name_ext'
        use_toc_anchors = False
        toc_anchor_style = 'simple'
    print()

    # Step 4: Summaries & Collapsible
    print(f"{BOLD}STEP 4:{RESET} {MAGENTA}Summaries & Collapsible Settings{RESET}")
    show_summary = get_yes_no_input("  Show project summary info?", default=True)
    use_collapsible = get_yes_no_input("  Use collapsible sections?", default=True)
    if use_collapsible:
        print(f"\n  Which sections should be collapsible?")
        print("    1. All sections (main & subsections)")
        print("    2. Only main sections")
        print("    3. Only subsections")
        c_choice = input("  Choice > ").strip()
        collapsible_level = {
            '1': 'all',
            '2': 'main',
            '3': 'subsections'
        }.get(c_choice, 'all')
    else:
        collapsible_level = 'none'
    use_minimal_format = get_yes_no_input("  Use minimal formatting?", default=False)
    print()

    # Step 5: Tree Detail
    print(f"{BOLD}STEP 5:{RESET} {MAGENTA}Tree Detail (if enabled){RESET}")
    if show_tree:
        print("  How should the tree be filtered?")
        print("    1. Same as included files")
        print("    2. All files")
        print("    3. Custom selection")
        tree_choice = input("  Choice > ").strip()
        show_all = (tree_choice == '2')
        if tree_choice == '1':
            show = include
        elif tree_choice == '3':
            show = input("  Enter extensions for tree > ").strip()
        else:
            show = None
    else:
        show_all = False
        show = include
    print()

    # Step 6: Detail Options
    print(f"{BOLD}STEP 6:{RESET} {MAGENTA}Detail Options{RESET}")
    show_file_info = get_yes_no_input("  Show file information sections?")
    if show_file_info:
        show_line_count = get_yes_no_input("  Include line counts?")
        show_file_stats = get_yes_no_input("  Include file type statistics?")
        show_timestamps = get_yes_no_input("  Show last modified timestamps?")
        show_sizes = get_yes_no_input("  Show file sizes?")
        show_path_info = get_yes_no_input("  Show file path information?", default=False)
    else:
        show_line_count = show_file_stats = show_timestamps = show_sizes = show_path_info = False

    show_line_numbers = get_yes_no_input("  Show line numbers in code blocks?", default=False)
    print()

    # Step 7: Advanced / Chunk size
    print(f"{BOLD}STEP 7:{RESET} {MAGENTA}Advanced (Chunk Size for Large Files){RESET}")
    print("  You can limit lines per code block for readability.")
    user_chunk = input("  Lines per chunk [default=200]: ").strip()
    if user_chunk.isdigit():
        chunk_size = int(user_chunk)
    else:
        chunk_size = 200
    print()

    # Step 8: Output Setup
    print(f"{BOLD}STEP 8:{RESET} {MAGENTA}Output Setup{RESET}")
    output_file = input("  Output file (default: project_code_documentation.md): ").strip() or "project_code_documentation.md"
    print()

    # Step 9: Offer to Show CLI Command
    print(f"{CYAN}────────── Additional Help ──────────{RESET}")
    want_cli = get_yes_no_input("Would you like to see a CLI command that replicates these settings?", default=False)

    # Build “equivalent CLI” string with `python3 docgen.py`
    base_cmd = f"python3 docgen.py \"{project_dir}\" -o \"{output_file}\""

    if include.lower() not in ['all', '*']:
        base_cmd += f" --include \"{include}\""
    if show_all:
        base_cmd += " --show-all"
    else:
        if show is not None and show != include:
            base_cmd += f" --show \"{show}\""
    if not show_summary:
        base_cmd += " --no-summary"
    if not show_tree:
        base_cmd += " --no-tree"
    if not show_file_info:
        base_cmd += " --no-file-info"
    if not show_line_count:
        base_cmd += " --no-line-count"
    if not show_file_stats:
        base_cmd += " --no-file-stats"
    if not show_timestamps:
        base_cmd += " --no-timestamps"
    if not show_sizes:
        base_cmd += " --no-sizes"
    if not show_toc:
        base_cmd += " --no-toc"
    if use_collapsible is False:
        base_cmd += " --no-collapsible"
    else:
        if collapsible_level != 'all':
            base_cmd += f" --collapsible-level {collapsible_level}"
    if use_minimal_format:
        base_cmd += " --minimal"
    if show_line_numbers:
        base_cmd += " --line-numbers"
    if show_path_info:
        base_cmd += " --path-info"
    if chunk_size != 200:
        base_cmd += f" --chunk-size {chunk_size}"

    if want_cli:
        print(f"\n{GREEN}Equivalent CLI command:{RESET}")
        print(f"  {base_cmd}\n")

    # Final Confirmation
    print(f"{CYAN}────────── Review & Confirm ──────────{RESET}")
    print(f"Directory: {GREEN}{project_dir}{RESET}")
    print(f"File Types: {GREEN}{include}{RESET}")
    print(f"Collapsible: {GREEN}{use_collapsible} ({collapsible_level}){RESET}")
    print(f"Minimal Format: {GREEN}{use_minimal_format}{RESET}")
    print(f"Line Numbers: {GREEN}{show_line_numbers}{RESET}")
    print(f"Chunk Size: {GREEN}{chunk_size}{RESET}")
    print(f"Output File: {GREEN}{output_file}{RESET}\n")

    proceed = get_yes_no_input("Proceed with these settings?", default=True)
    if not proceed:
        print(f"{YELLOW}Aborted by user.{RESET}")
        sys.exit(0)

    return DocumentationOptions(
        project_dir=project_dir,
        output_file=output_file,
        include_extensions=include,
        show_extensions=show,
        show_all=show_all,
        show_file_info=show_file_info,
        show_tree=show_tree,
        show_line_count=show_line_count,
        show_file_stats=show_file_stats,
        show_timestamps=show_timestamps,
        show_sizes=show_sizes,
        show_summary=show_summary,
        use_collapsible=use_collapsible,
        collapsible_level=collapsible_level,
        use_minimal_format=use_minimal_format,
        show_line_numbers=show_line_numbers,
        show_toc=show_toc,
        toc_format=toc_format,
        use_toc_anchors=use_toc_anchors,
        toc_anchor_style=toc_anchor_style,
        show_path_info=show_path_info,
        chunk_size=chunk_size
    )

#
# -----------------------------
#      Main CLI
# -----------------------------
#

def main():
    # Custom help formatter for better-looking help output
    class ColoredHelpFormatter(argparse.HelpFormatter):
        def __init__(self, prog, indent_increment=2, max_help_position=30, width=None):
            super().__init__(prog, indent_increment, max_help_position, width)

        def _format_action(self, action):
            # Colorize and format the help text
            help_text = super()._format_action(action)
            if action.option_strings:
                # Colorize options
                for opt in action.option_strings:
                    help_text = help_text.replace(opt, f"{CYAN}{opt}{RESET}")
            # Colorize choices if they exist
            if action.choices:
                choices_str = "{" + ",".join(action.choices) + "}"
                help_text = help_text.replace(choices_str, f"{YELLOW}{choices_str}{RESET}")
            return help_text

        def _format_usage(self, usage, actions, groups, prefix):
            return f"\n{BOLD}Usage:{RESET}\n  {super()._format_usage(usage, actions, groups, prefix)}\n"

    parser = argparse.ArgumentParser(
        description=f"{BOLD}📚 Generate beautiful markdown documentation from source files{RESET}",
        formatter_class=ColoredHelpFormatter,
        epilog=f"""
{BOLD}╭─ Examples ────────────────────────────────────────────────╮{RESET}
│                                                            │
│  {GREEN}# Interactive mode (recommended){RESET}                      │
│  {CYAN}py-code-docgen -i{RESET}                                     │
│                                                            │
│  {GREEN}# Quick project report{RESET}                               │
│  {CYAN}py-code-docgen --fast-report{RESET}                         │
│                                                            │
│  {GREEN}# Document Python files with minimal format{RESET}          │
│  {CYAN}py-code-docgen --include py --no-toc --minimal{RESET}       │
│                                                            │
│  {GREEN}# Full paths in TOC, main sections collapsible{RESET}      │
│  {CYAN}py-code-docgen --toc-format full --collapsible-level main{RESET} │
│                                                            │
╰────────────────────────────────────────────────────────────╯
"""
    )

    # Main options group
    main_group = parser.add_argument_group(f'{BOLD}Main Options{RESET}')
    main_group.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive wizard mode.')
    main_group.add_argument('--fast-report', action='store_true',
                        help='Generate a quick project report and exit.')
    main_group.add_argument('project_dir', nargs='?', default='.',
                        help='Directory containing the project (default: current).')
    main_group.add_argument('-o', '--output', default='project_code_documentation.md',
                        help='Output file name.')

    # Content options group
    content_group = parser.add_argument_group(f'{BOLD}Content Options{RESET}')
    content_group.add_argument('--include', default='*',
                        help='Extensions to include (e.g., "py,js,swift" or "*" for all)')
    content_group.add_argument('--show', default=None,
                        help='Extensions to show in tree view')
    content_group.add_argument('--show-all', action='store_true',
                        help='Show all files in tree, ignore extension filters')

    # Format options group
    format_group = parser.add_argument_group(f'{BOLD}Format Options{RESET}')
    format_group.add_argument('--no-collapsible', action='store_true',
                        help='Disable collapsible sections')
    format_group.add_argument('--collapsible-level', 
                        choices=['all', 'main', 'subsections', 'none'],
                        default='all',
                        help='Which sections to make collapsible')
    format_group.add_argument('--minimal', action='store_true',
                        help='Use minimal formatting')
    format_group.add_argument('--line-numbers', action='store_true',
                        help='Show line numbers in code blocks')

    # Display options group
    display_group = parser.add_argument_group(f'{BOLD}Display Options{RESET}')
    display_group.add_argument('--no-summary', action='store_true',
                        help='Hide project summary')
    display_group.add_argument('--no-tree', action='store_true',
                        help='Hide project tree')
    display_group.add_argument('--no-file-info', action='store_true',
                        help='Hide file information sections')
    display_group.add_argument('--no-line-count', action='store_true',
                        help='Hide line count info')
    display_group.add_argument('--no-file-stats', action='store_true',
                        help='Hide file type stats')
    display_group.add_argument('--no-timestamps', action='store_true',
                        help='Hide last modified timestamps')
    display_group.add_argument('--no-sizes', action='store_true',
                        help='Hide file size info')

    # TOC options group
    toc_group = parser.add_argument_group(f'{BOLD}Table of Contents Options{RESET}')
    toc_group.add_argument('--no-toc', action='store_true',
                        help='Hide table of contents')
    toc_group.add_argument('--toc-format', 
                        choices=['full', 'name_ext', 'name'],
                        default='name_ext',
                        help='How files are shown in TOC')
    toc_group.add_argument('--no-toc-anchors', action='store_true',
                        help='Disable clickable links in TOC')
    toc_group.add_argument('--toc-anchor-style',
                        choices=['simple', 'full_path'],
                        default='simple',
                        help='Style for anchor links in TOC')

    # Advanced options group
    advanced_group = parser.add_argument_group(f'{BOLD}Advanced Options{RESET}')
    advanced_group.add_argument('--path-info', action='store_true',
                        help='Show file path info in file info section')
    advanced_group.add_argument('--chunk-size', type=int, default=200,
                        help='Lines per code block chunk (default: 200)')

    args = parser.parse_args()

    try:
        # If user just wants a fast report, do so and exit
        if args.fast_report:
            print_fast_report(args.project_dir)
            sys.exit(0)

        if args.interactive:
            # Wizard mode
            options = interactive_mode()
            include_exts = parse_extensions(options.include_extensions)
            show_exts = None if options.show_all else (
                parse_extensions(options.show_extensions) if options.show_extensions else include_exts
            )
        else:
            # Non-interactive
            use_collapse = not args.no_collapsible
            collapsible_level = args.collapsible_level if use_collapse else 'none'

            options = DocumentationOptions(
                project_dir=args.project_dir,
                output_file=args.output,
                include_extensions=args.include,
                show_extensions=args.show,
                show_all=args.show_all,
                show_file_info=not args.no_file_info,
                show_tree=not args.no_tree,
                show_line_count=not args.no_line_count,
                show_file_stats=not args.no_file_stats,
                show_timestamps=not args.no_timestamps,
                show_sizes=not args.no_sizes,
                show_summary=not args.no_summary,
                use_collapsible=use_collapse,
                collapsible_level=collapsible_level,
                use_minimal_format=args.minimal,
                show_line_numbers=args.line_numbers,
                show_toc=not args.no_toc,
                toc_format=args.toc_format,
                use_toc_anchors=not args.no_toc_anchors,
                toc_anchor_style=args.toc_anchor_style,
                show_path_info=args.path_info,
                chunk_size=args.chunk_size
            )

            include_exts = parse_extensions(options.include_extensions)
            show_exts = None if args.show_all else (
                parse_extensions(options.show_extensions) if options.show_extensions else include_exts
            )

        create_markdown(
            options.project_dir,
            options.output_file,
            include_exts,
            show_exts,
            options
        )
    except Exception as exc:
        print(f"{YELLOW}Error:{RESET} {str(exc)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
