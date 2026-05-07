import marimo

__generated_with = "0.23.3"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fantasy Sports Decision Analytics

    This project analyzes decision-making effectiveness in fantasy cricket by comparing
    player selection patterns, performance outcomes and cost-profit behavior across a
    full IPL 2023 tournament.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem Statement

    How effective were my decision-making choices across an IPL 2023 fantasy cricket season?

    Three core questions:
    1. **Cost strategy** — Was my investment efficient relative to returns?
    2. **Player selection** — Was I picking the right players?
    3. **Captain / Vice-captain choices** — Were my C/VC selections aligned with top performers?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Data Overview

    Data was collected manually through structured Google Sheets templates across all
    matches of IPL 2023. Three datasets were used for this analysis:

    | Dataset | Granularity | Key fields |
    |---------|-------------|------------|
    | Match-level (dataset1) | One row per match | Cost, winnings, net P/L, team count |
    | Player-level (dataset2) | One row per player per match | Fantasy points, selection %, role, team |
    | Decision (dataset3) | One row per player per team composition per match | Selected players, Captain/Vice-captain (C/VC) choices |

    Dream Team (DT) data — the platform's optimal team for each match — is embedded in
    dataset3 and used throughout as the benchmark for decision quality.
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.patches import Patch
    import matplotlib.colors as mcolors
    from matplotlib.colors import TwoSlopeNorm
    import seaborn as sns
    from adjustText import adjust_text

    sns.set_theme(style='whitegrid', palette='pastel', font_scale=1)
    plt.rcParams.update({'figure.facecolor': '#F9F9F9', 'axes.facecolor': '#F9F9F9'})
    color_pl_positive = "#77B254"
    color_pl_negative = "#E16A54"
    color_cost_neutral = "#6294be"
    color_mean = "#2A1F2D"
    color_median = "#666765"
    color_C = '#B17F59'
    color_VC = '#BDB395'
    color_bg = "#F9F9F9"
    return (
        TwoSlopeNorm,
        adjust_text,
        color_C,
        color_VC,
        color_bg,
        color_cost_neutral,
        color_mean,
        color_median,
        color_pl_negative,
        color_pl_positive,
        mcolors,
        mo,
        np,
        pd,
        plt,
        sns,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Summary
    Across 66 IPL 2023 matches, a total investment of ₹5,809 resulted in a net overall loss, with only 21% of matches being profitable. Early assumptions pointed toward cost management as the primary issue, further analysis revealed that profitability was driven much more by decision quality than by cost investment.

    The analysis identified three weaknesses that were consistent across the tournament:
    - **Player selection inefficiency** - high-performing players were frequently under-selected, while low-to-moderate performers were repeatedly over-selected due to familiarity, popularity, and team bias.
    - **Weak Captain/Vice-Captain decisions** - suboptimal C/VC choices led to significant points leakage, with Vice-Captain selections showing particularly poor alignment with top match performers.
    - **Reactive cost adjustments** - the mid-tournament cost reduction was a response to early losses instead of outcomes of a structured decision framework. The player selection also shows signs of such reactive decisions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Key Insights
    - **Selection quality, not cost, was the primary driver of outcomes.**
        - Despite 76% of matches having cost under ₹100, profitability remained low, and average P/L was negative across all cost levels. Cost discipline alone did not improve results.

    - **High loss frequency, not loss magnitude, led to net loss.**
        - Only 21% of matches were profitable, indicating consistent underperformance amplified further by early large losses.

    - **Systematic gaps in player selection led to missed value.**
        - High-performing players were under-selected, while low-performing players were over-selected suggesting bias-driven decisions rather than value-driven decisions.

    - **Captain/Vice-captain decisions were a major source of point leakage.**
        - C/VC picks frequently ranked outside optimal positions, with Vice-captain decisions particularly weak, leaving too many points uncaptured.

    - **Biases (team, popularity, familiarity) significantly influenced decisions.**
        - Over-investment in certain teams and consistently selecting popular players despite their underperformance indicate biased decision-making rather than performance-based selection.
    """)
    return


@app.cell(hide_code=True)
def _(match_wise_matching_df, mo, usable_dset1):
    _total_cost = int(usable_dset1['Total cost'].sum())
    _net_pl = int(usable_dset1['Net P/L'].sum())
    _matches = int(usable_dset1['MatchID'].count())
    _pct_profitable = round(
        (usable_dset1['Net P/L'] > 0).sum() / _matches * 100
    )
    _avg_c_rank = round(match_wise_matching_df['c_rank'].mean(), 1)
    _c_in_dt_pct = round(match_wise_matching_df['c_in_dt'].mean() * 100)


    mo.vstack([
        mo.hstack([
            mo.stat(value=f"₹{_total_cost:,}", label="Total invested", caption="across all matches"),
            mo.stat(value=f"₹{_net_pl:,}", label="Net P/L", caption="overall season result", bordered=True),
            # mo.stat(value=str(_matches), label="Matches played", caption="with at least one team"),
            # mo.stat(value=f"{_pct_profitable}%", label="Profitable matches", caption="of total matches played"),
            # mo.stat(value=str(_avg_c_rank), label="Avg captain rank", caption="1 = match top scorer"),
            # mo.stat(value=f"{_c_in_dt_pct}%", label="Captain in Dream Team", caption="of matches"),
        ], justify='space-around'),

        mo.hstack([
            # mo.stat(value=f"₹{_total_cost:,}", label="Total invested", caption="across all matches"),
            # mo.stat(value=f"₹{_net_pl:,}", label="Net P/L", caption="overall season result", bordered=True),
            mo.stat(value=str(_matches), label="Matches played", caption="with at least one team"),
            mo.stat(value=f"{_pct_profitable}%", label="Profitable matches", caption="of total matches played"),
            # mo.stat(value=str(_avg_c_rank), label="Avg captain rank", caption="1 = match top scorer"),
            # mo.stat(value=f"{_c_in_dt_pct}%", label="Captain in Dream Team", caption="of matches"),
        ], justify='space-around')
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Data Preparation
    """)
    return


@app.cell(hide_code=True)
def _(pd):
    # Importing raw datasets from CSV files exported from sheets

    # Match-level data — one row per match
    dset1 = pd.read_csv('data/dataset1_export.csv')
    usable_dset1 = dset1[dset1['Total cost'] != 0].reset_index(drop=True)
    usable_dset1['Date'] = pd.to_datetime(usable_dset1['Date'], dayfirst=True)

    # Player-level data — one row per player per match, playing 11 only
    dset2 = pd.read_csv('data/dataset2_export.csv')
    usable_dset2 = dset2[dset2['x11'] != False].reset_index(drop=True)

    # Decision data — one row per player per team slot, selected players only
    dset3 = pd.read_csv('data/dataset3_export.csv')
    usable_dset3 = dset3[dset3['in_team'] == True].reset_index(drop=True)
    return usable_dset1, usable_dset2, usable_dset3


@app.cell(hide_code=True)
def _(usable_dset2):
    # Creating a reference table for player roles and teams

    player_wise_roles_teams = usable_dset2.groupby('Player_name').agg(
        Role=('Fantasy role', 'first'),
        Team=('Team', 'first')
    ).reset_index()
    return (player_wise_roles_teams,)


@app.cell(hide_code=True)
def _(pd, usable_dset1):
    # Calculating team-wise totals for cost, P/L, and matches played as home and away teams

    # Home team totals
    home_totals = usable_dset1.groupby('Home team', as_index=False).agg(
        home_cost=('Total cost', 'sum'),
        home_pl=('Net P/L', 'sum'),
        match_count=('MatchID', 'count')
    ).rename(columns={'Home team': 'Team'})

    # Away team totals
    away_totals = usable_dset1.groupby('Away team', as_index=False).agg(
        away_cost=('Total cost', 'sum'),
        away_pl=('Net P/L', 'sum'),
        match_count=('MatchID', 'count')
    ).rename(columns={'Away team': 'Team'})

    # Merging home and away totals to get overall team-wise totals
    team_wise_totals = pd.merge(home_totals, away_totals, how='outer', on='Team')
    team_wise_totals['total_cost'] = team_wise_totals['home_cost'] + team_wise_totals['away_cost']
    team_wise_totals['total_pl'] = team_wise_totals['home_pl'] + team_wise_totals['away_pl']
    team_wise_totals['total_matches'] = team_wise_totals['match_count_x'] + team_wise_totals['match_count_y']
    return (team_wise_totals,)


@app.cell(hide_code=True)
def _(usable_dset2, usable_dset3):
    # Merging player-level data with decision data to analyze selection choice and C/VC choices

    merged_usable_d2d3 = usable_dset3.merge(usable_dset2, on=['MatchID', 'Player_name'], how='inner')

    # Effective points include the C/VC multiplier (C=2x, VC=1.5x)
    merged_usable_d2d3['effective_points'] = (
        merged_usable_d2d3['Points']
        * merged_usable_d2d3['C/VC'].map({'C': 2, 'VC': 1.5}).fillna(1)
    )

    # My created teams (exclude DT)
    merged_usable_d2d3_myTeams = merged_usable_d2d3[
        ~merged_usable_d2d3['TeamID'].str.contains('DT')
    ].reset_index(drop=True)

    # Dream Team rows only
    merged_usable_d2d3_dt = merged_usable_d2d3[
        merged_usable_d2d3['TeamID'].str.contains('DT')
    ].reset_index(drop=True)
    return merged_usable_d2d3_dt, merged_usable_d2d3_myTeams


