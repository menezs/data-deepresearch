[referencia=13d0780828065ceb score=0.992]
##### **5.1 Baseline Results** 

**Baseline Estimates** Table 1 presents estimates of _β_ in Equation (1) on our overall index of poor mental health and shows that the introduction of Facebook at a college had a negative impact on student mental health. The first column in the table shows results for our 

16 

simplest specification, which includes only Facebook-expansion-group fixed effects, surveywave fixed effects, and an indicator for post-Facebook introduction. In the second column, we also include individual- and college-level control variables. In the third column, we replace Facebook-expansion-group fixed effects with college fixed effects to account for the changing composition of our sample. In the fourth column, we add expansion-group-level linear time trends, in order to take into account the possibility that colleges belonging to different Facebook expansion groups might be on different linear mental-health trends. Our results are fairly stable across specifications. 

The effect size on the index of poor mental health in our preferred specification, namely the one that includes college rather than expansion-group fixed effects and that does not include linear time trends, is 0.085 standard deviation units. The effect above is estimated on the entire population of students taking the NCHA survey, which includes both students who did and who did not sign-up for a Facebook account after Facebook was made available at their college. Therefore, the point estimate captures both the direct effect of Facebook on students who joined the platform and the indirect effect of Facebook on students who did not join the platform, but whose peers did.<sup>19</sup> 

In order to help build intuition about the magnitude of our baseline effects, we provide a few benchmarks. First, the magnitude of our baseline effect corresponds to approximately 84% of the difference in the index of poor mental health between students in our sample with and without credit card debt. Second, we benchmark the magnitude of our estimates against the effect of a sudden unemployment spell on mental health. Comparing our estimates to the most closely related ones in a meta-analysis by Paul and Moser (2009), we find that the impact of introducing Facebook at a college on mental health is around 22% of the effect of job loss.<sup>20</sup> Lastly, we benchmark our results against the canonical PHQ-9 and GAD-7 mental health scales. We use data from the validation survey mentioned in Section 4 and discussed in detail in Appendix C to determine how to weigh the variables contained in our index of

---

[referencia=13d0780828065ceb score=0.987]
> 2See Roth et al. (2022) for a recent overview. 

2 

Our main finding is that the introduction of Facebook at a college had a negative effect on student mental health. Our index of poor mental health, which aggregates all the relevant mental health variables in the NCHA survey, increased by 0.085 standard deviation units as a result of the introduction of Facebook. As a point of comparison, this magnitude is around 22% of the effect of losing one’s job on mental health, as reported in a meta-analysis by Paul and Moser (2009). We further benchmark our results against a clinically-validated depression scale: the PHQ-9 (Kroenke et al., 2001). The effect of the introduction of Facebook on our index of poor mental health is equivalent to a two-percentage-point increase in the share of students suffering from depression according to the PHQ-9 over a baseline of 25%. The negative effects on mental health are strongest for students who, based on immutable characteristics such as gender and age, are predicted to be most susceptible to mental illness. For those students, we also observe a significant increase in depression diagnoses, take-up of psychotherapy for depression, and use of anti-depressants. Finally, we find that, after the introduction of Facebook, students were more likely to report that their academic performance was negatively affected by conditions related to poor mental health. 

What explains the negative effects of Facebook on mental health? The pattern of results is consistent with Facebook increasing students’ ability to engage in unfavorable social comparisons. Two main pieces of evidence bear on this conclusion. First, we find that the effects are particularly pronounced for students who may view themselves as comparing unfavorably to their peers, such as students who live off-campus—and therefore are more likely to be excluded from on-campus social activities—students of lower socioeconomic status, and students not belonging to fraternities/sororities. Second, we show that the introduction of Facebook directly affected the students’ beliefs about their peers’ social lives and behaviors, especially in relation to alcohol consumption. As far as other channels are concerned, we do not find significant evidence that the negative effects of Facebook on mental health are due to disruptive internet use. We also rule out several alternative mechanisms, such as reduced stigma about mental illness and direct effects on drug use, alcohol consumption, and sexual behaviors.

---

[referencia=13d0780828065ceb score=0.939]
> 19Although we cannot separate these two channels in the absence of data on an individual’s Facebook use, we note that it is unlikely that our results are primarily driven by students who did not have a Facebook account. As discussed in Section 2, the average penetration rate of Facebook at each college was around 85%. Therefore, an effect concentrated solely among students who did not join the platform would have to be implausibly large— approximately 0.57 standard deviations in our main specification—to be consistent with our baseline effect. 

