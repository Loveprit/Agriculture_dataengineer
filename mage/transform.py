import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    crop = df["Crop"]
    crop_set = set(crop)
    crop_dim = []
    j = 0
    for item in crop_set:
        col = [j,item]
        crop_dim.append(col)
        j=j+1

    crop_dim = pd.DataFrame(crop_dim)
    crop_dim.rename(columns={0:"crop_id",1:"crop"},inplace = True)

    temp = df["Crop_Year"]
    temp_set = set(temp)
    temp_dim = []
    j = 0
    for item in temp_set:
        col = [j,item]
        temp_dim.append(col)
        j=j+1

    year_dim = pd.DataFrame(temp_dim)
    year_dim.rename(columns={0:"year_id",1:"year"},inplace = True)

    temp = df["Season"]
    temp_set = set(temp)
    temp_dim = []
    j = 0
    for item in temp_set:
        col = [j,item]
        temp_dim.append(col)
        j=j+1

    season_dim = pd.DataFrame(temp_dim)
    season_dim.rename(columns={0:"season_id",1:"season"},inplace = True)

    temp = df["State"]
    temp_set = set(temp)
    temp_dim = []
    j = 0
    for item in temp_set:
        col = [j,item]
        temp_dim.append(col)
        j=j+1

    state_dim = pd.DataFrame(temp_dim)
    state_dim.rename(columns={0:"state_id",1:"state"},inplace = True)

    fact_table = df.copy()

    fact_table["state_id"] = None
    fact_table["crop_id"] = None
    fact_table["year_id"] = None
    fact_table["season_id"] = None

    for j in range(df.shape[0]):
        fact_table["crop_id"][j] =  crop_dim.loc[crop_dim[crop_dim['crop'] == fact_table["Crop"][j]].index.values[0]]["crop_id"]
        fact_table["state_id"][j] =  state_dim.loc[state_dim[state_dim['state'] == fact_table["State"][j]].index.values[0]]["state_id"]
        fact_table["year_id"][j] =  year_dim.loc[year_dim[year_dim['year'] == fact_table["Crop_Year"][j]].index.values[0]]["year_id"]
        fact_table["season_id"][j] =  season_dim.loc[season_dim[season_dim['season'] == fact_table["Season"][j]].index.values[0]]["season_id"]

    fact_table.drop(['Crop','Crop_Year','Season','State'],axis = 1,inplace=True)

    return {"crop_dim":crop_dim.to_dict(orient="dict"),
        "year_dim":year_dim.to_dict(orient="dict"),
        "state_dim":state_dim.to_dict(orient="dict"),
        "season_dim":season_dim.to_dict(orient="dict"),
        "fact_table":fact_table.to_dict(orient="dict")}
        


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
