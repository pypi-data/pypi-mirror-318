import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from typing import Optional, Dict, Any, Union, List
from scipy.stats import chi2_contingency

import warnings
warnings.filterwarnings('ignore')



class AutoProfile:
    """
    A comprehensive data profiling tool for deep exploratory data analysis.
    
    This class provides a sophisticated set of methods to analyze and understand
    the characteristics, quality, and predictive power of features in a dataset.
    
    Key Capabilities:
    - Assess data completeness
    - Identify and visualize missing data
    - Detect numerical outliers
    - Compute feature importance metrics
    - Analyze categorical feature associations
    - Perform Information Value (IV) analysis for predictive power
    - Automatically generate distribution plots based on column type.
    
    Attributes:
        _data (pd.DataFrame): Internal copy of the input dataset
        target_column (str): Column used as the target for predictive analysis
        numeric_cols (List[str]): List of numerical feature columns
        categorical_cols (List[str]): List of categorical feature columns
    """

    def __init__(self, data: pd.DataFrame, target_column: str):
        """
        Initialize the AutoProfile with a dataset and target column.
        
        Args:
            data (pd.DataFrame): Input dataset to analyze
            target_column (str): Column used as the prediction target
        
        Raises:
            ValueError: If target column is not present in the dataset
            TypeError: If input is not a pandas DataFrame
        """
        # Validate input type
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame")
        
        # Validate target column presence
        if target_column not in data.columns:
            raise ValueError(f"Target column '{target_column}' not found in DataFrame")
        
        # Create a defensive copy to prevent modifying original data
        self._data = data.copy()
        
        # Ensure target is numeric
        self._data[target_column] = pd.to_numeric(self._data[target_column], errors='coerce')
        
        self.target_column = target_column
        
        # Categorize columns
        self.numeric_cols = self._data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        self.categorical_cols = self._data.select_dtypes(include=['object', 'category']).columns.tolist()
        
        # Remove target column from feature lists if present
        self.numeric_cols = [col for col in self.numeric_cols if col != target_column]
        self.categorical_cols = [col for col in self.categorical_cols if col != target_column]
    
    
    def __calculate_iv(self, feature: str, bins: Optional[int] = 20) -> float:
        """
        Calculate Information Value (IV) for a single feature.
        
        Information Value helps quantify how well a feature can predict 
        the target variable by measuring the predictive strength.
        
        Args:
            feature (str): Feature column name
            bins (Optional[int]): Number of bins for numeric features
        
        Returns:
            float: Information Value score
        """
        if feature == self.target_column:
            return np.nan
        
        data_copy = self._data.copy()
        
        # Apply binning for numeric features
        if feature in self.numeric_cols:
            data_copy[feature] = pd.qcut(data_copy[feature], q=bins, duplicates='drop')
        
        # Calculate IV
        iv = 0
        grouped = data_copy.groupby(feature)[self.target_column].agg(['count', 'sum'])
        grouped['% Good'] = grouped['sum'] / grouped['sum'].sum()
        grouped['% Bad'] = (grouped['count'] - grouped['sum']) / (grouped['count'].sum() - grouped['sum'].sum())
        
        # Handle potential division by zero and log(0)
        grouped['% Good'] = grouped['% Good'].clip(lower=1e-10)
        grouped['% Bad'] = grouped['% Bad'].clip(lower=1e-10)
        
        grouped['WOE'] = np.log(grouped['% Good'] / grouped['% Bad'])
        grouped['IV'] = (grouped['% Good'] - grouped['% Bad']) * grouped['WOE']
        
        return abs(grouped['IV'].sum())

    def __iv_analysis(self) -> go.Figure:
        """
        Compute Information Value (IV) to assess feature predictive power.
        
        Returns:
            Plotly Figure: Bar chart of Information Value for features
        """
        # Compute IV for features
        iv_scores = {
            feature: self.__calculate_iv(feature) 
            for feature in self.numeric_cols + self.categorical_cols 
            if feature != self.target_column
        }
        
        # Create DataFrame to store IV scores
        iv_df = pd.DataFrame.from_dict(iv_scores, orient='index', columns=['IV'])
        iv_df = iv_df.reset_index()
        iv_df = iv_df.rename(columns={'index':"Feature"})
        iv_df = iv_df.sort_values('IV', ascending=False)
        
        iv_df[['Interpretation', 'Color']] = iv_df['IV'].apply(lambda x: pd.Series(self.__interpret_iv(x)))

        
        fig = px.bar(
            iv_df, 
            x="Feature",
            y='IV', 
            title='Feature Information Value',
            text='IV', height=800,color='Interpretation',color_discrete_map={
                 'green': 'green', 'blue': 'blue', 'orange': 'orange', 'red': 'red'}
        )
        fig.update_layout(
            xaxis_title='Features', 
            yaxis_title='Information Value',
            height=500
        )
        fig.update_traces(texttemplate='%{text:.3f}', textposition='outside')
        fig.update_layout(yaxis_title='Information Value (IV)', xaxis_title='Features')
        return fig
    
    def __interpret_iv(self, iv):
        if iv > 0.3:
            return 'Very strong predictor', 'darkgreen'   # Green for very strong predictors
        elif iv >= 0.1:
            return 'Strong predictor', 'navyblue'         # Blue for strong predictors
        elif iv >= 0.02:
            return 'Medium predictor', 'orange'       # Orange for medium predictors
        else:
            return 'Weak predictor', 'red'            # Red for weak predictors
    
    def __missing_analysis(self) -> go.Figure:
        """
        Analyze and visualize missing data percentage across features.
        
        Computes the percentage of missing values for each column and creates
        a bar chart visualization to highlight data completeness issues.
        
        Returns:
            Plotly Figure: Bar chart showing missing data percentages
        """
        missing_percentages = self._data.isnull().sum() / len(self._data) * 100
        missing_percentages = missing_percentages[missing_percentages > 0].sort_values(ascending=False)
        
        fig = px.bar(
            x=missing_percentages.index, 
            y=missing_percentages.values,
            labels={'x': 'Feature', 'y': '% Missing'},
            title='Missing Data Analysis Per Column',
            color_discrete_sequence=['#FF6B6B']
        )
        fig.update_layout(
            xaxis_title='Features',
            yaxis_title='Percentage of Missing Values',
            height=500
        )
        return fig
    
    def __outlier_analysis(self) -> go.Figure:
        """
        Detect and visualize outliers in numerical features using 
        the Interquartile Range (IQR) method.
        
        Computes the number of outliers for each numeric column and 
        creates a bar chart to highlight potential data quality issues.
        
        Returns:
            Plotly Figure: Bar chart showing outlier counts per feature
        """
        def count_outliers(series: pd.Series) -> int:
            """
            Count outliers in a numeric series using the IQR method.
            
            Args:
                series (pd.Series): Numeric data series to analyze
            
            Returns:
                int: Number of outliers detected
            """
            Q1 = series.quantile(0.25)
            Q3 = series.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            return ((series < lower_bound) | (series > upper_bound)).sum()

        # Compute outliers for numeric columns
        outlier_counts = self._data[self.numeric_cols].apply(count_outliers)
        outlier_counts = outlier_counts[outlier_counts > 0].sort_values(ascending=False)
        
        fig = px.bar(
            x=outlier_counts.index, 
            y=outlier_counts.values,
            labels={'x': 'Feature', 'y': 'Outlier Count'},
            title='Outliers Per Numeric Feature',
            color_discrete_sequence=['#4ECDC4']
        )
        fig.update_layout(
            xaxis_title='Features',
            yaxis_title='Number of Outliers',
            height=500
        )
        return fig
    
    def __cramers_v_analysis(self) -> go.Figure:
        """
        Compute Cramér's V to assess associations between categorical features.
        
        Cramér's V measures the strength of association between categorical variables,
        helping identify potential meaningful relationships in the dataset.
        
        Returns:
            Plotly Figure: Bar chart of Cramér's V association values
        """
        def cramers_v(x: pd.Series, y: pd.Series) -> float:
            """
            Calculate Cramér's V coefficient to measure feature association.
            
            Args:
                x (pd.Series): First categorical variable
                y (pd.Series): Second categorical variable
            
            Returns:
                float: Cramér's V association value
            """
            contingency_table = pd.crosstab(x, y)
            chi2, _, _, _ = chi2_contingency(contingency_table)
            n = contingency_table.sum().sum()
            min_dim = min(contingency_table.shape) - 1
            return np.sqrt(chi2 / (n * min_dim))

        # Compute Cramér's V for categorical features against target
        cramer_values = {
            feature: cramers_v(self._data[feature], self._data[self.target_column])
            for feature in self.categorical_cols
            if feature != self.target_column
        }
        
        # Create DataFrame for visualization
        cramer_df = pd.DataFrame.from_dict(cramer_values, orient='index', columns=['Cramers_V'])
        cramer_df = cramer_df.sort_values('Cramers_V', ascending=False)
        
        # Color mapping based on association strength
        def color_cramers(v):
            if v > 0.5: return 'green'
            elif v > 0.3: return 'blue'
            elif v > 0.1: return 'orange'
            return 'red'
        
        fig = px.bar(
            cramer_df, 
            x=cramer_df.index, 
            y='Cramers_V', 
            title="Cramér's V Feature Association",
            color_discrete_sequence=[color_cramers(v) for v in cramer_df['Cramers_V']]
        )
        fig.update_layout(
            xaxis_title='Features', 
            yaxis_title="Cramér's V",
            height=500
        )
        return fig
    
    def __completeness_score(self) -> go.Figure:
        
        df = self._data
        
        score = round(100 - df.isnull().sum().sum() / (df.size) * 100,2)
        if score <= 50.00:
            color = 'darkred'
            backrgound = 'red'
        elif 50.01 < score <= 79.99:
            color = 'orange'
            backrgound = 'orangered'
        elif score >= 80.00:
            color = 'rgb(112,130,56)'
            backrgound = 'darkseagreen'
        fig = go.Figure(go.Indicator(mode="gauge+number",value=round(score,2), domain={'x': [0, 1],'y': [0, 1]},title={'text': "Data Completeness Score"},
                                     gauge={'bar': {'color': color},'axis': {'range': [None, 100],'tickwidth': 1,'tickcolor': "darkblue"},
                                            'steps': [{'range': [0, 100]}, {'range': [0, 100],'color': backrgound}]}))
        return fig
    
    def __correlation_analysis(self, 
                            correlation_type: str = 'pearson', 
                            include_target: bool = True) -> go.Figure:
        """
    Compute and visualize correlation matrix for numerical and categorical features.
    
    Args:
        correlation_type (str): Type of correlation to compute 
            - 'pearson': Linear correlation for numerical features
            - 'cramer': Association for categorical features
        include_target (bool): Whether to include target column in correlation analysis
    
    Returns:
        Plotly Figure: Heatmap of feature correlations
    """
        
        def cramers_v(x: pd.Series, y: pd.Series) -> float:
            """
            Calculate Cramér's V coefficient to measure feature association.
            
            Args:
                x (pd.Series): First categorical variable
                y (pd.Series): Second categorical variable
            
            Returns:
                float: Cramér's V association value
            """
            contingency_table = pd.crosstab(x, y)
            chi2, _, _, _ = chi2_contingency(contingency_table)
            n = contingency_table.sum().sum()
            min_dim = min(contingency_table.shape) - 1
            return np.sqrt(chi2 / (n * min_dim))
        
        # Prepare feature list
        features = (self.numeric_cols + self.categorical_cols)
        if include_target:
            features.append(self.target_column)
        
        # Create correlation matrix based on correlation type
        if correlation_type == 'pearson':
            # Numerical correlation using Pearson
            numeric_features = [col for col in features if col in self.numeric_cols]
            corr_matrix = self._data[numeric_features].corr(method='pearson')
            title = 'Pearson Correlation Heatmap'
            color_scale = 'RdBu_r'  # Diverging color scale for positive/negative correlations
            
        elif correlation_type == 'cramer':
            # Categorical association using Cramér's V
            categorical_features = [col for col in features if col in self.categorical_cols]
            # Create correlation matrix
            corr_matrix = pd.DataFrame(
                index=features, columns=features, dtype=float)
            
            # Compute Cramér's V for each pair of categorical variables
            for i, feature1 in enumerate(features):
                for j, feature2 in enumerate(features):
                    if i == j:
                        corr_matrix.iloc[i, j] = 1.0
                    else:
                        # Skip if not categorical or same type
                        if (feature1 in categorical_features and 
                            feature2 in categorical_features):
                            corr_matrix.iloc[i, j] = cramers_v(
                                self._data[feature1], 
                                self._data[feature2]
                            )
                        else:
                            corr_matrix.iloc[i, j] = np.nan
            
            title = "Cramér's V Categorical Association Heatmap"
            color_scale = 'Viridis'  # Sequential color scale

        else:
            raise ValueError("Invalid correlation type. Choose 'pearson' or 'cramer'.")
        
        # Create heatmap
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.index,
            colorscale=color_scale,
            zmin=-1 if correlation_type == 'pearson' else 0,zmax=1
            ))
        fig.update_layout(
            title=title,
            height=800,
            width=1000,
            xaxis_title='Features',
            yaxis_title='Features')
        return fig.show()
    
    def __turkey(self, column):
        """
        Detect outliers using the Tukey method (Interquartile Range method).
        
        Args:
            column (str): Name of the column to check for outliers
        
        Returns:
            int: Number of outliers detected
        """
        if column not in self.numeric_cols:
            return 0
        
        data = self._data[column]
        Q1 = data.quantile(0.25)
        Q3 = data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = ((data < lower_bound) | (data > upper_bound)).sum()
        return outliers
    
    def __convert_to_serializable(self, value):
        """
        Convert non-serializable types to JSON-friendly types.
        
        Args:
            value: Input value to convert
        
        Returns:
            Serializable representation of the value
        """
        if pd.isna(value):
            return '*'
        
        # Handle numpy/pandas specific types
        if isinstance(value, (np.integer, np.floating)):
            return float(value)
        
        if isinstance(value, np.ndarray):
            return value.tolist()
        
        if hasattr(value, 'dtype'):
            return str(value)
        
        return value
    
    def __autodistribution(self, column: str) -> go.Figure:
        """
        Automatically generate distribution plots based on column type.
        
        Args:
            column (str): Name of the column to analyze
            
        Returns:
            go.Figure: Distribution plot (histogram for numeric, bar plot for categorical)
        """
        if column not in self._data.columns:
            raise ValueError(f"Column '{column}' not found in DataFrame")
        
        data = self._data[column].dropna()
        if column in self.numeric_cols:
            data = data.replace([np.inf, -np.inf], np.nan).dropna()
            q75, q25 = np.percentile(data, [75, 25])
            iqr = q75 - q25
            bin_width = 2 * iqr / (len(data) ** (1 / 3)) if iqr > 0 else 1
            n_bins = int((data.max() - data.min()) / bin_width) if bin_width > 0 else 30
            n_bins = min(max(n_bins, 10), 50)  # Keep bins between 10 and 50
            fig = go.Figure(data=[
                go.Histogram(
                    x=data,
                    nbinsx=n_bins,
                    name=column,
                    histnorm="probability",
                    marker_color="rgb(55, 83, 109)",
                )
            ]
        )
            # Add stats
            mean_val = data.mean()
            median_val = data.median()
            
            fig.add_vline(
            x=mean_val,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Mean: {mean_val:.2f}",
            annotation=dict(textangle=-90,font=dict(size=12),yanchor='bottom')
            )
            fig.add_vline(
            x=median_val,
            line_dash="dash",
            line_color="green",
            annotation_text=f"Median: {median_val:.2f}",
            annotation=dict(textangle=-90,font=dict(size=12),yanchor='bottom')
            )
            fig.update_layout(
            title=f"Distribution of {column}",
            xaxis_title=column,
            yaxis_title="Probability",
            bargap=0.1,
            )
        else:
            # Check if categorical column is binary
            unique_values = set(data.replace([np.inf, -np.inf], np.nan).dropna().unique())
            is_binary = unique_values.issubset({0, 1}) or unique_values.issubset({True, False})
            if is_binary:
                # Handle binary variables
                value_counts = (
                data.replace([np.inf, -np.inf], np.nan).value_counts().fillna(0)
                )
                labels = (
                    ["No (0)", "Yes (1)"]
                    if unique_values.issubset({0, 1})else ["False", "True"]
                )
                values = (
                    [int(value_counts.get(0, 0)), int(value_counts.get(1, 0))]
                    if unique_values.issubset({0, 1})
                    else [int(value_counts.get(False, 0)), int(value_counts.get(True, 0))]
                )
                
                fig = go.Figure(
                    data=[
                        go.Pie(
                            labels=labels,
                            values=values,
                            hole=0.3,
                            marker_colors=["rgb(255, 99, 71)", "rgb(60, 179, 113)"],
                        )
                    ]
                )
                
                total = sum(values)
                percentage_0 = (values[0] / total * 100) if total > 0 else 0
                percentage_1 = (values[1] / total * 100) if total > 0 else 0
                
                fig.update_traces(
                textposition="inside",
                texttemplate=f"%{{label}}<br>%{{value}}<br>({percentage_0:.1f}%)",)
                
                fig.update_layout(title=f"Distribution of {column} (Binary Feature)",
                annotations=[
                    dict(text=f"Total: {total}", x=0.5, y=0.5, showarrow=False)
                ],)
            else:
                # Regular categorical variables
                value_counts = data.value_counts()
                fig = go.Figure(
                    data=[
                    go.Bar(
                        x=value_counts.index,
                        y=value_counts.values,
                        text=value_counts.values,
                        textposition="auto",
                        marker_color="rgb(55, 83, 109)",
                    )
                ])
                fig.update_layout(title=f"Distribution of {column}",xaxis_title=column,yaxis_title="Count")
                # Common layout settings
        fig.update_layout(height=500,width=800,plot_bgcolor="white",paper_bgcolor="white",showlegend=False,)
        return fig

        
    def __assessment_analysis(self):
        """
        Generate a comprehensive statistical assessment of the dataset.
        
        Returns:
            go.Figure: A Plotly table with detailed statistical summary
        """
        df = self._data
        sub = df.describe(include='all').T.reset_index()
        sub.rename(columns={'index':'Feature'}, inplace=True)
        
        sub['Data Type'] = sub['Feature'].apply(lambda x: str(df[x].dtype))
        sub['Missing Values'] = sub['Feature'].apply(lambda x: df[x].isnull().sum())
        sub['Missing Percent'] = sub['Feature'].apply(lambda x: round(df[x].isnull().sum()/len(df)*100, 2))
        sub['Duplicates'] = sub['Feature'].apply(lambda x: df[x].duplicated().sum())
        sub['Outliers'] = sub['Feature'].apply(lambda x: self.__turkey(x))
        
        # Calculate IV for each feature
        sub['IV (Target Predictiveness)'] = sub['Feature'].apply(lambda x: round(self.__calculate_iv(x),4))
        
        def compute_numeric_stats(column):
            """Compute advanced numeric statistics for a column."""
            if column in self.numeric_cols:
                col_data = df[column].dropna()
                return {
                    'Skewness': round(col_data.skew(), 4),
                    'Kurtosis': round(col_data.kurtosis(), 4),
                    'Variance': round(col_data.var(), 4)
                }
            return {
                'Skewness': '*',
                'Kurtosis': '*',
                'Variance': '*'
            }
        
        
        numeric_stats = sub['Feature'].apply(compute_numeric_stats)
        sub['Skewness'] = numeric_stats.apply(lambda x: x['Skewness'])
        sub['Kurtosis'] = numeric_stats.apply(lambda x: x['Kurtosis'])
        sub['Variance'] = numeric_stats.apply(lambda x: x['Variance'])
        
        sub.rename(columns={
            'count':'Records', 'unique':'Unique',
            'top':'Common Value', 'freq':'Frequency',
            'mean':'Mean', 'std':'Std Dev',
            'min':'Minimum', '25%':'25th Quartile',
            '50%':'Median', '75%':'75th Quartile',
            'max':'Maximum', 'top':'Common Value'
        }, inplace=True)
        
        for col in sub.columns:
            sub[col] = sub[col].apply(self.__convert_to_serializable)
        
        # Select and order columns
        columns = ['Feature', 'Data Type', 'Records', 'Unique', 'Common Value', 'Frequency', 
                   'Duplicates', 'Outliers', 'Missing Values', 'Missing Percent', 'Mean', 'Std Dev', 'Variance',
                   'IV (Target Predictiveness)','Skewness', 'Kurtosis','Minimum', '25th Quartile', 'Median', '75th Quartile', 'Maximum']
        sub = sub[columns]
        
        # Create Plotly table
        fig = go.Figure(data=[go.Table(
            header=dict(values=sub.columns.tolist(),
                        fill_color='paleturquoise',
                        align='left',
                        font=dict(size=10, color='black'),
                        line_color='darkslategray',
                        line_width=1.5
            ),
            cells=dict(values=[sub[col].tolist() for col in sub.columns],
                       fill_color='lavender',
                       align='left',
                       font=dict(size=9, color='darkblue'),
                       line_color='lightgray',
            # Enable text wrapping
                        ##format=['text'] * len(sub.columns)
                        ))
        ])
        
        fig.update_layout(
            title=f'Comprehensive Data Assessment',
            height=800,
            width=1200,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        
        return fig
    
    ## This function is too large and can crash your machine. be careful    
    def __pairplot_analysis(self) -> go.Figure:
        # Select numeric columns including target
        numeric_features = self.numeric_cols.copy()
        if self.target_column in self._data.columns:
            numeric_features.append(self.target_column)
            
        # Limit to top 6 features to prevent overcrowding
        if len(numeric_features) > 10:
            # Prioritize features with highest correlation to target
            correlations = self._data[numeric_features].corr()[self.target_column].abs()
            top_features = correlations.nlargest(10).index.tolist()
            numeric_features = top_features
            # Prepare data for pairplot
        plot_data = self._data[numeric_features].copy()

        # Create figure
        fig = go.Figure()

        # Add scatter plots for each pair of features
        for i, feature1 in enumerate(numeric_features):
            for j, feature2 in enumerate(numeric_features):
                if i != j:
                # Scatter plot
                    scatter = go.Scatter(
                        x=plot_data[feature2],
                        y=plot_data[feature1],
                        mode='markers',
                        name=f'{feature2} vs {feature1}',
                        marker=dict(
                            color=plot_data[self.target_column],
                            colorscale='Viridis',
                            showscale=True if i == 0 and j == 1 else False,
                            colorbar=dict(title=self.target_column) if i == 0 and j == 1 else None),
                        text=[f'{feature2}: {x}<br>{feature1}: {y}<br>{self.target_column}: {t}' 
                        for x, y, t in zip(plot_data[feature2], plot_data[feature1], plot_data[self.target_column])],
                        hoverinfo='text')
                    fig.add_trace(scatter)
                else:
                    # Histogram for diagonal
                    hist = go.Histogram(
                        x=plot_data[feature1],
                        name=feature1,
                        opacity=0.7)
                    fig.add_trace(hist)

        # Configure layout
        fig.update_layout(
        title='Pairplot of Numeric Features',
        height=800,
        width=1000,
        showlegend=False)

        # Create grid layout
        fig.update_layout(
            xaxis=dict(title=numeric_features[-1]),
            yaxis=dict(title=numeric_features[0]),
            plot_bgcolor='white')

        # Update subplot layout to create a grid
        rows = cols = len(numeric_features)
        fig.update_layout(
            grid=dict(rows=rows, columns=cols, pattern="independent"))
        
        return fig    
        
    def summary(self, 
            completeness: bool = False, 
            missing: bool = False, 
            outliers: bool = False, 
            iv_analysis: bool = False,
            cramers_v_analysis: bool = False,
            correlation: bool = False,
            assessment: bool = False,
            pairplot: bool = False,
            distribution: Optional[str] = None) -> Union[go.Figure, Dict[str, go.Figure]]:
        """
        Perform multiple data profiling analyses with flexible configuration.
    
    Args:
        completeness (bool): Calculate overall data completeness score
        missing (bool): Analyze missing data percentages
        outliers (bool): Detect and visualize numerical outliers
        iv_analysis (bool): Compute Information Value for predictive power
        cramers_v_analysis (bool): Assess categorical feature associations
        correlation (bool): Compute correlations between features
        pairplot (bool): Create interactive pairplot for numeric features
    
    Returns:
        Visualization results as a single figure or dictionary of figures
    
    Raises:
        ValueError: If no analysis type is selected
    """
    # Analysis methods dictionary
        analysis_methods = {
            'completeness': (completeness, self.__completeness_score),
            'missing': (missing, self.__missing_analysis),
            'outliers': (outliers, self.__outlier_analysis),
            'iv_analysis': (iv_analysis, self.__iv_analysis),
            'cramers_v_analysis': (cramers_v_analysis, self.__cramers_v_analysis),
            'correlation': (correlation, self.__correlation_analysis),
            'assessment': (assessment, self.__assessment_analysis),
            'pairplot': (pairplot, self.__pairplot_analysis)
            }
        
        if distribution:
            analysis_methods['distribution'] = (True, lambda: self.__autodistribution(distribution))
    
        # Filter active analyses
        active_analyses = [
            method for name, (is_active, method) in analysis_methods.items() 
            if is_active
        ]
    
        if not active_analyses:
            raise ValueError("Please specify at least one analysis type")
    
        # Execute selected analyses
        results = {}
        for name, (is_active, method) in analysis_methods.items():
            if is_active:
                if name == 'correlation':
                    # For correlation, create both Pearson and Cramér's V visualizations
                    results['numeric_correlation'] = method(correlation_type='pearson', include_target=True)
                    results['categorical_association'] = method(correlation_type='cramer', include_target=True)
                else:
                    results[name] = method()
    
        return results if len(results) > 1 else list(results.values())[0]