> 20Paul and Moser (2009) analyze studies estimating various aspects of mental health including symptoms of distress, depression, anxiety, psychosomatic symptoms, subjective well-being, and self-esteem. The estimates from Paul and Moser (2009) that can most credibly be interpreted as causal and hence be compared to our estimates are those that rely on quasi-experimental variation in job loss due to factory closures and mass layoffs. 

17 

poor mental health in a way that best predicts an indicator for having depression according to the PHQ-9 and an indicator for having generalized anxiety disorder according to the GAD7. Next, we apply these weights to the NCHA sample to predict whether a student taking the NCHA survey would be classified as having depression or generalized anxiety disorder according to the PHQ-9 and GAD-7. Appendix Table A.29 shows that the introduction of Facebook increased by two percentage points the fraction of students whom, according to our prediction, the PHQ-9 and GAD-7 would classify as having depression or generalized anxiety disorder. The two percentage point increase corresponds to a 9% increase over the pre-period mean of 25% for depression and a 12% increase over the pre-period mean of 16% for generalized anxiety disorder.<sup>21</sup>

---

[referencia=13d0780828065ceb score=0.887]
Figure 6: Heterogeneous Effects as Evidence of Unfavorable Social Comparisons 



<!-- Start of picture text -->
Post Facebook Introduction x<br>Off-campus Living<br>Post Facebook Introduction x<br>Not in Fraternity/Sorority<br>Post Facebook Introduction x<br>Credit-card Debt<br>Post Facebook Introduction x<br>Work<br>Post Facebook Introduction x<br>Overweight<br>Post Facebook Introduction x<br>Index Social Comparisons<br>-.08 -.04 0 .04 .08<br>Interaction Coefficient<br>(standard deviations)<br><!-- End of picture text -->

_Notes_ : This figure explores the mechanisms behind the effects of Facebook on mental health. It presents estimates from a version of Equation (1) in which our treatment indicator is interacted with a set of indicators for belonging to a certain sub-population of students. The outcome variable is our overall index of poor mental health. The estimates are obtained using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. For a detailed description of the outcome, treatment, interaction, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

41 

Table 1: Baseline Results: Index of Poor Mental Health 

||Ind|ex of Poor|Mental He|alth|
|---|---|---|---|---|
||(1)|(2)|(3)|(4)|
|Post Facebook Introduction|0.137<sup>_∗∗∗_</sup>|0.124<sup>_∗∗∗_</sup>|0.085<sup>_∗∗_</sup>|0.077<sup>_∗∗_</sup>|
||(0.040)|(0.022)|(0.033)|(0.032)|
|Observations|374,805|359,827|359,827|359,827|
|Survey Wave FE|✓|✓|✓|✓|
|FB Expansion Group FE|✓|✓|||
|Controls||✓|✓|✓|
|College FE|||✓|✓|
|FB Expansion GroupLinear Time Trends||||✓|

---

[referencia=13d0780828065ceb score=0.771]
Armed with our LASSO prediction, we can study how the introduction of Facebook at a college affected students across the mental-illness-susceptibility spectrum, and whether it induced students who are more likely to be on the margin of a depression diagnosis to seek out depression-related services such as psychotherapy. The upper left panel of Figure 3 presents the estimated effects on the index of poor mental health across quintiles of our LASSO-predicted measure of susceptibility to mental illness.<sup>28</sup> As shown in the figure, the effects of the introduction of Facebook on symptoms of poor mental health tend to be stronger for individuals with a higher baseline risk of developing mental illness.<sup>29</sup> 

The upper right panel of Figure 3 shows that the introduction of Facebook on the take-up of depression-related services exhibits a similar pattern. We find weak positive effects throughout the distribution of predicted susceptibility to mental illness, though for most quintiles the point estimates are fairly small and not statistically significant. The effects become more pronounced for individuals in the top quintile; in particular, the point estimate on the top quintile is relatively large in magnitude (0.063 standard deviations) and four times as large as the point estimate on the bottom quintile. As indicated in column (2) of Table A.5, the difference between the coefficients for the top and the bottom quintiles is significant at the 1% level. These results suggest that, indeed, students who are predicted to be most susceptible to mental illness—and therefore more likely to seek mental healthcare due to a worsening in symptoms—are more likely to take up depression-related services such as psychotherapy for depression and anti- 

