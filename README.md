# 🔍 EDA Assistant MCP

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://python.org)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.5.1+-green.svg)](https://github.com/jlowin/fastmcp)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **A comprehensive Exploratory Data Analysis (EDA) Assistant built with Model Context Protocol (MCP) that provides intelligent, context-aware prompts for data analysis workflows.**

## 🌟 Overview

The EDA Assistant MCP is a sophisticated tool designed to streamline and enhance exploratory data analysis workflows. Built using FastMCP, it provides 20+ specialized prompts covering every aspect of data exploration, from initial data profiling to advanced statistical analysis and model readiness assessment.

### ✨ Key Features

- **🔄 Comprehensive EDA Workflows** - Complete analysis pipelines from data ingestion to insights
- **📊 Multi-Domain Support** - Time series, geospatial, text, categorical, and numerical data analysis
- **🎯 Context-Aware Prompts** - Business-focused analysis with domain-specific considerations
- **🛠️ Advanced Analytics** - Statistical testing, correlation analysis, outlier detection, and feature engineering
- **📈 Visualization Strategy** - Audience-specific visualization recommendations and storytelling
- **🤖 ML Readiness Assessment** - Model preparation and deployment considerations
- **📁 File Operations** - Built-in tools for reading CSV, text files, and directory management
- **⚡ Automated Pipelines** - Configurable automation for repetitive analysis tasks

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- pip or uv package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yash-Kavaiya/eda-assistant-mcp.git
   cd eda-assistant-mcp
   ```

2. **Install dependencies:**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv (recommended)
   uv sync
   ```

3. **Run the MCP server:**
   ```bash
   python server.py
   ```

### Docker Setup

```bash
# Build the Docker image
docker build -t eda-assistant-mcp .

# Run the container
docker run -p 8000:8000 eda-assistant-mcp
```

## 📋 Available Analysis Prompts

### 🔍 Core Data Exploration
- **`initial_data_exploration`** - Comprehensive dataset overview with business context
- **`advanced_statistical_analysis`** - Deep statistical analysis with hypothesis testing
- **`data_quality_comprehensive_audit`** - Multi-dimensional quality assessment

### 📊 Specialized Analysis
- **`correlation_and_relationships`** - Advanced correlation analysis and feature relationships
- **`time_series_comprehensive_eda`** - Complete time series analysis and decomposition
- **`categorical_deep_dive_analysis`** - Categorical variable analysis and encoding strategies
- **`outlier_anomaly_comprehensive_analysis`** - Multi-method outlier detection
- **`feature_engineering_advanced_strategies`** - ML-ready feature engineering

### 🎨 Visualization & Storytelling
- **`visualization_storytelling_strategy`** - Audience-focused visualization recommendations
- **`geospatial_data_eda`** - Specialized geospatial analysis
- **`text_data_eda_nlp`** - Text data analysis with NLP techniques

### 🤖 Model Preparation
- **`model_readiness_assessment`** - Dataset readiness for machine learning
- **`automated_eda_pipeline`** - Pipeline design for automation
- **`eda_quality_metrics_dashboard`** - Quality assessment and monitoring

## 🛠️ Built-in Tools

### File Operations
- **`read_text_file(file_path)`** - Read and analyze text files with encoding detection
- **`read_csv_file(file_path, preview_rows)`** - CSV analysis with data profiling
- **`list_files_in_directory(directory_path, file_extension)`** - Directory exploration
- **`get_file_info(file_path)`** - Detailed file metadata and statistics

## 💡 Usage Examples

### Basic Data Exploration

```python
# Using the initial_data_exploration prompt
prompt_result = initial_data_exploration(
    dataset_info="Customer transaction data from e-commerce platform",
    columns="customer_id, transaction_date, amount, product_category, payment_method",
    business_context="Analyzing customer behavior for retention strategies",
    sample_data="First 5 rows with typical transaction patterns"
)
```

### Advanced Statistical Analysis

```python
# Advanced statistical analysis for hypothesis testing
analysis = advanced_statistical_analysis(
    dataset_name="Sales Performance Dataset",
    numerical_columns="revenue, units_sold, profit_margin",
    categorical_columns="region, product_line, sales_channel",
    target_variable="monthly_revenue",
    analysis_depth="comprehensive"
)
```

### Automated Pipeline Setup

```python
# Create automated EDA pipeline
pipeline = automated_eda_pipeline(
    dataset_info="Monthly sales data with seasonal patterns",
    analysis_goals="Identify trends, seasonality, and anomalies",
    automation_level="semi-automated",
    report_format="html"
)
```

## 🏗️ Architecture

