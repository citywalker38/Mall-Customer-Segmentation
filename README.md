# Mall Customer Segmentation

This project applies **machine learning clustering techniques** to segment mall customers based on their **age, annual income, and spending behavior**. The goal is to identify meaningful customer groups that can help businesses design **targeted marketing strategies**, improve customer retention, and maximize revenue.

The project implements and compares **K-Means** and **DBSCAN** clustering algorithms, visualizes clusters in **2D and 3D**, and evaluates model quality using **Silhouette Score** and the **Elbow Method**.

## Dataset

We are using the [Mall Customers Segmentation Dataset][def1] from [Kaggle][def2]. The dataset contains customer information with the following key features:

- **Age**
- **Annual Income (k$)**
- **Spending Score (1–100)**

These attributes are commonly used in customer behavior analysis and market segmentation.

## Machine Learning Techniques Used

### 1. **K-Means Clustering**

K-Means is used to group customers into a fixed number of clusters based on similarity.

- The **Elbow Method** is applied to determine the optimal number of clusters.
- The dataset is standardized before clustering to ensure fair distance calculation.
- Final clusters are visualized in 3D.

### 2. **DBSCAN (Density-Based Spatial Clustering)**

DBSCAN is used to detect clusters of arbitrary shape and identify outliers.

- The **k-distance graph** is used to estimate the optimal `eps`.
- **Silhouette Score** is used to find the best `min_samples`.
- Noise points are identified and handled separately.

## Data Preprocessing

- Selected features: `Age`, `Annual Income (k$)`, `Spending Score (1–100)`
- Standardization is applied using **StandardScaler** to normalize all features.

## Model Evaluation

| Method           | Purpose                                        |
| :--------------- | :--------------------------------------------- |
| Elbow Method     | To find optimal number of clusters for K-Means |
| Silhouette Score | To evaluate clustering quality                 |
| k-Distance Graph | To determine optimal eps for DBSCAN            |

## Visualizations

The project includes:

- Histograms with KDE plots
- Correlation heatmaps
- K-Means elbow curve
- 2D cluster plots
- Interactive 3D cluster plots (Plotly)
- DBSCAN noise and cluster visualization

## Model Saving

Trained models are saved using `pickle`.

```
model/
├── kmeans.pkl
└── dbscan.pkl
```

These can be reloaded later for predictions or deployment.

## Technologies Used

![Python][def3]
![UV][def4]
![NumPy][def5]
![Pandas][def6]
![Matplotlib][def7]
![Seaborn][def8]
![Plotly][def9]
![Scikit-Learn][def10]
![Streamlit][def11]
![Docker][def12]
![Render][def13]

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mall-customer-segmentation.git
cd mall-customer-segmentation
```

### 2. Create environment and install dependencies

```bash
uv venv
uv sync
```

### 3. Run the notebook or scripts

Open the Jupyter notebook or run the Python scripts to explore clustering and visualizations.

## Business Value

This project helps businesses:

- Identify high-value customers
- Detect low-spending or inactive customers
- Design personalized marketing campaigns
- Improve customer retention strategies

[def1]: https://www.kaggle.com/datasets/debarghamitraroy/mall-customers-segmentation-dataset
[def2]: https://www.kaggle.com/
[def3]: https://img.shields.io/badge/Python-%233776AB?logo=python&logoColor=yellow&Badge
[def4]: https://img.shields.io/badge/UV-%23DE5FE9?logo=uv&logoColor=black
[def5]: https://img.shields.io/badge/NumPy-%23013243?logo=numpy&logoColor=white
[def6]: https://img.shields.io/badge/Pandas-%23150458?logo=pandas&logoColor=white
[def7]: https://img.shields.io/badge/Matplotlib-%23004480
[def8]: https://img.shields.io/badge/Seaborn-%2334A7C1
[def9]: https://img.shields.io/badge/Plotly-%237A76FF?logo=plotly&logoColor=white
[def10]: https://img.shields.io/badge/Scikit%20Learn-%23F7931E?logo=scikitlearn&logoColor=black
[def11]: https://img.shields.io/badge/Streamlit-%23FF4B4B?logo=streamlit&logoColor=white
[def12]: https://img.shields.io/badge/Docker-%232496ED?logo=docker&logoColor=white
[def13]: https://img.shields.io/badge/Render-%23000000?logo=render&logoColor=white
