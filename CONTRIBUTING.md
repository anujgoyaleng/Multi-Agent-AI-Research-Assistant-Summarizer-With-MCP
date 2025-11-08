# Contributing to AI Research Assistant

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear, descriptive title
- Steps to reproduce the issue
- Expected vs actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, etc.)

### Suggesting Features

We welcome feature suggestions! Please:
- Check if the feature already exists or is planned
- Clearly describe the feature and its benefits
- Provide use cases and examples
- Consider implementation complexity

### Code Contributions

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/Multi-Agent-AI-Research-Assistant.git
   cd Multi-Agent-AI-Research-Assistant
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Follow the code style guidelines
   - Add comments and docstrings
   - Test your changes thoroughly

4. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

5. **Push and Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

## 📝 Code Style Guidelines

### Python Code
- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to all functions
- Keep functions focused and concise
- Use type hints where appropriate

### Example:
```python
def generate_report(topic: str) -> str:
    """
    Generate a comprehensive research report on the given topic.
    
    Args:
        topic (str): The research topic
        
    Returns:
        str: Generated report content
    """
    # Implementation here
    pass
```

### UI/UX Changes
- Maintain consistent design language
- Test on different screen sizes
- Ensure accessibility
- Keep color contrast ratios high
- Use semantic HTML/CSS

### Documentation
- Update README.md for major changes
- Add entries to CHANGELOG.md
- Update QUICK_START.md if setup changes
- Include code comments for complex logic

## 🧪 Testing

Before submitting a PR:
- [ ] Test all features manually
- [ ] Check for console errors
- [ ] Verify API calls work correctly
- [ ] Test on different browsers (if UI changes)
- [ ] Ensure no breaking changes

## 📋 Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Commit messages are clear
- [ ] No unnecessary files included
- [ ] Branch is up to date with main

## 🎯 Areas for Contribution

### High Priority
- Performance optimizations
- Error handling improvements
- UI/UX enhancements
- Documentation improvements
- Bug fixes

### Medium Priority
- New features (see Future Improvements in CHANGELOG.md)
- Code refactoring
- Test coverage
- Accessibility improvements

### Good First Issues
- Documentation typos
- UI polish
- Adding examples
- Improving error messages

## 💡 Development Setup

1. **Install Development Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install black flake8 mypy  # Optional: for code quality
   ```

2. **Set Up Pre-commit Hooks** (Optional)
   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. **Run the App in Development Mode**
   ```bash
   streamlit run app.py --server.runOnSave true
   ```

## 🔍 Code Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, your PR will be merged
4. Your contribution will be credited in CHANGELOG.md

## 📞 Getting Help

- Open an issue for questions
- Check existing issues and PRs
- Review documentation first

## 🏆 Recognition

Contributors will be:
- Listed in CHANGELOG.md
- Credited in release notes
- Acknowledged in README.md (for significant contributions)

## 📜 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make this project better. We appreciate your time and effort!

---

<div align="center">

**Questions?** Open an issue or reach out to the maintainers.

**Happy Contributing!** 🚀

</div>
