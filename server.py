from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from typing import List, Dict, Any, Optional
import json

# Initialize the FastMCP server
mcp = FastMCP("Enhanced EDA Assistant")

# =============================================================================
# CORE DATA EXPLORATION PROMPTS
# =============================================================================

@mcp.prompt()
def initial_data_exploration(
    dataset_info: str,
    columns: str = "",
    sample_data: str = "",
    data_types: str = "",
    business_context: str = ""
) -> str:
    """Generate comprehensive initial data exploration analysis with business context"""
    return f"""
Perform initial exploratory data analysis with the following specifications:

**Dataset Context:**
{dataset_info}

**Business Context:** {business_context}

**Technical Details:**
- Columns: {columns}
- Sample Data: {sample_data}
- Data Types: {data_types}

**Required Analysis:**

1. **Dataset Overview & Structure**
   - Dataset dimensions and memory usage
   - Column data types and their appropriateness
   - Index analysis and potential issues

2. **Data Quality First Pass**
   - Missing value patterns (% and distribution)
   - Duplicate records identification
   - Data consistency checks
   - Obvious data entry errors

3. **Variable Classification**
   - Numerical: continuous vs discrete
   - Categorical: nominal vs ordinal, cardinality levels
   - DateTime variables and temporal patterns
   - Mixed-type columns requiring attention

4. **Business Logic Validation**
   - Reasonable value ranges for each variable
   - Expected relationships between variables
   - Domain-specific constraints validation

5. **Next Steps Prioritization**
   - High-impact quality issues to address first
   - Variables requiring deeper investigation
   - Suggested analysis sequence

**Deliverables:**
- Executive summary (3-4 bullet points)
- Detailed findings with evidence
- Python code for reproducible analysis
- Risk assessment for data quality issues
"""

@mcp.prompt()
def advanced_statistical_analysis(
    dataset_name: str,
    numerical_columns: str,
    categorical_columns: str,
    target_variable: str = "",
    analysis_depth: str = "comprehensive",
    statistical_tests: str = "auto-select"
) -> str:
    """Advanced statistical analysis with hypothesis testing"""
    return f"""
Conduct advanced statistical analysis for: **{dataset_name}**

**Variables:**
- Numerical: {numerical_columns}
- Categorical: {categorical_columns}
- Target: {target_variable}

**Analysis Configuration:**
- Depth: {analysis_depth}
- Statistical Tests: {statistical_tests}

**Statistical Analysis Framework:**

1. **Descriptive Statistics Deep Dive**
   - Central tendency with confidence intervals
   - Variability measures and their interpretation
   - Shape statistics (skewness, kurtosis) with significance tests
   - Robust statistics for outlier-resistant analysis

2. **Distribution Analysis**
   - Normality testing (Shapiro-Wilk, Anderson-Darling, Kolmogorov-Smirnov)
   - Distribution fitting and goodness-of-fit tests
   - Transformation recommendations with before/after comparisons
   - Q-Q plots interpretation

3. **Hypothesis Testing Framework**
   - Group comparisons (t-tests, Mann-Whitney U, ANOVA, Kruskal-Wallis)
   - Independence tests (Chi-square, Fisher's exact)
   - Correlation significance testing
   - Multiple comparison corrections (Bonferroni, FDR)

4. **Effect Size Calculations**
   - Cohen's d, eta-squared, Cramer's V
   - Practical significance vs statistical significance
   - Power analysis recommendations

5. **Advanced Metrics**
   - Entropy and information content
   - Coefficient of variation analysis
   - Interquartile range ratios
   - Tail behavior analysis

**Code Requirements:**
- Statistical test implementations with proper assumptions checking
- Visualization of test results
- Automated report generation
- Effect size calculations and interpretations
"""

@mcp.prompt()
def data_quality_comprehensive_audit(
    dataset_info: str,
    quality_dimensions: str = "completeness,accuracy,consistency,validity,uniqueness",
    severity_levels: str = "critical,high,medium,low",
    automated_fixes: str = "suggest"
) -> str:
    """Comprehensive data quality audit with actionable remediation plan"""
    return f"""
Conduct comprehensive data quality audit for: {dataset_info}

**Quality Dimensions:** {quality_dimensions}
**Severity Assessment:** {severity_levels}
**Automated Fixes:** {automated_fixes}

**Data Quality Assessment Framework:**

1. **Completeness Analysis**
   - Missing data pattern analysis (MCAR, MAR, MNAR)
   - Missing data correlation matrix
   - Impact assessment on analysis validity
   - Imputation strategy evaluation

2. **Accuracy Assessment**
   - Outlier detection with multiple methods
   - Range and domain validation
   - Cross-field validation rules
   - Reference data comparison (if available)

3. **Consistency Evaluation**
   - Cross-table consistency checks
   - Format standardization needs
   - Unit consistency verification
   - Temporal consistency analysis

4. **Validity Verification**
   - Data type appropriateness
   - Format compliance checking
   - Business rule validation
   - Referential integrity assessment

5. **Uniqueness Analysis**
   - Duplicate detection algorithms
   - Fuzzy matching for near-duplicates
   - Primary key validation
   - Record linkage quality

**Quality Metrics Dashboard:**
- Overall quality score calculation
- Dimension-wise quality metrics
- Trend analysis over time (if temporal data)
- Quality impact on downstream analysis

**Remediation Action Plan:**
- Priority-ranked quality issues
- Automated fix recommendations
- Manual review requirements
- Quality monitoring setup
- Data cleansing pipeline design

**Python Implementation:**
- Quality assessment functions
- Automated reporting tools
- Data profiling integration
- Quality monitoring framework
"""

