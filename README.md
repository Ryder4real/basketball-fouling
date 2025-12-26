This project is to see when NBA teams should foul late in the game.   
overall_sim is the main file that runs everything. 

I go into much more detail at: https://www.ryderfried.com/projects

Length of a possession is modeled with a Normal Distribution. I decided on a Normal distribution based on the "normal_qq_plot.png" and "time_hist.png" in the plots folder. Points scored in a possession is modeled with a categorical distribution, when was generated using basketball reference statistics combined with a recursive simulation to account for offensive rebounds.

To actually determine when it was better to foul, I used recrusive game sequences to make my simulation more efficient.

Here is a graphic with my results. One note: for the game simulations to end, I set the minimum possession length to 0.51 seconds.

![When to Foul](plots/final_graphic.png)
