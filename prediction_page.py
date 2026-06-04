from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = df.copy()

le_sector = LabelEncoder()
le_investor = LabelEncoder()
le_founder = LabelEncoder()
le_outcome = LabelEncoder()

data["sector"] = le_sector.fit_transform(
    data["sector"]
)

data["investor_type"] = le_investor.fit_transform(
    data["investor_type"]
)

data["founder_background"] = (
    le_founder.fit_transform(
        data["founder_background"]
    )
)

data["outcome"] = (
    le_outcome.fit_transform(
        data["outcome"]
    )
)

X = data.drop("outcome", axis=1)
y = data["outcome"]

model = RandomForestClassifier(
    n_estimators=200
)

model.fit(X,y)
