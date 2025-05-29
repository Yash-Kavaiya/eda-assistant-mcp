#!/usr/bin/env python3
"""
Basic usage examples for EDA Assistant MCP

This script demonstrates how to use the various prompts and tools
available in the EDA Assistant MCP server.
"""

import sys
import os

# Add the parent directory to the path to import server
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import (
    initial_data_exploration,
    advanced_statistical_analysis,
    correlation_and_relationships,
    visualization_storytelling_strategy,
    read_csv_file,
    list_files_in_directory
)


def example_initial_exploration():
    """
    Example: Basic data exploration for an e-commerce dataset
    """
    print("\n" + "="*80)
    print("EXAMPLE 1: Initial Data Exploration")
    print("="*80)
    
    prompt = initial_data_exploration(
        dataset_info="E-commerce customer transaction dataset (Jan-Dec 2024)",
        columns="customer_id, transaction_date, product_category, amount, payment_method, customer_segment",
        business_context="Understanding customer behavior patterns for targeted marketing campaigns",
        sample_data="12345, 2024-01-15, Electronics, 299.99, Credit Card, Premium",
        data_types="int64, datetime64, object, float64, object, object"
    )
    
    print(prompt)


def example_statistical_analysis():
    """
    Example: Advanced statistical analysis for sales performance
    """
    print("\n" + "="*80)
    print("EXAMPLE 2: Advanced Statistical Analysis")
    print("="*80)
    
    prompt = advanced_statistical_analysis(
        dataset_name="Quarterly Sales Performance Dataset",
        numerical_columns="revenue, units_sold, profit_margin, customer_acquisition_cost",
        categorical_columns="region, product_line, sales_channel, quarter",
        target_variable="quarterly_growth_rate",
        analysis_depth="comprehensive",
        statistical_tests="auto-select"
    )
    
    print(prompt)


def example_correlation_analysis():
    """
    Example: Correlation analysis for marketing campaigns
    """
    print("\n" + "="*80)
    print("EXAMPLE 3: Correlation and Relationships Analysis")
    print("="*80)
    
    prompt = correlation_and_relationships(
        dataset_name="Digital Marketing Campaign Performance",
        variables="ad_spend, impressions, clicks, conversions, email_opens, social_engagement",
        target_variable="roi",
        correlation_methods="pearson,spearman,kendall",
        relationship_types="linear,monotonic,non-linear"
    )
    
    print(prompt)


def example_visualization_strategy():
    """
    Example: Visualization strategy for executive dashboard
    """
    print("\n" + "="*80)
    print("EXAMPLE 4: Visualization and Storytelling Strategy")
    print("="*80)
    
    prompt = visualization_storytelling_strategy(
        dataset_name="Company Performance Dashboard Data",
        analysis_objectives="Monthly performance tracking, trend identification, and strategic insights",
        target_audience="C-level executives and board members",
        key_insights="Revenue growth acceleration, cost optimization opportunities, market expansion potential",
        visualization_tools="plotly,tableau",
        interactivity_level="high"
    )
    
    print(prompt)


def example_file_operations():
    """
    Example: File operation tools demonstration
    """
    print("\n" + "="*80)
    print("EXAMPLE 5: File Operations")
    print("="*80)
    
    # List current directory files
    print("Listing files in current directory:")
    print("-" * 40)
    current_dir_files = list_files_in_directory(".", ".py")
    print(current_dir_files)
    
    # Create a sample CSV for demonstration
    sample_csv_content = """customer_id,age,annual_income,spending_score
1,23,15000,39
2,24,16000,81
3,25,17000,6
4,26,18000,77
5,27,19000,40
6,28,20000,76
7,29,21000,94
8,30,22000,3
9,31,23000,72
10,32,24000,27"""
    
    # Write sample CSV
    sample_file = "sample_data.csv"
    with open(sample_file, 'w') as f:
        f.write(sample_csv_content)
    
    print(f"\nReading sample CSV file: {sample_file}")
    print("-" * 40)
    csv_analysis = read_csv_file(sample_file, preview_rows=5)
    print(csv_analysis)
    
    # Clean up
    os.remove(sample_file)


def example_comprehensive_workflow():
    """
    Example: Comprehensive EDA workflow demonstration
    """
    print("\n" + "="*80)
    print("EXAMPLE 6: Comprehensive EDA Workflow")
    print("="*80)
    
    # Step 1: Initial exploration
    print("\n🔍 STEP 1: Initial Data Exploration")
    print("-" * 50)
    
    initial_prompt = initial_data_exploration(
        dataset_info="Customer churn prediction dataset - telecom company",
        columns="customer_id, tenure, monthly_charges, total_charges, contract_type, churn",
        business_context="Reducing customer churn and improving retention strategies"
    )
    
    # Print just the summary part
    lines = initial_prompt.split('\n')
    for i, line in enumerate(lines[:20]):  # First 20 lines
        print(line)
    print("... (truncated for brevity)")
    
    # Step 2: Statistical analysis
    print("\n📊 STEP 2: Statistical Analysis")
    print("-" * 50)
    
    statistical_prompt = advanced_statistical_analysis(
        dataset_name="Telecom Customer Churn Dataset",
        numerical_columns="tenure, monthly_charges, total_charges",
        categorical_columns="contract_type, payment_method, internet_service",
        target_variable="churn"
    )
    
    # Print summary
    lines = statistical_prompt.split('\n')
    for i, line in enumerate(lines[:15]):
        print(line)
    print("... (truncated for brevity)")
    
    # Step 3: Visualization strategy
    print("\n🎨 STEP 3: Visualization Strategy")
    print("-" * 50)
    
    viz_prompt = visualization_storytelling_strategy(
        dataset_name="Churn Analysis Dashboard",
        analysis_objectives="Identify churn patterns and present actionable insights",
        target_audience="Customer success team and product managers",
        key_insights="High-risk customer segments, retention opportunity areas"
    )
    
    # Print summary
    lines = viz_prompt.split('\n')
    for i, line in enumerate(lines[:15]):
        print(line)
    print("... (truncated for brevity)")
    
    print("\n✅ Comprehensive EDA workflow complete!")
    print("Each step provides detailed guidance for thorough analysis.")


def main():
    """
    Run all examples
    """
    print("EDA Assistant MCP - Usage Examples")
    print("=" * 80)
    print("This script demonstrates various prompts and tools available in the EDA Assistant.")
    print("Each example shows how to use different analysis capabilities.")
    
    try:
        # Run individual examples
        example_initial_exploration()
        example_statistical_analysis()
        example_correlation_analysis()
        example_visualization_strategy()
        example_file_operations()
        
        # Run comprehensive workflow
        example_comprehensive_workflow()
        
        print("\n" + "="*80)
        print("🎉 ALL EXAMPLES COMPLETED SUCCESSFULLY!")
        print("="*80)
        print("\nNext steps:")
        print("1. Modify the examples with your own dataset information")
        print("2. Use the generated prompts with your preferred AI assistant")
        print("3. Combine multiple prompts for comprehensive analysis")
        print("4. Explore additional prompts available in server.py")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()