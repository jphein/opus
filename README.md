# Claude Opus 4.6 on GitHub

A comprehensive census of open-source projects built with, powered by, or integrating Claude Opus 4.6 since its release on February 5, 2026.

**Live site:** [jphein.github.io/opus](https://jphein.github.io/opus/)

## The Numbers

- **245** public repositories tracked
- **1.4M** combined stars
- **24** programming languages
- **218** unique developers
- **500** hackathon builders (Cerebral Valley x Anthropic, Feb 2026)
- **321** Devpost projects across 14 regional hackathons

## What's Inside

The report is a single self-contained HTML file (`index.html`) with:

1. **Flagship Projects** — From Anthropic's own Claude Code (80K stars) to community tools
2. **The Numbers** — Animated charts: repos per week, language distribution, star tiers, categories
3. **Who's Building** — Developer profiles, "re-energized veterans" (dormant accounts awakened by Opus 4.6)
4. **The Hackathon** — Winners from the "Built with Opus 4.6" hackathon (13K applicants, 500 selected) + 14 regional Devpost events
5. **Top Repos** — The 15 highest-starred projects with donut chart
6. **Notable Projects** — Curated picks across categories
7. **The Bigger Picture** — Opus 4.6 in GitHub Copilot, production integrations
8. **Case Study** — @jphein, a 10-year dormant developer re-energized by Opus 4.6
9. **Detection Methodology** — How we found them: 5 signal types across GitHub's APIs
10. **Full Library** — Searchable, sortable, filterable table of all 245 repos

## Detection Signals

Projects were found through five methods:

| Signal | Method |
|--------|--------|
| `explicit` | Repo name, description, or README mentions Opus 4.6 |
| `commit` | `Co-Authored-By: Claude` in commit signatures |
| `config` | CLAUDE.md, `.claude/settings.json`, or action.yml references |
| `under` | Model catalogs, SDK configs, or CI workflows include `claude-opus-4-6` |
| `hackathon` | Built at the Cerebral Valley x Anthropic hackathon (Feb 2026) |

## Tech

- Zero dependencies — pure HTML/CSS/JS in a single file
- All charts rendered via DOM (`createElement`) and inline SVG
- Data computed dynamically from a single `libraryData` array
- Scroll-reveal animations via `IntersectionObserver`
- Dark editorial theme: JetBrains Mono + Instrument Serif

## Built With

This entire project — the research, the dashboard, and this README — was built using Claude Opus 4.6 via Claude Code.