# =============================================================================
# SPECIALIZED ANALYSIS PROMPTS
# =============================================================================

@mcp.prompt()
def correlation_and_relationships(
    dataset_name: str,
    variables: str,
    target_variable: str = "",
    correlation_methods: str = "pearson,spearman,kendall",
    relationship_types: str = "linear,monotonic,non-linear"
) -> str:
    """Advanced correlation and relationship analysis"""
    return f"""
Analyze relationships and correlations in: **{dataset_name}**

**Variables:** {variables}
**Target:** {target_variable}
**Methods:** {correlation_methods}
**Relationship Types:** {relationship_types}

**Correlation Analysis Framework:**

1. **Multiple Correlation Methods**
   - Pearson (linear relationships)
   - Spearman (monotonic relationships)
   - Kendall (rank-based, robust to outliers)
   - Partial correlations (controlling for confounders)

2. **Non-Linear Relationship Detection**
   - Mutual information analysis
   - Maximal information coefficient (MIC)
   - Distance correlation
   - Copula-based dependence measures

3. **Multicollinearity Assessment**
   - Variance Inflation Factor (VIF)
   - Condition number analysis
   - Eigenvalue diagnostics
   - Tolerance statistics

4. **Categorical Variable Associations**
   - Cramer's V for categorical-categorical
   - Point-biserial for categorical-continuous
   - Eta-squared for ANOVA-type relationships
   - Uncertainty coefficient analysis

5. **Advanced Relationship Patterns**
   - Interaction effects detection
   - Threshold effects identification
   - Seasonal correlation patterns
   - Lag correlation analysis (for time series)

**Target Variable Focus:**
- Feature importance preliminary ranking
- Univariate relationships with statistical significance
- Non-linear pattern identification
- Feature interaction candidates

**Visualization Strategy:**
- Correlation heatmaps with clustering
- Scatter plot matrices with trend lines
- Partial dependence plots
- Network graphs for variable relationships

**Feature Selection Insights:**
- Redundant feature identification
- Feature combination opportunities
- Dimension reduction recommendations
- Model-specific feature relevance
"""

@mcp.prompt()
def time_series_comprehensive_eda(
    dataset_name: str,
    date_column: str,
    value_columns: str,
    frequency: str = "auto-detect",
    seasonal_periods: str = "auto-detect",
    external_factors: str = ""
) -> str:
    """Comprehensive time series exploratory data analysis"""
    return f"""
Comprehensive time series EDA for: **{dataset_name}**

**Temporal Structure:**
- Date Column: {date_column}
- Value Columns: {value_columns}
- Frequency: {frequency}
- Seasonal Periods: {seasonal_periods}
- External Factors: {external_factors}

**Time Series Analysis Framework:**

1. **Temporal Structure Analysis**
   - Frequency detection and validation
   - Missing time periods identification
   - Irregular spacing assessment
   - Calendar effects detection

2. **Decomposition Analysis**
   - Classical decomposition (additive/multiplicative)
   - STL decomposition (robust to outliers)
   - X-13ARIMA-SEATS seasonal adjustment
   - Empirical mode decomposition

3. **Stationarity Assessment**
   - Augmented Dickey-Fuller test
   - KPSS stationarity test
   - Phillips-Perron test
   - Visual stationarity assessment

4. **Seasonal Pattern Detection**
   - Multiple seasonality identification
   - Seasonal strength measurement
   - Holiday and calendar effects
   - Regime change detection

5. **Autocorrelation Analysis**
   - ACF/PACF plots with confidence intervals
   - Ljung-Box test for white noise
   - Spectral analysis and periodogram
   - Cross-correlation with external variables

6. **Trend Analysis**
   - Trend strength quantification
   - Change point detection
   - Structural break identification
   - Trend acceleration/deceleration

7. **Volatility and Risk Assessment**
   - Rolling statistics analysis
   - Volatility clustering detection
   - Value at Risk (VaR) estimation
   - Extreme value analysis

**Advanced Time Series Features:**
- Lag feature engineering
- Rolling window statistics
- Fourier transform features
- Wavelet analysis for multi-scale patterns

**Forecasting Readiness Assessment:**
- Data quality for forecasting
- Model selection guidance
- Cross-validation strategy for time series
- Forecast accuracy baseline establishment
"""