> 28Specifically, we estimate the following modification of Equation (1): 



> where MHSusceptQ _i_ are the quintiles of _i_<sup>_′_</sup> _s_ predicted susceptibility to mental illness. Figure 3 presents the estimates of _βq_ . Appendix Table A.5 presents these estimates in a table form, together with _p_ -values for comparisons between the first quintile and other quintiles.

---

[referencia=13d0780828065ceb score=0.767]
#### **A Robustness Checks** 

This section presents a battery of exercises that probe the robustness of our estimates. 

First, as a placebo test, Table A.8 presents a set of specification checks on our LASSOpredicted measure of susceptibility to mental illness. Since the prediction is based on students’ immutable characteristics, it should not be affected by the introduction of Facebook at a college. In fact, if we did find an effect on this measure, we would worry that the introduction of Facebook affected the selection of students responding to the survey along dimensions that are predictive of mental illness. Comfortingly, the point estimates in Table A.8 are small and not significant. Table A.9 presents a similar robustness test using all available immutable individual-level characteristics as outcomes. Reassuringly, the point estimates are very small and only one out of the 13 estimates is statistically significant at the 10% level. 

As an additional placebo test, Table A.10 presents a set of specification checks on an index of all physical rather than mental health outcomes in our dataset (e.g., asthma, diabetes, hepatitis). Consistent with intuition, the effects of the introduction of Facebook on physical health are significantly smaller than the effects on mental health across all specifications and, in our preferred specification with college rather than Facebook-expansion-group fixed effects, also statistically indistinguishable from zero. Figure A.8 displays the cumulative distribution of coefficients on the individual components of our indices of poor mental and poor physical health. As shown in the figure, the distribution of coefficients on the components of the index of poor mental health first-order stochastically dominates the distribution of coefficients on the components of the index of poor physical health. A Mann-Whitney U test rejects the hypothesis of equality of the two distributions at the 1% significance level.<sup>46</sup> 

Next, we show that the results on our index of poor mental health are not driven by the way in which we construct the index, by any one outcome variable, by any particular Facebook expansion group, or by how we define treatment status when the semester in which a student

---

[referencia=13d0780828065ceb score=0.746]
52 

Figure A.5: Effect of the Introduction of Facebook on Student Mental Health, with Expansion-Group-Specific Linear Trends 



<!-- Start of picture text -->
Last year felt hopeless<br>Last year felt overwhelmed<br>Last year felt exhausted<br>Last year felt very sad<br>Last year severely depressed<br>Last year seriously considered suicide<br>Last year attempted suicide<br>Last year depression<br>Index Symptoms Depression<br>Last year anorexia<br>Last year anxiety disorder<br>Last year bulimia<br>Last year seasonal affect disorder<br>Index Symptoms Other Conditions<br>Last year depression diagnosis<br>Therapy depression<br>Current medication depression<br>Index Depression Services<br>Index Poor Mental Health<br>-.15 -.1 -.05 0 .05 .1 .15<br>Treatment effect<br>(standard deviations)<br>DepressionSymptoms<br>Other<br>Symptoms<br>Services<br>Depression<br><!-- End of picture text -->

_Notes_ : This figure explores the robustness of our baseline effects of the introduction of Facebook at a college on all our mental health outcome variables and on the related indices. Specifically, it presents estimates of coefficient _β_ from Equation (1) using a specification that includes survey-wave fixed effects, college fixed effects, controls, and Facebook expansion-group-specific linear time trends. The outcome variables are our overall index of poor mental health, the individual components of the index, and three sub-indices: the index of depression symptoms, the index of symptoms of other mental health conditions, and the index of depression services. All outcomes are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. The reason why the point estimate on an index might be relatively large compared to the point estimates on each of the components of the index is that averaging across the index components reduces noise and, as a consequence, might increase the effect size measured in standard deviation units. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

53 

Figure A.6: Heterogeneous Effects 



<!-- Start of picture text -->

---

