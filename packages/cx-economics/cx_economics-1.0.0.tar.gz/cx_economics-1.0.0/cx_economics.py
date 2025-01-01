from faker import Faker
import pandas as pd
import numpy as np
from typing import Literal

class CXEconomics:
    def __init__(self, seed: int = 42):
        self.seed = seed
        self.fake = Faker()
        Faker.seed(seed)
        np.random.seed(seed)
        self.data = None

    def generate_sample_data(self, num_customers: int = 1000, b2b: bool = False):
        """
        Generates sample customer or account data for analysis.
        """
        customers = []
        for _ in range(num_customers):
            pre_ltr = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p=[0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.1])
            post_ltr = pre_ltr + np.random.choice([-2, -1, 0, 1, 2], p=[0.1, 0.2, 0.4, 0.2, 0.1])
            pre_ltr = min(max(pre_ltr, 0), 10)
            post_ltr = min(max(post_ltr, 0), 10)

            pre_revenue = self.fake.random_int(min=100, max=1000) * (1 + 0.2 * (pre_ltr - 5))
            post_revenue = pre_revenue * (1 + 0.1 * (post_ltr - pre_ltr))

            customers.append({
                'customer_id': self.fake.uuid4(),
                'account_id': self.fake.uuid4() if b2b else None,
                'pre_ltr': pre_ltr,
                'post_ltr': post_ltr,
                'pre_revenue': pre_revenue,
                'post_revenue': post_revenue
            })

        self.data = pd.DataFrame(customers)
        return self.data

    def calculate_nps(self, data: pd.DataFrame, ltr_col: str):
        """
        Calculates the Net Promoter Score (NPS) for a given period.
        """
        promoters = data[ltr_col].apply(lambda x: x >= 9).sum()
        passives = data[ltr_col].apply(lambda x: 7 <= x <= 8).sum()
        detractors = data[ltr_col].apply(lambda x: x <= 6).sum()
        nps = (promoters - detractors) / len(data) * 100
        return {
            "nps": nps,
            "promoters": promoters,
            "passives": passives,
            "detractors": detractors
        }

    def analyze_cx_economics(self, survey_type: Literal['B2C', 'B2B'] = 'B2C',
                             pre_ltr: str = 'pre_ltr', post_ltr: str = 'post_ltr',
                             pre_revenue: str = 'pre_revenue', post_revenue: str = 'post_revenue'):
        """
        Performs CX economic analysis based on survey type and given data.
        """
        if self.data is None:
            raise ValueError("Sample data not generated or provided.")

        data = self.data.copy()

        if survey_type == 'B2B':
            data = data.groupby('account_id').mean().reset_index()

        nps_pre = self.calculate_nps(data, pre_ltr)
        nps_post = self.calculate_nps(data, post_ltr)

        stats = {
            "nps_pre": nps_pre,
            "nps_post": nps_post,
            "avg_revenue_pre": data[pre_revenue].mean(),
            "avg_revenue_post": data[post_revenue].mean(),
            "median_revenue_pre": data[pre_revenue].median(),
            "median_revenue_post": data[post_revenue].median()
        }

        return stats

    def get_transition_stats(self, pre_ltr: str = 'pre_ltr', post_ltr: str = 'post_ltr',
                              pre_revenue: str = 'pre_revenue', post_revenue: str = 'post_revenue'):
        """
        Calculates transition statistics between CX categories for pre and post periods, including revenue metrics.
        """
        if self.data is None:
            raise ValueError("Sample data not generated or provided.")

        data = self.data.dropna(subset=[pre_ltr, post_ltr, pre_revenue, post_revenue])  # Exclude rows with missing data

        transitions = []
        for transition, (pre_cond, post_cond) in {
            'Promoter to Promoter': (9, 9),
            'Promoter to Passive': (9, (7, 8)),
            'Promoter to Detractor': (9, (0, 6)),
            'Passive to Promoter': ((7, 8), 9),
            'Passive to Passive': ((7, 8), (7, 8)),
            'Passive to Detractor': ((7, 8), (0, 6)),
            'Detractor to Promoter': ((0, 6), 9),
            'Detractor to Passive': ((0, 6), (7, 8)),
            'Detractor to Detractor': ((0, 6), (0, 6)),
        }.items():
            filtered_data = self._transition_data(data, pre_ltr, post_ltr, pre_revenue, post_revenue, pre_cond, post_cond)
            filtered_data['transition'] = transition
            transitions.append(filtered_data)

        transitions_df = pd.DataFrame(transitions)
        return transitions_df

    def _transition_data(self, data, pre_ltr, post_ltr, pre_revenue, post_revenue, pre_cond, post_cond):
        if isinstance(pre_cond, tuple):
            pre_mask = data[pre_ltr].between(pre_cond[0], pre_cond[1])
        else:
            pre_mask = data[pre_ltr] >= pre_cond
        if isinstance(post_cond, tuple):
            post_mask = data[post_ltr].between(post_cond[0], post_cond[1])
        else:
            post_mask = data[post_ltr] >= post_cond

        filtered_data = data[pre_mask & post_mask]
        return {
            "count": filtered_data.shape[0],
            "avg_revenue_pre": filtered_data[pre_revenue].mean(),
            "avg_revenue_post": filtered_data[post_revenue].mean(),
            "median_revenue_pre": filtered_data[pre_revenue].median(),
            "median_revenue_post": filtered_data[post_revenue].median()
        }

# Example Usage
if __name__ == "__main__":
    cx = CXEconomics()
    data = cx.generate_sample_data()
    print("Sample Data:")
    print(data.head())

    stats = cx.analyze_cx_economics()
    print("Analysis Statistics:")
    print(stats)

    transitions = cx.get_transition_stats()
    print("CX Transitions (DataFrame):")
    print(transitions)
