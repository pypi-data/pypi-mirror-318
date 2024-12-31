# Crawler Update detector

This Python package provides the following features:

Website Content Hash Checking
It calculates the hash value of the entire website content using MD5 or SHA algorithms and regularly checks if the website content has changed. If the website content's hash value changes, the package detects that the website has been updated.

Text Change Analysis
When a change in the website content is detected, the package extracts the changed text and uses the Azure GPT API to analyze whether the text change is important information. For example, it can identify whether there are new key news items, product updates, policy changes, etc.

XPath for Updated Information
For the detected text changes, the package provides the corresponding XPath to easily locate the updated content, allowing users to further process or update their scraping logic.
