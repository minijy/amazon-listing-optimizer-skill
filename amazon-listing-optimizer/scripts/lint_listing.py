#!/usr/bin/env python3
"""Conservative preflight checks for an Amazon listing JSON document."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


TITLE_FORBIDDEN = set("!$?_{}^¬¦")
TITLE_REPEAT_EXEMPT = {
    "a", "an", "and", "as", "at", "by", "for", "from", "in", "of", "on",
    "or", "the", "to", "with", "de", "del", "la", "las", "el", "los", "y",
}
PROMOTIONAL_PATTERNS = {
    "price_promotion": re.compile(r"\b(?:sale|discount|coupon|deal|lowest price|limited time|today only)\b", re.I),
    "refund_guarantee": re.compile(r"\b(?:money[- ]back|refund|satisfaction guaranteed|risk[- ]free)\b", re.I),
    "ranking_superlative": re.compile(r"(?:#\s*1|\bnumber one\b|\bbest(?:-selling)?\b|\btop[- ]rated\b)", re.I),
    "external_contact": re.compile(r"(?:https?://|www\.|@[A-Za-z0-9._-]+|\b(?:email|contact us|visit our)\b)", re.I),
    "regulated_claim_needs_evidence": re.compile(r"\b(?:cure|cures|treat|treats|prevent|prevents|diagnose|diagnoses|fda approved|clinically proven|non[- ]toxic|hypoallergenic|organic|biodegradable|carbon neutral|bpa[- ]free)\b", re.I),
    "absolute_claim": re.compile(r"\b(?:100% safe|works for everyone|permanent results?|never fails?|guaranteed results?)\b", re.I),
}


def issue(level: str, field: str, code: str, message: str) -> dict[str, str]:
    return {"level": level, "field": field, "code": code, "message": message}


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:[-'][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)?", text.lower())


def visible_text(data: dict[str, Any]) -> str:
    bullets = data.get("bullets") or []
    return " ".join([str(data.get("title", "")), *map(str, bullets), str(data.get("description", ""))])


def lint(data: dict[str, Any]) -> dict[str, Any]:
    findings: list[dict[str, str]] = []
    title = str(data.get("title") or "").strip()
    bullets = data.get("bullets") or []
    description = str(data.get("description") or "").strip()
    backend = str(data.get("backend_search_terms") or "").strip()
    title_max = int(data.get("constraints", {}).get("title_max_chars", 200))

    if not title:
        findings.append(issue("error", "title", "missing_title", "Title is required."))
    if len(title) > title_max:
        findings.append(issue("error", "title", "title_too_long", f"Title has {len(title)} characters; configured maximum is {title_max}."))
    if 80 < len(title) <= title_max:
        findings.append(issue("warning", "title", "title_long", f"Title has {len(title)} characters; concise titles often scan and truncate better."))
    bad_chars = sorted(set(title) & TITLE_FORBIDDEN)
    if bad_chars:
        findings.append(issue("error", "title", "forbidden_title_characters", f"Remove prohibited title characters: {' '.join(bad_chars)}"))

    counts = Counter(w for w in words(title) if w not in TITLE_REPEAT_EXEMPT)
    repeated = sorted(w for w, count in counts.items() if count > 2)
    if repeated:
        findings.append(issue("error", "title", "title_word_repetition", f"Words appearing more than twice: {', '.join(repeated)}"))

    if not isinstance(bullets, list):
        findings.append(issue("error", "bullets", "invalid_bullets", "Bullets must be a JSON array."))
        bullets = []
    if len(bullets) < 3:
        findings.append(issue("warning", "bullets", "few_bullets", f"Only {len(bullets)} bullets supplied; Amazon commonly recommends at least three."))
    if len(bullets) > 5:
        findings.append(issue("warning", "bullets", "many_bullets", f"{len(bullets)} bullets supplied; confirm the category supports them."))

    fields = {"title": title, "description": description, "backend_search_terms": backend}
    fields.update({f"bullets[{i}]": str(value) for i, value in enumerate(bullets)})
    for field, value in fields.items():
        if value and value.isupper() and len(words(value)) >= 3:
            findings.append(issue("warning", field, "all_caps", "Avoid all-capital copy."))
        if re.search(r"[\U0001F300-\U0001FAFF]", value):
            findings.append(issue("warning", field, "emoji", "Remove emojis from catalog copy."))
        for code, pattern in PROMOTIONAL_PATTERNS.items():
            if pattern.search(value):
                findings.append(issue("warning", field, code, f"Review potentially non-compliant {code.replace('_', ' ')} language."))

    normalized_bullets = [re.sub(r"\s+", " ", str(x).strip().lower()) for x in bullets]
    if any(text and count > 1 for text, count in Counter(normalized_bullets).items()):
        findings.append(issue("warning", "bullets", "duplicate_bullets", "Two or more bullet points are identical."))

    if "," in backend or ";" in backend:
        findings.append(issue("warning", "backend_search_terms", "backend_punctuation", "Use single spaces rather than commas or semicolons unless current field guidance differs."))
    visible = set(words(visible_text(data)))
    backend_words = set(words(backend))
    if backend_words:
        duplicate_ratio = len(visible & backend_words) / len(backend_words)
        if duplicate_ratio >= 0.6:
            findings.append(issue("warning", "backend_search_terms", "backend_duplication", f"{duplicate_ratio:.0%} of backend terms already occur in visible copy; prioritize incremental coverage."))

    if re.search(r"\[(?:NEEDS EVIDENCE|UNKNOWN|TODO)[^\]]*\]", visible_text(data), re.I):
        findings.append(issue("error", "listing", "unresolved_placeholders", "Resolve evidence placeholders before publishing."))

    errors = sum(item["level"] == "error" for item in findings)
    warnings = sum(item["level"] == "warning" for item in findings)
    return {
        "status": "fail" if errors else ("warn" if warnings else "pass"),
        "summary": {"errors": errors, "warnings": warnings},
        "findings": findings,
        "note": "Conservative preflight only; current marketplace and category validation remains authoritative.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("listing", type=Path, help="Path to listing JSON")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    args = parser.parse_args()
    try:
        data = json.loads(args.listing.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False))
        return 2
    if not isinstance(data, dict):
        print(json.dumps({"status": "error", "message": "Top-level JSON must be an object."}, ensure_ascii=False))
        return 2
    report = lint(data)
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None))
    return 1 if report["summary"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
