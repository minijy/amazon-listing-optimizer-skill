#!/usr/bin/env python3

import unittest

from lint_listing import lint


class LintListingTests(unittest.TestCase):
    def test_clean_listing_passes_without_errors(self):
        report = lint({
            "title": "Northstar Stainless Steel Water Bottle, 24 oz, Blue",
            "bullets": [
                "Double-wall insulation helps maintain drink temperature during daily commutes",
                "Leak-resistant threaded lid fits the included 24 oz bottle",
                "Stainless steel body is sized for standard backpack bottle pockets",
            ],
            "description": "A reusable bottle for work, school, and everyday travel.",
            "backend_search_terms": "flask canteen hydration vessel",
        })
        self.assertEqual(report["summary"]["errors"], 0)

    def test_policy_risks_fail_or_warn(self):
        report = lint({
            "title": "BEST Bottle! Bottle Bottle Bottle [NEEDS EVIDENCE]",
            "bullets": ["TODAY ONLY SALE 😀"],
            "description": "Satisfaction guaranteed or get a refund.",
            "backend_search_terms": "bottle,best",
        })
        codes = {item["code"] for item in report["findings"]}
        self.assertIn("forbidden_title_characters", codes)
        self.assertIn("title_word_repetition", codes)
        self.assertIn("unresolved_placeholders", codes)
        self.assertIn("price_promotion", codes)

    def test_regulated_claim_is_flagged_for_evidence(self):
        report = lint({
            "title": "Herbal Skin Cream, 2 oz",
            "bullets": [
                "Clinically proven to treat eczema",
                "Hypoallergenic formula",
                "Compact jar for daily care",
            ],
            "description": "A topical cream.",
            "backend_search_terms": "skin moisturizer",
        })
        codes = {item["code"] for item in report["findings"]}
        self.assertIn("regulated_claim_needs_evidence", codes)


if __name__ == "__main__":
    unittest.main()
