# Milestone 2: Behavior Clustering & Pattern Detection - Report Summary

## Objective
Perform customer behavior clustering and pattern detection using retail transaction data to identify distinct customer segments based on purchasing patterns. This analysis aims to understand customer behavior through unsupervised learning techniques and provide actionable insights for business strategy.

## Dataset Source
- **Dataset**: Online Retail Dataset from Milestone 1
- **Source**: UCI Machine Learning Repository - Online Retail Dataset
- **Description**: Contains transaction data from a UK-based online retail store from 2010-2011
- **Size**: 402,528 transactions from 4,372 unique customers
- **Features**: CustomerID, InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, Country

## Steps Followed

### 1. Data Loading and Preprocessing
- Loaded customer and transaction datasets from Milestone 1
- Merged datasets on CustomerID
- Cleaned data by removing negative quantities (returns) and zero prices
- Converted InvoiceDate to datetime format
- Created Revenue feature (Quantity × UnitPrice)

### 2. Feature Engineering
- Aggregated transaction-level data to customer-level features:
  - **Quantity_sum**: Total quantity purchased
  - **Quantity_mean**: Average quantity per transaction
  - **UnitPrice_mean**: Average unit price
  - **Revenue_sum**: Total revenue generated
  - **Revenue_mean**: Average revenue per transaction
  - **InvoiceNo_nunique**: Number of unique orders (frequency)
  - **days_active**: Customer lifetime in days
  - **avg_order_value**: Average order value
  - **avg_items_per_order**: Average items per order

### 3. Feature Selection and Preparation
- Selected 9 relevant numerical features for clustering
- Handled missing values and infinite values using median imputation
- Applied StandardScaler for data standardization
- Implemented PCA for dimensionality reduction and visualization
- First 2 principal components explain significant variance for 2D visualization

### 4. Clustering Algorithm Implementation

#### K-Means Clustering
- Applied Elbow Method and Silhouette Score to determine optimal number of clusters
- Tested k values from 2 to 10
- Selected optimal k based on highest silhouette score
- Fitted final K-Means model with optimal parameters

#### DBSCAN Clustering
- Experimented with different eps (0.5, 1.0, 1.5, 2.0, 2.5) and min_samples (5, 10, 15, 20) parameters
- Evaluated performance using silhouette score
- Selected best parameters based on highest silhouette score
- Identified noise points and cluster distribution

### 5. Visualization Creation
- **Scatter Plot (2D PCA)**: Visualized clusters in reduced dimensional space
- **Cluster Characteristics Bar Plots**: Compared mean values of key metrics across clusters
- **Pair Plot**: Analyzed feature distributions and relationships across clusters
- **Cluster Size Distribution**: Pie charts showing cluster membership distribution
- **Correlation Heatmap**: Feature correlation analysis

### 6. Cluster Analysis and Interpretation
- Analyzed cluster characteristics and profiles
- Identified distinct customer segments based on purchasing behavior
- Provided business insights and recommendations

## Tools Used
- **Python Libraries**: pandas, numpy, matplotlib, seaborn
- **Machine Learning**: scikit-learn (StandardScaler, PCA, KMeans, DBSCAN, silhouette_score)
- **Visualization**: matplotlib, seaborn for comprehensive plotting
- **Environment**: Jupyter Notebook (.ipynb format)

## Key Insights and Graphs

### 1. Customer Segmentation Results
The clustering analysis successfully identified distinct customer segments:

- **High-Value Frequent Customers**: High revenue, high order frequency
- **High-Value Occasional Customers**: High revenue, low order frequency  
- **Low-Value Frequent Customers**: Low revenue, high order frequency
- **Low-Value Occasional Customers**: Low revenue, low order frequency

### 2. Algorithm Performance
- **K-Means**: Achieved optimal clustering with good silhouette score
- **DBSCAN**: Successfully identified clusters with noise point detection
- Both algorithms revealed similar customer behavior patterns

### 3. Key Differentiators
- **Revenue** and **Order Frequency** are primary differentiators between clusters
- **Customer Lifetime** varies significantly across segments
- **Average Order Value** provides additional segmentation insights

### 4. Business Implications
- High-value customers represent a smaller but significant portion of the customer base
- Customer lifetime varies across segments, indicating different engagement patterns
- Revenue and frequency patterns suggest opportunities for targeted marketing strategies

### 5. Visualizations Generated
- `cluster_scatter.png`: 2D PCA visualization of clustering results
- `cluster_profile_bar.png`: Bar plots comparing cluster characteristics
- `pair_plot.png`: Feature distribution analysis across clusters
- `cluster_size_distribution.png`: Pie charts showing cluster membership
- `correlation_heatmap.png`: Feature correlation analysis
- `elbow_silhouette.png`: Parameter optimization plots

## Conclusion
The clustering analysis successfully identified distinct customer behavior patterns in the retail dataset. The combination of K-Means and DBSCAN algorithms provided comprehensive insights into customer segmentation, revealing opportunities for targeted business strategies based on purchasing behavior, frequency, and value patterns.

The analysis demonstrates the effectiveness of unsupervised learning techniques in understanding customer behavior and provides a foundation for data-driven business decisions in customer relationship management and marketing strategies.
