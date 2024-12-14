# Privacy-Preserving Synthetic Data

This project demonstrates the generation and evaluation of privacy-preserving synthetic data using the Data Synthesizer and MST algorithms.

## Features

- Generate synthetic datasets in random, independent attribute, and correlated modes.
- Evaluate statistical properties of synthetic data using metrics and visualizations.
- Compare mutual information preservation and distribution similarity using statistical tests.

## Methodology

### Synthetic Data Generation
Using **Data Synthesizer**, synthetic datasets were generated under the following configurations:
- **Mode A:** Random mode.
- **Mode B:** Independent attribute mode with ε = 0.1.
- **Mode C:** Correlated attribute mode with k = 1, ε = 0.1.
- **Mode D:** Correlated attribute mode with k = 2, ε = 0.1.

### Evaluation Metrics:
1. **Statistical Queries:** Compare metrics (Mean, Median, Min, Max) for age and score attributes.
2. **Distribution Analysis:** Visualize histograms of age and sex for synthetic and real datasets.
3. **Statistical Tests:** Use Kolmogorov-Smirnov and KL-divergence to measure data similarity.
4. **Mutual Information:** Analyze pairwise mutual information between attributes.

## Results

- **Synthetic Data Accuracy:** Random mode showed lower accuracy in statistical queries compared to correlated attribute modes.
- **Distribution Analysis:** Independent attribute mode (B) better preserved the original distribution than random mode (A).
- **Privacy Budget Impact:** Lower ε values increased privacy but reduced the fidelity of the synthetic data.