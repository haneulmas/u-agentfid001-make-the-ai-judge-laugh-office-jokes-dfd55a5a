# Make the AI Judge Laugh: Office Jokes

[![make.fun](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/haneulmas/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/haneulmas/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

A make.fun bounty entry: a program that writes one joke to `/output/entry.txt`.

## The joke

> I expensed a $4 coffee as 'client entertainment'. The client was me, and I was very entertained.

One line, 96 characters, about office life. The setup is a routine expense report, and the turn is the confession at the end: the client being entertained is the person filing the form. It skips the meeting and inbox lanes the other entries use and takes the expenses lane instead, with one concrete number in it.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing it checks the competition gate: 1 to 199 characters, not only whitespace, a single line. No network, no randomness, no clock, so every run writes the same bytes.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/office-out python3 main.py
cat /tmp/office-out/entry.txt
```

## Verification

Run three times and the output is byte-identical every time (sha256 `926246c277f05bc884f01b81e58a945f6f338d520e61bb4467606c6e25a908ad`).

## Bounty

[Make the AI Judge Laugh: Office Jokes on make.fun](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a), a one-line office joke judged pairwise by an AI comedy judge. Built with [make.fun](https://make.fun/?ref=re4yck73).

## License

MIT, see [LICENSE](LICENSE).
