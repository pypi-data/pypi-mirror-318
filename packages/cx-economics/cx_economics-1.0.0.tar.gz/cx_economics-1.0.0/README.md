
# cx_economics

`cx_economics` is a Python library designed to analyze the economics of customer experience (CX) using Net Promoter Score (NPS) and revenue data. It supports both B2C and B2B scenarios, providing insights into CX transitions and their financial implications.

## Features

1. Generate synthetic customer or account data with pre- and post-NPS scores and revenue.
2. Compute Net Promoter Score (NPS) for pre- and post-periods.
3. Calculate revenue metrics (average, median) for pre- and post-periods.
4. Analyze customer transitions across NPS categories (Promoter, Passive, Detractor).
5. Support for B2C and B2B survey types with appropriate data aggregation.

## Installation

You can install `cx_economics` via pip:

```bash
pip install cx_economics
```

## Quick Start

### 1. Import and Initialize the Library

```python
from cx_economics import CXEconomics

# Initialize the CXEconomics class with a seed for reproducibility
cx = CXEconomics(seed=42)
```

### 2. Generate Sample Data

```python
# Generate 1000 customer records for a B2C scenario
data = cx.generate_sample_data(num_customers=1000, b2b=False)
print("Sample Data:")
print(data.head())
```

### 3. Analyze CX Economics

```python
# Analyze CX economics for a B2C survey
stats = cx.analyze_cx_economics(survey_type='B2C')
print("Analysis Statistics:")
print(stats)
```

### 4. Calculate Transition Statistics

```python
# Calculate transition statistics
transitions = cx.get_transition_stats()
print("CX Transitions (DataFrame):")
print(transitions)
```

## Use Cases

1. **Identify CX Trends:** Compare pre- and post-NPS scores to track improvements or declines in customer satisfaction.
2. **Revenue Impact Analysis:** Understand the financial implications of changes in customer loyalty.
3. **Transition Analysis:** Gain insights into how customers move between loyalty categories and their associated revenue impact.
4. **Support for B2B Scenarios:** Aggregate data at the account level for business-to-business CX analysis.

## License

This library is licensed under the MIT License.
