# Blackjack-Simulation
Overview
This project uses Python and R to simulate blackjack and analyze how different player stopping scores affect win rates and expected returns.

The Python simulation generates 600,000 hands across 12 strategies, with stopping scores ranging from 10 to 21. The resulting data is analyzed in R to compare win rates, loss rates, and expected value, including the effect of a 3:2 blackjack payout.

Technologies
Python: Simulation and data generation
Pandas: Data storage and CSV export
R: Statistical analysis
dplyr, tidyr, ggplot2: Data manipulation and visualization
Methodology
Simulates blackjack using an eight-deck shoe, reshuffled when approximately half the cards remain.
Tests 50,000 hands for each stopping score from 10 through 21.
Assumes the player hits below their selected stopping score and the dealer hits below 17.
Treats aces as 11 unless the hand would exceed 21, then reduces them to 1 as needed.
Calculates win rates, loss rates, expected value, and approximate 95% confidence intervals.
The simulation excludes splitting, doubling down, and other advanced blackjack decisions.

Key Findings
Highest win rate: Approximately 41.35% at a stopping score of 16.
Best expected value: A stopping score of 17, with an estimated return of -$0.078 per $1 wagered under an even-money payout model.
With blackjack payouts: The estimated return at 17 improves to approximately -$0.056 per $1 wagered.
These results suggest that maximizing win rate does not necessarily maximize expected return. All tested strategies produced negative expected returns under the simulated rules.

How to Run
Install the required Python package:


pip install pandas
Run the simulation:


python blackjack_simulation.py
This generates BlackjackSimData.csv.

In R, install the required packages and load the data:


install.packages(c("dplyr", "tidyr", "ggplot2"))

library(dplyr)
library(tidyr)
library(ggplot2)

bjsim <- read.csv("BlackjackSimData.csv")
Run blackjack_analysis.Rmd in RStudio to reproduce the statistical analysis and visualizations.

Limitations
This is a simplified simulation, not a complete casino blackjack model. Results are subject to random variation, dependence between hands drawn from the same shoe, and simplified payout and dealer rules. The simulation does not guarantee real-world outcomes.

Conclusion
The analysis found that a stopping score of 16 produced the highest observed win rate, while 17 produced the best expected value. The project demonstrates how simulation and statistical analysis can be used to compare strategies and evaluate outcomes under uncertainty.
