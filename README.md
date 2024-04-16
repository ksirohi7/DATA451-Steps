# DATA451-Steps
Code Storage :)

## File Descriptions
**SanityCheck.*:** R code to generate sanity check plots
* Line plot of steps over time 
* Posture bars

**act24_conversion.py:** Add datetime column to each ACT24 participant file at 80Hz

**cum_steps_vis.Rmd:** R code to generate sanity check plots 
* Line plot of steps over time
* Predicted steps
* Posture bars

**feature_gt_merge.ipynb:** Jupyter notebook that grabs ACT24_*.csv files from server and saves them in ACT24_<ID>_<SESSION>_CTRAIN.csv format

**ground_truth.ipynb:** Creates behavioral ground truth second-by-second file

**ground_truth_step_count.ipynb:** Gives total step counts for each id, session pair

**merge_behavior_steps.ipynb:** Merges behavioral and step second-by-second ground truths

**process_sessions.py:** Processes ACT24 sessions using do_log file

**steps_comp.ipynb:** Visualizations for quarter 1 presentation of actual vs estimated steps
