from datetime import datetime, timezone

now = datetime(2026, 3, 19, tzinfo=timezone.utc)

users = [
    # From your specific list
    {"login": "dr3d", "created": "2009-08-19", "repos": 5, "bio": "MIT OG | Media Lab. Started with asm & fortran, now markdown. Fascinated by artificial creativity.", "name": "Scott Evernden", "opus_repos": "SomaFM-for-CardPuter", "source": "list"},
    {"login": "dorman", "created": "2009-11-09", "repos": 27, "bio": "Cyber Threat Intelligence, Agentic Offensive Security. Creator of ThreatLegionCLI", "name": "Eric Dorman", "opus_repos": "threatlegionCLI", "source": "list"},
    {"login": "indexzero", "created": "2008-04-03", "repos": 175, "bio": "Early node person; herder of mammals. You probably npm install a module I created.", "name": "Charlie Robbins", "opus_repos": "vlurp", "source": "list"},
    {"login": "eltmon", "created": "2011-03-19", "repos": 130, "bio": None, "name": "Eltmon", "opus_repos": "panopticon-cli", "source": "list"},
    {"login": "davekiss", "created": "2011-12-11", "repos": 81, "bio": "Making stuff for the internet and sharing what I learn along the way.", "name": "Dave Kiss", "opus_repos": "homedaysband.com", "source": "list"},
    {"login": "wealth", "created": "2011-04-17", "repos": 18, "bio": None, "name": None, "opus_repos": "crystalclaw", "source": "list"},
    {"login": "lunard", "created": "2014-07-21", "repos": 17, "bio": "I like very much every technology, that I use with passion.", "name": "Luca Nardelli", "opus_repos": "startup-eu-scout", "source": "list"},
    {"login": "futureCreator", "created": "2016-02-14", "repos": 15, "bio": "Kubestronaut", "name": "Eric Han", "opus_repos": "v-terminal", "source": "list"},
    {"login": "Matt-Dionis", "created": "2016-03-16", "repos": 47, "bio": "Software Engineer. Web3, AI/ML enthusiast. Mentor, family man, rock climber & weather geek.", "name": "Matt Dionis", "opus_repos": "claude-drexler", "source": "list"},
    {"login": "jphein", "created": "2016-05-11", "repos": 41, "bio": "Just plain helpful.", "name": "Jeffrey Hein", "opus_repos": "(reference user)", "source": "reference"},
    {"login": "adamswbrown", "created": "2017-06-08", "repos": 23, "bio": "Principal Consultant @ Altra", "name": None, "opus_repos": "ukfoodfacts", "source": "list"},
    {"login": "njlevy", "created": "2017-01-02", "repos": 9, "bio": None, "name": None, "opus_repos": "anytype-export", "source": "list"},
    {"login": "gorduan", "created": "2018-01-08", "repos": 5, "bio": None, "name": None, "opus_repos": "paragraf", "source": "list"},
    {"login": "jinchiwei", "created": "2018-03-02", "repos": 12, "bio": None, "name": "Jinchi Wei", "opus_repos": "aria_causal-inference", "source": "list"},
    {"login": "ComeOnOliver", "created": "2018-09-12", "repos": 42, "bio": "AI & Blockchain Engineer", "name": "Haoran Shu", "opus_repos": "skillshub", "source": "list"},
    {"login": "arjdroid", "created": "2019-11-11", "repos": 23, "bio": "Computer Science and Philosophy Undergraduate at UCSD", "name": "Arjun Singh", "opus_repos": "artiist", "source": "list"},
    {"login": "liquidsnakeblue", "created": "2020-05-10", "repos": 11, "bio": None, "name": None, "opus_repos": "Zork-Opus", "source": "list"},
    {"login": "taka-avantgarde", "created": "2020-01-20", "repos": 1, "bio": "Founder and CEO", "name": "Takayuki Miyano", "opus_repos": "Due-diligence-engine", "source": "list"},
    {"login": "urusamir", "created": "2023-03-04", "repos": 4, "bio": None, "name": None, "opus_repos": "hormozibot", "source": "list"},
    {"login": "aniiiiXD", "created": "2023-08-30", "repos": 37, "bio": None, "name": "Aniruddh Sharma", "opus_repos": "Clove", "source": "list"},
    {"login": "bersu77", "created": "2023-11-25", "repos": 26, "bio": None, "name": None, "opus_repos": "lead-manager", "source": "list"},
    {"login": "EmmaLeonhart", "created": "2024-12-29", "repos": 32, "bio": "My name is Emma and my passion is neuro-symbolic ai.", "name": "Emma Leonhart", "opus_repos": "SutraDB", "source": "list"},
    {"login": "Elliot-Tram", "created": "2024-11-11", "repos": 6, "bio": None, "name": None, "opus_repos": "saas-pro", "source": "list"},
    {"login": "chrbailey", "created": "2025-01-29", "repos": 24, "bio": "Founder ERP Access, Inc.", "name": "Christopher Bailey", "opus_repos": "MyPersona", "source": "list"},
    {"login": "mark366pl", "created": "2025-08-11", "repos": 1, "bio": None, "name": None, "opus_repos": "asana-clone", "source": "list"},
    {"login": "amakki-a11y", "created": "2025-12-05", "repos": 6, "bio": None, "name": "MAK", "opus_repos": "trader-intelligence-platform", "source": "list"},
    {"login": "aureliusawake-claude", "created": "2026-02-21", "repos": 1, "bio": None, "name": None, "opus_repos": "corvus-thought-archive", "source": "list"},
    {"login": "donglin-ai", "created": "2026-02-26", "repos": 1, "bio": None, "name": "Dong Lin", "opus_repos": "scratchpad", "source": "list"},
    {"login": "Ozzy-hub", "created": "2026-03-07", "repos": 1, "bio": None, "name": None, "opus_repos": "outbreak-shooter", "source": "list"},

    # From commit search (interesting finds)
    {"login": "knan", "created": "2009-02-16", "repos": 3, "bio": None, "name": "Erik Inge Bolso", "opus_repos": "ensure (via knanamsbusiness-star)", "source": "search"},
    {"login": "seanahrens", "created": "2009-07-29", "repos": 25, "bio": None, "name": "Sean Ahrens", "opus_repos": "unarxiv", "source": "search"},
    {"login": "anthonyterrell", "created": "2010-11-18", "repos": 12, "bio": "Chicago based programmer with over a decade of experience.", "name": "Ant", "opus_repos": "hookline", "source": "search"},
    {"login": "stevehansen", "created": "2012-08-13", "repos": 28, "bio": None, "name": "Steve Hansen", "opus_repos": "TerminalHost", "source": "search"},
    {"login": "marchiesa", "created": "2013-08-16", "repos": 7, "bio": None, "name": None, "opus_repos": "proof-lifting", "source": "search"},
    {"login": "rsonnad", "created": "2013-08-09", "repos": 4, "bio": "I do wingsie", "name": "Rahul", "opus_repos": "alpacapps", "source": "search"},
    {"login": "knazark", "created": "2014-03-02", "repos": 1, "bio": None, "name": None, "opus_repos": "happy-farming", "source": "search"},
    {"login": "Ricardo-Marques", "created": "2014-11-23", "repos": 22, "bio": None, "name": 'Ricardo "Meida" Marques', "opus_repos": "betaflight-tuning-helper", "source": "search"},
    {"login": "figrita", "created": "2015-02-22", "repos": 9, "bio": None, "name": None, "opus_repos": "silvia", "source": "search"},
    {"login": "jshin42", "created": "2015-12-10", "repos": 4, "bio": None, "name": "jjfisherbooks", "opus_repos": "vitalityweeks-site", "source": "search"},
    {"login": "Wiesenwischer", "created": "2015-02-12", "repos": 29, "bio": "Software-Architect and MMORPG nerd from lower saxony who loves mountain climbing", "name": "Marcus Dammann", "opus_repos": "rsgo-ams-project-rc", "source": "search"},
    {"login": "timvanhelsdingen", "created": "2017-10-23", "repos": 3, "bio": None, "name": "Tim van Helsdingen", "opus_repos": "arkestrator", "source": "search"},
    {"login": "deepai-org", "created": "2017-06-01", "repos": 14, "bio": "AI image/video recognition", "name": "DeepAI", "opus_repos": "growing-code, dementia", "source": "search"},
    {"login": "FilipRut", "created": "2020-09-26", "repos": 1, "bio": None, "name": "Filip Rut", "opus_repos": "portfolio", "source": "search"},
    {"login": "Hollings", "created": "2013-03-07", "repos": 55, "bio": None, "name": "John Hollingsworth", "opus_repos": "wendy", "source": "search"},
    {"login": "concaption", "created": "2018-09-05", "repos": 96, "bio": "wannabe polymath; selling my art", "name": "Usama Navid", "opus_repos": "form-filler", "source": "search"},
    {"login": "ryanpate", "created": "2020-02-24", "repos": 11, "bio": None, "name": None, "opus_repos": "CHAgent", "source": "search"},
    {"login": "omnomdombomb", "created": "2020-07-23", "repos": 3, "bio": None, "name": None, "opus_repos": "cmu-scholars-metadata-harvester", "source": "search"},
    {"login": "hongsoohyuk", "created": "2020-04-06", "repos": 9, "bio": None, "name": "hongsoohyuk", "opus_repos": "hongsoohyuk", "source": "search"},
    {"login": "Scottcjn", "created": "2022-12-23", "repos": 128, "bio": "IT Specialist | Vintage Computing Enthusiast | Blockchain Consultant | AI Researcher", "name": "AutoJanitor", "opus_repos": "Rustchain", "source": "search"},
    {"login": "jhol", "created": "2012-02-18", "repos": 99, "bio": None, "name": None, "opus_repos": "wendy (contributor)", "source": "search"},
]

