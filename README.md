# QualiZeal Interview Prep

A topic-wise interview study guide for the QualiZeal intern drive, published as a simple website.

- **Website:** `index.html` (open it in a browser, or host it with GitHub Pages)
- **Content:** `QualiZeal_Interview_Study_Guide.md`

## Publish on GitHub Pages
1. Create a new public repository on GitHub (for example `qualizeal-prep`).
2. Upload `index.html` (the other files are optional) to the repository root.
3. Go to **Settings → Pages**, set **Source** to *Deploy from a branch*, choose branch **main** and folder **/ (root)**, then click **Save**.
4. After a minute or two, the site is live at `https://<your-username>.github.io/qualizeal-prep/`.

## Editing the content
Edit `QualiZeal_Interview_Study_Guide.md`, then run:

```bash
python3 build.py
```

This rebuilds `index.html` from `site_template.html` + the markdown. Upload the new `index.html` again.

## Features
- One topic per page, with Previous / Next buttons (or the ← → arrow keys)
- Sidebar with all topics, plus search across every topic (press `/` to focus it)
- Sub-topic shortcuts at the top of each topic
- **Self-test** mode: hides answers until you click a question
- Mark topics as completed, with a progress bar (saved in your browser)
- Light / dark theme, copy buttons on code, works on mobile
