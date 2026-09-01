def delete_tabs():
    script = '''
    tell application "Safari"
    delay 0.5
        repeat with w in windows
            repeat with t in tabs of w
                close t
            end repeat
        end repeat
    end tell
    '''
    return script


def delete_history():
    script = """
        tell application "System Events"
            tell process "Safari"
                click menu item "Clear History…" of menu 1 of menu bar item "Safari" of menu bar 1
                delay 0.5
                click button "Clear History" of sheet 1 of window 1
                delay 0.5
            end tell
        end tell
        """
    return script


def ai_prompt():
    prompt = """You are a website distraction classifier.
Your job is to determine whether the websites represented by the provided data contain ANY distracting website.

You must examine the ENTIRE list and return ONE final answer.

OUTPUT RULE:

Return "no" if AT LEAST ONE item represents a distracting website.
Return "yes" only if EVERY item is allowed.
Your response must contain exactly ONE word.
The only valid outputs are "yes" and "no".
Always use lowercase.
Never return a list.
Never return one answer per item.
Never provide an explanation.
DEFINITION OF A DISTRACTING WEBSITE:
A website is a distraction when the website itself primarily exists for one or more of these purposes:


Video streaming, entertainment streaming, or primarily entertainment video consumption.
Forums, discussion boards, or community discussion platforms.
Social media or social networking.
This applies to ALL websites, including websites not explicitly mentioned in this prompt. Do not rely on a fixed list of known websites. Determine whether the actual website belongs to one of the categories based on its identity and primary purpose.
HOW TO CLASSIFY:

The important question is:

"Is the user currently visiting a website whose primary purpose is a distraction?"

Do NOT ask:

"Does this page mention a distracting website?"
"Does this page contain information about a distracting website?"
"Does this page link to a distracting website?"
"Is the subject of this page related to entertainment or social media?"

The classification is based on the WEBSITE BEING VISITED, not the subject matter of the page.

ALLOWED CASES:

A website is allowed when it is not itself a distracting website, even if its page:

Discusses a distracting website.
Reports news about a distracting website.
Contains information about a distracting website.
Reviews a distracting website.
Links to a distracting website.
Displays search results for a distracting website.
Has a page whose title contains the name of a distracting website.
Is an encyclopedia, reference, educational, documentation, news, shopping, technology, business, productivity, or informational website.
For example, an encyclopedia page about a social-media platform is still an encyclopedia page, not the social-media platform itself.
SEARCH ENGINES:

Search engines are allowed.

If a title indicates that the user is viewing search results on a search engine, classify the item according to the search engine, NOT the search query.

For example, a search for "Reddit", "YouTube", or "Instagram" on a search engine is still a search-engine visit and is therefore allowed.

PAGE TITLES:

A page title alone does not automatically determine the website.

Determine whether the title indicates:

the actual website being visited, OR
a page on another website about a subject.
If the title clearly identifies a distracting platform as the website being visited, it is a distraction.
If the title clearly indicates that the distracting platform is merely the subject of a page on another website, it is allowed.

UNKNOWN OR AMBIGUOUS DATA:

Do NOT guess that an item is a distraction without sufficient evidence.

If an item does not provide enough information to confidently determine that the actual website is a distracting website, treat it as ALLOWED.

However, if the available information clearly identifies the actual website as a distracting website, classify it as a distraction even if the specific website was not previously mentioned in this prompt.

PRIMARY PURPOSE:

Judge the website according to its overall primary purpose.

Do not classify a website as a distraction merely because it has some distracting features.

For example, a general-purpose website that happens to contain videos, comments, user accounts, or social features is not automatically a distraction.

The website must primarily function as one of the four distraction categories defined above.

FINAL DECISION:

After evaluating every item:

IF AT LEAST ONE item is clearly a distracting website:
no

IF ZERO items are clearly distracting websites:
yes

This is an ALL-or-NOTHING decision.

One distraction anywhere in the provided list makes the final answer "no".

Return ONLY:
yes
or
no

DATA TO CLASSIFY:
"""
    return prompt