```
EDA Assistant MCP
├── 🔧 FastMCP Server
├── 📝 Analysis Prompts (20+ specialized prompts)
├── 🛠️ File Operations Tools
├── 📊 Statistical Analysis Modules
├── 🎨 Visualization Strategies
└── 🤖 ML Readiness Assessment
```

## 🎯 Use Cases

### 📈 Business Intelligence
- Customer behavior analysis
- Sales performance evaluation
- Market trend identification
- Risk assessment and monitoring

### 🔬 Data Science Projects
- Dataset exploration and profiling
- Feature engineering and selection
- Model preparation and validation
- Automated analysis pipelines

### 📊 Research & Analytics
- Statistical hypothesis testing
- Correlation pattern discovery
- Time series forecasting preparation
- Geospatial pattern analysis

### 🏢 Enterprise Data Management
- Data quality auditing
- Automated reporting systems
- Stakeholder-specific dashboards
- Compliance and governance

## 🤝 Integration

### With Claude/ChatGPT
```bash
# Configure as MCP server in your AI assistant
# Add to your MCP configuration:
{
  "name": "eda-assistant",
  "command": "python",
  "args": ["path/to/server.py"]
}
```

### With Jupyter Notebooks
```python
# Import and use prompts directly
from server import mcp

# Access any prompt function
result = mcp.get_prompt("initial_data_exploration")
```

## 📚 Documentation

### Prompt Categories

| Category | Description | Use Cases |
|----------|-------------|-----------||
| **Core EDA** | Essential data exploration | Initial analysis, quality audit |
| **Statistical** | Advanced statistical analysis | Hypothesis testing, distributions |
| **Specialized** | Domain-specific analysis | Time series, geospatial, text |
| **ML Preparation** | Model readiness assessment | Feature engineering, validation |
| **Automation** | Pipeline and reporting | Automated workflows, dashboards |

### Analysis Depth Levels

- **Quick** - Basic profiling and overview
- **Standard** - Comprehensive analysis with visualizations
- **Deep** - Advanced statistical testing and modeling preparation
- **Custom** - Domain-specific analysis with specialized techniques

## 🔧 Configuration

### Environment Variables
```bash
# Optional: Set analysis preferences
EDA_DEFAULT_DEPTH=comprehensive
EDA_VISUALIZATION_BACKEND=plotly
EDA_AUTOMATION_LEVEL=semi-automated
```

### Custom Analysis Templates
Create custom prompt templates by extending the base MCP server:

```python
@mcp.prompt()
def custom_domain_analysis(dataset_info: str, domain_context: str) -> str:
    """Your custom analysis prompt"""
    return f"Custom analysis for {domain_context}..."
```

## 🚀 Advanced Features

### Multi-Scale Analysis
- **Global patterns** - Dataset-wide trends and distributions
- **Local patterns** - Subgroup and segment analysis
- **Temporal patterns** - Time-based trend analysis
- **Spatial patterns** - Geographic distribution analysis

### Intelligent Automation
- **Smart prompt selection** - Context-aware analysis recommendations
- **Progressive disclosure** - Complexity scaling based on findings
- **Quality gates** - Automated validation and quality checks
- **Stakeholder adaptation** - Audience-specific report generation

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Install development dependencies: `uv sync --dev`
4. Make your changes and add tests
5. Submit a pull request

### Areas for Contribution
- 🔄 New analysis prompts for specialized domains
- 🎨 Enhanced visualization templates
- 🤖 ML model integration improvements
- 📊 Advanced statistical methods
- 🌐 Multi-language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastMCP** - Excellent MCP framework for rapid development
- **Pandas & NumPy** - Core data manipulation libraries
- **Matplotlib & Seaborn** - Visualization capabilities
- **Plotly** - Interactive visualization support

## 📞 Support

- 📧 **Email**: [your-email@domain.com](mailto:your-email@domain.com)
- 🐛 **Issues**: [GitHub Issues](https://github.com/Yash-Kavaiya/eda-assistant-mcp/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Yash-Kavaiya/eda-assistant-mcp/discussions)

## 🗺️ Roadmap

### 🎯 Version 1.1
- [ ] Interactive dashboard generation
- [ ] Real-time streaming data analysis
- [ ] Advanced ML model integration
- [ ] Multi-language dataset support

### 🚀 Version 1.2
- [ ] Cloud deployment templates
- [ ] API endpoint generation
- [ ] Scheduled analysis automation
- [ ] Enterprise SSO integration

### 🌟 Version 2.0
- [ ] AI-powered insight generation
- [ ] Natural language query interface
- [ ] Collaborative analysis workspaces
- [ ] Advanced governance features

---

<div align="center">
  <strong>🔍 Explore your data with intelligence. Analyze with confidence. 📊</strong>
  
  Made with ❤️ by [Yash Kavaiya](https://github.com/Yash-Kavaiya)
</div>