# Sort by created date (oldest first)
users.sort(key=lambda u: u["created"])

# Calculate age and classify
print(f"{'Username':<28} {'Created':<12} {'Age(yr)':<8} {'Repos':<6} {'R/yr':<6} {'Pattern':<24} {'Opus Repo(s)':<36} Bio/Name")
print("=" * 200)

veterans = []
for u in users:
    created = datetime.strptime(u["created"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    age_days = (now - created).days
    age_years = age_days / 365.25
    repos_per_year = u["repos"] / age_years if age_years > 0 else 999

    if age_years >= 10:
        if u["repos"] < 30:
            pattern = "*** VETERAN DORMANT ***"
        else:
            pattern = "veteran-active"
    elif age_years >= 3:
        if u["repos"] < 30:
            pattern = "** RE-ENERGIZED **"
        else:
            pattern = "veteran-moderate"
    elif age_years >= 1:
        pattern = "newer account"
    else:
        pattern = "brand new"

    bio_str = ""
    if u.get("name"):
        bio_str = u["name"]
    if u.get("bio"):
        bio_str += (" | " if bio_str else "") + u["bio"][:60]

    marker = ""
    if "VETERAN DORMANT" in pattern or "RE-ENERGIZED" in pattern:
        marker = " <<<"
        veterans.append({**u, "age_years": age_years, "repos_per_year": repos_per_year, "pattern": pattern})

    print(f"{u['login']:<28} {u['created']:<12} {age_years:>5.1f}   {u['repos']:>4}   {repos_per_year:>5.1f} {pattern:<24} {u['opus_repos']:<36} {bio_str[:70]}{marker}")

print("\n\n")
print("=" * 120)
print("MOST DRAMATIC 'RE-ENERGIZED VETERAN' CASES (sorted by account age, most dramatic first)")
print("=" * 120)
veterans.sort(key=lambda v: (-v["age_years"], v["repos"]))
for i, v in enumerate(veterans, 1):
    bio_str = ""
    if v.get("name"):
        bio_str = v["name"]
    if v.get("bio"):
        bio_str += (" | " if bio_str else "") + v["bio"][:80]
    print(f"\n{i}. @{v['login']}")
    print(f"   Account created: {v['created']} ({v['age_years']:.1f} years old)")
    print(f"   Public repos: {v['repos']} ({v['repos_per_year']:.1f} repos/year)")
    print(f"   Opus 4.6 repo: {v['opus_repos']}")
    if bio_str:
        print(f"   Identity: {bio_str}")
    print(f"   Pattern: {v['pattern']}")
