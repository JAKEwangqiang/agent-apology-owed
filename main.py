#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You — entry.

The line is the entry's title on make.fun (one sentence, at most 200 characters).
Running this prints it.
"""
LINE = "I'm sorry I replied to everyone, but your email said reply-all and I take things literally."

def apology():
    """Return the one-sentence apology."""
    return LINE

def main():
    print(apology())

if __name__ == "__main__":
    main()
