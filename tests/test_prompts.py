#!/usr/bin/env python3
"""
Test suite for EDA Assistant MCP prompts
"""

import pytest
from server import (
    initial_data_exploration,
    advanced_statistical_analysis,
    data_quality_comprehensive_audit,
    correlation_and_relationships,
    time_series_comprehensive_eda,
    categorical_deep_dive_analysis,
    outlier_anomaly_comprehensive_analysis,
    feature_engineering_advanced_strategies,
    visualization_storytelling_strategy,
    model_readiness_assessment,
    automated_eda_pipeline
)


class TestCoreDataExplorationPrompts:
    """Test core data exploration prompts"""
    
    def test_initial_data_exploration_basic(self):
        """Test basic initial data exploration prompt"""
        result = initial_data_exploration(
            dataset_info="Test e-commerce dataset",
            columns="customer_id, order_date, amount",
            business_context="Customer behavior analysis"
        )
        
        assert "Test e-commerce dataset" in result
        assert "Customer behavior analysis" in result
        assert "Dataset Overview & Structure" in result
        assert "Data Quality First Pass" in result
        assert "Variable Classification" in result
        assert len(result) > 500  # Ensure comprehensive output
    
    def test_initial_data_exploration_with_sample_data(self):
        """Test initial data exploration with sample data"""
        result = initial_data_exploration(
            dataset_info="Sales dataset",
            columns="product, price, quantity",
            sample_data="Product A, 19.99, 5",
            data_types="object, float64, int64"
        )
        
        assert "Sales dataset" in result
        assert "Product A, 19.99, 5" in result
        assert "object, float64, int64" in result
    
    def test_advanced_statistical_analysis(self):
        """Test advanced statistical analysis prompt"""
        result = advanced_statistical_analysis(
            dataset_name="Customer Analytics",
            numerical_columns="age, income, spend",
            categorical_columns="gender, segment",
            target_variable="lifetime_value"
        )
        
        assert "Customer Analytics" in result
        assert "age, income, spend" in result
        assert "gender, segment" in result
        assert "lifetime_value" in result
        assert "Descriptive Statistics Deep Dive" in result
        assert "Distribution Analysis" in result
        assert "Hypothesis Testing Framework" in result
    
    def test_data_quality_comprehensive_audit(self):
        """Test data quality audit prompt"""
        result = data_quality_comprehensive_audit(
            dataset_info="Transaction dataset with quality issues",
            quality_dimensions="completeness,accuracy,consistency",
            severity_levels="critical,high,medium"
        )
        
        assert "Transaction dataset with quality issues" in result
        assert "completeness,accuracy,consistency" in result
        assert "Completeness Analysis" in result
        assert "Accuracy Assessment" in result
        assert "Consistency Evaluation" in result
        assert "Remediation Action Plan" in result


class TestSpecializedAnalysisPrompts:
    """Test specialized analysis prompts"""
    
    def test_correlation_and_relationships(self):
        """Test correlation analysis prompt"""
        result = correlation_and_relationships(
            dataset_name="Marketing Campaign Data",
            variables="email_opens, clicks, conversions",
            target_variable="revenue",
            correlation_methods="pearson,spearman"
        )
        
        assert "Marketing Campaign Data" in result
        assert "email_opens, clicks, conversions" in result
        assert "revenue" in result
        assert "Multiple Correlation Methods" in result
        assert "Non-Linear Relationship Detection" in result
    
    def test_time_series_comprehensive_eda(self):
        """Test time series EDA prompt"""
        result = time_series_comprehensive_eda(
            dataset_name="Daily Sales Data",
            date_column="sale_date",
            value_columns="revenue, units_sold",
            frequency="daily"
        )
        
        assert "Daily Sales Data" in result
        assert "sale_date" in result
        assert "revenue, units_sold" in result
        assert "daily" in result
        assert "Temporal Structure Analysis" in result
        assert "Decomposition Analysis" in result
        assert "Stationarity Assessment" in result
    
    def test_categorical_deep_dive_analysis(self):
        """Test categorical analysis prompt"""
        result = categorical_deep_dive_analysis(
            dataset_name="Customer Segmentation",
            categorical_variables="region, product_category, customer_type",
            target_variable="churn",
            cardinality_thresholds="low:<5, medium:5-20, high:>20"
        )
        
        assert "Customer Segmentation" in result
        assert "region, product_category, customer_type" in result
        assert "churn" in result
        assert "Cardinality Assessment" in result
        assert "Encoding Strategy Optimization" in result
    
    def test_outlier_anomaly_comprehensive_analysis(self):
        """Test outlier detection prompt"""
        result = outlier_anomaly_comprehensive_analysis(
            dataset_name="Financial Transactions",
            variables="amount, frequency, account_age",
            methods="statistical,distance,density",
            domain_context="Fraud detection context"
        )
        
        assert "Financial Transactions" in result
        assert "amount, frequency, account_age" in result
        assert "Fraud detection context" in result
        assert "Statistical Methods" in result
        assert "Distance-Based Methods" in result
        assert "Machine Learning Methods" in result
    
    def test_feature_engineering_advanced_strategies(self):
        """Test feature engineering prompt"""
        result = feature_engineering_advanced_strategies(
            dataset_name="Predictive Modeling Dataset",
            current_features="age, income, tenure",
            target_variable="response",
            ml_objective="classification"
        )
        
        assert "Predictive Modeling Dataset" in result
        assert "age, income, tenure" in result
        assert "response" in result
        assert "classification" in result
        assert "Mathematical Transformations" in result
        assert "Feature Selection Integration" in result


