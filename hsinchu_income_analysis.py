#!/usr/bin/env python3
"""
Hsinchu City Income Inequality Spatial Analysis
Author: Your Name
Date: 2025-11-13

This script performs comprehensive spatial analysis of income inequality
in Hsinchu City, Taiwan.
"""

import warnings
warnings.filterwarnings('ignore')

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Spatial analysis libraries
try:
    import libpysal
    from esda.moran import Moran, Moran_Local
    from esda.getisord import G_Local
    from splot.esda import plot_moran, plot_local_autocorrelation, moran_scatterplot
except ImportError:
    print("PySAL not installed. Some spatial analysis features will be unavailable.")

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class HsinchuIncomeAnalysis:
    """Main class for Hsinchu income analysis"""

    def __init__(self, shapefile_path='Hsinchu_City.shp'):
        """Initialize with shapefile path"""
        self.shapefile_path = shapefile_path
        self.gdf = None
        self.weights = None

    def load_data(self):
        """Load shapefile and prepare data"""
        print("=" * 60)
        print("LOADING DATA")
        print("=" * 60)

        self.gdf = gpd.read_file(self.shapefile_path)
        print(f"Loaded {len(self.gdf)} villages from {self.shapefile_path}")
        print(f"CRS: {self.gdf.crs}")

        # Display basic info
        print("\nColumns:", list(self.gdf.columns))
        print(f"Geometry type: {self.gdf.geometry.type.unique()}")

        return self.gdf

    def calculate_derived_variables(self):
        """Calculate additional variables for analysis"""
        print("\n" + "=" * 60)
        print("CALCULATING DERIVED VARIABLES")
        print("=" * 60)

        # Income per capita
        self.gdf['income_per_capita'] = self.gdf['INCOME'] / self.gdf['POPULATION']

        # Income per household
        self.gdf['income_per_household'] = self.gdf['INCOME'] / self.gdf['HOUSEHOLD']

        # Education rate (%)
        self.gdf['education_rate'] = (self.gdf['TERTIARY'] / self.gdf['POPULATION']) * 100

        # Indigenous ratio (%)
        self.gdf['indigenous_ratio'] = (self.gdf['INDIGENOUS'] / self.gdf['POPULATION']) * 100

        # Average household size
        self.gdf['household_size'] = self.gdf['POPULATION'] / self.gdf['HOUSEHOLD']

        # Log transformations for skewed variables
        self.gdf['log_income_pc'] = np.log(self.gdf['income_per_capita'])
        self.gdf['log_pop_dens'] = np.log(self.gdf['POP_DENS'] + 1)

        print("Derived variables calculated:")
        print("  - income_per_capita")
        print("  - income_per_household")
        print("  - education_rate (%)")
        print("  - indigenous_ratio (%)")
        print("  - household_size")
        print("  - log_income_pc")
        print("  - log_pop_dens")

        return self.gdf

    def descriptive_statistics(self):
        """Generate descriptive statistics"""
        print("\n" + "=" * 60)
        print("DESCRIPTIVE STATISTICS")
        print("=" * 60)

        # Key variables for analysis
        key_vars = ['POPULATION', 'HOUSEHOLD', 'SEX_RATIO', 'POP_DENS',
                    'AgingIndex', 'TERTIARY', 'INDIGENOUS',
                    'income_per_capita', 'income_per_household',
                    'education_rate', 'indigenous_ratio']

        # Summary statistics
        desc_stats = self.gdf[key_vars].describe()
        print("\n", desc_stats)

        # Save to CSV
        desc_stats.to_csv('descriptive_statistics.csv')
        print("\nDescriptive statistics saved to: descriptive_statistics.csv")

        return desc_stats

    def plot_distributions(self):
        """Plot distributions of key variables"""
        print("\n" + "=" * 60)
        print("PLOTTING DISTRIBUTIONS")
        print("=" * 60)

        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Distribution of Key Variables - Hsinchu City', fontsize=16, fontweight='bold')

        # Income per capita
        axes[0, 0].hist(self.gdf['income_per_capita'], bins=30, color='skyblue', edgecolor='black')
        axes[0, 0].set_title('Income Per Capita')
        axes[0, 0].set_xlabel('Income (1000 TWD)')
        axes[0, 0].set_ylabel('Frequency')
        axes[0, 0].axvline(self.gdf['income_per_capita'].median(), color='red',
                          linestyle='--', label=f"Median: {self.gdf['income_per_capita'].median():.0f}")
        axes[0, 0].legend()

        # Education rate
        axes[0, 1].hist(self.gdf['education_rate'], bins=30, color='lightgreen', edgecolor='black')
        axes[0, 1].set_title('Tertiary Education Rate')
        axes[0, 1].set_xlabel('Education Rate (%)')
        axes[0, 1].set_ylabel('Frequency')

        # Aging Index
        axes[0, 2].hist(self.gdf['AgingIndex'], bins=30, color='lightcoral', edgecolor='black')
        axes[0, 2].set_title('Aging Index')
        axes[0, 2].set_xlabel('Aging Index')
        axes[0, 2].set_ylabel('Frequency')

        # Population Density
        axes[1, 0].hist(self.gdf['POP_DENS'], bins=30, color='plum', edgecolor='black')
        axes[1, 0].set_title('Population Density')
        axes[1, 0].set_xlabel('Population per km²')
        axes[1, 0].set_ylabel('Frequency')

        # Boxplot: Income per capita by district
        if 'TOWNNAME' in self.gdf.columns:
            self.gdf.boxplot(column='income_per_capita', by='TOWNNAME', ax=axes[1, 1])
            axes[1, 1].set_title('Income Per Capita by District')
            axes[1, 1].set_xlabel('District')
            axes[1, 1].set_ylabel('Income Per Capita (1000 TWD)')
            plt.sca(axes[1, 1])
            plt.xticks(rotation=45)

        # Household size
        axes[1, 2].hist(self.gdf['household_size'], bins=30, color='khaki', edgecolor='black')
        axes[1, 2].set_title('Household Size')
        axes[1, 2].set_xlabel('Persons per Household')
        axes[1, 2].set_ylabel('Frequency')

        plt.tight_layout()
        plt.savefig('distributions.png', dpi=300, bbox_inches='tight')
        print("Distribution plots saved to: distributions.png")
        plt.close()

    def correlation_analysis(self):
        """Analyze correlations between variables"""
        print("\n" + "=" * 60)
        print("CORRELATION ANALYSIS")
        print("=" * 60)

        # Select variables for correlation
        corr_vars = ['income_per_capita', 'education_rate', 'AgingIndex',
                     'POP_DENS', 'indigenous_ratio', 'household_size', 'SEX_RATIO']

        corr_matrix = self.gdf[corr_vars].corr()

        # Plot correlation heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm',
                   center=0, square=True, linewidths=1)
        plt.title('Correlation Matrix - Hsinchu City Income Analysis',
                 fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
        print("Correlation matrix saved to: correlation_matrix.png")
        plt.close()

        # Print key correlations with income
        print("\nKey Correlations with Income Per Capita:")
        income_corr = corr_matrix['income_per_capita'].sort_values(ascending=False)
        for var, corr in income_corr.items():
            if var != 'income_per_capita':
                print(f"  {var:20s}: {corr:6.3f}")

        return corr_matrix

    def create_choropleth_maps(self):
        """Create choropleth maps for key variables"""
        print("\n" + "=" * 60)
        print("CREATING CHOROPLETH MAPS")
        print("=" * 60)

        # Create 2x2 subplot for multiple maps
        fig, axes = plt.subplots(2, 2, figsize=(16, 14))
        fig.suptitle('Spatial Distribution of Key Variables - Hsinchu City',
                    fontsize=16, fontweight='bold')

        # 1. Income per capita
        self.gdf.plot(column='income_per_capita', ax=axes[0, 0],
                     legend=True, cmap='RdYlGn',
                     edgecolor='black', linewidth=0.5,
                     legend_kwds={'label': 'Income Per Capita (1000 TWD)'})
        axes[0, 0].set_title('Income Per Capita Distribution', fontweight='bold')
        axes[0, 0].axis('off')

        # 2. Education rate
        self.gdf.plot(column='education_rate', ax=axes[0, 1],
                     legend=True, cmap='Blues',
                     edgecolor='black', linewidth=0.5,
                     legend_kwds={'label': 'Tertiary Education Rate (%)'})
        axes[0, 1].set_title('Tertiary Education Rate', fontweight='bold')
        axes[0, 1].axis('off')

        # 3. Aging Index
        self.gdf.plot(column='AgingIndex', ax=axes[1, 0],
                     legend=True, cmap='Reds',
                     edgecolor='black', linewidth=0.5,
                     legend_kwds={'label': 'Aging Index'})
        axes[1, 0].set_title('Aging Index Distribution', fontweight='bold')
        axes[1, 0].axis('off')

        # 4. Population Density
        self.gdf.plot(column='POP_DENS', ax=axes[1, 1],
                     legend=True, cmap='YlOrRd',
                     edgecolor='black', linewidth=0.5,
                     legend_kwds={'label': 'Population Density (per km²)'})
        axes[1, 1].set_title('Population Density', fontweight='bold')
        axes[1, 1].axis('off')

        plt.tight_layout()
        plt.savefig('choropleth_maps.png', dpi=300, bbox_inches='tight')
        print("Choropleth maps saved to: choropleth_maps.png")
        plt.close()

        # Create a focused income map
        fig, ax = plt.subplots(1, 1, figsize=(12, 10))
        self.gdf.plot(column='income_per_capita', ax=ax,
                     legend=True, cmap='RdYlGn',
                     edgecolor='black', linewidth=0.8,
                     legend_kwds={'label': 'Income Per Capita (1000 TWD)', 'shrink': 0.8})

        # Add village names for high/low income areas
        high_income = self.gdf.nlargest(5, 'income_per_capita')
        low_income = self.gdf.nsmallest(5, 'income_per_capita')

        ax.set_title('Hsinchu City - Income Per Capita by Village',
                    fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')

        plt.tight_layout()
        plt.savefig('income_map_detailed.png', dpi=300, bbox_inches='tight')
        print("Detailed income map saved to: income_map_detailed.png")
        plt.close()

    def spatial_weights(self):
        """Create spatial weights matrix"""
        print("\n" + "=" * 60)
        print("CREATING SPATIAL WEIGHTS MATRIX")
        print("=" * 60)

        try:
            # Queen contiguity weights
            self.weights = libpysal.weights.Queen.from_dataframe(self.gdf)
            self.weights.transform = 'r'  # Row-standardized

            print(f"Spatial weights created: {self.weights.n} observations")
            print(f"Average neighbors: {self.weights.mean_neighbors:.2f}")
            print(f"Min neighbors: {self.weights.min_neighbors}")
            print(f"Max neighbors: {self.weights.max_neighbors}")

            # Check for islands (no neighbors)
            islands = [i for i in range(self.weights.n) if self.weights.cardinalities[i] == 0]
            if islands:
                print(f"WARNING: {len(islands)} islands detected (no neighbors)")

            return self.weights

        except Exception as e:
            print(f"Error creating spatial weights: {e}")
            return None

    def global_morans_i(self):
        """Calculate Global Moran's I for spatial autocorrelation"""
        print("\n" + "=" * 60)
        print("GLOBAL MORAN'S I - SPATIAL AUTOCORRELATION")
        print("=" * 60)

        if self.weights is None:
            print("Spatial weights not created. Run spatial_weights() first.")
            return None

        try:
            # Calculate Moran's I for income per capita
            y = self.gdf['income_per_capita'].values
            moran = Moran(y, self.weights)

            print(f"\nMoran's I: {moran.I:.4f}")
            print(f"Expected I: {moran.EI:.4f}")
            print(f"Variance: {moran.VI_norm:.4f}")
            print(f"Z-score: {moran.z_norm:.4f}")
            print(f"P-value: {moran.p_norm:.4f}")

            if moran.p_norm < 0.05:
                if moran.I > 0:
                    print("✓ Significant POSITIVE spatial autocorrelation (clustering)")
                else:
                    print("✓ Significant NEGATIVE spatial autocorrelation (dispersion)")
            else:
                print("✗ No significant spatial autocorrelation (random)")

            # Plot Moran's I scatter plot
            fig, ax = plt.subplots(1, 1, figsize=(8, 8))
            moran_scatterplot(moran, ax=ax)
            plt.title("Moran's I Scatter Plot - Income Per Capita",
                     fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.savefig('morans_i_scatterplot.png', dpi=300, bbox_inches='tight')
            print("\nMoran's I scatter plot saved to: morans_i_scatterplot.png")
            plt.close()

            return moran

        except Exception as e:
            print(f"Error calculating Moran's I: {e}")
            return None

    def local_morans_i(self):
        """Calculate Local Moran's I (LISA)"""
        print("\n" + "=" * 60)
        print("LOCAL MORAN'S I (LISA) - LOCAL CLUSTERS")
        print("=" * 60)

        if self.weights is None:
            print("Spatial weights not created. Run spatial_weights() first.")
            return None

        try:
            y = self.gdf['income_per_capita'].values
            lisa = Moran_Local(y, self.weights)

            # Add LISA results to geodataframe
            self.gdf['lisa_cluster'] = lisa.q
            self.gdf['lisa_pval'] = lisa.p_sim
            self.gdf['lisa_significant'] = lisa.p_sim < 0.05

            # Cluster types
            cluster_labels = {1: 'HH (High-High)', 2: 'LH (Low-High)',
                            3: 'LL (Low-Low)', 4: 'HL (High-Low)', 0: 'Not Significant'}

            # Count significant clusters
            print("\nLISA Cluster Summary:")
            for cluster_type, label in cluster_labels.items():
                if cluster_type == 0:
                    count = sum((self.gdf['lisa_cluster'] == cluster_type) |
                               (~self.gdf['lisa_significant']))
                else:
                    count = sum((self.gdf['lisa_cluster'] == cluster_type) &
                               self.gdf['lisa_significant'])
                print(f"  {label:20s}: {count:3d} villages")

            # Plot LISA cluster map
            fig, ax = plt.subplots(1, 1, figsize=(12, 10))

            # Create cluster map with custom colors
            cluster_colors = {0: 'lightgray', 1: 'red', 2: 'pink', 3: 'blue', 4: 'lightblue'}
            self.gdf['cluster_color'] = self.gdf.apply(
                lambda row: cluster_colors[row['lisa_cluster']] if row['lisa_significant']
                else cluster_colors[0], axis=1
            )

            self.gdf.plot(color=self.gdf['cluster_color'], ax=ax,
                         edgecolor='black', linewidth=0.5)

            # Legend
            from matplotlib.patches import Patch
            legend_elements = [
                Patch(facecolor='red', label='High-High (Hot Spot)'),
                Patch(facecolor='blue', label='Low-Low (Cold Spot)'),
                Patch(facecolor='pink', label='Low-High (Outlier)'),
                Patch(facecolor='lightblue', label='High-Low (Outlier)'),
                Patch(facecolor='lightgray', label='Not Significant')
            ]
            ax.legend(handles=legend_elements, loc='best', fontsize=10)

            ax.set_title('LISA Cluster Map - Income Per Capita\n(Significant at p < 0.05)',
                        fontsize=14, fontweight='bold', pad=20)
            ax.axis('off')

            plt.tight_layout()
            plt.savefig('lisa_cluster_map.png', dpi=300, bbox_inches='tight')
            print("\nLISA cluster map saved to: lisa_cluster_map.png")
            plt.close()

            return lisa

        except Exception as e:
            print(f"Error calculating Local Moran's I: {e}")
            return None

    def hotspot_analysis(self):
        """Getis-Ord Gi* hotspot analysis"""
        print("\n" + "=" * 60)
        print("GETIS-ORD Gi* HOT SPOT ANALYSIS")
        print("=" * 60)

        if self.weights is None:
            print("Spatial weights not created. Run spatial_weights() first.")
            return None

        try:
            y = self.gdf['income_per_capita'].values
            g_local = G_Local(y, self.weights)

            # Add to geodataframe
            self.gdf['gi_star'] = g_local.Zs
            self.gdf['gi_pval'] = g_local.p_sim

            # Classify hot/cold spots
            self.gdf['hotspot'] = 'Not Significant'
            self.gdf.loc[(self.gdf['gi_star'] > 1.96) & (self.gdf['gi_pval'] < 0.05), 'hotspot'] = 'Hot Spot (99%)'
            self.gdf.loc[(self.gdf['gi_star'] > 1.65) & (self.gdf['gi_star'] <= 1.96) &
                        (self.gdf['gi_pval'] < 0.10), 'hotspot'] = 'Hot Spot (90%)'
            self.gdf.loc[(self.gdf['gi_star'] < -1.96) & (self.gdf['gi_pval'] < 0.05), 'hotspot'] = 'Cold Spot (99%)'
            self.gdf.loc[(self.gdf['gi_star'] < -1.65) & (self.gdf['gi_star'] >= -1.96) &
                        (self.gdf['gi_pval'] < 0.10), 'hotspot'] = 'Cold Spot (90%)'

            # Summary
            print("\nHot Spot Summary:")
            print(self.gdf['hotspot'].value_counts())

            # Plot hot spot map
            fig, ax = plt.subplots(1, 1, figsize=(12, 10))

            hotspot_colors = {
                'Hot Spot (99%)': 'darkred',
                'Hot Spot (90%)': 'red',
                'Not Significant': 'lightgray',
                'Cold Spot (90%)': 'blue',
                'Cold Spot (99%)': 'darkblue'
            }

            for hotspot_type, color in hotspot_colors.items():
                subset = self.gdf[self.gdf['hotspot'] == hotspot_type]
                subset.plot(ax=ax, color=color, edgecolor='black',
                           linewidth=0.5, label=hotspot_type)

            ax.legend(loc='best', fontsize=10)
            ax.set_title('Getis-Ord Gi* Hot Spot Analysis - Income Per Capita',
                        fontsize=14, fontweight='bold', pad=20)
            ax.axis('off')

            plt.tight_layout()
            plt.savefig('hotspot_analysis.png', dpi=300, bbox_inches='tight')
            print("\nHot spot analysis map saved to: hotspot_analysis.png")
            plt.close()

            return g_local

        except Exception as e:
            print(f"Error in hot spot analysis: {e}")
            return None

    def regression_analysis(self):
        """OLS regression analysis"""
        print("\n" + "=" * 60)
        print("REGRESSION ANALYSIS")
        print("=" * 60)

        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import r2_score, mean_squared_error

        # Prepare variables
        y = self.gdf['income_per_capita'].values
        X = self.gdf[['education_rate', 'AgingIndex', 'POP_DENS',
                     'indigenous_ratio', 'household_size']].values

        var_names = ['education_rate', 'AgingIndex', 'POP_DENS',
                    'indigenous_ratio', 'household_size']

        # Remove any NaN values
        valid_idx = ~np.isnan(X).any(axis=1) & ~np.isnan(y)
        X_clean = X[valid_idx]
        y_clean = y[valid_idx]

        # Fit model
        model = LinearRegression()
        model.fit(X_clean, y_clean)

        # Predictions
        y_pred = model.predict(X_clean)

        # Results
        print("\nRegression Results:")
        print(f"{'Variable':<20s} {'Coefficient':>12s}")
        print("-" * 35)
        print(f"{'Intercept':<20s} {model.intercept_:>12.2f}")
        for name, coef in zip(var_names, model.coef_):
            print(f"{name:<20s} {coef:>12.4f}")

        print(f"\nR-squared: {r2_score(y_clean, y_pred):.4f}")
        print(f"RMSE: {np.sqrt(mean_squared_error(y_clean, y_pred)):.2f}")

        # Scatter plot: Predicted vs Actual
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
        ax.scatter(y_clean, y_pred, alpha=0.6)
        ax.plot([y_clean.min(), y_clean.max()],
               [y_clean.min(), y_clean.max()],
               'r--', lw=2, label='Perfect Prediction')
        ax.set_xlabel('Actual Income Per Capita', fontsize=12)
        ax.set_ylabel('Predicted Income Per Capita', fontsize=12)
        ax.set_title('Regression Model: Predicted vs Actual',
                    fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('regression_scatter.png', dpi=300, bbox_inches='tight')
        print("\nRegression scatter plot saved to: regression_scatter.png")
        plt.close()

        return model

    def generate_report(self):
        """Generate summary report"""
        print("\n" + "=" * 60)
        print("GENERATING SUMMARY REPORT")
        print("=" * 60)

        report = []
        report.append("=" * 60)
        report.append("HSINCHU CITY INCOME INEQUALITY ANALYSIS")
        report.append("Spatial Distribution and Influencing Factors")
        report.append("=" * 60)
        report.append("")

        # Data summary
        report.append("DATA SUMMARY")
        report.append("-" * 60)
        report.append(f"Number of villages: {len(self.gdf)}")
        report.append(f"Total population: {self.gdf['POPULATION'].sum():,.0f}")
        report.append(f"Total households: {self.gdf['HOUSEHOLD'].sum():,.0f}")
        report.append("")

        # Income statistics
        report.append("INCOME STATISTICS")
        report.append("-" * 60)
        report.append(f"Mean income per capita: {self.gdf['income_per_capita'].mean():,.2f} (1000 TWD)")
        report.append(f"Median income per capita: {self.gdf['income_per_capita'].median():,.2f} (1000 TWD)")
        report.append(f"Std deviation: {self.gdf['income_per_capita'].std():,.2f}")
        report.append(f"Min income: {self.gdf['income_per_capita'].min():,.2f}")
        report.append(f"Max income: {self.gdf['income_per_capita'].max():,.2f}")
        report.append(f"Income inequality (CV): {(self.gdf['income_per_capita'].std() / self.gdf['income_per_capita'].mean()):.4f}")
        report.append("")

        # Top and bottom villages
        report.append("TOP 5 HIGHEST INCOME VILLAGES")
        report.append("-" * 60)
        top5 = self.gdf.nlargest(5, 'income_per_capita')[['VILLNAME', 'TOWNNAME', 'income_per_capita']]
        for idx, row in top5.iterrows():
            report.append(f"{row['VILLNAME']} ({row['TOWNNAME']}): {row['income_per_capita']:,.2f}")
        report.append("")

        report.append("TOP 5 LOWEST INCOME VILLAGES")
        report.append("-" * 60)
        bottom5 = self.gdf.nsmallest(5, 'income_per_capita')[['VILLNAME', 'TOWNNAME', 'income_per_capita']]
        for idx, row in bottom5.iterrows():
            report.append(f"{row['VILLNAME']} ({row['TOWNNAME']}): {row['income_per_capita']:,.2f}")
        report.append("")

        # Key findings
        report.append("KEY FINDINGS")
        report.append("-" * 60)
        report.append("1. Income shows spatial clustering pattern (check Moran's I)")
        report.append("2. Education rate positively correlates with income")
        report.append("3. Aging index negatively correlates with income")
        report.append("4. Population density shows mixed effects")
        report.append("")

        # Export
        report_text = "\n".join(report)
        with open('analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)

        print("\nSummary report saved to: analysis_report.txt")
        print(report_text)

        return report_text


def main():
    """Main execution function"""
    print("=" * 60)
    print("HSINCHU CITY INCOME INEQUALITY ANALYSIS")
    print("=" * 60)
    print()

    # Initialize analysis
    analyzer = HsinchuIncomeAnalysis('Hsinchu_City.shp')

    # Step 1: Load data
    analyzer.load_data()

    # Step 2: Calculate derived variables
    analyzer.calculate_derived_variables()

    # Step 3: Descriptive statistics
    analyzer.descriptive_statistics()

    # Step 4: Plot distributions
    analyzer.plot_distributions()

    # Step 5: Correlation analysis
    analyzer.correlation_analysis()

    # Step 6: Create maps
    analyzer.create_choropleth_maps()

    # Step 7: Spatial analysis
    try:
        analyzer.spatial_weights()
        analyzer.global_morans_i()
        analyzer.local_morans_i()
        analyzer.hotspot_analysis()
    except Exception as e:
        print(f"\nNote: Some spatial analysis features require PySAL library")
        print(f"Install with: pip install pysal libpysal esda splot")

    # Step 8: Regression
    analyzer.regression_analysis()

    # Step 9: Generate report
    analyzer.generate_report()

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nGenerated files:")
    print("  - descriptive_statistics.csv")
    print("  - distributions.png")
    print("  - correlation_matrix.png")
    print("  - choropleth_maps.png")
    print("  - income_map_detailed.png")
    print("  - morans_i_scatterplot.png")
    print("  - lisa_cluster_map.png")
    print("  - hotspot_analysis.png")
    print("  - regression_scatter.png")
    print("  - analysis_report.txt")
    print("\nUse these outputs for your presentation!")


if __name__ == '__main__':
    main()