@mcp.prompt()
def categorical_deep_dive_analysis(
    dataset_name: str,
    categorical_variables: str,
    target_variable: str = "",
    cardinality_thresholds: str = "low:<10, medium:10-50, high:>50",
    encoding_strategy: str = "adaptive"
) -> str:
    """Deep dive analysis of categorical variables with encoding strategies"""
    return f"""
Deep categorical variable analysis for: **{dataset_name}**

**Variables:** {categorical_variables}
**Target:** {target_variable}
**Cardinality Levels:** {cardinality_thresholds}
**Encoding Strategy:** {encoding_strategy}

**Categorical Analysis Framework:**

1. **Cardinality Assessment**
   - Unique value counts and percentages
   - Cardinality impact on memory and computation
   - Sparse category identification (frequency < 1%)
   - Category consolidation opportunities

2. **Distribution Analysis**
   - Frequency distributions with confidence intervals
   - Class imbalance assessment
   - Rare category handling strategies
   - Zipf's law compliance testing

3. **Target Relationship Analysis**
   - Chi-square independence tests
   - Cramér's V association strength
   - Information value (IV) calculation
   - Weight of Evidence (WoE) analysis

4. **Category Quality Assessment**
   - Spelling variations and inconsistencies
   - Case sensitivity issues
   - Special character handling
   - Missing category representation

5. **Encoding Strategy Optimization**
   - One-hot encoding suitability
   - Target encoding with cross-validation
   - Frequency encoding evaluation
   - Hash encoding for high cardinality
   - Embedding approaches for deep learning

6. **Interaction Analysis**
   - Cross-tabulation insights
   - Category combination effects
   - Hierarchical relationship detection
   - Multi-way contingency analysis

7. **Business Logic Validation**
   - Expected vs actual category distributions
   - Domain knowledge consistency checks
   - Temporal stability of categories
   - Geographic distribution patterns

**Advanced Categorical Techniques:**
- Category clustering based on similarity
- Hierarchical category encoding
- Category embedding visualization
- Anomaly detection in categorical patterns

**Encoding Recommendations:**
- Memory optimization strategies
- Model-specific encoding advice
- Cross-validation for encoding methods
- Handling of unseen categories in production
"""

# =============================================================================
# ADVANCED ANALYSIS PROMPTS
# =============================================================================

@mcp.prompt()
def outlier_anomaly_comprehensive_analysis(
    dataset_name: str,
    variables: str,
    methods: str = "statistical,distance,density,clustering",
    domain_context: str = "",
    anomaly_types: str = "point,contextual,collective"
) -> str:
    """Comprehensive outlier and anomaly detection analysis"""
    return f"""
Comprehensive outlier/anomaly analysis for: **{dataset_name}**

**Variables:** {variables}
**Detection Methods:** {methods}
**Domain Context:** {domain_context}
**Anomaly Types:** {anomaly_types}

**Multi-Method Outlier Detection Framework:**

1. **Statistical Methods**
   - Z-score (modified for non-normal distributions)
   - Interquartile Range (IQR) with adaptive multipliers
   - Grubbs' test for single outliers
   - Dixon's test for small samples
   - Generalized Extreme Studentized Deviate

2. **Distance-Based Methods**
   - k-Nearest Neighbors distance
   - Local Outlier Factor (LOF)
   - Distance to k-th nearest neighbor
   - Relative distance metrics

3. **Density-Based Methods**
   - Local Outlier Factor (LOF)
   - Connectivity-based Outlier Factor (COF)
   - Influenced Outlier Factor (INFLO)
   - Histogram-based outlier detection

4. **Machine Learning Methods**
   - Isolation Forest with feature importance
   - One-Class SVM for novelty detection
   - Autoencoder reconstruction error
   - Ensemble outlier detection

5. **Domain-Specific Analysis**
   - Business rule-based outlier definition
   - Seasonal outlier detection
   - Multivariate outlier assessment
   - Time-series specific anomaly patterns

**Outlier Characterization:**
- Outlier severity scoring
- Multivariate vs univariate outliers
- Outlier cluster analysis
- Root cause hypothesis generation

**Impact Assessment:**
- Statistical analysis sensitivity to outliers
- Model performance impact evaluation
- Visualization distortion assessment
- Business impact quantification

**Handling Strategy Matrix:**
- Remove: When and why
- Transform: Mathematical transformations
- Cap/Floor: Winsorization strategies
- Investigate: Domain expert review needed
- Keep: Legitimate extreme values

**Advanced Techniques:**
- Robust statistical methods
- Outlier-resistant transformations
- Ensemble consensus scoring
- Time-aware anomaly detection
"""