[referencia=13d0780828065ceb score=0.732]
Figure 1 presents results on our individual outcome variables and shows that most of the dimensions of mental health in our dataset were negatively affected by the introduction of Facebook.<sup>22</sup> For all but one of the mental health outcomes from Figure 1, the point estimates are positive, which indicates worsened mental health. The conditions that appear to be most affected are depression and anxiety-related disorders, while the point estimates on anorexia and bulimia are close to zero.<sup>23</sup> The effect on severe depression is similar in magnitude to the effect observed in Allcott et al. (2020) on whether a respondent felt depressed in the past month (0.07 vs. 0.09 standard deviations, respectively). Such similarity is striking, especially in light of the fact that the time period, target population, and empirical strategy in Allcott et al. (2020) are different from the ones in this paper. 

The bottom section of Figure 1 also presents suggestive evidence that the introduction of Facebook at a college might have increased the extent to which students took up depressionrelated services. For all three items comprising the index of depression services—receiving an official depression diagnosis, going to therapy for depression, and taking anti-depressants— the point estimates are positive, though not significant at conventional levels.<sup>24</sup> Finding a 

> 21 This exercise is discussed in more detail in Appendix C. 

> 22Appendix Table A.4 provides regression results for the individual mental health variables in both normalized (standard deviation) units and un-normalized (original) units. The table also provides unadjusted _p_ -values and “sharpened” False Discovery Rate (FDR)-adjusted _q_ -values following the procedure of Benjamini et al. (2006), as outlined by Anderson (2008). The _p_ -values are appropriate for readers with a priori interest in a particular outcome; the _q_ -values adjust the inference for multiple hypotheses testing. 

> 23Similar patterns can be observed in Figure A.5 which is a version of Figure 1 with expansion-group-specific linear trends. 

> 24Note that, given the low average take-up of these services, the estimates represent large increases over the baseline mean. For anti-depressants and psychotherapy, the point estimates represent an increase of about 13% 

18

---

[referencia=13d0780828065ceb score=0.676]
39 

Figure 4: Effect on Poor Mental Health by Length of Exposure to Facebook 



<!-- Start of picture text -->
0 1 2 3 4 5<br>Treatment Length in Semesters<br>.2<br>.1<br>Coefficient<br>0<br><!-- End of picture text -->

_Notes_ : This figure explores the effects of length of exposure to Facebook on our index of poor mental health by presenting estimates of Equation (4). The index is standardized so that, in the pre-period, it has a mean of zero and a standard deviation of one. The dashed curve is the quadratic curve of best fit. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. Students who entered college in 2006 might have been exposed to Facebook already in high-school, because, starting in September 2005, college students with Facebook access could invite high-school students to join the platform. Such students are excluded from the regression. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

40 

Figure 5: Downstream Effects on Academic Performance 



<!-- Start of picture text -->
Academic perform attention deficit<br>Academic perform depression/anxiety/<br>seasonal affect disorder<br>Academic perform eating disorder<br>Academic perform sleep difficulty<br>Academic perform stress<br>Index Downstream Effects<br>-.15 -.1 -.05 0 .05 .1 .15<br>Treatment effect<br>(standard deviations)<br><!-- End of picture text -->

_Notes_ : This figure explores downstream effects of the introduction of Facebook on the students’ academic performance. It presents estimates of coefficient _β_ from Equation (1) using our preferred specification, including survey-wave fixed effects, college fixed effects, and controls. The outcome variables are answers to questions inquiring as to whether various mental health conditions affected the students’ academic performance and our index of downstream effects. All outcomes are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level.

---

[referencia=13d0780828065ceb score=0.583]
55 

Figure A.8: Cumulative Distribution of Coefficients on Components of the Index of Poor Mental Health and the Index of Poor Physical Health 



<!-- Start of picture text -->
back pain<br>bronchitis felt hopeless<br>strep<br>HIV severely depressed<br>pelvic inflammatory<br>anxiety disorder<br>had allergy<br>hep. B or C seasonal affect disorder<br>high blood pressure<br>chronic fatigue felt exhausted<br>diabetes<br>endometriosis depression<br>high cholesterol<br>ear infection felt very sad<br>mono<br>asthma seriously considered suicide<br>sinus infection<br>tuberculosis felt overwhelmed<br>broken bone<br>gential herpes bulimia<br>gential warts<br>carpal tunnel attempted suicide<br>gonnorrhea<br>chlamydia anorexia<br>-.05 0 .05 .1<br>Point Estimate (standard deviation units)<br>Index of Poor Physical Health Components  Index of Poor Mental Health Components<br>1<br>.8<br>.6<br>.4<br>Empirical CDF<br>.2<br>0<br><!-- End of picture text -->

