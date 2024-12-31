import typing as tp

import numpy as np
import matplotlib.pyplot as plt
import pingouin as pg

from seaborn_extensions._types import Figure, Axis, DataFrame
from seaborn_extensions._utils import get_grid_dims


def volcano_plot(
    stats: DataFrame,
    annotate_text: tp.Union[bool, tp.Sequence[str]] = True,
    diff_threshold: tp.Optional[float] = 0.05,
    n_top: int = None,
    invert_direction: bool = True,
    fig_kws: tp.Dict = None,
    axes: tp.Sequence[Axis] = None,
) -> Figure:
    """
    Assumes stats dataframe from seaborn_extensions.swarmboxenplot:
        - "hedges/coefs" column with effect sizes
        - "p-unc/pvalues" column with significance
        - "p-cor" column with significance corrected for multiple testing (will be added if missing)
        - "Variable" column with variable names (will use dataframe index if missing)
        If multiple tests are performed, each will be plotted in a subplot:
        - "A", "B" group identifiers such that hedges is positive value ~if mean(A) > mean(B).
    """
    if diff_threshold is not None:
        assert n_top is None
    else:
        assert n_top is not None

    if "hedges" not in stats.columns and "coefs" in stats.columns:
        print("Using columns 'coefs' as effect size estimates.")
        stats["hedges"] = stats["coefs"]
    if "p-unc" not in stats.columns and "pvalues" in stats.columns:
        print("Using columns 'pvalues' as effect size estimates.")
        stats["p-unc"] = stats["pvalues"]
    if "p-cor" not in stats.columns:
        print("Corrected p-values not given, using BH-FDR method.")
        stats["p-cor"] = pg.multicomp(stats["p-unc"], method="fdr_bh")[1]

    if (stats[["p-unc", "p-cor"]] == 0).any().any():
        print("p-values include zeros, replacing values around 1e-300 for display.")
        sel = stats["p-unc"] == 0
        stats.loc[sel, "p-unc"] = np.exp(-np.random.randint(280, 300, sel.sum())) ** 2.3
        stats.loc[stats["p-cor"] == 0, "p-cor"] = (
            np.exp(-np.random.randint(280, 300, sel.sum())) ** 2.3
        )

    if "Variable" not in stats.columns:
        print("Using dataframe index as variable names.")
        stats["Variable"] = stats.index

    for col in ["A", "B"]:
        if col not in stats.columns:
            stats[col] = col

    stats["A"] = stats["A"].astype(str)
    stats["B"] = stats["B"].astype(str)
    # Fix for matplotlib not supporting pandas Float64 type yet
    stats["hedges"] = stats["hedges"].astype(float)

    combs = stats[["A", "B"]].drop_duplicates().reset_index(drop=True)
    if invert_direction:
        stats["hedges"] *= -1.0  # convert to B / A which is often more intuitive
    stats["logp-unc"] = -np.log10(stats["p-unc"].fillna(1))
    stats["logp-cor"] = -np.log10(stats["p-cor"].fillna(1))
    stats["p-cor-plot"] = (stats["logp-cor"] / stats["logp-cor"].max()).fillna(1) * 5
    n, m = get_grid_dims(combs.shape[0])
    default_kws = dict(nrows=n, ncols=m, figsize=(4 * m, 4 * n), squeeze=False)
    default_kws.update(fig_kws or {})
    if axes is None:
        fig, axes = plt.subplots(**default_kws)
    else:
        axes = np.asarray(axes)
        if len(axes.shape) == 1:
            axes = axes.reshape((-1, 1))
        fig = axes.flatten()[0].figure
    idx = -1
    for idx, (a, b) in combs.iterrows():
        ax = axes.flatten()[idx]
        p = stats.query(f"A == '{a}' & B == '{b}'")
        ax.axvline(0, linestyle="--", color="grey")
        v = p["hedges"].abs().max()
        ax.scatter(
            p["hedges"],
            p["logp-unc"],
            c=p["hedges"],
            s=5 + (2 ** p["p-cor-plot"]),
            cmap="coolwarm",
            vmin=-v,
            vmax=v,
            rasterized=True,
        )
        ax.set(title=f"{b} / {a}", ylabel=None, xlabel=None)
        if annotate_text is not False:
            if annotate_text is True:
                if diff_threshold is not None:
                    ts = p.query(f"`p-cor` < {diff_threshold}").index
                else:
                    ts = p.sort_values("p-unc").head(n_top).index
            else:
                ts = p.loc[p["Variable"].isin(annotate_text)].index
            for t in ts:
                ax.text(
                    p.loc[t, "hedges"],
                    p.loc[t, "logp-unc"],
                    s=p.loc[t, "Variable"],
                    ha="left" if p.loc[t, "hedges"] > 0 else "right",
                )
    for ax in axes.flatten()[idx + 1 :]:
        ax.axis("off")

    for ax in axes[:, 0]:
        ax.set(ylabel="-log10(p-val)")
    for ax in axes[-1, :]:
        ax.set(xlabel="Hedges' g")

    if "p-cor-plot" in stats.columns:
        stats = stats.drop("p-cor-plot", axis=1)
    return fig