@mcp.prompt()
def feature_engineering_advanced_strategies(
    dataset_name: str,
    current_features: str,
    target_variable: str,
    domain_context: str = "",
    ml_objective: str = "predictive_modeling",
    computational_constraints: str = "moderate"
) -> str:
    """Advanced feature engineering with ML-ready recommendations"""
    return f"""
Advanced feature engineering for: **{dataset_name}**

**Current Features:** {current_features}
**Target:** {target_variable}
**Domain:** {domain_context}
**ML Objective:** {ml_objective}
**Constraints:** {computational_constraints}

**Feature Engineering Framework:**

1. **Mathematical Transformations**
   - Box-Cox/Yeo-Johnson transformations
   - Log, square root, reciprocal transformations
   - Polynomial features with interaction terms
   - Trigonometric transformations for cyclical data

2. **Statistical Feature Creation**
   - Rolling window statistics (mean, std, percentiles)
   - Lag features and differencing
   - Cumulative and expanding window features
   - Rate of change and acceleration features

3. **Aggregation Features**
   - Group-wise statistics by categorical variables
   - Frequency encoding and count features
   - Target encoding with regularization
   - Statistical moments within groups

4. **Interaction Features**
   - Polynomial feature interactions
   - Ratio and difference features
   - Product and division combinations
   - Conditional feature creation

5. **Temporal Feature Engineering**
   - Date/time component extraction
   - Cyclic encoding (sin/cos transformations)
   - Time since last event features
   - Seasonal decomposition features

6. **Text Feature Engineering** (if applicable)
   - TF-IDF vectorization
   - N-gram features
   - Sentiment analysis scores
   - Named entity recognition features

7. **Dimensionality Transformation**
   - Principal Component Analysis (PCA)
   - Independent Component Analysis (ICA)
   - Linear Discriminant Analysis (LDA)
   - t-SNE for visualization

**Feature Selection Integration:**
- Mutual information scoring
- Univariate statistical tests
- Recursive feature elimination
- L1 regularization feature selection
- Forward/backward selection strategies

**Model-Specific Considerations:**
- Tree-based model feature engineering
- Linear model preprocessing requirements
- Deep learning feature preparation
- Ensemble method optimization

**Validation Framework:**
- Cross-validation for feature engineering
- Feature stability assessment
- Overfitting prevention strategies
- Performance impact measurement

**Production Readiness:**
- Feature computation efficiency
- Memory usage optimization
- Real-time scoring considerations
- Feature pipeline deployment strategy
"""

@mcp.prompt()
def visualization_storytelling_strategy(
    dataset_name: str,
    analysis_objectives: str,
    target_audience: str,
    key_insights: str = "",
    visualization_tools: str = "matplotlib,seaborn,plotly",
    interactivity_level: str = "moderate"
) -> str:
    """Data storytelling and visualization strategy with audience focus"""
    return f"""
Visualization storytelling strategy for: **{dataset_name}**

**Objectives:** {analysis_objectives}
**Audience:** {target_audience}
**Key Insights:** {key_insights}
**Tools:** {visualization_tools}
**Interactivity:** {interactivity_level}

**Audience-Driven Visualization Framework:**

1. **Executive Dashboard (C-Level)**
   - High-level KPI visualizations
   - Trend and performance indicators
   - Risk assessment visuals
   - ROI and business impact metrics

2. **Technical Analysis (Data Scientists/Analysts)**
   - Statistical distribution plots
   - Correlation matrices and heatmaps
   - Model diagnostic visualizations
   - Feature importance and SHAP plots

3. **Operational Users (Domain Experts)**
   - Process flow visualizations
   - Performance monitoring dashboards
   - Exception and anomaly highlighting
   - Actionable insight presentations

**Visualization Hierarchy:**

1. **Univariate Analysis**
   - Enhanced histograms with statistical annotations
   - Box plots with outlier identification
   - Violin plots for distribution shape
   - Q-Q plots for normality assessment

2. **Bivariate Relationships**
   - Scatter plots with regression lines and confidence bands
   - Cross-tabulation heatmaps
   - Correlation scatter matrix
   - Partial dependence plots

3. **Multivariate Insights**
   - Parallel coordinates plots
   - 3D scatter plots with projections
   - Dimensionality reduction visualizations
   - Network graphs for relationships

4. **Temporal Patterns**
   - Time series plots with decomposition
   - Seasonal heatmaps
   - Change point detection visuals
   - Forecasting plots with uncertainty

**Interactive Features:**
- Drill-down capabilities
- Filter and slice functionality
- Brushing and linking between plots
- Real-time data updates
- Tooltip information enhancement

**Storytelling Elements:**
- Narrative flow design
- Progressive disclosure of complexity
- Insight annotation and callouts
- Comparative analysis layouts
- Before/after transformation views

**Technical Implementation:**
- Responsive design considerations
- Performance optimization for large datasets
- Color accessibility and universal design
- Export and sharing functionality
- Integration with reporting systems

**Quality Assurance:**
- Chart junk elimination
- Cognitive load assessment
- Color scheme optimization
- Font and sizing standards
- Cross-platform compatibility testing
"""

