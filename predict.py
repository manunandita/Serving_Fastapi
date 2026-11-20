import pickle 

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

prediction=model.predict([[34.350461, "middle_aged", "medium", 2, 50.000000, "unemployed"]]])