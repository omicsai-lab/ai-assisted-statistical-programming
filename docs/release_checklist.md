# Release checklist

Before tagging a release:

- [ ] Run `python run_all_python_examples.py` from a clean environment.
- [ ] Run `Rscript run_all_R_examples.R` from a clean R environment.
- [ ] Confirm that all generated files are written to `output/`.
- [ ] Confirm that no private data, API keys, credentials, or unpublished manuscript files are committed.
- [ ] Update `CHANGELOG.md`.
- [ ] Update `ERRATA.md` if needed.
- [ ] Create a GitHub release tag, for example `v1.0.0`.
- [ ] Add the release URL or repository URL to the book front matter and KDP description.