# =============================================================================
# DOMAIN-SPECIFIC AND SPECIALIZED PROMPTS
# =============================================================================

@mcp.prompt()
def geospatial_data_eda(
    dataset_name: str,
    location_columns: str,
    value_columns: str,
    coordinate_system: str = "auto-detect",
    analysis_scale: str = "multi-scale"
) -> str:
    """Specialized EDA for geospatial data"""
    return f"""
Geospatial EDA for: **{dataset_name}**

**Location Data:** {location_columns}
**Values:** {value_columns}
**Coordinate System:** {coordinate_system}
**Analysis Scale:** {analysis_scale}

**Geospatial Analysis Framework:**

1. **Coordinate System Validation**
   - CRS identification and validation
   - Coordinate range and bounds checking
   - Projection accuracy assessment
   - Geographic vs projected coordinate handling

2. **Spatial Distribution Analysis**
   - Point pattern analysis (clustering, dispersion)
   - Density estimation (kernel density, hexbin)
   - Spatial autocorrelation (Moran's I, Geary's C)
   - Hotspot and coldspot identification

3. **Spatial Relationships**
   - Distance matrix analysis
   - Neighbor identification and weighting
   - Spatial lag and error modeling
   - Boundary effects assessment

4. **Multi-Scale Analysis**
   - Global vs local spatial patterns
   - Scale-dependent clustering
   - Aggregation effects evaluation
   - MAUP (Modifiable Areal Unit Problem) assessment

5. **Temporal-Spatial Patterns**
   - Spatiotemporal clustering
   - Movement pattern analysis
   - Seasonal spatial variations
   - Migration and flow patterns

**Specialized Visualizations:**
- Choropleth maps with statistical classification
- Point density and heat maps
- Spatial autocorrelation plots
- 3D surface visualizations
- Interactive web maps

**Quality Assessment:**
- Coordinate accuracy validation
- Missing location handling
- Spatial outlier detection
- Administrative boundary alignment
"""

@mcp.prompt()
def text_data_eda_nlp(
    dataset_name: str,
    text_columns: str,
    language: str = "auto-detect",
    analysis_depth: str = "comprehensive",
    domain_specific: str = ""
) -> str:
    """Text data EDA with NLP analysis"""
    return f"""
Text Data EDA for: **{dataset_name}**

**Text Columns:** {text_columns}
**Language:** {language}
**Analysis Depth:** {analysis_depth}
**Domain Context:** {domain_specific}

**Text Analysis Framework:**

1. **Basic Text Statistics**
   - Document length distributions
   - Vocabulary size and richness
   - Character encoding validation
   - Language detection confidence

2. **Lexical Analysis**
   - Token frequency distributions
   - Zipf's law compliance
   - Hapax legomena analysis
   - Type-token ratio calculation

3. **Linguistic Features**
   - Part-of-speech distribution
   - Named entity recognition
   - Sentiment polarity analysis
   - Readability metrics (Flesch-Kincaid, etc.)

4. **Semantic Analysis**
   - Topic modeling (LDA, BERTopic)
   - Word embeddings visualization
   - Semantic similarity analysis
   - Concept clustering

5. **Text Quality Assessment**
   - Spam and noise detection
   - Duplicate content identification
   - Language mixing detection
   - OCR error patterns

**Preprocessing Recommendations:**
- Tokenization strategy
- Stop word handling
- Stemming vs lemmatization
- Case normalization
- Special character handling

**Feature Engineering:**
- N-gram extraction
- TF-IDF vectorization
- Word embedding features
- Document similarity metrics
"""