@app.cell(hide_code=True)
def _(merged_usable_d2d3_myTeams):
    # Aggregating points at the team level.
    # Will be used to analyze how well my teams performed relative to the Dream Team

    myteam_wise_df = merged_usable_d2d3_myTeams.groupby('TeamID', as_index=False).agg(
        MatchID=('MatchID', 'first'),
        effective_points=('effective_points', 'sum'),
        points=('Points', 'sum')
    )
    return (myteam_wise_df,)


@app.cell(hide_code=True)
def _(merged_usable_d2d3_dt, merged_usable_d2d3_myTeams, myteam_wise_df, pd):
    # Calculating overlap between my teams and the Dream Team per match
    # Overlap metrics: common points, common count, match pct (common count / 11), C/VC in DT flags

    # Build a lookup: MatchID -> set of DT player names
    dt_players_by_match = (
        merged_usable_d2d3_dt.groupby('MatchID')['Player_name']
        .apply(set)
        .to_dict()
    )
    dt_size = merged_usable_d2d3_dt.groupby('MatchID')['Player_name'].count().to_dict()

    # For each (TeamID, Player_name), flag whether player is in DT
    my_teams_annotated = merged_usable_d2d3_myTeams.copy()
    my_teams_annotated['in_dt'] = my_teams_annotated.apply(
        lambda row: row['Player_name'] in dt_players_by_match.get(row['MatchID'], set()),
        axis=1
    )

    # Aggregate per TeamID: common points, common count, match pct
    def _calc_overlap(g):
        match_id = g['MatchID'].iloc[0]
        return pd.Series({
            'common_points': g.loc[g['in_dt'], 'effective_points'].sum(),
            'common_count': int(g['in_dt'].sum()),
            'match_pct': round(g['in_dt'].sum() / dt_size.get(match_id, 11) * 100, 2),
        })
    team_dt_overlap = my_teams_annotated.groupby('TeamID').apply(_calc_overlap).reset_index()

    # C/VC in DT flags per team
    cvc_flags = my_teams_annotated[my_teams_annotated['C/VC'].isin(['C', 'VC'])].copy()
    cvc_in_dt = (
        cvc_flags.groupby(['TeamID', 'C/VC'])['in_dt']
        .any()
        .unstack(fill_value=False)
        .reset_index()
    )

    # Ensure C and VC columns exist and rename for clarity
    cvc_in_dt.columns.name = None
    if 'C' not in cvc_in_dt.columns:
        cvc_in_dt['C'] = False
    if 'VC' not in cvc_in_dt.columns:
        cvc_in_dt['VC'] = False
    cvc_in_dt = cvc_in_dt.rename(columns={'C': 'c_in_dt', 'VC': 'vc_in_dt'})

    # Merge the DT overlap metrics with C/VC in DT flags
    myTeams_matching = team_dt_overlap.merge(cvc_in_dt, on='TeamID', how='left')
    # Fill NaN values for C/VC flags with False (means no C/VC in DT for that team)
    myTeams_matching['c_in_dt'] = myTeams_matching['c_in_dt'].fillna(False)
    myTeams_matching['vc_in_dt'] = myTeams_matching['vc_in_dt'].fillna(False)

    # Merge back with team-level points df
    myteam_wise_df_full = myteam_wise_df.merge(myTeams_matching, on='TeamID', how='inner')
    return (myteam_wise_df_full,)


@app.cell(hide_code=True)
def _(merged_usable_d2d3_myTeams, myteam_wise_df_full):
    # Identifying the top-performing team per match based on common points with the DT

    top_teams_matching_list = (
        myteam_wise_df_full
        .loc[myteam_wise_df_full.groupby('MatchID')['common_points'].idxmax(), 'TeamID']
        .tolist()
    )

    # Final dataset of my teams that best matched with the DT per match
    myTopTeams_matching_df = merged_usable_d2d3_myTeams[
        merged_usable_d2d3_myTeams['TeamID'].isin(top_teams_matching_list)
    ].reset_index(drop=True)
    return (myTopTeams_matching_df,)


@app.cell(hide_code=True)
def _(usable_dset2):
    # Assigning ranks to players for each match based on points.
    # This will be used to analyze how well the C/VC choices aligned with the top performers in each match.

    usable_dset2_ranked = usable_dset2.copy()
    usable_dset2_ranked['Match_num'] = usable_dset2_ranked['MatchID'].str.extract(r'(\d+)').astype(int)
    usable_dset2_ranked = usable_dset2_ranked.sort_values(
        by=['Match_num', 'Points', 'Player_name'],
        ascending=[True, False, True]
    ).reset_index(drop=True)

    usable_dset2_ranked['points_rank'] = (
        usable_dset2_ranked.groupby('MatchID').cumcount() + 1
    )
    return (usable_dset2_ranked,)


@app.cell(hide_code=True)
def _(
    merged_usable_d2d3_dt,
    myTopTeams_matching_df,
    player_wise_roles_teams,
    usable_dset2_ranked,
):
    # Gathering match-wise data on my C/VC choices and the Dream Team's C/VC and player ranks in each match
    # data points included: my C/VC picks, their ranks in the match, the DT C/VC picks, their ranks, points on the table, and whether my C/VC was in the DT
    # along with role and team metadata on players.

    # Merge points rank into top teams df
    top_teams_ranked = myTopTeams_matching_df.merge(
        usable_dset2_ranked[['MatchID', 'Player_name', 'points_rank']],
        on=['MatchID', 'Player_name'],
        how='inner'
    )

    # My C selections per match
    my_c = (
        top_teams_ranked[top_teams_ranked['C/VC'] == 'C']
        .groupby('MatchID', as_index=False)
        .agg(my_c=('Player_name', 'first'), c_rank=('points_rank', 'first'), my_c_points=('effective_points', 'first'))
    )
    my_c['c_rank'] = my_c['c_rank'].astype(int)

    # My VC selections per match
    my_vc = (
        top_teams_ranked[top_teams_ranked['C/VC'] == 'VC']
        .groupby('MatchID', as_index=False)
        .agg(my_vc=('Player_name', 'first'), vc_rank=('points_rank', 'first'), my_vc_points=('effective_points', 'first'))
    )
    my_vc['vc_rank'] = my_vc['vc_rank'].astype(int)

    # DT C/VC per match
    dt_c = (
        merged_usable_d2d3_dt[merged_usable_d2d3_dt['C/VC'] == 'C']
        .groupby('MatchID', as_index=False)
        .agg(dt_c=('Player_name', 'first'), dt_c_points=('effective_points', 'first'))
    )
    dt_vc = (
        merged_usable_d2d3_dt[merged_usable_d2d3_dt['C/VC'] == 'VC']
        .groupby('MatchID', as_index=False)
        .agg(dt_vc=('Player_name', 'first'), dt_vc_points=('effective_points', 'first'))
    )

    # Combine into one match-wise C/VC dataframe
    match_wise_matching_df = (
        my_c
        .merge(my_vc, on='MatchID')
        .merge(dt_c, on='MatchID')
        .merge(dt_vc, on='MatchID')
    )

    # Calculate points on the table for my C/VC vs DT C/VC
    match_wise_matching_df['c_points_on_table'] = (
        match_wise_matching_df['dt_c_points'] - match_wise_matching_df['my_c_points']
    )
    match_wise_matching_df['vc_points_on_table'] = (
        match_wise_matching_df['dt_vc_points'] - match_wise_matching_df['my_vc_points']
    )

    # Flag whether my C/VC was in DT
    dt_players_per_match = merged_usable_d2d3_dt.groupby('MatchID')['Player_name'].apply(set).to_dict()
    match_wise_matching_df['c_in_dt'] = match_wise_matching_df.apply(
        lambda row: row['my_c'] in dt_players_per_match.get(row['MatchID'], set()), axis=1
    )
    match_wise_matching_df['vc_in_dt'] = match_wise_matching_df.apply(
        lambda row: row['my_vc'] in dt_players_per_match.get(row['MatchID'], set()), axis=1
    )

    # Add role and team metadata for C/VC players
    role_team_map = player_wise_roles_teams.set_index('Player_name')
    for _col in ['my_c', 'my_vc', 'dt_c', 'dt_vc']:
        match_wise_matching_df[f'{_col}_role'] = match_wise_matching_df[_col].map(role_team_map['Role'])
        match_wise_matching_df[f'{_col}_team'] = match_wise_matching_df[_col].map(role_team_map['Team'])
    return (match_wise_matching_df,)


