# Contributing to EDA Assistant MCP

🎉 Thank you for your interest in contributing to the EDA Assistant MCP! We welcome contributions from the community and are excited to see what you can bring to the project.

## 🌟 Ways to Contribute

- 🐛 **Bug Reports**: Found a bug? Let us know!
- 💡 **Feature Requests**: Have an idea for a new feature?
- 📝 **Documentation**: Help improve our docs
- 🧪 **Code Contributions**: Fix bugs or add new features
- 🎨 **Visualization Templates**: Create new visualization strategies
- 📊 **Analysis Prompts**: Add specialized domain prompts

## 🚀 Getting Started

### Development Environment Setup

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/eda-assistant-mcp.git
   cd eda-assistant-mcp
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install development dependencies**:
   ```bash
   # Using uv (recommended)
   uv sync --dev
   
   # Or using pip
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

5. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-amazing-feature
   ```

## 📝 Adding New Analysis Prompts

### Prompt Structure

When adding new analysis prompts, follow this structure:

```python
@mcp.prompt()
def your_analysis_prompt(
    dataset_name: str,
    required_param: str,
    optional_param: str = "default_value",
    context: str = ""
) -> str:
    """Brief description of what this prompt does
    
    Args:
        dataset_name: Name or description of the dataset
        required_param: Required parameter description
        optional_param: Optional parameter with default
        context: Additional context for the analysis
        
    Returns:
        Formatted prompt string for EDA analysis
    """
    return f"""
Your comprehensive analysis prompt here...

**Dataset:** {dataset_name}
**Context:** {context}

**Analysis Framework:**

1. **Section 1**
   - Detailed analysis points
   - Specific methodologies
   - Expected outcomes

2. **Section 2**
   - Additional analysis components
   - Implementation guidelines
   - Quality checks

**Deliverables:**
- Clear, actionable outputs
- Code implementation guidance
- Validation strategies
"""
```

### Prompt Categories

Organize your prompts into these categories:

- **Core Data Exploration**: Basic EDA functions
- **Specialized Analysis**: Domain-specific analysis
- **Advanced Analytics**: Statistical and ML-focused
- **Visualization**: Chart and dashboard strategies
- **Quality & Validation**: Data quality assessment
- **Automation**: Pipeline and workflow prompts

## 🛠️ Adding New Tools

### Tool Structure

```python
@mcp.tool()
def your_new_tool(parameter: str, optional_param: int = 10) -> str:
    """
    Brief description of what this tool does.
    
    Args:
        parameter: Description of required parameter
        optional_param: Description of optional parameter
        
    Returns:
        String containing tool output or analysis results
        
    Raises:
        SpecificError: When specific error conditions occur
    """
    try:
        # Your tool implementation here
        result = perform_analysis(parameter, optional_param)
        
        return f"Tool output: {result}"
        
    except Exception as e:
        return f"Error in tool execution: {str(e)}"
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_prompts.py

# Run with coverage
pytest --cov=server
```

### Writing Tests

Create tests for new prompts and tools:

```python
def test_your_new_prompt():
    """Test your new analysis prompt"""
    result = your_analysis_prompt(
        dataset_name="Test Dataset",
        required_param="test_value"
    )
    
    assert "Dataset: Test Dataset" in result
    assert "Analysis Framework:" in result
    assert len(result) > 100  # Ensure comprehensive output
```

## 📋 Code Style Guidelines

### Python Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and returns
- Write comprehensive docstrings
- Keep functions focused and single-purpose
- Use meaningful variable names

### Prompt Writing Style

- Use clear, actionable language
- Structure prompts with numbered sections
- Include specific deliverables
- Provide context and business relevance
- Include code implementation guidance

### Example Style:

```python
# Good ✅
@mcp.prompt()
def customer_segmentation_analysis(
    dataset_info: str,
    customer_features: str,
    business_objective: str = "retention"
) -> str:
    """Comprehensive customer segmentation analysis with business focus"""
    return f"""
**Customer Segmentation Analysis for:** {dataset_info}

**Business Objective:** {business_objective}
**Features:** {customer_features}

**Analysis Framework:**

1. **Segmentation Strategy**
   - RFM analysis implementation
   - Behavioral clustering approaches
   - Demographic segmentation

**Python Implementation:**
```python
# Segmentation code here
```
"""

# Avoid ❌
def analyze_customers(data):
    return "Do customer analysis"
```

## 🔍 Code Review Process

1. **Self-Review**: Review your own code before submitting
2. **Testing**: Ensure all tests pass
3. **Documentation**: Update relevant documentation
4. **Pull Request**: Create a detailed PR description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Added tests for new functionality
- [ ] All existing tests pass
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

## 📊 Priority Areas for Contribution

### High Priority
- 🔄 **Domain-specific analysis prompts** (healthcare, finance, marketing)
- 🎨 **Interactive visualization templates**
- 🤖 **ML model integration improvements**
- 📱 **Real-time data analysis capabilities**

### Medium Priority
- 🌐 **Multi-language support**
- ☁️ **Cloud deployment templates**
- 📊 **Advanced statistical methods**
- 🔗 **Integration with popular data tools**

### Good First Issues
- 📝 **Documentation improvements**
- 🐛 **Bug fixes in existing prompts**
- 🧪 **Adding test cases**
- 🎨 **UI/UX improvements for outputs**

## 🚫 What We Don't Accept

- Code without proper documentation
- Changes that break existing functionality without justification
- Prompts that are too generic or lack business context
- Tools without proper error handling
- Contributions that don't follow our code style

## 📞 Getting Help

- 💬 **GitHub Discussions**: Ask questions and share ideas
- 🐛 **GitHub Issues**: Report bugs or request features
- 📧 **Email**: Direct contact for sensitive issues

## 🏆 Recognition

Contributors will be:
- 📛 **Listed in CONTRIBUTORS.md**
- 🎉 **Mentioned in release notes**
- 🌟 **Credited in documentation**
- 🏅 **Eligible for contributor badges**

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- 🤝 Be respectful and inclusive
- 💬 Communicate constructively
- 🎯 Focus on the project goals
- 🚫 Avoid discriminatory language or behavior

## 🔄 Development Workflow

1. **Issue Creation**: Create or claim an issue
2. **Branch Creation**: Create feature branch
3. **Development**: Write code and tests
4. **Testing**: Ensure all tests pass
5. **Documentation**: Update relevant docs
6. **Pull Request**: Submit PR for review
7. **Review**: Address feedback
8. **Merge**: Code gets merged to main

---

**Thank you for contributing to EDA Assistant MCP! 🚀**

Your contributions help make data analysis more accessible and powerful for everyone.