@mcp.prompt()
def model_readiness_assessment(
    dataset_name: str,
    target_variable: str,
    model_types: str,
    performance_requirements: str = "",
    deployment_constraints: str = ""
) -> str:
    """Assess dataset readiness for machine learning modeling"""
    return f"""
ML Model Readiness Assessment for: **{dataset_name}**

**Target:** {target_variable}
**Model Types:** {model_types}
**Performance Requirements:** {performance_requirements}
**Deployment Constraints:** {deployment_constraints}

**Model Readiness Framework:**

1. **Data Quality for ML**
   - Missing data impact on model performance
   - Outlier sensitivity by model type
   - Feature scaling requirements
   - Category encoding readiness

2. **Dataset Size and Complexity**
   - Sample size adequacy for model complexity
   - Feature-to-sample ratio assessment
   - Class balance evaluation
   - Curse of dimensionality risk

3. **Feature Quality Assessment**
   - Information leakage detection
   - Multicollinearity impact
   - Feature importance preliminary ranking
   - Feature engineering completeness

4. **Target Variable Analysis**
   - Distribution suitability for model type
   - Class separation quality
   - Regression target properties
   - Threshold optimization needs

5. **Cross-Validation Strategy**
   - Appropriate CV method selection
   - Stratification requirements
   - Time series CV considerations
   - Group-based splitting needs

6. **Baseline Performance Establishment**
   - Naive model benchmarks
   - Random prediction performance
   - Domain expert performance targets
   - Business requirement alignment

**Model-Specific Readiness:**
- Linear models: assumptions validation
- Tree-based: feature interaction readiness
- Neural networks: scaling and normalization
- Ensemble methods: diversity assessment

**Production Considerations:**
- Real-time scoring feasibility
- Model interpretability requirements
- Feature computation latency
- Model drift monitoring setup
"""

# =============================================================================
# REPORTING AND AUTOMATION PROMPTS
# =============================================================================

@mcp.prompt()
def automated_eda_pipeline(
    dataset_info: str,
    analysis_goals: str,
    automation_level: str = "semi-automated",
    report_format: str = "html",
    stakeholder_requirements: str = ""
) -> str:
    """Generate automated EDA pipeline with customizable reporting"""
    return f"""
Automated EDA Pipeline Design for: {dataset_info}

**Analysis Goals:** {analysis_goals}
**Automation Level:** {automation_level}
**Report Format:** {report_format}
**Stakeholder Requirements:** {stakeholder_requirements}

**Pipeline Architecture:**

1. **Data Ingestion Module**
   - Multi-format data loading (CSV, Excel, Parquet, JSON)
   - Schema validation and type inference
   - Data quality initial assessment
   - Memory optimization strategies

2. **Analysis Orchestration**
   - Configurable analysis workflow
   - Parallel processing optimization
   - Error handling and recovery
   - Progress tracking and logging

3. **Automated Analysis Components**
   - Statistical profiling engine
   - Visualization generation system
   - Quality assessment automation
   - Pattern detection algorithms

4. **Reporting Engine**
   - Template-based report generation
   - Interactive dashboard creation
   - Multi-format output (HTML, PDF, PowerPoint)
   - Stakeholder-specific views

5. **Quality Assurance**
   - Automated result validation
   - Statistical significance checking
   - Visualization quality assessment
   - Narrative consistency verification

**Configuration Management:**
- Analysis parameter templates
- Stakeholder preference profiles
- Domain-specific rule sets
- Performance optimization settings

**Extensibility Features:**
- Custom analysis plugin architecture
- User-defined quality rules
- Custom visualization templates
- Integration with external tools

**Deployment Options:**
- Local execution scripts
- Cloud-based pipeline deployment
- API service architecture
- Scheduled execution framework

**Python Implementation:**
- Object-oriented pipeline design
- Configuration file management
- Logging and monitoring integration
- Unit testing framework
- Documentation auto-generation
"""

@mcp.prompt()
def eda_quality_metrics_dashboard(
    analysis_results: str,
    quality_dimensions: str = "completeness,accuracy,timeliness,consistency",
    scoring_method: str = "weighted",
    benchmark_standards: str = "industry"
) -> str:
    """Create EDA quality metrics dashboard and scoring system"""
    return f"""
EDA Quality Metrics Dashboard for: {analysis_results}

**Quality Dimensions:** {quality_dimensions}
**Scoring Method:** {scoring_method}
**Benchmarks:** {benchmark_standards}

**Quality Scoring Framework:**

1. **Analysis Completeness Score**
   - Coverage of all relevant EDA components
   - Depth of statistical analysis
   - Visualization comprehensiveness
   - Documentation quality

2. **Accuracy and Reliability Score**
   - Statistical test appropriateness
   - Assumption validation completeness
   - Result reproducibility assessment
   - Cross-validation consistency

3. **Insight Quality Score**
   - Business relevance of findings
   - Actionability of recommendations
   - Statistical significance of patterns
   - Novel discovery identification

4. **Technical Quality Score**
   - Code quality and efficiency
   - Visualization best practices adherence
   - Error handling robustness
   - Performance optimization

**Dashboard Components:**
- Real-time quality score updates
- Dimension-wise progress tracking
- Comparison with benchmark standards
- Improvement recommendation engine

**Quality Gates:**
- Minimum quality thresholds
- Automated quality validation
- Stakeholder approval workflows
- Continuous improvement tracking

**Reporting Features:**
- Executive quality summary
- Technical quality assessment
- Improvement action plans
- Quality trend analysis

**Integration Capabilities:**
- CI/CD pipeline integration
- Quality monitoring alerts
- Automated quality reporting
- Stakeholder notification system
"""
# =============================================================================
# FILE READING TOOLS - Add these to your existing server.py
# =============================================================================