_Notes_ : This figure displays cumulative distribution functions of the coefficients on the components of the indices of poor mental and poor physical health. The figure is constructed as follows: first, we computed estimates of coefficients _β_ from Equation (1) for each component of the index of poor physical health and for each component of the index of poor mental health. Second, we constructed two cumulative distribution functions using the estimated coefficients: one for the components of the index of poor physical health, and one for the components of the index of poor mental health. All estimates are obtained using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. The outcomes are always standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the index components, the treatment and the control variables, see Appendix Table A.30. 

56

---

[referencia=13d0780828065ceb score=0.572]
65 

Table A.5: Heterogeneous Effects by Predicted Susceptibility to Mental Illness 

||Index<br>Symptoms<br>Poor Mental<br>Health<br>(1)|Index<br>Depression<br>Services<br>(2)|Index<br>Downstream<br>Effects<br>(3)|
|---|---|---|---|
|Post Facebook Introduction_×_|0.068**|0.015|0.033|
|_×_1st Quintile in Mental Illness Susceptibility|(0.033)|(0.029)|(0.031)|
|Post Facebook Introduction_×_|0.067*|0.034|0.062**|
|_×_2nd Quintile in Mental Illness Susceptibility|(0.035)|(0.029)|(0.031)|
|_P-value for coeff. diff. with 1st quintile_|_0.878_|_0.039_|_0.019_|
|Post Facebook Introduction_×_|0.079**|0.028|0.079**|
|_×_3rd Quintile in Mental Illness Susceptibility|(0.033)|(0.028)|(0.032)|
|_P-value for coeff. diff. with 1st quintile_|_0.358_|_0.228_|_0.000_|
|Post Facebook Introduction_×_|0.089***|0.035|0.072**|
|_×_4th Quintile in Mental Illness Susceptibility|(0.035)|(0.030)|(0.033)|
|_P-value for coeff. diff. with 1st quintile_|_0.066_|_0.103_|_0.002_|
|Post Facebook Introduction_×_|0.138***|0.063**|0.121***|
|_×_5th Quintile in Mental Illness Susceptibility|(0.035)|(0.031)|(0.033)|
|_P-value for coeff. diff. with 1st quintile_|_0.000_|_0.002_|_0.000_|
|Observations|361,045|378,456|368,344|
|College FE|✓|✓|✓|
|Surve Wave FE|✓|✓|✓|
|Controls|✓|✓|✓|

---

[referencia=13d0780828065ceb score=0.561]
###### Figure A.9: Robustness to Excluding Each Variable from the Index of Poor Mental Health 



<!-- Start of picture text -->
Index Poor Mental Health<br>Excluding Felt Hopeless<br>Excluding Felt Overwhelmed<br>Excluding Felt Exhausted<br>Excluding Felt Very Sad<br>Excluding Severely Depressed<br>Excluding Ser. Considered Suicide<br>Excluding Attempted Suicide<br>Excluding Was Depressed<br>Excluding Anorexia<br>Excluding Anxiety Disorder<br>Excluding Bulimia<br>Excluding Seasonal Affect Dis.<br>Excluding Depression Diagnosis<br>Excluding Therapy Depression<br>Excluding Medication Depression<br>-.15 -.1 -.05 0 .05 .1 .15<br>Treatment effect<br>(standard deviations)<br>Excluded Variable<br><!-- End of picture text -->

_Notes_ : This figure explores the robustness of our baseline results to excluding each individual variable from the construction of the index of poor mental health. Specifically, it presents estimates of coefficient _β_ from Equation (1). Each row excludes a different variable from the construction of the index. The index is always standardized so that, in the pre-period, it has a mean of zero and a standard deviation of one. All estimates are obtained using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

57 

Figure A.10: Heterogeneous Effects by Predicted Susceptibility to Mental Illness, with Susceptibility Defined Using the Index of Poor Mental Health 



<!-- Start of picture text -->

---

[referencia=13d0780828065ceb score=0.556]
##### **5.2 Heterogeneity** 