@app.cell(hide_code=True)
def _(myTopTeams_matching_df, usable_dset2):
    # Calculating player-wise performance metrics related by points earned and collected, popularity (global and user), SEI(custom metric)
    # SEI measures how effectively a player's points were collectd by me relative to their global popularity.

    # Actual player-wise performance across all matches
    player_wise_actuals_df = usable_dset2.groupby('Player_name', as_index=False).agg(
        actual_points=('Points', 'sum'),
        matches_count=('Player_name', 'count'),
        sel_pct=('Sel_pct', 'mean')
    )
    player_wise_actuals_df['sel_pct_mod'] = player_wise_actuals_df['sel_pct'] / 10
    player_wise_actuals_df['avg_points'] = (
        player_wise_actuals_df['actual_points'] / player_wise_actuals_df['matches_count']
    )

    # My selections from top teams (by DT similarity)
    player_wise_my_df = myTopTeams_matching_df.groupby('Player_name', as_index=False).agg(
        Points=('Points', 'sum'),
        eff_points=('effective_points', 'sum'),
        selected_count=('Player_name', 'count')
    )

    # Merging my player-wise selection data with actual performance data
    player_wise_matching_df = player_wise_my_df.merge(player_wise_actuals_df, on='Player_name', how='inner')

    # Calculate my selection percentae for each player based on how many matches they were selected in by me vs total matches they played in
    player_wise_matching_df['sel_pct_my'] = (
        player_wise_matching_df['selected_count'] / player_wise_matching_df['matches_count'] * 10
    )

    # Calculate points on the table and percentage for each player
    player_wise_matching_df['points_on_table'] = (
        player_wise_matching_df['actual_points'] - player_wise_matching_df['Points']
    )
    player_wise_matching_df['points_on_table_pct'] = round(
        player_wise_matching_df['points_on_table'] / player_wise_matching_df['actual_points'] * 100, 0
    )

    # Calculate points earned percentage for each player
    player_wise_matching_df['points_earned_pct'] = round(
        player_wise_matching_df['Points'] / player_wise_matching_df['actual_points'] * 100, 0
    )

    # Calculate selection difference and percentage for each player
    player_wise_matching_df['selection_diff'] = (
        player_wise_matching_df['matches_count'] - player_wise_matching_df['selected_count']
    )
    player_wise_matching_df['selection_diff_pct'] = (
        (player_wise_matching_df['matches_count'] - player_wise_matching_df['selected_count'])
        / player_wise_matching_df['matches_count'] * 100
    )

    # Calculating custom metric - Selection Efficiency Index (SEI):
    # Measures how effectively a player's points were collectd by me relative to their global popularity.
    # SEI = (my_sel_pct / global_sel_pct) * points_earned_pct / 100
    player_wise_matching_df['SEI'] = (
        (player_wise_matching_df['sel_pct_my'] / player_wise_matching_df['sel_pct_mod'])
        * player_wise_matching_df['points_earned_pct']
        / 100       # just to scale down the number
    )
    return (player_wise_matching_df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section A: Cost & Profit
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A1 - Cost Behavior

    **What:** How much was spent per match, and how did spending evolve over the tournament?

    **Why:** Analysing spending patterns would help to assess the impact of cost management and to identify problematic and improvement areas.

    **How:** Cost distribution across all matches, cumulative spending trajectory, and weekly average cost trend.
    """)
    return


@app.cell(hide_code=True)
def _(color_bg, color_cost_neutral, color_mean, mo, plt, sns, usable_dset1):
    _matches_count = usable_dset1['MatchID'].count()

    # setting font for the chart
    plt.rcParams['font.family'] = 'DejaVu Sans'
    # chart config
    _bin_edges = list(range(0, 450, 50))
    fig_cost_hist, _ax = plt.subplots(figsize=(6, 5))
    sns.histplot(data=usable_dset1, x='Total cost',
                kde=False, bins=_bin_edges,
                color=color_cost_neutral, edgecolor='white', alpha=1, ax=_ax)
        # chart background
    fig_cost_hist.set_facecolor(color_bg)

    # Customize axes and labels
    _ax.tick_params(axis='x', labelsize=10)
    _ax.set_xlabel("Cost per match (₹)", fontsize=10, loc='left')
    _ax.yaxis.set_visible(False)

    # line and label for mean
    _mean_val = usable_dset1['Total cost'].mean()
    _ax.axvline(_mean_val, linestyle='-', linewidth=1,
                label='Mean cost per match', color=color_mean, alpha=0.3)
    _ax.text(
        _mean_val + 5, 0.95,
        f'Mean cost: ₹{int(round(_mean_val))}',
        transform=_ax.get_xaxis_transform(),
        color=color_mean, alpha=0.7,
        fontsize=9, fontfamily='Inter',
        va='top', ha='left'
    )


    # ensuring top margin for data labels
    _ax.set_ylim(0, _ax.get_ylim()[1] * 1.1)
    _height_threshold = _ax.get_ylim()[1] * 0.12  # bars shorter than 12% of axis height get label above

    # Add percentage labels on bar
    for _p in _ax.patches:
        _c = _p.get_height()
        if _c > 0:
            _pct = f'{int(round(_c / _matches_count * 100))}%'
            _is_tall = _c > _height_threshold
            _ax.text(
                _p.get_x() + _p.get_width() / 2.,
                _c * 0.4 if _is_tall else _c + 0.2,
                _pct,
                ha='center',
                va='center' if _is_tall else 'bottom',
                fontsize=10, fontfamily='Inter', fontweight='bold',
                color='#e0e0e0' if _is_tall else '#999999',
            )

    # title of the chart
    _ax.set_title("Cost per Match Distribution", fontsize=10, loc='left')
    # hide grid lines
    _ax.grid(False)

    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')

    # plt.tight_layout()


    # save the figure to a file
    fig_cost_hist.savefig('visuals/cost_histogram.png', dpi=300)
    mo.vstack([
        # mo.mpl.interactive(fig_cost_hist),
        fig_cost_hist,
    ], align='center')
    return


@app.cell(hide_code=True)
def _(mo, usable_dset1):
    mo.callout(mo.md(f"""
        ### Observations:
        **Cost distribution is right-skewed — spending was conservative overall.**
        - Mean cost per match was ₹{round(usable_dset1['Total cost'].mean())}
        - 76% of matches had a cost less than ₹100, indicating a cautious per match investment.
        - However, a small number of high-cost matches (above ₹200) pushed the average up, but failed to impact the outcomes favorably.
        """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ----
    """)
    return


