import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ── Constants ─────────────────────────────────────────────────────────────────
FEATURES = [
    'Income', 'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
    'NumWebPurchases', 'NumStorePurchases', 'Recency'
]

ALL_COLS = [
    'ID', 'Year_Birth', 'Education', 'Marital_Status', 'Income',
    'Kidhome', 'Teenhome', 'Recency', 'MntWines', 'MntFruits',
    'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
    'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases',
    'NumStorePurchases', 'NumWebVisitsMonth', 'AcceptedCmp3', 'AcceptedCmp4',
    'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain',
    'Z_CostContact', 'Z_Revenue', 'Response'
]


def ApplyClusteringKmeans(csv_path='marketing_campaign.csv'):
    """
    Reads marketing_campaign.csv, runs K-Means (k=3) and returns a dict
    with all the data the Flask template needs (no HTTP fetch required).
    """

    # ── 1. Load ───────────────────────────────────────────────────────────────
    df = pd.read_csv(csv_path, sep='\t')
    total_raw     = len(df)
    nulls_dropped = int(df['Income'].isna().sum())

    # ── 2. Preprocessing ──────────────────────────────────────────────────────
    df = df.dropna(subset=['Income']).copy()
    total_clean = len(df)

    X      = df[FEATURES].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ── 3. Model ──────────────────────────────────────────────────────────────
    model  = KMeans(n_clusters=3, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    df['Cluster'] = labels.tolist()

    # Centroids converted back to original scale
    centers_original = scaler.inverse_transform(model.cluster_centers_)

    # ── 4. Table rows (first 100 for display) ─────────────────────────────────
    table_rows = []
    for _, row in df.head(100).iterrows():
        table_rows.append({
            'ID':                int(row['ID']),
            'Income':            int(row['Income']),
            'MntWines':          int(row['MntWines']),
            'MntMeatProducts':   int(row['MntMeatProducts']),
            'NumWebPurchases':   int(row['NumWebPurchases']),
            'NumStorePurchases': int(row['NumStorePurchases']),
            'Recency':           int(row['Recency']),
            'Cluster':           int(row['Cluster']),
        })

    # ── 5. Cluster summaries ──────────────────────────────────────────────────
    summaries = []
    for c in range(3):
        sub = df[df['Cluster'] == c]
        s   = {'cluster': c, 'count': len(sub)}
        for f in FEATURES:
            s[f] = round(float(sub[f].mean()), 2)
        summaries.append(s)

    # ── 6. Centroids dict (original scale) ───────────────────────────────────
    centroids = []
    for i, row in enumerate(centers_original):
        d = {'cluster': i}
        for j, f in enumerate(FEATURES):
            d[f] = round(float(row[j]), 2)
        centroids.append(d)

    # ── 7. Scatter sample (max 800 pts for chart performance) ─────────────────
    scatter_sample = df.sample(min(800, total_clean), random_state=42)
    scatter_pts    = []
    for _, row in scatter_sample.iterrows():
        total_spend = int(
            row['MntWines']    + row['MntFruits']       + row['MntMeatProducts'] +
            row['MntFishProducts'] + row['MntSweetProducts'] + row['MntGoldProds']
        )
        scatter_pts.append({'x': int(row['Income']), 'y': total_spend, 'c': int(row['Cluster'])})

    return {
        'total_raw':     total_raw,
        'total_clean':   total_clean,
        'nulls_dropped': nulls_dropped,
        'features':      FEATURES,
        'all_cols':      ALL_COLS,
        'inertia':       round(float(model.inertia_), 2),
        'table_rows':    table_rows,
        'summaries':     summaries,
        'centroids':     centroids,
        'scatter_pts':   scatter_pts,
    }