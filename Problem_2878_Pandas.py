#Get the Size of a Dataframe, Feb 13 2025
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
