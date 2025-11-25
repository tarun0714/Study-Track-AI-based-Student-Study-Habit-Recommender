from __future__ import annotations

import numpy as np
import pandas as pd


def correlation_improvement(df_before_after: pd.DataFrame) -> float:
    """
    Expects dataframe with columns: studentid, before_quizscore, after_quizscore
    Returns Pearson correlation between recommended adherence proxy and improvement.
    This is a placeholder until real feedback/adherence is integrated.
    """
    if not {"before_quizscore", "after_quizscore"}.issubset(df_before_after.columns):
        return float("nan")
    improvement = df_before_after["after_quizscore"] - df_before_after["before_quizscore"]
    # proxy adherence: assume equal weights for now
    adherence = np.ones_like(improvement)
    if improvement.std() == 0:
        return 0.0
    corr = np.corrcoef(adherence, improvement)[0, 1]
    return float(corr)
