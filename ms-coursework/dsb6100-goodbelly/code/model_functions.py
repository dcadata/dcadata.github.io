"""DSB 6100 Marketing Analytics - Goodbelly Case Assignment"""

### FUNCTIONS NEEDED TO CREATE MODELS AND PLOTS ###

def replace_multiple(s, to_replace):
    """Function to replace multiple characters within a string with commas"""
    for i in to_replace:
        s = s.replace(i,',')
    return s

def summary2df(pd, summary, sig_level=0.05):
    """Converts model output summary to pandas dataframe;
    returns R2, # of variables (size of dataframe), and the dataframe itself"""

    t1 = pd.read_html(summary.tables[0].as_html(), header=None, index_col=0)[0]
    r2 = t1[t1[2] == 'R-squared:'][3].values[0]

    r2 = f'{r2:.3f}'

    t2 = pd.read_html(summary.tables[1].as_html(), header=None, index_col=None)[0]\
        .drop(columns=[2,3,5,6])\
        .rename(columns={0: 'term', 1: 'coef', 4: 'p'})
    t2 = t2[t2.coef != 'coef']

    t2.coef = t2.coef.map(float)
    t2.p = t2.p.map(float)

    t2 = t2.assign(sig = t2.p.apply(lambda x: True if x <= sig_level else False))
    t2 = t2.assign(type = t2.term.apply(lambda x: 'intr' if ':' in x else 'pure'))

    sze = t2.shape[0]

    t2 = t2.sort_values(by=['sig', 'coef'], ascending=False)
    t2 = t2.reset_index(drop=True)

    return r2, sze, t2

def get_coefficients(t2):
    """Returns new dataframe with only pure coefficients (no interaction terms);
    returns only term and coefficient fields"""
    return t2[t2.type == 'pure'][['term', 'coef']]

def get_coefficient(df_coeff, target_term):
    """Gets a coefficient for a particular term from the above dataframe"""
    return df_coeff[df_coeff.term == target_term].coef.values[0]

def create_equation(t2):
    """Creates regression equation for a given model
    (based on the dataframe the model was converted to above)"""

    t2 = t2.sort_values(by=['type', 'term'], ascending=False)
    terms = t2.term.tolist()
    terms.remove('Intercept')
    term_blocks = []
    for n in range(1, len(terms)+1):
        term_name = terms[n-1].replace(':','.').upper()
        term_blocks.append(f'B{n}({term_name})')
    eqn = 'B0 + ' + ' + '.join(term_blocks)
    return eqn

def condensed_summary(pd, formula, summary, sig_level=0.05):
    """Return summary that can be outputted to a text file for saving;
    includes IV list, R2, equation, and summary"""

    r2, sze, t2 = summary2df(pd, summary, sig_level)

    eqn = create_equation(t2)
    t2_sig = t2[t2.sig]
    eqn_condensed = ''
    if t2_sig.shape[0] != t2.shape[0]:
        eqn_drop_insig = create_equation(t2_sig)
        eqn_condensed = f"condensed equation w/o insignificant terms: Y = {eqn_drop_insig}\n\n"

    y_title, x_title = formula.split(' ~ ', 1)

    output = f"X: {x_title}\n" \
        f"Y: {y_title}\n\n" \
        f"R2: {r2}\n\n" \
        f"full equation: Y = {eqn}\n\n" \
        + eqn_condensed + \
        f"no. of terms: {sze}\n\n" \
        f"{t2.to_string()}"

    filename = f'{r2}_{y_title}~' + replace_multiple(x_title, [' * ', ' + ', ':']) + '.txt'

    return output, filename