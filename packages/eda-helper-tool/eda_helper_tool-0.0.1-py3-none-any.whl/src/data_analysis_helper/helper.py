import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


class EDA:
    """
    A class to perform exploratory data analysis (EDA) on a pandas DataFrame.
    """

    def __init__(self, df):
        """
        Initialize with the dataframe to perform EDA on.
        
        Parameters:
        df (pandas.DataFrame): The dataframe containing the data.
        """
        self.df = df

    def univariate_analysis(self, col_name):
        """
        Perform univariate analysis on a numerical column in the DataFrame.
        Prints statistical summary, remarks, and conclusions.
        """
        # Step 1: Describe the column (Descriptive statistics)
        description = self.df[col_name].describe()
        count = description['count']
        mean = description['mean']
        std = description['std']
        min_val = description['min']
        p25 = description['25%']
        p50 = description['50%']
        p75 = description['75%']
        max_val = description['max']
        
        print(f"\nUnivariate Analysis for '{col_name}':\n")
        print(description)
        
        # Step 2: Remarks based on the descriptive statistics
        remarks = []
        if min_val < 1:  # This is an example of detecting a potential issue (e.g., ages under 1 might indicate data errors)
            remarks.append(f"Min value is {min_val}. There might be children or data entry issues.")
        
        if p25 < (mean - std) and p75 > (mean + std):
            remarks.append(f"Most data points are spread around the mean value of {mean:.2f}.")
        
        if max_val > 70:
            remarks.append(f"Max value is {max_val}. Some values are potentially outliers.")
        
        if len(remarks) == 0:
            remarks.append("Data distribution appears normal.")
        
        print("\nRemarks:")
        for remark in remarks:
            print(f"- {remark}")
        
        # Step 3: Plotting (Histogram, KDE, Boxplot)
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        # Histogram
        self.df[col_name].plot(kind='hist', bins=20, ax=axes[0], color='skyblue', edgecolor='black')
        axes[0].set_title(f'{col_name} Histogram')
        
        # KDE Plot
        self.df[col_name].plot(kind='kde', ax=axes[1], color='orange')
        axes[1].set_title(f'{col_name} KDE Plot')

        # Boxplot
        self.df[col_name].plot(kind='box', ax=axes[2], color='green')
        axes[2].set_title(f'{col_name} Boxplot')
        
        plt.tight_layout()
        plt.show()
        
        # Step 4: Skewness check
        skewness = self.df[col_name].skew()
        print(f"\nSkewness of {col_name}: {skewness:.2f}")
        if abs(skewness) < 0.5:
            print(f"The data is approximately normally distributed (skewness near 0).")
        else:
            print(f"The data is skewed, suggesting a non-normal distribution.")
        
        # Step 5: Identify Outliers
        # Find outliers based on interquartile range (IQR)
        Q1 = self.df[col_name].quantile(0.25)
        Q3 = self.df[col_name].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = self.df[(self.df[col_name] < lower_bound) | (self.df[col_name] > upper_bound)]
        
        # Check if there are any outliers
        if not outliers.empty:
            print(f"\nOutliers detected: {len(outliers)}")
            print(f"Outliers are outside the range ({lower_bound:.2f}, {upper_bound:.2f})")
            # If there are outliers, print a random sample of 5
            print(outliers.sample(5))
        else:
            print("\nNo outliers detected.")

        # Step 6: Conclusion
        missing_data = self.df[col_name].isnull().sum()
        total_data = self.df[col_name].shape[0]
        missing_percentage = (missing_data / total_data) * 100
        
        conclusion = []
        conclusion.append(f"The data contains {missing_percentage:.2f}% missing values.")
        
        if missing_percentage > 5:
            conclusion.append("A significant percentage of the data is missing.")
        
        if len(outliers) > 0:
            conclusion.append("There are some outliers in the data.")
        
        if abs(skewness) < 0.5:
            conclusion.append("The data is approximately normally distributed.")
        else:
            conclusion.append("The data is not normally distributed.")
        
        print("\nConclusion:")
        for point in conclusion:
            print(f"- {point}")
        
        print("\n" + "="*50 + "\n")
    
    def categorical_univariate_analysis(self, col_name):
        """
        Perform univariate analysis on a categorical column in the DataFrame.
        Prints frequency counts, remarks, and conclusions.
        """
        # Step 1: Count the frequency of each category
        value_counts = self.df[col_name].value_counts()
        print(f"\nUnivariate Analysis for '{col_name}':\n")
        print(value_counts)
        
        # Step 2: Remarks based on the frequency distribution
        remarks = []
        total_count = self.df[col_name].shape[0]
        
        # Check if any category has more than 50% of the data
        for category, count in value_counts.items():
            percentage = (count / total_count) * 100
            if percentage > 50:
                remarks.append(f"More than 50% of the values are in the '{category}' category.")
        
        if len(remarks) == 0:
            remarks.append("The data is fairly distributed across categories.")
        
        print("\nRemarks:")
        for remark in remarks:
            print(f"- {remark}")
        
        # Step 3: Plotting (Bar chart, Pie chart)
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Bar Chart
        value_counts.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
        axes[0].set_title(f'{col_name} Frequency Distribution (Bar Chart)')
        axes[0].set_ylabel('Count')
        
        # Pie Chart
        value_counts.plot(kind='pie', ax=axes[1], autopct='%0.1f%%', colors=['#ff9999', '#66b3ff'], startangle=90)
        axes[1].set_title(f'{col_name} Frequency Distribution (Pie Chart)')
        axes[1].set_ylabel('')  # Remove y-label from pie chart
        
        plt.tight_layout()
        plt.show()
        
        # Step 4: Check for missing values
        missing_data = self.df[col_name].isnull().sum()
        missing_percentage = (missing_data / total_count) * 100
        
        print(f"\nMissing Values: {missing_data} ({missing_percentage:.2f}%)")
        
        # Step 5: Conclusion
        conclusion = []
        
        if missing_percentage > 0:
            conclusion.append(f"The data contains {missing_percentage:.2f}% missing values.")
        else:
            conclusion.append("No missing values.")
        
        # Add more conclusions based on the frequency distribution
        if len(remarks) == 0:
            conclusion.append("The data is fairly distributed across categories.")
        
        print("\nConclusion:")
        for point in conclusion:
            print(f"- {point}")
        
        print("\n" + "="*50 + "\n")
    
    def bivariate_numerical_analysis(self, col1, col2):
        """
        Perform bivariate analysis for two numerical columns in the DataFrame.
        It generates visualizations (scatter plot, 2D hist plot, 2D KDE plot),
        checks the correlation coefficient, and provides insights on their relationship.
        """
        print(f"\nBivariate Analysis for '{col1}' and '{col2}':\n")
        
        # Step 1: Scatter Plot
        plt.figure(figsize=(6, 5))
        sns.scatterplot(data=self.df, x=col1, y=col2, color='b', alpha=0.6)
        plt.title(f'Scatter Plot between {col1} and {col2}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.show()
        
        # Step 2: 2D Histplot
        plt.figure(figsize=(6, 5))
        sns.histplot(data=self.df, x=col1, y=col2, bins=30, cmap='Blues', pthresh=.1, cbar=True)
        plt.title(f'2D Histogram between {col1} and {col2}')
        plt.show()
        
        # Step 3: 2D KDE Plot (Kernel Density Estimate)
        plt.figure(figsize=(6, 5))
        sns.kdeplot(data=self.df, x=col1, y=col2, cmap='Blues', fill=True)
        plt.title(f'2D KDE Plot between {col1} and {col2}')
        plt.show()
        
        # Step 4: Correlation Coefficient
        correlation = self.df[[col1, col2]].corr().iloc[0, 1]
        print(f"\nCorrelation Coefficient between {col1} and {col2}: {correlation:.2f}")
        
        # Step 5: Insights based on correlation coefficient
        if correlation > 0.8:
            print(f"The two variables have a strong positive correlation ({correlation:.2f}).")
        elif correlation > 0.5:
            print(f"The two variables have a moderate positive correlation ({correlation:.2f}).")
        elif correlation > 0.2:
            print(f"The two variables have a weak positive correlation ({correlation:.2f}).")
        elif correlation > -0.2:
            print(f"The two variables have a very weak correlation ({correlation:.2f}).")
        elif correlation > -0.5:
            print(f"The two variables have a moderate negative correlation ({correlation:.2f}).")
        else:
            print(f"The two variables have a strong negative correlation ({correlation:.2f}).")
        
        # Step 6: Conclusion
        conclusion = []
        if correlation > 0.8:
            conclusion.append(f"{col1} and {col2} are strongly positively correlated.")
        elif correlation < -0.8:
            conclusion.append(f"{col1} and {col2} are strongly negatively correlated.")
        else:
            conclusion.append(f"The correlation between {col1} and {col2} is weak to moderate.")
        
        print("\nConclusion:")
        for point in conclusion:
            print(f"- {point}")
        
        print("\n" + "="*50 + "\n")
    
    def bivariate_numerical_categorical_analysis(self, target_col, cat_col):
        """
        Perform bivariate analysis for a numerical target column and a categorical feature.
        It generates visualizations (box plot, violin plot, bar plot), checks statistical significance (ANOVA/t-test),
        and provides insights on their relationship.
        """
        # Clean column names (strip spaces)
        self.df.columns = self.df.columns.str.strip()
        
        # Ensure target column is numeric
        self.df[target_col] = pd.to_numeric(self.df[target_col], errors='coerce')
        
        # Step 1: Box Plot
        plt.figure(figsize=(6, 5))
        sns.boxplot(data=self.df, x=cat_col, y=target_col)
        plt.title(f'Box Plot of {target_col} by {cat_col}')
        plt.xticks(rotation=45)  # Rotate x-axis labels
        plt.yticks(rotation=90)  # Rotate y-axis labels vertically
        plt.show()

        # Step 2: Violin Plot
        plt.figure(figsize=(6, 5))
        sns.violinplot(data=self.df, x=cat_col, y=target_col)
        plt.title(f'Violin Plot of {target_col} by {cat_col}')
        plt.xticks(rotation=45)  # Rotate x-axis labels
        plt.yticks(rotation=90)  # Rotate y-axis labels vertically
        plt.show()

        # Step 3: Bar Plot (Mean or Median of the Target by Category)
        plt.figure(figsize=(6, 5))
        sns.barplot(data=self.df, x=cat_col, y=target_col, estimator='mean', ci=None)
        plt.title(f'Mean of {target_col} by {cat_col}')
        plt.xticks(rotation=45)  # Rotate x-axis labels
        plt.yticks(rotation=90)  # Rotate y-axis labels vertically
        plt.show()

        # Step 4: Statistical Test (ANOVA or t-test)
        categories = self.df[cat_col].nunique()
        
        if categories > 2:
            # Perform One-Way ANOVA
            groups = [self.df[self.df[cat_col] == category][target_col] for category in self.df[cat_col].unique()]
            f_stat, p_value = stats.f_oneway(*groups)
            test_result = f"ANOVA test result: F-statistic = {f_stat:.2f}, p-value = {p_value:.4f}"
        else:
            # Perform T-test for two categories
            group1 = self.df[self.df[cat_col] == self.df[cat_col].unique()[0]][target_col]
            group2 = self.df[self.df[cat_col] == self.df[cat_col].unique()[1]][target_col]
            t_stat, p_value = stats.ttest_ind(group1, group2)
            test_result = f"T-test result: T-statistic = {t_stat:.2f}, p-value = {p_value:.4f}"
        
        print(test_result)
        
        # Step 5: Conclusion
        conclusion = []
        if p_value < 0.05:
            conclusion.append(f"There is a statistically significant difference in {target_col} across {cat_col}.")
        else:
            conclusion.append(f"There is no statistically significant difference in {target_col} across {cat_col}.")
        
        print("\nConclusion:")
        for point in conclusion:
            print(f"- {point}")
        
        print("\n" + "="*50 + "\n")
    
    def multivariate_analysis(self, annot=True, cmap='coolwarm', figsize=(12, 10), corr_thresh=0.1):
        """
        Perform multivariate analysis by calculating the correlation matrix and plotting a heatmap.
        """
        # Step 1: Handle missing values (drop rows with missing data)
        df_clean = self.df.dropna()
        
        # Step 2: Calculate correlation matrix
        corr_matrix = df_clean.corr(numeric_only=True)
        
        # Step 3: Filter correlations based on a threshold (optional)
        if corr_thresh:
            corr_matrix = corr_matrix[(corr_matrix.abs() >= corr_thresh) | (corr_matrix.abs() == 1.0)]
        
        # Step 4: Plot heatmap
        plt.figure(figsize=figsize)
        sns.heatmap(corr_matrix, annot=annot, cmap=cmap, fmt=".2f", linewidths=0.5, vmin=-1, vmax=1)
        plt.title('Correlation Matrix', fontsize=16)
        plt.show()