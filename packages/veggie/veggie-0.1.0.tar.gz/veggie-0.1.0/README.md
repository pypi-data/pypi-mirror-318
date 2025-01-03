# Development
```bash
# Setup virtual environment
python -m venv venv
.\venv\Scripts\activate # On Linux: . venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
mypy --install-types
```

# Roadmap
- [X] Click on events table to view details
- [ ] Update event status periodically
- [ ] README with usage and nice intro
- [X] Requirements versions
- [ ] Pypi packaging: veggie
- [X] Parameterize ports, etc.
- [ ] Reddit post
- [ ] Add tests