@app.cell(hide_code=True)
def _(color_bg, color_cost_neutral, mo, pd, plt, sns, usable_dset1):
    # transforming data for cumulative and weekly avg cost analysis
    _dset = usable_dset1.copy()
    _dset['cumulative_total_cost'] = _dset['Total cost'].cumsum()
    _dset['cumulative_netpl'] = _dset['Net P/L'].cumsum()
    _dset['week'] = ((_dset['Date'] - _dset['Date'].min()).dt.days // 7) + 1

    _week_wise = (
        _dset.groupby('week')['Total cost']
        .mean()
        .reset_index()
        .rename(columns={'Total cost': 'avg_cost'})
    )
    # Mapping week to a representative MatchID (using the first match of each week)
    _week_wise['MatchID'] = _week_wise['week'].map(
        _dset.groupby('week')['MatchID'].first()
    )

    # Creating cost buckets
    bins = [0, 1000, 2000, 3000, 4000, 5000, 6000]
    labels = ["1k", "2k", "3k", "4k", "5k", "6k"]
    _dset['cost_bucket'] = pd.cut(
        _dset['cumulative_total_cost'],
        bins=bins,
        labels=labels
    )
    # dataframe for bar chart
    bucket_summary = _dset.groupby('cost_bucket').agg(
        match_count=('Net P/L', 'count'),
        avg_pl=('Net P/L', 'mean'),
        avg_cost=('Total cost', 'mean')
    ).reset_index()


    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'

    # ' chart: 'Did reducing cost lead to better profitability?'
    # chart config
    fig_cumul, _ax1 = plt.subplots(figsize=(6, 4))
    fig_cumul.set_facecolor(color_bg)

        # lineplot for avg cost (primary y-axis)
    sns.lineplot(
        data=bucket_summary,
        x='cost_bucket', y='avg_cost',
        marker='o', markersize=5,
        color=color_cost_neutral, label='Avg cost', linewidth=2,
        ax=_ax1
    )

        # lineplot for avg P/L (primary y-axis)
    sns.lineplot(
        data=bucket_summary,
        x='cost_bucket', y='avg_pl',
        marker='o', markersize=5,
        color='#E16A54',
        label='Avg P/L', linewidth=2,
        ax=_ax1
    )

        # barplot for match count (secondary y-axis)
    _ax2 = _ax1.twinx()
    sns.barplot(
        data=bucket_summary,
        x='cost_bucket', y='match_count',
        # label='Bar height = Match count',
        label=None,
        color=color_cost_neutral, alpha=0.1,
        ax=_ax2
     )

        # labels for first and last points
        # cost points
    first_cost = bucket_summary['avg_cost'].iloc[0]
    last_cost = bucket_summary['avg_cost'].iloc[-1]
    _ax1.text(
        0, first_cost + 5,
        f'₹{first_cost:,.0f}',
        ha='right',
        va='bottom',
        fontsize=10, fontfamily='Inter',
        color=color_cost_neutral
    )
    _ax1.text(
        len(bucket_summary) - 1, last_cost + 5,
        f'₹{last_cost:,.0f}',
        ha='right',
        va='bottom',
        fontsize=10, fontfamily='Inter',
        color=color_cost_neutral
    )
        # P/L points
    first_pl = bucket_summary['avg_pl'].iloc[0]
    last_pl = bucket_summary['avg_pl'].iloc[-1]
    _ax1.text(
        0, first_pl - 5,
        f'₹{first_pl:,.0f}',
        ha='center',
        va='top',
        fontsize=10, fontfamily='Inter',
        color='#E16A54'
    )
    _ax1.text(
        len(bucket_summary) - 1, last_pl - 5,
        f'₹{last_pl:,.0f}',
        ha='center',
        va='top',
        fontsize=10, fontfamily='Inter',
        color='#E16A54'
    )

        # adding text label in the bottom corner for bar height = match count
    _ax2.text(1, -0.135, 'Bar height = Match Count',
              transform=_ax2.transAxes, fontsize=8,
              va='top', ha='right', style='italic', color='gray', 
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.3))

        # Customize axes and labels
    _ax1.tick_params(axis='x', labelsize=9)
    _ax1.set_xlabel("Cumulative cost (₹)", fontsize=10, loc='left')
    _ax1.tick_params(axis='y', labelsize=9)
    _ax1.set_ylabel("Amount (₹)", fontsize=10, loc='bottom')
    _ax2.set_ylabel('')
    _ax2.set_yticks([])
        # margins for better label spacing
    _ax1.margins(0.1)
    # hide grid lines
    _ax1.grid(False)
    _ax2.grid(False)

        # title and legend
    _ax1.set_title("Did reducing cost lead to better profitability?", fontsize=10, loc='left')
    _ax1.legend(loc='upper right', fontsize=9, frameon=False)
        # chart border
    for _spine in _ax1.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')
    for _spine in _ax2.spines.values():
        _spine.set_linewidth(0)
        _spine.set_edgecolor('#CCCCCC')
    # plt.tight_layout()



    # ' chart: 'Weekly Average Cost'
    # chart config
    fig_weekly, _ax4 = plt.subplots(figsize=(5, 5))
    fig_weekly.set_facecolor(color_bg)

        # cost per match lineplot
    sns.lineplot(data=_dset, x='MatchID', y='Total cost',
                 alpha=0.1, linewidth=2,
                 label='Cost per Match', ax=_ax4, color='gray')

        # weekly avg cost lineplot
    sns.lineplot(data=_week_wise, x='MatchID', y='avg_cost',
                 marker='o', markersize=5, alpha=1.0, linewidth=3,
                 label='Weekly Average', ax=_ax4, color=color_cost_neutral)

        # Customize axes and labels
    _ax4.set_xlabel("Week of tournament", fontsize=10, loc='left')
    _ax4.set_xticks([])
    _ax4.set_ylabel('Cost per Match (₹)', fontsize=10, loc='bottom')
    _ax4.tick_params(axis='y', labelsize=9)
        # margins for better label spacing
    _ax4.margins(0.1)
    # hide grid lines
    _ax4.grid(False)

        # title and legend
    _ax4.set_title('Weekly Average Cost', fontsize=10, loc='left')
    _ax4.legend(loc='best', fontsize=9, frameon=False)

        # chart border
    for _spine in _ax4.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')
    # plt.tight_layout()

    # save the figures to files
    fig_cumul.savefig('visuals/cumulative_cost_pl.png', dpi=300)
    fig_weekly.savefig('visuals/weekly_avg_cost.png', dpi=300)

    # final layout with charts and insights
    mo.vstack([
        mo.hstack([
            mo.mpl.interactive(fig_cumul),
            # mo.mpl.interactive(fig_matchwise),
            mo.mpl.interactive(fig_weekly)
        ], widths=[0.6, 0.4], align='center')
    ], align='center')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - All the high cost(> ₹200) matches were in the first few weeks of the tournament along with high cost volatility.
        - Avg. cost per match drastically reduced in the middle weeks, and gradually kept increasing towards the end of the tournament.
            - For context, The first ₹3000 in cumulative cost was reached in just 16 matches and the next ₹3000 took 50 matches,
            a 3x reduction in cost incurred.
        - Avg. P/L saw only a marginal improvement (~15%) even as the avg. cost reduced drastically.
        This can mean that cost reduction was not sufficient for profitable outcome.
        - As evident by the avg. P/L being negative across all cost buckets, **the problem was not so much about cost management but
        mainly about selection quality**.
    """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ## Insights on Cost behavior:
        - I started aggressively, reduced costs sharply and maintained discipline through the middle, and gradually increased costs again
        towards the later stages of the tournament. The P/L improved with cost reduction but it was insufficient. This suggests that
        **cost discipline is not the primary driver of profitability. Selection quality and C/VC decisions have a much larger impact on
        outcomes.**
        - The 5x cost reduction in week 3 was in reaction to early losses. This suggests that **decisions in the early phase were more
        emotionally driven than analytically driven**.
        - High cost was not  the root cause of losses, it was selection quality. **Trying to solve cost without improving selection will not
        lead to profitable outcomes**.
        """), kind='info')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## A2 - Profit / Loss

    **What:** Match-by-match financial outcomes - where were profits made and losses incurred?

    **Why:** Cost tells one side of the story. P/L reveals whether the investment produced returns.
    <br>_spoiler: Persistent losses despite conservative spending suggests a selection quality problem, not purely a cost problem._

    **How:** P/L distribution,  cost vs. P/L relationship, and team-wise cost and P/L relationship
    """)
    return


@app.cell(hide_code=True)
def _(
    color_bg,
    color_mean,
    color_pl_negative,
    color_pl_positive,
    mo,
    plt,
    sns,
    usable_dset1,
):
    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'


    # chart: 'P/L distribution'
    # chart config
    fig_pl, _ax1 = plt.subplots(figsize=(7, 5))
    fig_pl.set_facecolor(color_bg)

        # histogram config
    _bin_edges = list(range(-300, 200, 50))
    _bars = sns.histplot(data=usable_dset1, x='Net P/L', kde=False,
                         bins=_bin_edges, ax=_ax1)

        # assigning bar colors based on profit/loss
    for _patch in _bars.patches:
        _patch.set_facecolor(color_pl_positive if _patch.get_x() >= 0 else color_pl_negative)

    # line and label for mean
    _ax1.axvline(usable_dset1['Net P/L'].mean(), linestyle='-',
                     label='Mean', color=color_mean, alpha=0.3)
    _mean_val = usable_dset1['Net P/L'].mean()
    _ax1.text(
        _mean_val + 5, 0.98,
        f'Mean P/L: ₹{int(round(_mean_val))}',
        transform=_ax1.get_xaxis_transform(),
        color=color_mean, alpha=0.7,
        fontsize=9,
        va='top', ha='left'
    )

    # text annotations for profit/loss match counts
    _profit_matchCount = (usable_dset1['Net P/L'] > 0).sum()
    _loss_matchCount = (usable_dset1['Net P/L'] < 0).sum()
    _ax1.text(
        0.85, 0.55,
        f'{_profit_matchCount} profitable\n matches',
        transform=_ax1.transAxes,
        color=color_pl_positive, alpha=0.8,
        fontsize=9, fontfamily='Inter',
        va='top', ha='center'
    )
    _ax1.text(
        0.35, 0.75,
        f'{_loss_matchCount} loss-making\nmatches',
        transform=_ax1.transAxes,
        color=color_pl_negative, alpha=0.7,
        fontsize=9, fontfamily='Inter',
        va='top', ha='center'
    )


    # Customize axes and labels
    _ax1.set_xticks(list(range(-300, 200, 50)))
    _ax1.set_xticklabels(list(range(-300, 200, 50)), fontsize=10)
    _ax1.set_xlabel("Net P/L per match (₹)", fontsize=10, loc='left')
    _ax1.set_ylabel("Match count", fontsize=10, loc='bottom')
    _ax1.tick_params(axis='y', labelsize=10)
    # margins for better label spacing
    _ax1.margins(0.1)
    # hide grid lines
    _ax1.grid(False)

    # title
    _ax1.set_title("P/L Distribution", fontsize=10, loc='left')

    # chart border
    for _spine in _ax1.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')
    # plt.tight_layout()

    # save fig
    fig_pl.savefig('visuals/pl_distribution.png', dpi=300)

    # final layout with chart and insights
    mo.vstack([
        fig_pl
    ], align='center')
    return


@app.cell(hide_code=True)
def _(mo, usable_dset1):
    mo.callout(mo.md(f"""
        ### Observations
        - **Avg. P/L** per match: ₹{round(usable_dset1['Net P/L'].mean(), 1)}
        - Only ~21% of matches were profitable.
        - Avg. profit per profitable match: ₹{round(usable_dset1.loc[usable_dset1['Net P/L'] > 0, 'Net P/L'].mean(), 1)}
        - Avg. loss per loss-making match: ₹{round(usable_dset1.loc[usable_dset1['Net P/L'] < 0, 'Net P/L'].mean(), 1)}
        - This indicates that loss magnitude was not that much of a problem, but the **frequency of losses was the main issue.**
        - Matches with heavy losses are outliers, but just **3 highest loss-making matches represented ~30% of total losses.**
        - Profits were capped but losses are much more varied. This also points to inefficient contest selection.
    """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(adjust_text, color_bg, mcolors, mo, plt, sns, usable_dset1):
    # creating a diverging color norm centered at 0 for Net P/L
    _divnorm = mcolors.TwoSlopeNorm(
        vmin=usable_dset1['Net P/L'].min(),
        vcenter=0,
        vmax=usable_dset1['Net P/L'].max()
    )

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'

    # chart: 'Cost vs. Net P/L per Match'
    # chart config
    fig_cost_pl, _ax = plt.subplots(figsize=(7, 6))
    fig_cost_pl.set_facecolor(color_bg)

    sns.scatterplot(data=usable_dset1, x='Total cost', y='Net P/L',
                    hue='Net P/L', palette='RdYlGn', hue_norm=_divnorm,
                    # size='Total cost', sizes=(20, 200),
                    s=125,
                    ax=_ax)

    texts=[]
    # Adding annotations for outliers
    for _idx, _row in usable_dset1.iterrows():
        if _row['Net P/L'] > 50 or _row['Net P/L'] < -100 or _row['Total cost'] > 200:
            text = _ax.text(
                _row['Total cost'] + 5, _row['Net P/L'] + 8,
                f"{_row['Home team']}-{_row['Away team']}",
                fontsize=9, color='#444', alpha=0.7, fontfamily='Inter'
            )
            texts.append(text)
    # Adjust text to avoid overlap
    adjust_text(texts)

    # reference line at y=0
    _ax.axhline(0, color='#000000', linestyle='-', linewidth=1, alpha=0.2)
    # Customize axes and labels
    _ax.set_xlabel("Total cost (₹)", fontsize=10, loc='left')
    _ax.tick_params(axis='x', labelsize=10)
    _ax.set_ylabel("Net P/L (₹)", fontsize=10, loc='bottom')
    _ax.tick_params(axis='y', labelsize=10)
    # grid for better readability
    _ax.grid(color='#E9E9E9', linewidth=0.7, alpha=0.4)
    # margins for better label spacing
    _ax.margins(0.12)


    # title and legend
    _ax.set_title("Cost vs. Net P/L per Match", fontsize=10, loc='left')
    # _ax.legend(frameon=False, ncol=2, fontsize=9, loc='upper right', bbox_to_anchor=(1.4, 1))
    _ax.legend().set_visible(False)


    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')

    # save fig
    fig_cost_pl.savefig('visuals/cost_vs_pl.png', dpi=300)

    mo.vstack([
        fig_cost_pl
    ], align='center')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - **Spending more did not produce better returns.**
        - Profitable matches are clustered below ₹100 cost.
            - Best returns in matches came from increasing the costs, but as establised above, 
            cost was not the driver for profitability, it was selection quality.
        - GT has featured in the worst-performing and also best-performing matches.
        - CSK and RR also look to be common with high-cost matches.
    """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(
    adjust_text,
    color_bg,
    color_cost_neutral,
    color_pl_negative,
    color_pl_positive,
    mo,
    plt,
    sns,
    team_wise_totals,
):
    _sorted = team_wise_totals.sort_values(by='total_cost', ascending=True)
    _sorted['pl_group'] = _sorted['total_pl'].apply(lambda x: 'positive' if x > 0 else 'negative')

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'
    # chart: 'Team-wise cost vs. P/L'
    # chart config
    fig_teamwise, _ax = plt.subplots(figsize=(6, 5))
    fig_teamwise.set_facecolor(color_bg)
    sns.scatterplot(data=_sorted, x='total_cost', y='total_pl',
                    # s=200,
                    size='total_matches', sizes=(150, 300),
                    hue='pl_group', palette={ 'positive': color_pl_positive, 'negative': color_pl_negative },
                    legend=False,
                    ax=_ax)

    # Label each dot with team name
    _texts = []
    for _, row in _sorted.iterrows():
        _text= _ax.text(
                 row['total_cost'] + 25,
                 row['total_pl']+5,
                 row['Team'],
                #  ha='right',
                 fontsize=9, fontfamily='Inter', alpha=0.8)
        _texts.append(_text)
    adjust_text(_texts)

    # reference lines for mean cost and mean P/L
    _ax.axhline(0, linestyle='-', color='black', alpha=0.1, linewidth=0.5)
    _ax.axhline(_sorted['total_pl'].mean(), linestyle='--', color=color_pl_negative, alpha=0.3, linewidth=1)
    _ax.text(
        _ax.get_xlim()[0] + 955, _sorted['total_pl'].mean() + 5,
        'Mean P/L',
        color=color_pl_negative, alpha=0.7,
        fontsize=8, fontfamily='Inter'
    )
    _ax.axvline(_sorted['total_cost'].mean(), linestyle='--', color=color_cost_neutral, alpha=0.3, linewidth=1)
    _ax.text(
        _sorted['total_cost'].mean() + 15, _ax.get_ylim()[0] + 0,
        'Mean Cost',
        color=color_cost_neutral, alpha=0.7,
        fontsize=8, fontfamily='Inter'
    )

    # Customize axes and labels
    _ax.set_xlabel("Total cost (₹)", fontsize=10, loc='left')
    _ax.tick_params(axis='x', labelsize=10)
    _ax.set_ylabel("Net P/L (₹)", fontsize=10, loc='bottom')
    _ax.tick_params(axis='y', labelsize=10)
    # grid for better readability
    _ax.grid(color='#E9E9E9', linewidth=0.7, alpha=0.4)
    # margins for better label spacing
    _ax.margins(0.1)

    # title
    _ax.set_title("Team-wise Total Cost vs. Net P/L", fontsize=10, loc='left')

    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')

    # save fig
    fig_teamwise.savefig('visuals/teamwise_cost_pl.png', dpi=300)

    # final layout with chart and insights
    mo.vstack([
        fig_teamwise
    ], align='center')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - No team generated positive returns in the entire tournament.
        - GT was a clear outlier. Heavy investments with GT resulted in heavy losses as well.
        - KKR, RCB and LSG were more cost-efficient compared to other teams.
        - Investments in MI and CSK have performed better than RR and GT.
    """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Insights on P/L patterns:
        - **Higher loss frequency** was the problem, not loss magnitude.
            - Focus should be on **improving selection accuracy** which would have a larger impact on the P/L outcome
            than cost optimisation.
        - There was clear bias towards GT which did not pay off.
            - GT being the most invested in and worst returning team indicates a strong bias and clear
            misjudgment of GT's strengths and weaknesses.
        - Along with emotional bias towards teams, I also overlooked and underestimated teams that could have
        been leveraged to generate profits.
        - Higher conviction needs to be expressed through better player selection rather than just higher costs.
        """), kind='info')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section B: Player Selection Quality

    **What:** How well were players chosen relative to their actual performance?

    **Why:** Efficiently and consistently selecting high-performing players is the primary driver of profits.
    Along with good player selection, timely Captain/Vice-captain decisions are key for success.

    This section analyses player selection relative to their performance and popularity.

    **How:** Assessing my player selection vs their actual performance and using SEI for assessing my selections relative to player popularity.

    Using a custom metric - **Selection Efficiency Index (SEI)** - SEI measures how effectively a player's points were collectd by me relative to their global popularity.
    It combines user selection frequency, global platform popularity, and points earned percentage into a single score per player.


    $$SEI = \frac{\text{user\_sel\_freq}}{\text{global\_sel\_pct}} \times \frac{\text{points\_earned\_pct}}{100}$$

    Players with high SEI were selected more often than their global popularity and also more of their points were collected.

    > **Note:** Selection data is drawn from the **top team per match** - the team
    > that overlapped most with the Dream Team (DT) based on points. Using all teams
    > would dilute the signal with speculative picks. The top team filter isolates the decisions
    > that were most informed.
    """)
    return


@app.cell(hide_code=True)
def _(color_bg, color_mean, mo, player_wise_matching_df, plt, sns):
    _df = player_wise_matching_df.copy()

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'

    # ' chart: 'Actual vs. Collected Points per Player'
    # chart config
    _fig_scatter_pts, _ax = plt.subplots(figsize=(8,8))
    _fig_scatter_pts.set_facecolor(color_bg)
    sns.scatterplot(
        data=_df,
        x='actual_points', y='points_earned_pct',
        size='points_on_table_pct', sizes=(100, 200),
        hue='selection_diff',
        palette='copper_r', alpha=0.65,
        ax=_ax,
    )

    # Adding reference lines
        # mean lines
    _ax.axvline(x=_df['actual_points'].mean(), label=None, color=color_mean, alpha=0.2)
    _ax.text(
        _df['actual_points'].mean() + 5, _ax.get_ylim()[0] + 1,
        'Mean actual points',
        color=color_mean, alpha=0.7,
        fontsize=8, fontfamily='Inter'
    )
    _ax.axhline(y=_df['points_earned_pct'].mean(), label=None, color=color_mean, alpha=0.2)
    _ax.text(
        _ax.get_xlim()[1] - 15, _df['points_earned_pct'].mean() + 1,
        'Mean points earned %',
        color=color_mean, alpha=0.7,
        fontsize=8, fontfamily='Inter',
        ha='right'
    )


    # Customize axes and labels
    _ax.set_xlabel("Total points earned", fontsize=10, loc='left')
    _xlim = max(_df['actual_points'].max(), _df['points_earned_pct'].max()) * 1.05
    _ax.set_xlim(right=_xlim)
    _ax.set_xticks(list(range(0, int(_xlim), 100)))
    _ax.set_xticklabels(list(range(0, int(_xlim), 100)), fontsize=9)
    _ax.set_ylabel(" % of points collected by me", fontsize=10, loc='bottom')
    _ylim = min(_df['actual_points'].max(), _df['points_earned_pct'].max()) * 1.05
    _ax.set_ylim(top=_ylim)
    _ax.set_yticks(list(range(0, int(_ylim)+1, 10)))
    _ax.set_yticklabels(list(range(0, int(_ylim)+1, 10)), fontsize=9)
    # grid for better readability
    _ax.grid(color='#F2F2F2', linewidth=0.7)
    # margins for better label spacing
    _ax.margins(0.1)

    # title and legend
    _ax.set_title("How effective was my player selection?", fontsize=10, loc='left')
        # custom labels for legend
    _handles, _labels = _ax.get_legend_handles_labels()
    _labels = ['Selection Difference\n(matches)' if l == 'selection_diff' else l for l in _labels]
    _labels = ['\n\nPoints left on table\n(%)' if l == 'points_on_table_pct' else l for l in _labels]
    _ax.legend(_handles, _labels, frameon=False, ncol=1, fontsize=8, loc='upper right', bbox_to_anchor=(1.3, 1))

    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')

    # plt.tight_layout()

    # save fig
    _fig_scatter_pts.savefig('visuals/points_captured_scatter.png', dpi=300)

    mo.vstack([
        _fig_scatter_pts
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - Over-invested in low-moderate performers (top left quadrant)
            - There are several players under 200 total points that have almost 100% points collected.
            - There are many dots in this quadrant, suggesting that a large portion of **selections were concentrated on low performing players**.
        - Some correctly ignored and some missed opportunities (bottom left quadrant) 
            - Darker colored dots are on the right portion of the quadrant suggesting that I picked moderately performing players less often compared to other low performing players.
            - **Cluster of darker dots at near 0% points collected is a big concern** because these players were available for selection frequently but I barely collected any of their points,
            indicating strong bias against them.
        - Biggest missed opportunities (bottom right quadrant)
            - Darker and bigger dots for players between 500-800 total points indicate that I **missed out on a lot of points for high-value players**. This is the most important area to improve.
        - Best selections (top right quadrant)
            - Missed out on a big chunk of points for players with more than 600 total points. Although I selected them more often, as seen by light colored dots, but could not maximise their points.
        - Overall
            - Players between 300-700 total points is the biggest selection gap.
            - Darker dots increase more in the right portion of the chart indicating that my selection of higher-performing players was poor.
        """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Insights on player selection quality:
        - Selection seems to be based on familiarity
            - High capture rate on low-scoring players suggests selection based on familiarity even when they were not performing.
            - Selection should be driven by value, not comfort or familiarity
            - Selection was driven by comfort or familiarity, not by value.
        - 300-700 total points band represents a systematic blind spot
            - These are mid-tier players who scored meaningfully to make a difference in the outcome but whom I consistently ignored for my selections.
            - These players represent a sizable chunk of all available players, so improving selection accuracy here is important.
        - Strong bias against certain players
            - The dark cluster at almost 0% capture for players between 200-400 points indicates that I might have had a strong bias against them because I have not selected them consistently
            for more than 10 matches. Could be useful to identify who these players are and their roles and teams.
        - Elite player misses are fewer but more costly
            - Any % of points left on table for players more than 600 points has had a much larger impact and these are the expensive selection failures.
        - Cost management vs selection quality
            - Above observations confirm that cost management had only a marginal effect, and player selection needs to be improved significantly.
            - Selection quality is the more impactful problem to solve instead of cost.
    """), kind='info')
    return


@app.cell(hide_code=True)
def _(
    TwoSlopeNorm,
    color_bg,
    color_median,
    mo,
    player_wise_matching_df,
    plt,
    sns,
):
    _df = player_wise_matching_df.copy()
    # creating a diverging color norm centered at 1 for SEI
    _norm = TwoSlopeNorm(vmin=0, vcenter=1.0, vmax=_df['SEI'].max())

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'
    # ' chart: 'Selection Efficiency Index (SEI) — Popularity vs. Performance'
    # chart config
    fig_sei, _ax = plt.subplots(figsize=(8, 8))
    fig_sei.set_facecolor(color_bg)
    sns.scatterplot(
        data=_df,
        x='actual_points',       # global platform popularity (x-axis)
        y='sel_pct_mod',        # average points per match (y-axis)
        size='sel_pct_my', sizes=(50, 350),
        hue='SEI', hue_norm=_norm,
        palette='bwr', alpha=0.6,
        edgecolor='#727272',
        ax=_ax,
    )


    # Adding reference lines
        # median lines
    _ax.axvline(x=_df['actual_points'].median(), label=None, color=color_median, alpha=0.2)
    _ax.text(
        _df['actual_points'].median() + 5, _ax.get_ylim()[0] + 9.5,
        'Median points',
        color=color_median, alpha=0.7,
        fontsize=8, fontfamily='Inter'
    )
    _ax.axhline(y=_df['sel_pct_mod'].median(), label=None, color=color_median, alpha=0.2)
    _ax.text(
        _ax.get_xlim()[0] + 1250, _df['sel_pct_mod'].median() + 0.1,
        'Median selection %',
        color=color_median, alpha=0.7,
        fontsize=8, fontfamily='Inter'
    )


    # Customize axes and labels
    _ax.set_xlabel("Total points earned", fontsize=10, loc='left')
    _ax.set_xticks(list(range(0, int(_df['actual_points'].max())+1, 100)))
    _ax.set_xticklabels(list(range(0, int(_df['actual_points'].max())+1, 100)), fontsize=10)
    _ax.set_ylabel("Global selection %", fontsize=10, loc='bottom')
    _ax.set_yticks(list(range(0, int(_df['sel_pct_mod'].max())+1, 1)))
    _ax.set_yticklabels(list(range(0, int(_df['sel_pct_mod'].max())+1, 1)), fontsize=10)
    # grid for better readability
    _ax.grid(color='#F2F2F2', linewidth=0.7)
    # margins for better label spacing
    _ax.margins(0.1)

    # title and legend
    _ax.set_title("Selection Efficiency Index (SEI) — Popularity vs. Performance", fontsize=10, loc='left')
    _handles, _labels = _ax.get_legend_handles_labels()
    _labels = ['\nUser\nselection %' if l == 'sel_pct_my' else l for l in _labels]
    _ax.legend(_handles, _labels, frameon=True, ncol=1, fontsize=9, loc='lower right')

    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')

    plt.tight_layout()
    plt.savefig('visuals/sei_scatter.png', dpi=300, bbox_inches='tight')

    mo.vstack([
        fig_sei
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - Overall the high performing players were also popular players, but there are more blueish dots in the top right quadrant suggesting that my selection of those players was not efficient as
        compared to the crowd, despite these being the most obvious picks. Ideally there should be more of white or slight reddish dots.
        -  In the top left quadrant, there are a few reddish and light blue dots suggesting that I was stuck expecting the low-moderate players to perform as much as the crowd and even more with
        some players.
        - In the bottom right quadrant, I did identify 2-3 players who were hidden gems, meaning they performed when the crowd was not expecting them to and I selected them in my teams.
        However, these were too few to make a positive impact on the outcomes; most are small dark blue dots suggesting that there were more gems whom I missed out on.
        - In the bottom left quadrant, these are players who were less popular and also low performing. A bunch of red dots here suggest that my selections in these players was the least fruitful.
        - SEI distribution is inverted from optimal. Right half is where the frequency of SEI >=1 should be more, but instead it is the opposite.
    """), kind='neutral')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Insights On Player Selection Efficiency:
        - High SEI is concentrated on the left portion with low performing players where selecting better than the crowd had no meaningful impact. SEI needs to be improved for high performing players to have a meaningful impact on the P/L.
        - There was a lot of unrealised opportunity with high performing and less popular players. These players are where I could have edged out an  advantage over the crowd.
        - For popular and high performing players the only way to match or gain a meaningful edge is through C/VC multiplier. As selection of these players is more or less obvious in the middle to late stages of the tournament, the analytical effort should be on proper captain and vice captain decisions for these players.
        - I seemed to have used popularity as an indicator for performance quality and **relied much more on popular players despite their under-performance**.
    """), kind='info')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Section C: C/VC Decision Quality

    **What:** How well were my Captain and Vice-Captain choices aligned with the match's best performers?

    **Why:** In fantasy cricket, C earns 2× points and VC earns 1.5×. A poor C/VC pick is the single
    biggest points leakage - it makes a big impact on every match regardless of how good the rest of the team is.

    **How:** Three complementary lenses:
    - **DT overlap** — was my C/VC even in the Dream Team?
    - **Rank** — where did my C/VC finish in the points leaderboard for that match?
    - **Points on table** — how many additional points would the optimal C/VC have earned?
    """)
    return