class TestVisualizationPrompts:
    """Test visualization and storytelling prompts"""
    
    def test_visualization_storytelling_strategy(self):
        """Test visualization strategy prompt"""
        result = visualization_storytelling_strategy(
            dataset_name="Business Intelligence Dashboard",
            analysis_objectives="Performance monitoring and insights",
            target_audience="C-level executives",
            key_insights="Revenue growth, cost optimization"
        )
        
        assert "Business Intelligence Dashboard" in result
        assert "Performance monitoring and insights" in result
        assert "C-level executives" in result
        assert "Revenue growth, cost optimization" in result
        assert "Audience-Driven Visualization Framework" in result
        assert "Executive Dashboard (C-Level)" in result


class TestModelPreparationPrompts:
    """Test model preparation prompts"""
    
    def test_model_readiness_assessment(self):
        """Test model readiness assessment prompt"""
        result = model_readiness_assessment(
            dataset_name="ML Training Dataset",
            target_variable="conversion",
            model_types="logistic_regression,random_forest",
            performance_requirements="AUC > 0.8"
        )
        
        assert "ML Training Dataset" in result
        assert "conversion" in result
        assert "logistic_regression,random_forest" in result
        assert "AUC > 0.8" in result
        assert "Data Quality for ML" in result
        assert "Model-Specific Readiness" in result
    
    def test_automated_eda_pipeline(self):
        """Test automated EDA pipeline prompt"""
        result = automated_eda_pipeline(
            dataset_info="Automated analysis dataset",
            analysis_goals="Comprehensive profiling and insights",
            automation_level="fully-automated",
            report_format="html"
        )
        
        assert "Automated analysis dataset" in result
        assert "Comprehensive profiling and insights" in result
        assert "fully-automated" in result
        assert "html" in result
        assert "Pipeline Architecture" in result
        assert "Analysis Orchestration" in result


class TestPromptParameterValidation:
    """Test prompt parameter validation and edge cases"""
    
    def test_empty_parameters(self):
        """Test prompts with minimal parameters"""
        result = initial_data_exploration(
            dataset_info="Minimal dataset info"
        )
        
        assert "Minimal dataset info" in result
        assert len(result) > 100  # Should still generate comprehensive output
    
    def test_long_parameters(self):
        """Test prompts with very long parameters"""
        long_columns = ", ".join([f"column_{i}" for i in range(50)])
        
        result = initial_data_exploration(
            dataset_info="Dataset with many columns",
            columns=long_columns
        )
        
        assert "Dataset with many columns" in result
        assert "column_0" in result
        assert "column_49" in result
    
    def test_special_characters_in_parameters(self):
        """Test prompts with special characters"""
        result = initial_data_exploration(
            dataset_info="Dataset with special chars: !@#$%^&*()",
            columns="col_1, col-2, col@3, col#4"
        )
        
        assert "Dataset with special chars: !@#$%^&*()" in result
        assert "col_1, col-2, col@3, col#4" in result


if __name__ == "__main__":
    pytest.main([__file__])