**Heterogeneity by Predicted Susceptibility to Mental Illness.** In order to study whether the introduction of Facebook at a college led students on the margin of a depression diagnosis to take up depression-related services, we proceed in two steps: first, we estimate a LASSO to identify individuals who, based on baseline immutable characteristics, are more susceptible to mental illness. Second, we show heterogeneous treatment effects based on our LASSOpredicted measure of susceptibility to mental illness. 

The LASSO prediction is generated as follows: first, we construct an indicator that equals one if a student has ever been diagnosed with a mental health condition. Second, we consider a set of immutable individual-level characteristics (age, year in school, gender, race, an indicator for U.S. citizenship, and height), generate all two-way interactions between these characteristics, and generate second- and third-order monomials of each characteristic. Third, we implement a LASSO procedure in the pre-period to predict our indicator for ever having been diagnosed with a mental health condition based on the immutable individual-level char- 

> 26Appendix Figure A.4 shows the TWFE OLS estimates of a version of equation (2) that considers each of the first three Facebook expansion groups in turn and compares it to the last Facebook expansion group. These figures are constructed at the yearly level to reduce noise arising from the smaller number of observations. Consistent with Facebook having a negative impact on student mental health, in all the pairwise comparisons, all the estimates in the post-period are positive and most are statistically significant while the estimates in the pre-period are not statistically different from zero. 

> 27Contrary to the recently-developed robust estimators, the OLS estimator shows a relatively flat trend in the post-period. This is likely because, in the case of dynamically-increasing treatment effects, the OLS estimator, which uses already-treated units as controls for newly-treated units, exhibits a downward bias. 

20 

acteristics and functions thereof described above. 

In order to test the quality of the prediction, we plot our measure of predicted susceptibility to mental illness against our index of poor mental health. Appendix Figure A.7 shows a strong relationship between the index of poor mental health and our predicted measure of susceptibility to mental illness.

---

[referencia=13d0780828065ceb score=0.547]
##### **5.5 Downstream Implications of Poor Mental Health** 

Does the effect of Facebook on mental health have negative downstream repercussions on academic performance? According to the students’ reports, the answer is affirmative. 

One of the NCHA survey questions inquires as to whether various conditions affected the students’ academic performance. The conditions related to mental health are: attention deficit disorder, depression/anxiety disorder/seasonal affect disorder, eating disorders, stress, 

> 32Indeed, missing values are more common in the NCHA survey among sensitive questions (Kays et al., 2012). 

24 

and sleep difficulties.<sup>33</sup> The main advantage of analyzing these questions is that they trace a pathway from the introduction of Facebook to perceptions of worsened academic performance via poor mental health. It is important to emphasize, however, that we do not directly measure effects on grades, and that we do not rule out potential positive effects of Facebook on students’ academic performance due to channels unrelated to mental health, such as improved teamwork.<sup>34</sup> 

Figure 5 presents estimates of Equation (1) and shows how the introduction of Facebook affected each of the measures described in the previous paragraph. All the point estimates are positive and the coefficient for an equally-weighted index summarizing them is positive and significant, suggesting that, after the introduction of Facebook, students were more likely to report that their academic performance was impaired as a result of poor mental health. The effect size on the index is 0.067 standard deviation units. Consistent with our evidence suggesting that depression and anxiety-related disorders are the conditions most severely affected by the introduction of Facebook, we find the largest effect on the depression/anxietydisorder/seasonal-affect-disorder measure. The number of students who reported that those conditions impaired their academic performance increased by three percentage points over a baseline of 13%. Finally, the bottom-left panel in Figure 3 and column (3) of Table A.5 show that the negative effect of poor mental health on self-reported academic performance is especially pronounced among the students who are predicted to be most susceptible to mental illnesses.

---

[referencia=13d0780828065ceb score=0.542]
_Notes_ : This figure explores the relationship between our index of symptoms of depression and ever having been diagnosed with depression. Specifically, for each ventile of our index of depression symptoms, the figure plots the fraction of individuals who have ever received a depression diagnosis. The index is standardized so that, in the preperiod, it has a mean of zero and a standard deviation of one. The figure also displays the correlation coefficient between the index of depression symptoms and the fraction of individuals ever diagnosed with depression. 

