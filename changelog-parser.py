#!/usr/bin/env python3

import sys

version = sys.argv[1]
changelog = sys.argv[2]

changelog_file = open(changelog, "r")
changelog = changelog_file.read()
changelog_file.close()

version_string = f"## [{version}"
next_version_string = "## ["

changelog_start = changelog.rfind(version_string)

changelog_end = changelog.find(next_version_string, changelog_start + len(version_string))

print(changelog[changelog_start:changelog_end])