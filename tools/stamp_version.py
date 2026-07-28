#!/usr/bin/env python3
"""Regenerate `version.json` — the realm-sigil version surface for this page.

WHY THIS EXISTS
`version.json` was hand-added in fdc9ee7 (2026-04-05) and nothing has regenerated it since.
It has stayed *accurate* only because `index.html` has not changed since — luck, not design.
`https://jphein.github.io/opus/version.json` is a registered check on status.realm.watch, so
the moment the page does change, monitoring would report a version that is not deployed. A
monitored surface that cannot fail is worse than an unmonitored one: it manufactures the
appearance of verification.

WHY THE FILE STAYS COMMITTED (and is NOT gitignored like smol's)
This repo's Pages deployment is `build_type: legacy` — GitHub serves files straight from the
`main` branch, with no Actions artifact step. CI therefore cannot inject a file into the
deploy. smol's site gitignores its version.json because it publishes via
`upload-pages-artifact`; doing that here would simply 404 the monitored endpoint. Same goal,
different mechanism, because the deployment mechanism is different.

WHY `hash` IS index.html's LAST COMMIT, NOT HEAD
A committed file cannot name the commit that contains it — stamping HEAD is impossible, which
is exactly why the original recorded its own PARENT (fc24f95) and looked two commits behind
forever. So this records the last commit that touched the deployed page instead. That is:

  · honest      — it answers the question a reader actually has, "which version of this page
                  am I looking at", and `index.html` IS the page (see CLAUDE.md: everything
                  lives in one file);
  · idempotent  — committing version.json does not touch index.html, so re-running this
                  produces byte-identical output and can never trigger a stamp loop;
  · CHECKABLE   — `built` is that commit's own committer date, not "now", so the whole file is
                  a pure function of git history. CI can re-derive it and compare. Nothing
                  here depends on when the script happened to run.

That last property is the point. A hand-maintained file rots silently; a reproducible one
fails a check the moment it drifts.

NO VENDORED CORPUS — DELIBERATELY
The word list is taken from canonical realm-sigil and nowhere else. Copying the corpus in here
is what put six projects on a three-months-frozen vocabulary (see the 2026-07-28 audit): a
broken install path does not stop consumption, it silently converts dependencies into copies.
If canonical cannot be reached this script REFUSES to write, rather than inventing a name or
freezing a fourth copy. The existing file is left untouched and the exit code is non-zero, so
the failure is loud and the endpoint keeps serving what it already had.

Realm is `stellar`, preserved from the original stamp. Note the canonical python binding is
itself frozen at the 2026-04-05 corpus, so this reproduces "Radiant Dwarf" rather than the
"Twinkling Comet" the newer `words/realms.json` would give. That continuity is intentional —
renaming this page's build history is not a side effect this script gets to cause.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "version.json"
PAGE = "index.html"
REALM = "stellar"
NAME = "opus"
DESCRIPTION = "Claude Opus 4.6 info page"
REPO_URL = "https://github.com/jphein/opus"

# Canonical realm-sigil, in preference order. Installed package first; the local checkout is
# the fallback for a workstation that has not installed it. Never a copy inside this repo.
SIGIL_CHECKOUT = Path.home() / "Projects" / "sigil.realm.watch" / "python"


def git(*args: str) -> str:
    try:
        return subprocess.check_output(("git", *args), cwd=REPO, text=True,
                                       stderr=subprocess.DEVNULL).strip()
    except Exception:
        return ""


def load_generate_name():
    """Return canonical generate_name, or None. Never falls back to a local corpus."""
    try:
        from realm_sigil import generate_name          # installed package
        return generate_name
    except ImportError:
        pass
    if (SIGIL_CHECKOUT / "realm_sigil").is_dir():
        sys.path.insert(0, str(SIGIL_CHECKOUT))
        try:
            from realm_sigil import generate_name      # local canonical checkout
            return generate_name
        except ImportError:
            return None
    return None


def main() -> int:
    # The last commit that changed the deployed page — stable under our own commits.
    sha = git("log", "-1", "--format=%h", "--", PAGE)
    built = git("log", "-1", "--format=%cd", "--date=format-local:%Y-%m-%dT%H:%M:%SZ",
                "--", PAGE)
    if not sha or not built:
        print(f"ERROR: cannot read git history for {PAGE}; refusing to write.", file=sys.stderr)
        return 1

    generate_name = load_generate_name()
    if generate_name is None:
        print("ERROR: canonical realm-sigil is not available (not installed, and no checkout "
              f"at {SIGIL_CHECKOUT}).\n"
              "       Refusing to write: this script will not vendor a corpus or invent a "
              "name.\n"
              "       Install it with:  pip install "
              "'git+https://github.com/jphein/sigil.realm.watch.git#subdirectory=python'",
              file=sys.stderr)
        return 1

    payload = {
        "name": NAME,
        "description": DESCRIPTION,
        "version": generate_name(sha, REALM),
        "hash": sha,
        "branch": git("rev-parse", "--abbrev-ref", "HEAD") or "main",
        "dirty": False,          # derived from committed history, so never a dirty snapshot
        "built": built,
        "realm": REALM,
        "repo": REPO_URL,
        "commit_url": f"{REPO_URL}/commit/{sha}",
    }

    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"stamped version.json: {payload['version']}  (page last changed {sha} @ {built})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