Figure A.13: Performance of Binary Classifier based on Index of Symptoms of Depression 



<!-- Start of picture text -->
0.00 0.25 0.50 0.75 1.00<br>False Positive Rate<br>Area under ROC curve = 0.7707<br>1.00<br>0.75<br>0.50<br>True Positive Rate<br>0.25<br>0.00<br><!-- End of picture text -->

_Notes_ : The figure presents the Receiver-Operating-Characteristic curves of the binary classifiers constructed by running a logit model of ever having been diagnosed with depression on our index of depression symptoms. 

60 

Figure A.14: Relationship Between the Index of Poor Mental Health and the PHQ-9 



<!-- Start of picture text -->
Correlation coef. 0.66<br>15<br>10<br>5<br>−1 0 1 2<br>NCHA − Poor Mental Health Index, Std. Dev.<br>PHQ−9 Total<br><!-- End of picture text -->

_Notes_ : This figure explores the relationship between our index of poor mental health and PHQ-9 scores in a survey conducted among college students in 2022 and described in detail in Appendix C. Specifically, for each ventile of our index of poor mental health, the figure plots the mean PHQ-9 score. The figure also displays the correlation coefficient between the index of poor mental health and the PHQ-9 score. 

Figure A.15: Relationship Between the Index of Poor Mental Health and the GAD-7 



<!-- Start of picture text -->
16 Correlation coef. 0.61<br>12<br>8<br>4<br>−1 0 1 2<br>NCHA − Poor Mental Health Index, Std. Dev.<br>GAD−7 Total<br><!-- End of picture text -->

---

[referencia=13d0780828065ceb score=0.539]
38 

Figure 3: Heterogeneous Effects by Predicted Susceptibility to Mental Illness 



<!-- Start of picture text -->
Index Symptoms Poor Mental Health Index Depression Services<br>1 2 3 4 5 1 2 3 4 5<br>Quintile of Predicted Susceptibility to Mental Illness Quintile of Predicted Susceptibility to Mental Illness<br>Index Downstream Effects<br>1 2 3 4 5<br>Quintile of Predicted Susceptibility to Mental Illness<br>.2<br>.2<br>.15 .15<br>Coefficient .1.05 Coefficient .1.05<br>0 0<br>-.05 -.05<br>.2<br>.15<br>Coefficient .1.05<br>0<br>-.05<br><!-- End of picture text -->

_Notes_ : This figure explores the extent to which the effects of the introduction of Facebook at a college are heterogeneous depending on students’ predicted susceptibility to mental illness. Specifically, it presents the estimates from equation (3) in which our indicator for post-Facebook introduction is interacted with a set of indicators for belonging to each quintile of a LASSO-predicted measure of susceptibility to mental illness. The outcome variable in the top-left panel is our index of symptoms of poor mental health; the outcome variable in the top-right panel is our index of depression services; the outcome variable in the bottom-left panel is our index measuring whether students reported that conditions related to poor mental health negatively affected their academic performance. All indices are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. The estimates (also displayed in Table A.5) are obtained using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the outcome, treatment, interaction, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

39 

Figure 4: Effect on Poor Mental Health by Length of Exposure to Facebook 



<!-- Start of picture text -->

---

[referencia=13d0780828065ceb score=0.520]
_Notes_ : This table explores the effects of length of exposure to Facebook on student mental health. It presents estimates of coefficient _β_ from an equation similar to Equation (4) where we assume that the number of treated semester has a linear effect on mental health and includes survey-wave by college fixed effects: _Yicgt_ = _β ×_ FB _gt ×_ [ _t −_ max _{τi, τc}_ ]+ **X** _i · γ_ + _λct_ + _εicgt_ . The outcome variables are the overall index of poor mental health (columns (1) and (2)), the index of symptoms of poor mental health (columns (3) and (4)), and the index of depression services (columns (5) and (6)). All indices are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. Odd-numbered columns present estimates of Equation (4) including survey-wave fixed effects, college fixed effects, and controls; even-numbered columns replace survey-wave fixed effects and college fixed effects with survey-wave _×_ college fixed effects. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. Cohorts of students who might have been exposed to Facebook in high school are excluded from the regression. See Footnote 31 for details. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. Standard errors in parentheses are clustered at the college level. * p _<_ 0.1, ** p _<_ 0.05, *** p _<_ 0.01. 