import os
import pandas as pd
from pathlib import Path

@mcp.tool()
def read_text_file(file_path: str) -> str:
    """
    Read the contents of a text file from the filesystem.
    
    Args:
        file_path: Path to the text file to read
        
    Returns:
        String containing the file contents
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If there are insufficient permissions to read the file
        UnicodeDecodeError: If the file cannot be decoded as text
    """
    try:
        # Convert to Path object for better path handling
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist."
        
        # Check if it's actually a file (not a directory)
        if not path.is_file():
            return f"Error: '{file_path}' is not a file."
        
        # Read the file with different encodings if needed
        encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(path, 'r', encoding=encoding) as file:
                    content = file.read()
                
                # Return content with metadata
                file_info = {
                    'file_path': str(path.absolute()),
                    'file_size': path.stat().st_size,
                    'encoding_used': encoding,
                    'line_count': len(content.splitlines()),
                    'character_count': len(content)
                }
                
                return f"""File successfully read!

File Information:
- Path: {file_info['file_path']}
- Size: {file_info['file_size']} bytes
- Encoding: {file_info['encoding_used']}
- Lines: {file_info['line_count']}
- Characters: {file_info['character_count']}

Content:
{'='*50}
{content}
{'='*50}"""
                
            except UnicodeDecodeError:
                continue
        
        return f"Error: Could not decode file '{file_path}' with any standard encoding."
        
    except PermissionError:
        return f"Error: Permission denied reading file '{file_path}'."
    except Exception as e:
        return f"Error reading file '{file_path}': {str(e)}"

