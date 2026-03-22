# CLAUDE.md

## What This Is

Census dashboard of open-source projects built with Claude Opus 4.6 on GitHub. Single self-contained HTML page deployed via GitHub Pages.

**Live:** https://jphein.github.io/opus/

## Architecture

Everything lives in `index.html` — one file, zero dependencies, no build step.

- **HTML**: 10 sections (flagship projects, charts, developers, hackathon, top repos, notable projects, production use, case study, methodology, full library)
- **CSS**: Inline `<style>` block. Dark editorial theme. Color tokens: `--accent-cyan`, `--accent-orange`, `--accent-violet`, `--accent-green`, `--accent-rose`, `--accent-gold`. Fonts: JetBrains Mono (body) + Instrument Serif (headings)
- **JS**: Inline `<script>` block. All data in `libraryData` array (245 entries). Charts built with `createElement` + inline SVG. Scroll-reveal via IntersectionObserver. All aggregate stats computed dynamically from `libraryData`

## Data

The `libraryData` array near the bottom of `index.html` is the single source of truth. Each entry has: `name`, `owner`, `stars`, `lang`, `desc`, `created`, `signal`, `url`, `category`.

Other embedded data arrays: `weeklyData`, `devTypeData`, `accountAgeData`, `dormantDevs`, `flagshipProjects`, `notableProjects`, `hackathonWinners`.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The entire dashboard — edit this for any content/data/style changes |
| `analyze_veterans.py` | One-off Python script that classified GitHub users by account age + activity |
| `all-ways-to-access-opus-4.6.md` | Reference doc: 40 access methods for Opus 4.6 |
| `*.png` | Screenshots for README / documentation |

## Deployment

GitHub Pages from `main` branch. Push to `main` and the site updates automatically.

```bash
git add index.html
git commit -m "feat: add new repos to census"
git push origin main
```

## Design Conventions

- Dark background (`#0a0a0c`), surface cards (`#111114`, `#18181c`)
- Monospace for data, serif for headings — editorial data-journalism aesthetic
- Scroll-reveal animations: elements get `.revealed` class via IntersectionObserver
- Stat cards use colored number + uppercase label pattern
- Chart bars/segments use the 6 accent colors
- Responsive: grid layouts collapse on mobile via `@media` queries

## Research Methodology

Five detection signals were used to find Opus 4.6 projects on GitHub:
1. **explicit** — Repo name/description/README mentions Opus 4.6
2. **commit** — `Co-Authored-By: Claude` in commit signatures
3. **config** — CLAUDE.md, `.claude/settings.json`, or action.yml references
4. **under** — Model catalogs, SDK configs, or CI workflows include `claude-opus-4-6`
5. **hackathon** — Built at the Cerebral Valley x Anthropic hackathon (Feb 2026)

GitHub Search API, `gh` CLI, Playwright (for Devpost scraping), and manual profile analysis were all used during research.