Table A.7: Length of Exposure to Facebook and Depression Services

---

[referencia=13d0780828065ceb score=0.509]
> 24Note that, given the low average take-up of these services, the estimates represent large increases over the baseline mean. For anti-depressants and psychotherapy, the point estimates represent an increase of about 13% 

18 

more muted average effect on depression-related services than on depression symptoms is arguably in line with intuition, in that an increase in symptoms of poor mental health induces the marginal student, rather than the average student, to take up mental healthcare services.<sup>25</sup> In Section 5.2 below, we show that students who, based on immutable baseline characteristics, are predicted to be most susceptible to mental illness—and therefore more likely to be on the margin of receiving a depression diagnosis—are indeed significantly more likely to take up depression-related services after the introduction of Facebook. 

**Event Study Figures.** In order to test for parallel trends and study the dynamics of treatment effects, we estimate an event study-version of the TWFE model with indicators for distance to/from the introduction of Facebook. Specifically, we estimate the following specification: 



where _Yigt_ is our index of poor mental health and _Dk_ ( _gt_ ) is set of indicator variables that take value one if, for expansion group _g_ in survey wave _t_ , the introduction of Facebook was _k_ semesters away. When estimating the model using OLS, we treat students who took the survey in the semester just before Facebook was rolled out at their college as the omitted category and compare them to students who took the NCHA survey in other semesters. 

As discussed in Sun and Abraham (2021), the fully-dynamic version of the TWFE model in Equation (2) estimated using OLS delivers consistent estimates only under relatively strong assumptions regarding treatment effect homogeneity. In order to allow for heterogeneity in treatment effects across time and treated units, we also present the event study figures generated by a set of recently-proposed estimators that are robust to treatment effect heterogeneity (Borusyak et al., 2021; Callaway and Sant’Anna, 2021; De Chaisemartin and d’Haultfoeuille, 2020; Sun and Abraham, 2021). 

Figure 2 presents the event-study figures and shows that the estimates are consistent with the parallel trends assumption: independently of the estimator used, the coefficients on the semesters prior to the introduction of Facebook at a college are all close to zero and exhibit no

---

[referencia=13d0780828065ceb score=0.483]
_Notes_ : This figure explores the effects of the introduction of Facebook at a college on all our mentalhealth outcome variables and on the related indices. Specifically, it presents estimates of coefficient _β_ from Equation (1) using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. The outcome variables are our overall index of poor mental health, the individual components of the index, and three sub-indices: the index of depression symptoms, the index of symptoms of other mental health conditions, and the index of depression services. All outcomes are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. The reason why the point estimate on an index might be relatively large compared to the point estimates on each of the components of the index is that averaging across the index components reduces noise and, as a consequence, might increase the effect size measured in standard deviation units. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

37

---

[referencia=13d0780828065ceb score=0.481]
53 

Figure A.6: Heterogeneous Effects 



<!-- Start of picture text -->
Post Facebook Introduction x<br>Female<br>Post Facebook Introduction x<br>White (not Hispanic)<br>Post Facebook Introduction x<br>Above Median Height<br>Post Facebook Introduction x<br>International<br>Post Facebook Introduction x<br>Above Median Age<br>Post Facebook Introduction x<br>Volunteer<br>Post Facebook Introduction x<br>First-year<br>Post Facebook Introduction x<br>First-Year, Immediate Effect<br>-.08 -.04 0 .04 .08<br>Interaction Coefficient<br>(standard deviations)<br><!-- End of picture text -->

_Notes_ : This figure explores whether the effects of the introduction of Facebook on student mental health are heterogeneous across a host of demographic characteristics. Specifically, it presents estimates from a version of Equation (1) in which our treatment indicator is interacted with various moderators. The outcome variable is our index of poor mental health. The index is standardized so that, in the pre-period, it has a mean of zero and a standard deviation of one. The moderators are indicators for: identifying as female, identifying as white (non-Hispanic), being an international student, being above median age, volunteering, and being a first-year student (freshman). In the last row, we restrict our sample to only include students who took the survey at most one semester after the introduction of Facebook at their college. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

54 

Figure A.7: Relationship between the LASSO-Predicted Measure of Susceptibility to Mental Illness and the Index of Poor Mental Health 



<!-- Start of picture text -->