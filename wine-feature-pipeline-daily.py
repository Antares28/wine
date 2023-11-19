import os
#import modal

LOCAL=True
if LOCAL == False:
   stub = modal.Stub("wine_daily")
   image = modal.Image.debian_slim().pip_install(["hopsworks"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("id2223"))
   def f():
       g()


def generate_wine(fixed_acidity_max, fixed_acidity_min, 
                  volatile_acidity_max, volatile_acidity_min,
                  citric_acid_max, citric_acid_min,
                  residual_sugar_max, residual_sugar_min,
                  chlorides_max, chlorides_min,
                  free_sulfur_dioxide_max, free_sulfur_dioxide_min,
                  total_sulfur_dioxide_max, total_sulfur_dioxide_min,
                  density_max, density_min,
                  ph_max, ph_min,
                  sulphates_max, sulphates_min,
                  alcohol_max, alcohol_min):
    """
    Returns a single iris flower as a single row in a DataFrame
    """
    import pandas as pd
    import random

    df = pd.DataFrame({"type": [random.randint(0, 1)],
                       "fixed_acidity": [random.uniform(fixed_acidity_max, fixed_acidity_min)],
                       "volatile_acidity": [random.uniform(volatile_acidity_max, volatile_acidity_min)],
                       "citric_acid": [random.uniform(citric_acid_max, citric_acid_min)],
                       "residual_sugar": [random.uniform(residual_sugar_max, residual_sugar_min)],
                       "chlorides": [random.uniform(chlorides_max, chlorides_min)],
                       "free_sulfur_dioxide": [random.uniform(free_sulfur_dioxide_max, free_sulfur_dioxide_min)],
                       "total_sulfur_dioxide": [random.uniform(total_sulfur_dioxide_max, total_sulfur_dioxide_min)],
                       "density": [random.uniform(density_max, density_min)],
                       "ph": [random.uniform(ph_max, ph_min)],
                       "sulphates": [random.uniform(sulphates_max, sulphates_min)],
                       "alcohol": [random.uniform(alcohol_max, alcohol_min)],
                       "quality": [random.randint(3, 9)]
                      })
    return df


def get_random_wine():
    """
    Returns a DataFrame containing one random iris flower
    """
    import pandas as pd
    import random

    wine_df = generate_wine(15.9, 3.8, 1.58, 0.08, 1.66, 0, 65.8, 0.6, 0.611, 0.009, 289, 1, 440, 6, 1.03898, 0.98711, 4.01, 2.72, 2, 0.22, 14.9, 8)
    print("Wine added")

    return wine_df


def g():
    import hopsworks
    import pandas as pd
    
    project = hopsworks.login()
    fs = project.get_feature_store()

    wine_df = get_random_wine()

    wine_fg = fs.get_feature_group(name="wine",version=1)
    wine_fg.insert(wine_df)

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        stub.deploy("wine_daily")
        with stub.run():
            f()
