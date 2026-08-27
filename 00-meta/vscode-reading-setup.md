# VS Code Reading Setup

## Recommended layout

1. Open the repository folder in VS Code.
2. Open `CURRENT-FOCUS.md`.
3. Press `Command+Shift+V` for rendered Markdown, or use **Open Preview to the Side**.
4. Keep Explorer on the left and Outline on the right.
5. Open PDFs in a second editor group when a module references them.

The workspace recommends Markdown, Mermaid, YAML, spelling, linting, and PDF extensions. Install only the extensions you use; the repository remains readable without them.

## Searchable local website

From the repository terminal, run:

```bash
python3 scripts/docs.py serve
```

Then open `http://127.0.0.1:8000`. The command keeps the GitHub-friendly repository layout intact, rebuilds pages when files change, and removes its temporary build directory when stopped with `Control+C`.

To verify a production build without leaving generated files in the repository:

```bash
python3 scripts/docs.py build --strict
```

## Navigation conventions

- `README.md` is the entry page for a folder.
- Pathways are ordered playlists.
- Knowledge pages are canonical and should not be duplicated.
- Relative links work locally and on GitHub.
- `Command+P` finds a page by filename.
- `Command+Shift+F` searches the complete library.