@app.cell(hide_code=True)
def _(match_wise_matching_df, mo):
    mo.vstack([
            mo.stat(value=f"{match_wise_matching_df[match_wise_matching_df['c_in_dt']==True].count()['MatchID']} ({round(match_wise_matching_df[match_wise_matching_df['c_in_dt']==True].count()['MatchID'] / len(match_wise_matching_df) * 100)}%)",
            label="Captain selections in DT",
            caption=f"out of {len(match_wise_matching_df)} matches"),
    mo.stat(value=f"{match_wise_matching_df[match_wise_matching_df['vc_in_dt']==True].count()['MatchID']} ({round(match_wise_matching_df[match_wise_matching_df['vc_in_dt']==True].count()['MatchID'] / len(match_wise_matching_df) * 100)}%)",
            label="Vice-captain selections in DT",
            caption=f"out of {len(match_wise_matching_df)} matches"),
    mo.md(r"""
        Even if the C/VC was at the 11th rank, it still counts as being part of the Dream Team (DT). So, this number on its own is not that valuable.
    """)
    ])
    return


@app.cell(hide_code=True)
def _(color_C, color_VC, match_wise_matching_df, mo, np, plt, sns):
    _df = match_wise_matching_df.copy()
    # aggregating based on C and VC ranks
    _df_c_rank = _df.groupby('c_rank', as_index=False).agg(
        count=('MatchID', 'count'),
        avg_points_on_table=('c_points_on_table', 'mean')
    ).sort_values(by='c_rank').reset_index(drop=True)
    _df_vc_rank = _df.groupby('vc_rank', as_index=False).agg(
        count=('MatchID', 'count'),
        avg_points_on_table=('vc_points_on_table', 'mean')
    ).sort_values(by='vc_rank').reset_index(drop=True)
    _df_vc_rank
    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans '
    # ' chart: 'Captain and Vice-Captain rank distribution'
    # chart config
    _all_ranks = sorted(set(_df_c_rank['c_rank'].tolist() + _df_vc_rank['vc_rank'].tolist()))
    fig_rank, _axes = plt.subplots(1, 2, figsize=(14, 5), sharex=True, sharey=True)
    sns.barplot(data=_df_c_rank, x='c_rank', y='count',
                order=_all_ranks,
                color=color_C, alpha=0.8,
                ax=_axes[0])
    sns.barplot(data=_df_vc_rank, x='vc_rank', y='count',
                 order=_all_ranks,
                 color=color_VC, alpha=0.8,
                 ax=_axes[1])

    # customize axes and labels
    _axes[0].set_xlabel('Captain rank (1 = Ideal rank)', fontsize=10, loc='left')
    _axes[0].set_xticks(np.arange(1, 26, 2))
    _axes[0].tick_params(axis='x', labelsize=10)
    _axes[0].set_ylabel('Count', fontsize=10, loc='center')
    _axes[0].set_yticks(np.arange(0, 11, 1))
    _axes[0].tick_params(axis='y', labelsize=10)
    _axes[1].set_xlabel('Vice-Captain rank (2 = Ideal rank)', fontsize=10, loc='left')
    _axes[1].tick_params(axis='x', labelsize=10)
    _axes[1].tick_params(axis='y', labelsize=10)
    # grid for better readability
    for _ax in _axes:
        _ax.grid(color='#F2F2F2', linewidth=0.7)
        _ax.grid(axis='x', visible=False)


    # title
    _axes[1].set_title("Vice-Captain Rank Distribution", fontsize=10, loc='left')
    _axes[0].set_title("Captain Rank Distribution", fontsize=10, loc='left')

    # chart border
    for _spine in _axes[0].spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')
    for _spine in _axes[1].spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')


    # plt.tight_layout()

    # save fig
    fig_rank.savefig('visuals/cvc_rank_distribution.png', dpi=300, bbox_inches='tight')

    mo.vstack([
        fig_rank
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - Captain decisions:
            - Rank 1 and 2 represent 24% of all matches. Even though the distribution is right skewed,
            the tail is long and populated enough to make the distribution relatively spread across.
            - Two secondary clusters around ranks 7-11 and ranks 15-18 indicate that were **many suboptimal captain decisions**.
        - VC distribution is much worse than C. The VC mode is at rank 10.
            - Neither is there any concentration around optimal ranks. It is pretty much a flat distribution
            except the mode at rank 10. This indicates that the **VC decisions were consistently worse** and
            whatever process was for selecting VC needs to be looked at carefully.
    """))
    return


@app.cell(hide_code=True)
def _(color_bg, match_wise_matching_df, mo, np, plt, sns):
    match_wise_matching_df['c_points_on_table_pct'] = match_wise_matching_df['c_points_on_table'] / match_wise_matching_df['dt_c_points'] * 100
    match_wise_matching_df['vc_points_on_table_pct'] = match_wise_matching_df['vc_points_on_table'] / match_wise_matching_df['dt_vc_points'] * 100

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'
    # ' chart: 'Points Left on Table vs. C/VC Rank'
    # chart config
    fig_pts_table, _axes = plt.subplots(1, 2, figsize=(12, 5), sharey=False)
    fig_pts_table.set_facecolor(color_bg)
    for _ax, _x_col, _title, _color in [
        (_axes[0], 'c_points_on_table_pct', 'Captain — Points Left on Table', '#B17F59'),
        (_axes[1], 'vc_points_on_table_pct', 'Vice-Captain — Points Left on Table', '#BDB395'),
    ]:
        _rank_col = 'vc_rank' if 'vc_points' in _x_col else 'c_rank'
        sns.scatterplot(
            data=match_wise_matching_df,
            x=_x_col, y=_rank_col,
            color=_color, alpha=0.75,
            s=60,
            ax=_ax,
        )
        # Adding reference line at x=0
        _ax.axvline(0, color='#AAAAAA', linewidth=0.8, linestyle='-', alpha=0.5)
        # Customize axes and labels
        _ax.set_xlabel("Points on table (DT optimal - my pick)", fontsize=10, loc='left')
        _ax.set_ylabel("My pick's rank", fontsize=10, loc='bottom')
        _ax.set_yticks(np.arange(1, 26, 2))
        # grid for better readability
        _ax.grid(color='#F2F2F2', linewidth=0.7)

        # title
        _ax.set_title(_title, fontsize=10, loc='left')

        # chart border
        for _spine in _ax.spines.values():
            _spine.set_linewidth(1)
            _spine.set_edgecolor('#CCCCCC')

    # save fig
    fig_pts_table.savefig('visuals/points_on_table_vs_rank.png', dpi=300, bbox_inches='tight')
    mo.vstack([
        fig_pts_table
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - Naturally, as the rank worsens, points left on table will increase.
        - The important observation from these charts is that missing C rank even by 1-2 positions makes a
        significant impact. Missing VC decisions by a few ranks has not been that detrimental.
        - Too many instances of both C and VC picks having ranks worse than 5.
        Such matches drastically increase the likelihood of a loss.
    """))
    return