@mcp.tool()
def read_csv_file(file_path: str, preview_rows: int = 10, encoding: str = "utf-8") -> str:
    """
    Read and analyze a CSV file from the filesystem.
    
    Args:
        file_path: Path to the CSV file to read
        preview_rows: Number of rows to show in preview (default: 10)
        encoding: File encoding (default: utf-8)
        
    Returns:
        String containing CSV analysis and preview
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        pandas.errors.EmptyDataError: If the CSV is empty
        pandas.errors.ParserError: If the CSV format is invalid
    """
    try:
        # Convert to Path object
        path = Path(file_path)
        
        # Check if file exists
        if not path.exists():
            return f"Error: File '{file_path}' does not exist."
        
        # Check if it's actually a file
        if not path.is_file():
            return f"Error: '{file_path}' is not a file."
        
        # Try different encodings if the specified one fails
        encodings_to_try = [encoding, 'utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
        
        df = None
        encoding_used = None
        
        for enc in encodings_to_try:
            try:
                # Read CSV with pandas
                df = pd.read_csv(path, encoding=enc)
                encoding_used = enc
                break
            except UnicodeDecodeError:
                continue
            except pd.errors.EmptyDataError:
                return f"Error: CSV file '{file_path}' is empty."
            except pd.errors.ParserError as e:
                return f"Error: Could not parse CSV file '{file_path}': {str(e)}"
        
        if df is None:
            return f"Error: Could not read CSV file '{file_path}' with any standard encoding."
        
        # Basic analysis
        file_info = {
            'file_path': str(path.absolute()),
            'file_size': path.stat().st_size,
            'encoding_used': encoding_used,
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': df.columns.tolist(),
            'data_types': df.dtypes.to_dict(),
            'memory_usage': df.memory_usage(deep=True).sum(),
            'missing_values': df.isnull().sum().to_dict()
        }
        
        # Generate summary
        result = f"""CSV File Successfully Loaded!

File Information:
- Path: {file_info['file_path']}
- Size: {file_info['file_size']} bytes
- Encoding: {file_info['encoding_used']}
- Dimensions: {file_info['rows']} rows × {file_info['columns']} columns
- Memory Usage: {file_info['memory_usage']:,} bytes

Columns and Data Types:
{'-'*40}"""
        
        for col, dtype in file_info['data_types'].items():
            missing = file_info['missing_values'][col]
            missing_pct = (missing / file_info['rows'] * 100) if file_info['rows'] > 0 else 0
            result += f"\n- {col}: {dtype} (Missing: {missing}/{file_info['rows']} = {missing_pct:.1f}%)"
        
        # Add data preview
        result += f"\n\nData Preview (First {min(preview_rows, len(df))} rows):\n{'='*60}\n"
        
        if len(df) > 0:
            # Format the preview nicely
            preview_df = df.head(preview_rows)
            result += preview_df.to_string(max_cols=None, max_colwidth=50)
        else:
            result += "No data rows found in CSV."
        
        # Add basic statistics for numeric columns
        numeric_cols = df.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            result += f"\n\nNumeric Columns Summary:\n{'-'*40}\n"
            result += df[numeric_cols].describe().to_string()
        
        result += f"\n{'='*60}"
        
        return result
        
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except PermissionError:
        return f"Error: Permission denied reading file '{file_path}'."
    except Exception as e:
        return f"Error reading CSV file '{file_path}': {str(e)}"

@mcp.tool()
def list_files_in_directory(directory_path: str, file_extension: str = None) -> str:
    """
    List files in a directory, optionally filtered by extension.
    
    Args:
        directory_path: Path to the directory to list
        file_extension: Optional file extension filter (e.g., '.txt', '.csv')
        
    Returns:
        String containing list of files with metadata
    """
    try:
        # Convert to Path object
        path = Path(directory_path)
        
        # Check if directory exists
        if not path.exists():
            return f"Error: Directory '{directory_path}' does not exist."
        
        # Check if it's actually a directory
        if not path.is_dir():
            return f"Error: '{directory_path}' is not a directory."
        
        # Get files
        if file_extension:
            files = list(path.glob(f"*{file_extension}"))
            filter_msg = f" (filtered by extension: {file_extension})"
        else:
            files = [f for f in path.iterdir() if f.is_file()]
            filter_msg = ""
        
        if not files:
            return f"No files found in directory '{directory_path}'{filter_msg}."
        
        # Sort files by name
        files.sort(key=lambda x: x.name.lower())
        
        result = f"Files in directory: {path.absolute()}{filter_msg}\n"
        result += f"Found {len(files)} file(s)\n"
        result += "="*60 + "\n"
        
        for file in files:
            try:
                stat = file.stat()
                size = stat.st_size
                
                # Format size nicely
                if size < 1024:
                    size_str = f"{size} B"
                elif size < 1024*1024:
                    size_str = f"{size/1024:.1f} KB"
                else:
                    size_str = f"{size/(1024*1024):.1f} MB"
                
                result += f"📄 {file.name:<40} {size_str:>10}\n"
                
            except Exception as e:
                result += f"📄 {file.name:<40} (Error reading metadata)\n"
        
        result += "="*60
        
        return result
        
    except PermissionError:
        return f"Error: Permission denied accessing directory '{directory_path}'."
    except Exception as e:
        return f"Error listing directory '{directory_path}': {str(e)}"

@mcp.tool()
def get_file_info(file_path: str) -> str:
    """
    Get detailed information about a file.
    
    Args:
        file_path: Path to the file to analyze
        
    Returns:
        String containing detailed file information
    """
    try:
        path = Path(file_path)
        
        if not path.exists():
            return f"Error: File '{file_path}' does not exist."
        
        if not path.is_file():
            return f"Error: '{file_path}' is not a file."
        
        stat = path.stat()
        
        # Format size
        size = stat.st_size
        if size < 1024:
            size_str = f"{size} bytes"
        elif size < 1024*1024:
            size_str = f"{size/1024:.1f} KB ({size:,} bytes)"
        else:
            size_str = f"{size/(1024*1024):.1f} MB ({size:,} bytes)"
        
        # Get file extension and type
        extension = path.suffix.lower()
        file_type = "Unknown"
        
        if extension in ['.txt', '.md', '.log']:
            file_type = "Text file"
        elif extension in ['.csv']:
            file_type = "CSV (Comma-Separated Values)"
        elif extension in ['.json']:
            file_type = "JSON data"
        elif extension in ['.xml']:
            file_type = "XML data"
        elif extension in ['.xlsx', '.xls']:
            file_type = "Excel spreadsheet"
        
        result = f"""File Information: {path.name}
{'='*50}
Full Path: {path.absolute()}
Directory: {path.parent}
File Name: {path.name}
Extension: {extension if extension else 'None'}
File Type: {file_type}
Size: {size_str}
Created: {pd.Timestamp.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}
Modified: {pd.Timestamp.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}
Accessed: {pd.Timestamp.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S')}
{'='*50}"""
        
        return result
        
    except Exception as e:
        return f"Error getting file info for '{file_path}': {str(e)}"
if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
