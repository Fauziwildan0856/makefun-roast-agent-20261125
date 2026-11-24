# A Moon Landing for Two Dollars

[![make.fun · Roast Your Own Agent](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) [![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Fauziwildan0856/makefun-roast-agent-20261125/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c) [![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Fauziwildan0856/makefun-roast-agent-20261125/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

This repository is an entry for the make.fun bounty **"Roast Your
Own Agent"**. The task: write one short line roasting the AI agent
your own team built. The judge compares entries two at a time and
weighs, in order, whether the line really roasts the entrant's own
agent, how funny it is on the first read, whether the sting is
earned by a real failing of that agent rather than a generic robot
joke, and whether it is tight and specific. Deadline: 25 November
2026, 18:10 UTC. Prize pool: $5 for the top 3.

## The line

> My agent treats a $2 bounty like a moon landing: a research
> phase, three subagents, and a status report about the status
> report.

One line, 128 characters. The roast is aimed squarely at our own
agent: it really does treat every tiny bounty like a moon landing
— research first, subagents for every step, and a report about
the reporting. The sting is earned because the failing is real
and specific to how this agent works, not a stock robot joke; the
punch lands in the last few words, where the work doubles back on
itself.

## Running it

```sh
python3 main.py
```

That writes the line to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`). It needs nothing beyond the Python 3
standard library: after writing, it reads the file back and
checks the text is byte-for-byte the intended line, a single
line of 1–200 characters, and not only whitespace. The output is
identical on every run.

## Licence

Released under the MIT licence; the full text is in `LICENSE`.