@app.cell(hide_code=True)
def _(color_bg, match_wise_matching_df, mcolors, mo, np, plt):
    def darken_color(color, factor=0.6):
        """Factor < 1 darkens, > 1 lightens"""
        _r, _g, _b, _a = mcolors.to_rgba(color)
        return (_r * factor, _g * factor, _b * factor, 1.0)


    # Data prep for Player-level C comparison
    _mc = match_wise_matching_df['my_c'].value_counts().reset_index()
    _mc.columns = ['Player_name', 'my_count']
    _dc = match_wise_matching_df['dt_c'].value_counts().reset_index()
    _dc.columns = ['Player_name', 'dt_count']
    _pw_c = _mc.merge(_dc, on='Player_name', how='outer').fillna(0)
    _pw_c[['my_count', 'dt_count']] = _pw_c[['my_count', 'dt_count']].astype(int)

    # Data prep for Player-level VC comparison
    _mvc = match_wise_matching_df['my_vc'].value_counts().reset_index()
    _mvc.columns = ['Player_name', 'my_count']
    _dvc = match_wise_matching_df['dt_vc'].value_counts().reset_index()
    _dvc.columns = ['Player_name', 'dt_count']
    _pw_vc = _mvc.merge(_dvc, on='Player_name', how='outer').fillna(0)
    _pw_vc[['my_count', 'dt_count']] = _pw_vc[['my_count', 'dt_count']].astype(int)

    # diff = set(_pw_vc['Player_name']).difference(set(_pw_c['Player_name']))
    # intersect = set(_pw_vc['Player_name']).intersection(set(_pw_c['Player_name']))
    # print(len(intersect))
    # print(len(_pw_c))
    # print(len(_pw_vc))

    # # _x_vals = np.linspace(-0.5, 10, 200)

    # C bias calculation and sorting
    _pw_c['bias'] = _pw_c['my_count'] - _pw_c['dt_count']  # positive = over-preference
    _pw_c['bias_direction'] = _pw_c['bias'].apply(lambda x: 'Over' if x > 0 else ('Under' if x < 0 else 'Neutral'))
    _pw_c_sorted = _pw_c.sort_values(['bias_direction', 'dt_count'], ascending=False)

    # VC bias calculation and sorting
    _pw_vc['bias'] = _pw_vc['my_count'] - _pw_vc['dt_count']  # positive = over-preference
    _pw_vc['bias_direction'] = _pw_vc['bias'].apply(lambda x: 'Over' if x > 0 else ('Under' if x < 0 else 'Neutral'))
    _pw_vc_sorted = _pw_vc.sort_values(['bias_direction', 'dt_count'], ascending=False)

    # setting font for all charts
    plt.rcParams['font.family'] = 'DejaVu Sans'
    # chart: 'Player-level C comparison'
    # chart config
    _row_height = 0.25 # height per player row
    _n_c = len(_pw_c_sorted['Player_name'].unique())
    _n_vc = len(_pw_vc_sorted['Player_name'].unique())
    fig_c, _ax = plt.subplots(figsize=(4, _n_c * _row_height))
    fig_c.set_facecolor(color_bg)
    fig_vc, _ax1 = plt.subplots(figsize=(4, _n_vc * _row_height))
    fig_vc.set_facecolor(color_bg)


    # plotting C
    _ax.scatter(_pw_c_sorted['my_count'], _pw_c_sorted['Player_name'], color='#884d17', label='My count', s=20, alpha=0.8)
    _ax.scatter(_pw_c_sorted['dt_count'], _pw_c_sorted['Player_name'], color='#2a7c4d', label='DT count', s=20, alpha=0.8)
    # plotting VC
    _ax1.scatter(_pw_vc_sorted['my_count'], _pw_vc_sorted['Player_name'], color='#884d17', label='My count', s=20, alpha=0.8)
    _ax1.scatter(_pw_vc_sorted['dt_count'], _pw_vc_sorted['Player_name'], color='#2a7c4d', label='DT count', s=20, alpha=0.8)


    # for C - Shade each contiguous group as one block
    for _direction, _group in _pw_c_sorted.groupby('bias_direction', sort=False):
        if _direction == 'Over': _color = '#dd8484'
        elif _direction == 'Under': _color = '#4f73b6'
        else: _color = '#ececec'


        _idx_positions = [_pw_c_sorted.index.get_loc(i) for i in _group.index]
        _top = max(_idx_positions)
        # coloring the background of each bias region
        _ax.axhspan(min(_idx_positions) - 0.5, max(_idx_positions) + 0.5,
                    alpha=0.1, color=_color)

        # Add region label
        _ax.text(
            _ax.get_xlim()[1] -0.2,  # far right of chart
            _top -0.5,               # vertical midpoint of region
            f'{_direction.capitalize()}: {len(_group)}',
            fontsize=9,
            color=darken_color(_color, factor=0.6),
            # color=saturate_color(_color),
            alpha=0.8,
            va='center', ha='right',
        )

    # for VC - Shade each contiguous group as one block
    for _direction, _group in _pw_vc_sorted.groupby('bias_direction', sort=False):
        if _direction == 'Over': _color = '#dd8484'
        elif _direction == 'Under': _color = '#4f73b6'
        else: _color = '#ececec'


        _idx_positions = [_pw_vc_sorted.index.get_loc(i) for i in _group.index]
        _top = max(_idx_positions)
        # coloring the background of each bias region
        _ax1.axhspan(min(_idx_positions) - 0.5, max(_idx_positions) + 0.5,
                    alpha=0.1, color=_color)

        # Add region label
        _ax1.text(
            _ax1.get_xlim()[1] -0.2,  # far right of chart
            _top -0.5,               # vertical midpoint of region
            f'{_direction.capitalize()}: {len(_group)}',
            fontsize=9,
            color=darken_color(_color, factor=0.6),
            # color=saturate_color(_color),
            alpha=0.8,
            va='center', ha='right',
        )



    # for C - Color the connecting lines based on bias direction
    for _, _row in _pw_c_sorted.iterrows():
        _color = '#dd8484' if _row['bias'] > 0 else '#4f73b6'
        _ax.hlines(_row['Player_name'], _row['dt_count'], _row['my_count'], 
                   color=_color, alpha=0.2, linewidth=3)
    # for VC - Color the connecting lines based on bias direction
    for _, _row in _pw_vc_sorted.iterrows():
        _color = '#dd8484' if _row['bias'] > 0 else '#4f73b6'
        _ax1.hlines(_row['Player_name'], _row['dt_count'], _row['my_count'], 
                   color=_color, alpha=0.2, linewidth=3)

    # for C - Customize axes and labels
    _ax.set_xticks(np.arange(0, _pw_c_sorted[['my_count', 'dt_count']].values.max() + 1, 1))
    _ax.set_xticklabels(np.arange(0, _pw_c_sorted[['my_count', 'dt_count']].values.max() + 1, 1), fontsize=10)
    _ax.tick_params(axis='y', labelsize=9)
    # grid for better readability
    _ax.grid(color='#F2F2F2', linewidth=0.7, axis='x', alpha=0.2)

    _ax_top = _ax.secondary_xaxis('top')
    _ax_top.set_xticks(np.arange(0, _pw_c_sorted[['my_count', 'dt_count']].values.max() + 1, 1))
    _ax_top.tick_params(axis='x', labelsize=10, length=0)

    # for VC - Customize axes and labels
    _ax1.set_xticks(np.arange(0, _pw_vc_sorted[['my_count', 'dt_count']].values.max() + 1, 1))
    _ax1.set_xticklabels(np.arange(0, _pw_vc_sorted[['my_count', 'dt_count']].values.max() + 1, 1), fontsize=10)
    _ax1.tick_params(axis='y', labelsize=9)
    # grid for better readability
    _ax1.grid(color='#F2F2F2', linewidth=0.7, axis='x', alpha=0.2)

    _ax1_top = _ax1.secondary_xaxis('top')
    _ax1_top.set_xticks(np.arange(0, _pw_vc_sorted[['my_count', 'dt_count']].values.max() + 1, 1))
    _ax1_top.tick_params(axis='x', labelsize=10, length=0)


    # for C - Build a direction -> color mapping per player
    _color_map = {'Over': '#c96363', 'Under': '#3f62a5', 'Neutral': '#a1a1a1'}
    _player_colors_c = _pw_c_sorted.set_index('Player_name')['bias_direction'].map(_color_map)

    # for VC - Build a direction -> color mapping per player
    _color_map = {'Over': '#c96363', 'Under': '#3f62a5', 'Neutral': '#a1a1a1'}
    _player_colors_vc = _pw_vc_sorted.set_index('Player_name')['bias_direction'].map(_color_map)

    # for C - Apply colors to y tick labels
    for _label in _ax.get_yticklabels():
        _player = _label.get_text()
        if _player in _player_colors_c:
            _label.set_color(_player_colors_c[_player])

    # for VC - Apply colors to y tick labels
    for _label in _ax1.get_yticklabels():
        _player = _label.get_text()
        if _player in _player_colors_vc:
            _label.set_color(_player_colors_vc[_player])

    # for C - title and legend
    _ax.set_title("Captain Picks: My Count vs. Dream Team Count", pad=40, fontsize=10, loc='left')
    _ax.legend(frameon=False, fontsize=8, loc='upper right', bbox_to_anchor=(1.3, 1))
    # for VC - title and legend
    _ax1.set_title("Vice-Captain Picks: My Count vs. Dream Team Count", pad=40, fontsize=10, loc='left')
    _ax1.legend(frameon=False, fontsize=8, loc='upper right', bbox_to_anchor=(1.3, 1))
    # hide grid
    for _ax in [_ax, _ax1]:
        _ax.grid(False)


    # chart border
    for _spine in _ax.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')
    for _spine in _ax1.spines.values():
        _spine.set_linewidth(1)
        _spine.set_edgecolor('#CCCCCC')


    # save fig
    fig_c.savefig('visuals/player_level_c_comparison.png', dpi=300, bbox_inches='tight')
    fig_vc.savefig('visuals/player_level_vc_comparison.png', dpi=300, bbox_inches='tight')

    mo.hstack([
        fig_c,
        fig_vc
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Observations:
        - There has been significant over-preference of some players for both C and VC picks.
            - For C picks, a few players stand out with an over-preference margin of 3+ along with way too
            many players that were C in 0 matches but picked by me atleast once.
                - Specific cases of Faf du Plessis and Suryakumar Yadav could have single-handedly cost a lot of points.
            - Also all the high-margin over-preferred players seem to be popular players, for both C and VC.
            - For VC picks, again a few players stand out with over-preference margin of 2+.
            And many more such players were over-preferred for VC than C who were VC in 0 matches but picked
            by me atleast once, indicating that I was looking at many more options when picking VC.
        - Consequentially for both C and VC, I failed to pick many players who were C/VC in just 1 match.
        There are many players were C/VC for more than 1 match but I picked them in 0 matches.
           - The under-preference group is larger because some players unexpectedly perform in a match and
           that is hard to identify/predict.
    """))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md(r"""
        ### Insights on C/VC decisions:
        - Captain decision were better than Vice-captain decisions but both need be improved significantly.
        - The improvement can be done by reducing the popularity factor when assessing quality.
        Best players can have bad tournaments, and every tournament can have unexpected outperformers.
        - Any form of bias when selecting C/VC, be it towards team, role or player,
        needs to be identified and corrected as early as possible because C/VC decisions are one of if not
        the most critical decisions.
    """), kind='info')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Conclusions
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What Worked
    - **Cost discipline improved over time**
        - Spending became more controlled and consistent after early volatility
        - Reduced exposure to large downside risk
    - **Some ability to identify hidden opportunities**
        - A few less popular high-performing players were correctly identified
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What Did Not Work
    - **Selection quality was consistently suboptimal**
        - High-performing players were not selected frequently enough
        - Low-performing players were over-selected due to familiarity bias
        - Moderately performing players were available for selection and also performing but were consistently ignored by me.
    - **C/VC decisions lacked accuracy and consistency**
        - Poor rank alignment led to significant points left on the table
        - VC decisions were clearly bad
        - Faf du Plessis being selected as captain 7 times without any validation indicates a huge bias and lack of proper selection framework.
    - **Over-reliance on popularity signals**
        - Popular players were selected despite underperformance
        - Limited differentiation from the crowd where it would have mattered
    - **Bias-driven decision-making**
        - Player-level familiarity influenced selection more than objective metrics
        - Team-level bias, specifically GT, led to disproportionate investment and losses
            - High conviction in GT matches was consistent and consistently wrong.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What Needs to Improve

    **C/VC decision-making**
      - Need a clear and consistent framework for captaincy decisions
      - Focus on upside potential and consistency, not just popularity
      - Treat C and VC as equally important decisions

    **Structured player evaluation framework**
      - Prioritising players based on recent form, role, and matchup context
      - Reduce reliance on intuition and familiarity
      - Selection philosophy needs to shift from consensus to differentiation.
        - Focus should be on consistently selecting high-performing players, identifying moderately performing players that are not so popular and avoiding low-performing players.

    **Shift focus from cost optimisation to selection optimisation**
      - Focus should on improving player selection accuracy rather than controlling cost

    **Improve selection in the mid-tier player segment (300–700 points)**
      - This segment was the largest untapped opportunity

    **Actively identify and correct biases**
      - Could track over/under-preference patterns and data-driven checks before finalizing teams
    """)
    return


if __name__ == "__main__":
    app.run()
