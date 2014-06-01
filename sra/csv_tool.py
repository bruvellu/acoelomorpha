#!/usr/bin/env python
'''Manage sra.csv as a database.

This CSVTool has 2 main functions.

1. Every time we query SRA, new packages appear. We need a simple way to merge
the results of these successive queries into one main file. The `merge`
function combines the current CSV file with the specified CSV file.

2. Merging is needed because the sra.csv is annotated with the status of each
package and we want to keep this information when including new packages.
'''

import pandas as pd


class CSVTool:
    '''Execute several operations on main CSV file.'''

    def __init__(self):
        self.csv = 'sra.csv'
        # Try to open main CSV file.
        try:
            self.df = pd.read_csv(self.csv, index_col=False, dtype=object)
        except:
            self.df = pd.DataFrame(columns=['status', 'id', 'accession',
                                            'title', 'lineage', 'taxon_id',
                                            'scientific_name',
                                            'library_strategy',
                                            'library_layout',
                                            'instrument_model',
                                            'run_accession', 'nreads',
                                            'read_average', 'total_spots',
                                            'total_bases', 'size',
                                            'published'])
            self.df.to_csv(self.csv, index=False)

    def merge(self, new_csv):
        '''Import new queries into current CSV.'''

        # Import new CSV file.
        new_df = pd.read_csv(new_csv, index_col=False, dtype=object)

        # Use merge function from Pandas to merge datasets.
        merged_df = pd.merge(self.df, new_df, how='outer')

        # Printout updated dataframe.
        merged_df.to_csv(self.csv, index=False)

    def update(self, id, column):
        '''Updates a value from a row/column match.'''
        pass
