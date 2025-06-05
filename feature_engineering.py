import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_age_groups(df):
    """Create age groups based on meaningful categories."""
    bins = [0, 25, 35, 45, 55, 65, 100]
    labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
    return df

def create_income_ratios(df):
    """Create income-related ratio features."""
    # Capital gain to loss ratio (handling division by zero)
    df['capital_gain_loss_ratio'] = df['capital-gain'] / (df['capital-loss'].replace(0, 1))
    
    # Hours worked to capital gain ratio
    df['hours_to_gain_ratio'] = df['hours-per-week'] / (df['capital-gain'].replace(0, 1))
    
    # Normalize ratios using log transformation
    for col in ['capital_gain_loss_ratio', 'hours_to_gain_ratio']:
        df[col] = np.log1p(df[col])
    
    return df

def create_work_life_indicators(df):
    """Create work-life balance related indicators."""
    # Standard work week indicator (40 hours)
    df['standard_work_week'] = (df['hours-per-week'] == 40).astype(int)
    
    # Overwork indicator (> 45 hours)
    df['overwork'] = (df['hours-per-week'] > 45).astype(int)
    
    # Part-time indicator (< 35 hours)
    df['part_time'] = (df['hours-per-week'] < 35).astype(int)
    
    # Work intensity score (normalized hours)
    df['work_intensity'] = (df['hours-per-week'] - df['hours-per-week'].mean()) / df['hours-per-week'].std()
    
    return df

def plot_feature_distributions(df):
    """Plot distributions of engineered features."""
    plt.figure(figsize=(15, 10))
    
    # Age group distribution
    plt.subplot(2, 2, 1)
    sns.countplot(data=df, x='age_group', hue='income')
    plt.title('Income Distribution by Age Group')
    plt.xticks(rotation=45)
    
    # Work-life indicators
    plt.subplot(2, 2, 2)
    work_status = df[['standard_work_week', 'overwork', 'part_time']].sum()
    work_status.plot(kind='bar')
    plt.title('Distribution of Work Patterns')
    
    # Capital gain-loss ratio distribution
    plt.subplot(2, 2, 3)
    sns.boxplot(data=df, x='income', y='capital_gain_loss_ratio')
    plt.title('Capital Gain-Loss Ratio by Income')
    
    # Work intensity distribution
    plt.subplot(2, 2, 4)
    sns.kdeplot(data=df, x='work_intensity', hue='income')
    plt.title('Work Intensity Distribution by Income')
    
    plt.tight_layout()
    return plt.gcf()
