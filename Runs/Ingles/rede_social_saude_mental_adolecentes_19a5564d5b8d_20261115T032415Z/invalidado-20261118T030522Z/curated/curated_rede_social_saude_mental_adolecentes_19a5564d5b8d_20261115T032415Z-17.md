[referencia=13d0780828065ceb score=0.965]
> 29We note that, for predicting baseline susceptibility to mental illness, the stock variable of ‘having ever been diagnosed’ with a mental illness is arguably more relevant than the flow variable of having exhibited a certain symptom in the past year, because the former captures information covering a longer time span. Appendix Figure A.10 examines robustness of our results to an alternative measure of susceptibility to mental illness based on a LASSO regression predicting whether a respondent’s index of poor mental health is in the top 10% of the pre-period sample. The results are qualitatively similar. 

21 

depressants as a result of the introduction of Facebook. 

**Other dimensions of heterogeneity.** Appendix Figure A.6 estimates heterogeneous effects across several baseline characteristics. Consistent with surveys showing that women use social media more often and are more likely to report using Facebook for longer than they intend, we find suggestive evidence that the results are larger among women (Thompson and Lougheed, 2012; Lin et al., 2016).<sup>30</sup> We also find stronger effects on non-Hispanic whites, and a weaker effect on international students, younger students, and first-years.

---

[referencia=13d0780828065ceb score=0.937]
Armed with our LASSO prediction, we can study how the introduction of Facebook at a college affected students across the mental-illness-susceptibility spectrum, and whether it induced students who are more likely to be on the margin of a depression diagnosis to seek out depression-related services such as psychotherapy. The upper left panel of Figure 3 presents the estimated effects on the index of poor mental health across quintiles of our LASSO-predicted measure of susceptibility to mental illness.<sup>28</sup> As shown in the figure, the effects of the introduction of Facebook on symptoms of poor mental health tend to be stronger for individuals with a higher baseline risk of developing mental illness.<sup>29</sup> 

The upper right panel of Figure 3 shows that the introduction of Facebook on the take-up of depression-related services exhibits a similar pattern. We find weak positive effects throughout the distribution of predicted susceptibility to mental illness, though for most quintiles the point estimates are fairly small and not statistically significant. The effects become more pronounced for individuals in the top quintile; in particular, the point estimate on the top quintile is relatively large in magnitude (0.063 standard deviations) and four times as large as the point estimate on the bottom quintile. As indicated in column (2) of Table A.5, the difference between the coefficients for the top and the bottom quintiles is significant at the 1% level. These results suggest that, indeed, students who are predicted to be most susceptible to mental illness—and therefore more likely to seek mental healthcare due to a worsening in symptoms—are more likely to take up depression-related services such as psychotherapy for depression and anti- 

> 28Specifically, we estimate the following modification of Equation (1): 



> where MHSusceptQ _i_ are the quintiles of _i_<sup>_′_</sup> _s_ predicted susceptibility to mental illness. Figure 3 presents the estimates of _βq_ . Appendix Table A.5 presents these estimates in a table form, together with _p_ -values for comparisons between the first quintile and other quintiles.

---

[referencia=13d0780828065ceb score=0.912]
##### **5.3 Effects Based on Length of Exposure to Facebook** 

The effects of the introduction of Facebook estimated thus far leverage variation that occurs at the college–survey-wave level. Our dataset also features variation at the college–survey-wave– year-in-school level that we can leverage to study the effects of length of exposure to Facebook at the level of individual students. For instance, in the early spring of 2006, a freshman at Harvard would have been exposed to Facebook for one full semester, whereas a senior at Harvard would have been exposed for more than three full semesters. 

In order to study the effects of length of exposure to Facebook at the level of individual students, we estimate a version of Equation (1) with individual-level treatment intensity. In this alternative specification, we include a student-level treatment component that equals the number of semesters that the student had access to Facebook given: i) the college the student attends; ii) the survey wave the student participated in; and iii) the year in which the student started college. Specifically, we estimate the following equation: 



where Semesters _k_ ( _ict_ ) is a set of indicators that equal one if student _i_ at college _c_ in surveywave _t_ had access to Facebook for _k_ semesters. The number of treated semesters is calculated as _k_ = FB _gt ×_ [ _t −_ max _{τi, τc}_ ]; _t_ represents time in semesters; _τc_ represents the semester in 

> 30Furthermore, baseline prevalence of depression is found to be higher among women, across different nations, cultures, and age groups (Nolen-Hoeksema and Hilt, 2008; Albert, 2015; Salk et al., 2017). Thus, the slightly stronger effects among women are also consistent with studies showing that women are more likely to be affected by certain mental illnesses. 

22 

which Facebook was introduced at college _c_ attended by student _i_ ; _τi_ represents the semester in which student _i_ started studying at college _c_ ; and, as before, FB _gt_ is the indicator function for whether Facebook was available at student _i_ ’s college _c_ by time _t_ .<sup>31</sup>

---

[referencia=13d0780828065ceb score=0.869]
Figure 1 presents results on our individual outcome variables and shows that most of the dimensions of mental health in our dataset were negatively affected by the introduction of Facebook.<sup>22</sup> For all but one of the mental health outcomes from Figure 1, the point estimates are positive, which indicates worsened mental health. The conditions that appear to be most affected are depression and anxiety-related disorders, while the point estimates on anorexia and bulimia are close to zero.<sup>23</sup> The effect on severe depression is similar in magnitude to the effect observed in Allcott et al. (2020) on whether a respondent felt depressed in the past month (0.07 vs. 0.09 standard deviations, respectively). Such similarity is striking, especially in light of the fact that the time period, target population, and empirical strategy in Allcott et al. (2020) are different from the ones in this paper. 

The bottom section of Figure 1 also presents suggestive evidence that the introduction of Facebook at a college might have increased the extent to which students took up depressionrelated services. For all three items comprising the index of depression services—receiving an official depression diagnosis, going to therapy for depression, and taking anti-depressants— the point estimates are positive, though not significant at conventional levels.<sup>24</sup> Finding a 

> 21 This exercise is discussed in more detail in Appendix C. 

> 22Appendix Table A.4 provides regression results for the individual mental health variables in both normalized (standard deviation) units and un-normalized (original) units. The table also provides unadjusted _p_ -values and “sharpened” False Discovery Rate (FDR)-adjusted _q_ -values following the procedure of Benjamini et al. (2006), as outlined by Anderson (2008). The _p_ -values are appropriate for readers with a priori interest in a particular outcome; the _q_ -values adjust the inference for multiple hypotheses testing. 

> 23Similar patterns can be observed in Figure A.5 which is a version of Figure 1 with expansion-group-specific linear trends. 

> 24Note that, given the low average take-up of these services, the estimates represent large increases over the baseline mean. For anti-depressants and psychotherapy, the point estimates represent an increase of about 13% 

18

---

[referencia=13d0780828065ceb score=0.831]
> 24Note that, given the low average take-up of these services, the estimates represent large increases over the baseline mean. For anti-depressants and psychotherapy, the point estimates represent an increase of about 13% 

18 

more muted average effect on depression-related services than on depression symptoms is arguably in line with intuition, in that an increase in symptoms of poor mental health induces the marginal student, rather than the average student, to take up mental healthcare services.<sup>25</sup> In Section 5.2 below, we show that students who, based on immutable baseline characteristics, are predicted to be most susceptible to mental illness—and therefore more likely to be on the margin of receiving a depression diagnosis—are indeed significantly more likely to take up depression-related services after the introduction of Facebook. 

**Event Study Figures.** In order to test for parallel trends and study the dynamics of treatment effects, we estimate an event study-version of the TWFE model with indicators for distance to/from the introduction of Facebook. Specifically, we estimate the following specification: 



where _Yigt_ is our index of poor mental health and _Dk_ ( _gt_ ) is set of indicator variables that take value one if, for expansion group _g_ in survey wave _t_ , the introduction of Facebook was _k_ semesters away. When estimating the model using OLS, we treat students who took the survey in the semester just before Facebook was rolled out at their college as the omitted category and compare them to students who took the NCHA survey in other semesters. 

As discussed in Sun and Abraham (2021), the fully-dynamic version of the TWFE model in Equation (2) estimated using OLS delivers consistent estimates only under relatively strong assumptions regarding treatment effect homogeneity. In order to allow for heterogeneity in treatment effects across time and treated units, we also present the event study figures generated by a set of recently-proposed estimators that are robust to treatment effect heterogeneity (Borusyak et al., 2021; Callaway and Sant’Anna, 2021; De Chaisemartin and d’Haultfoeuille, 2020; Sun and Abraham, 2021). 

Figure 2 presents the event-study figures and shows that the estimates are consistent with the parallel trends assumption: independently of the estimator used, the coefficients on the semesters prior to the introduction of Facebook at a college are all close to zero and exhibit no

---

[referencia=13d0780828065ceb score=0.758]
Appendix Table A.27 compares the sample we recruited to the NCHA sample analyzed in the paper. The samples have a similar share of international students and women (we intentionally attempted to recruit a sample that was balanced on sex), while the NCHA sample has a higher share of white respondents. The final three rows calculate the average response to all numeric and binary questions composing our index of poor mental health. The students who completed our survey on Prolific are more likely to suffer from poor mental health compared to the students in the NCHA sample. This may reflect the deterioration of mental health among young adults that occurred over the past two decades. 

47 

Appendix Figures A.14 and A.15 show that there is a strong correlation between our main index of poor mental health and the PHQ-9 and GAD-7 indices, respectively. The figures present binned scatter plots where each point shows the mean PHQ-9 or GAD-7 score for different ventiles of our index of poor mental health. The strong correlation suggests that if Facebook negatively affected our index of poor mental health, it also negatively affect the clinically-validated PHQ-9 and GAD-7 measures. 

As discussed in Section 5, we can leverage our survey to get a better sense of the magnitude of our treatment effects. Specifically, using data from our survey, we can determine how to weigh the variables contained in our index of poor mental health in a way that best predicts an indicator for having depression according to the PHQ-9 (10 _≤_ PHQ-9) and an indicator for having generalized anxiety disorder according to the GAD-7 (10 _≤_ GAD-7). We calculate such weights using an OLS (linear probability model), a logistic regression, and a LASSO. The resulting weights are shown in Appendix Table A.28. Unsurprisingly, the symptom most predictive of depression is being severely depressed and the strongest predictor of anxiety is saying that one had anxiety disorder in the last year. Interestingly, taking medication for depression, conditional on the other coefficients, predicts that a respondent is less likely to suffer from depression.

---

[referencia=13d0780828065ceb score=0.715]
> 2See Roth et al. (2022) for a recent overview. 

2 

Our main finding is that the introduction of Facebook at a college had a negative effect on student mental health. Our index of poor mental health, which aggregates all the relevant mental health variables in the NCHA survey, increased by 0.085 standard deviation units as a result of the introduction of Facebook. As a point of comparison, this magnitude is around 22% of the effect of losing one’s job on mental health, as reported in a meta-analysis by Paul and Moser (2009). We further benchmark our results against a clinically-validated depression scale: the PHQ-9 (Kroenke et al., 2001). The effect of the introduction of Facebook on our index of poor mental health is equivalent to a two-percentage-point increase in the share of students suffering from depression according to the PHQ-9 over a baseline of 25%. The negative effects on mental health are strongest for students who, based on immutable characteristics such as gender and age, are predicted to be most susceptible to mental illness. For those students, we also observe a significant increase in depression diagnoses, take-up of psychotherapy for depression, and use of anti-depressants. Finally, we find that, after the introduction of Facebook, students were more likely to report that their academic performance was negatively affected by conditions related to poor mental health. 

What explains the negative effects of Facebook on mental health? The pattern of results is consistent with Facebook increasing students’ ability to engage in unfavorable social comparisons. Two main pieces of evidence bear on this conclusion. First, we find that the effects are particularly pronounced for students who may view themselves as comparing unfavorably to their peers, such as students who live off-campus—and therefore are more likely to be excluded from on-campus social activities—students of lower socioeconomic status, and students not belonging to fraternities/sororities. Second, we show that the introduction of Facebook directly affected the students’ beliefs about their peers’ social lives and behaviors, especially in relation to alcohol consumption. As far as other channels are concerned, we do not find significant evidence that the negative effects of Facebook on mental health are due to disruptive internet use. We also rule out several alternative mechanisms, such as reduced stigma about mental illness and direct effects on drug use, alcohol consumption, and sexual behaviors.

---

[referencia=13d0780828065ceb score=0.682]
##### **5.2 Heterogeneity** 

**Heterogeneity by Predicted Susceptibility to Mental Illness.** In order to study whether the introduction of Facebook at a college led students on the margin of a depression diagnosis to take up depression-related services, we proceed in two steps: first, we estimate a LASSO to identify individuals who, based on baseline immutable characteristics, are more susceptible to mental illness. Second, we show heterogeneous treatment effects based on our LASSOpredicted measure of susceptibility to mental illness. 

The LASSO prediction is generated as follows: first, we construct an indicator that equals one if a student has ever been diagnosed with a mental health condition. Second, we consider a set of immutable individual-level characteristics (age, year in school, gender, race, an indicator for U.S. citizenship, and height), generate all two-way interactions between these characteristics, and generate second- and third-order monomials of each characteristic. Third, we implement a LASSO procedure in the pre-period to predict our indicator for ever having been diagnosed with a mental health condition based on the immutable individual-level char- 

> 26Appendix Figure A.4 shows the TWFE OLS estimates of a version of equation (2) that considers each of the first three Facebook expansion groups in turn and compares it to the last Facebook expansion group. These figures are constructed at the yearly level to reduce noise arising from the smaller number of observations. Consistent with Facebook having a negative impact on student mental health, in all the pairwise comparisons, all the estimates in the post-period are positive and most are statistically significant while the estimates in the pre-period are not statistically different from zero. 

> 27Contrary to the recently-developed robust estimators, the OLS estimator shows a relatively flat trend in the post-period. This is likely because, in the case of dynamically-increasing treatment effects, the OLS estimator, which uses already-treated units as controls for newly-treated units, exhibits a downward bias. 

20 

acteristics and functions thereof described above. 

In order to test the quality of the prediction, we plot our measure of predicted susceptibility to mental illness against our index of poor mental health. Appendix Figure A.7 shows a strong relationship between the index of poor mental health and our predicted measure of susceptibility to mental illness.

---

[referencia=13d0780828065ceb score=0.679]
###### Figure A.11: Heterogeneous Effects as Evidence of Unfavorable Social Comparisons Mechanism, Controlling for Predicted Susceptibility to Mental Illness 



<!-- Start of picture text -->
Post Facebook Introduction x<br>Off-campus Living<br>Post Facebook Introduction x<br>Not in Fraternity/Sorority<br>Post Facebook Introduction x<br>Credit-card Debt<br>Post Facebook Introduction x<br>Work<br>Post Facebook Introduction x<br>Overweight<br>Post Facebook Introduction x<br>Index Social Comparisons<br>-.08 -.04 0 .04 .08<br>Interaction Coefficient<br>(standard deviations)<br><!-- End of picture text -->

_Notes_ : This figure presents a version of Figure 6 controlling for heterogeneity by the predicted susceptibility to mental illness. Specifically, it presents regressions similar to Equation (1) in which our treatment indicator is interacted with a set of indicators for belonging to a certain sub-population of students and in which our treatment indicator is also interacted with our LASSO-predicted measure of susceptibility to mental illness. The outcome variable is our overall index of poor mental health. The sub-populations of students are: students who live off-campus, students who do not belong to a fraternity or sorority, students who carry some credit card debt, students who work alongside studying, and students who are overweight according to the body mass index (BMI). The estimates are obtained using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the outcome, treatment, interaction, and control variables, see Appendix Table A.30. The bars represent 95% confidence intervals. Standard errors are clustered at the college level. 

59 

Figure A.12: Relationship between the Index of Symptoms of Depression and Ever Having Been Diagnosed with Depression 



<!-- Start of picture text -->
Correlation coeff. 0.37<br>-1 0 1 2 3<br>Index of Depression Symptoms<br>.6<br>.4<br>.2<br>Fraction Ever Diagnosed with Depression<br>0<br><!-- End of picture text -->

---

[referencia=13d0780828065ceb score=0.575]
_Notes_ : This table explores the effects of length of exposure to Facebook on student mental health. It presents estimates of coefficient _β_ from an equation similar to Equation (4) where we assume that the number of treated semester has a linear effect on mental health and includes survey-wave by college fixed effects: _Yicgt_ = _β ×_ FB _gt ×_ [ _t −_ max _{τi, τc}_ ]+ **X** _i · γ_ + _λct_ + _εicgt_ . The outcome variables are the overall index of poor mental health (columns (1) and (2)), the index of symptoms of poor mental health (columns (3) and (4)), and the index of depression services (columns (5) and (6)). All indices are standardized so that, in the pre-period, they have a mean of zero and a standard deviation of one. Odd-numbered columns present estimates of Equation (4) including survey-wave fixed effects, college fixed effects, and controls; even-numbered columns replace survey-wave fixed effects and college fixed effects with survey-wave _×_ college fixed effects. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. Cohorts of students who might have been exposed to Facebook in high school are excluded from the regression. See Footnote 31 for details. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. Standard errors in parentheses are clustered at the college level. * p _<_ 0.1, ** p _<_ 0.05, *** p _<_ 0.01. 

Table A.7: Length of Exposure to Facebook and Depression Services

---

[referencia=13d0780828065ceb score=0.566]
Figure 4 displays the estimates of _βk_ and shows that the negative effects of the introduction of Facebook on mental health worsen the longer students are exposed to Facebook. Appendix Table A.6 presents the results in a regression framework where we assume that the effects grow linearly over time. The table shows that the number of treated semesters has a significant effect on our main index, on symptoms of poor mental health, and on the utilization of depressionrelated healthcare services. 

Since the index of depression services only comprises binary variables that have a straightforward yes-no interpretation, we provide intuition for the magnitude of our results by presenting the effects on each component of the index of poor mental health services in original units. Specifically, Appendix Table A.7 shows that being exposed to Facebook for 5 semesters increases the probability that a student is diagnosed with depression by around 32%, the probability that a student is in therapy for depression by around 50%, and the probability that a student is on anti-depressants by around 33%.

---

[referencia=13d0780828065ceb score=0.548]
Table A.7: Length of Exposure to Facebook and Depression Services 

||Last Year<br>Depression Diagnosis<br>(1)|Therapy For<br>Depression<br>(2)|Current Medication<br>Depression<br>(3)|
|---|---|---|---|
|Num. Treated Semesters|0.003<sup>_∗∗∗_</sup>|0.003<sup>_∗∗∗_</sup>|0.003<sup>_∗∗∗_</sup>|
||(0.001)|(0.001)|(0.001)|
|Observations|332,292|332,271|332,216|
|Baseline mean|0.047|0.030|0.045|
|Controls|✓|✓|✓|
|SurveyWave_×_College FE|✓|✓|✓|



_Notes_ : This table explores the effects of length of exposure to Facebook on the take-up of depression-related services. It presents estimates of coefficient _β_ from an equation similar to similar to Equation (4) where we assume that the number of treated semester has a linear effect on mental health and includes survey-wave by college fixed effects: _Yicgt_ = _β ×_ FB _gt ×_ [ _t −_ max _{τi, τc}_ ] + **X** _i · γ_ + _λct_ + _εicgt_ . The outcome variables are the components of the index of depression services (in original units), namely whether a student was diagnosed with depression within the last year, whether a student was in therapy for depression in the last year, and whether a student was taking anti-depressants over the last year. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. Cohorts of students who might have been exposed to Facebook in high school are excluded from the regression. See Footnote 31 for details. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. Standard errors in parentheses are clustered at the college level. * p _<_ 0.1, ** p _<_ 0.05, *** p _<_ 0.01. 

67

---

[referencia=13d0780828065ceb score=0.520]
##### **Abstract** 

The diffusion of social media coincided with a worsening of mental health conditions among adolescents and young adults in the United States, giving rise to speculation that social media might be detrimental to mental health. In this paper, we provide quasi-experimental estimates of the impact of social media on mental health by leveraging a unique natural experiment: the staggered introduction of Facebook across U.S. colleges. Our analysis couples data on student mental health around the years of Facebook's expansion with a generalized difference-indifferences empirical strategy. We find that the roll-out of Facebook at a college increased symptoms of poor mental health, especially depression. We also find that, among students predicted to be most susceptible to mental illness, the introduction of Facebook led to increased utilization of mental healthcare services. Lastly, we find that, after the introduction of Facebook, students were more likely to report experiencing impairments to academic performance resulting from poor mental health. Additional evidence on mechanisms suggests that the results are due to Facebook fostering unfavorable social comparisons. 

JEL Classification: D12, D72, D90, I10, L82, L86 

Keywords: social media, mental health 

Luca Braghieri - luca.braghieri@gmail.com 

_Ludwig Maximilan University of Munich and CEPR_ 

Alexey Makarin - alexey.makarin@eief.it _Einaudi Institute for Economics and Finance (EIEF) and CEPR_ 

Roee Levy - roeelevy@tauex.tau.ac.il 

_Tel Aviv University_

---

[referencia=13d0780828065ceb score=0.479]
|Therapy depression|0.01|0.01|0.03|0.04|0.34|0.33|
|Current medication depression|0.01|0.00|0.03|0.02|0.14|0.22|



_Notes_ : This table presents estimates of coefficient _β_ from Equation (1) using our preferred specification, namely the one including survey-wave fixed effects, college fixed effects, and controls. Columns (1) and (2) present effects and standard errors on un-normalized outcomes. Columns (3) and (4) present effects and standard errors on normalized outcomes, where the normalization is such that the mean in the pre-period is zero and the standard deviation in the pre-period is one. Columns (5) and (6) present unadjusted _p_ -values and sharpened False Discovery Rate-adjusted two-stage _q_ -values, respectively. Our controls consist of: age, age squared, gender, indicators for year in school (freshman, sophomore, junior, senior), indicators for race (White, Black, Hispanic, Asian, Indian, and other), and an indicator for international student. For a detailed description of the outcome, treatment, and control variables, see Appendix Table A.30. Standard errors are clustered at the college level. 

65 

Table A.5: Heterogeneous Effects by Predicted Susceptibility to Mental Illness

---

[referencia=13d0780828065ceb score=0.409]
###### **Abstract** 

The diffusion of social media coincided with a worsening of mental health conditions among adolescents and young adults in the United States, giving rise to speculation that social media might be detrimental to mental health. In this paper, we provide quasiexperimental estimates of the impact of social media on mental health by leveraging a unique natural experiment: the staggered introduction of Facebook across U.S. colleges. Our analysis couples data on student mental health around the years of Facebook’s expansion with a generalized difference-in-differences empirical strategy. We find that the roll-out of Facebook at a college increased symptoms of poor mental health, especially depression. We also find that, among students predicted to be most susceptible to mental illness, the introduction of Facebook led to increased utilization of mental healthcare services. Lastly, we find that, after the introduction of Facebook, students were more likely to report experiencing impairments to academic performance resulting from poor mental health. Additional evidence on mechanisms suggests that the results are due to Facebook fostering unfavorable social comparisons. 

_JEL Codes: D12, D72, D90, I10, L82, L86_

---

[referencia=13d0780828065ceb score=0.384]
> 19Although we cannot separate these two channels in the absence of data on an individual’s Facebook use, we note that it is unlikely that our results are primarily driven by students who did not have a Facebook account. As discussed in Section 2, the average penetration rate of Facebook at each college was around 85%. Therefore, an effect concentrated solely among students who did not join the platform would have to be implausibly large— approximately 0.57 standard deviations in our main specification—to be consistent with our baseline effect. 

> 20Paul and Moser (2009) analyze studies estimating various aspects of mental health including symptoms of distress, depression, anxiety, psychosomatic symptoms, subjective well-being, and self-esteem. The estimates from Paul and Moser (2009) that can most credibly be interpreted as causal and hence be compared to our estimates are those that rely on quasi-experimental variation in job loss due to factory closures and mass layoffs. 

17 

poor mental health in a way that best predicts an indicator for having depression according to the PHQ-9 and an indicator for having generalized anxiety disorder according to the GAD7. Next, we apply these weights to the NCHA sample to predict whether a student taking the NCHA survey would be classified as having depression or generalized anxiety disorder according to the PHQ-9 and GAD-7. Appendix Table A.29 shows that the introduction of Facebook increased by two percentage points the fraction of students whom, according to our prediction, the PHQ-9 and GAD-7 would classify as having depression or generalized anxiety disorder. The two percentage point increase corresponds to a 9% increase over the pre-period mean of 25% for depression and a 12% increase over the pre-period mean of 16% for generalized anxiety disorder.<sup>21</sup>

---

[referencia=13d0780828065ceb score=0.346]
##### **5.5 Downstream Implications of Poor Mental Health** 

Does the effect of Facebook on mental health have negative downstream repercussions on academic performance? According to the students’ reports, the answer is affirmative. 

One of the NCHA survey questions inquires as to whether various conditions affected the students’ academic performance. The conditions related to mental health are: attention deficit disorder, depression/anxiety disorder/seasonal affect disorder, eating disorders, stress, 

> 32Indeed, missing values are more common in the NCHA survey among sensitive questions (Kays et al., 2012). 

24 

and sleep difficulties.<sup>33</sup> The main advantage of analyzing these questions is that they trace a pathway from the introduction of Facebook to perceptions of worsened academic performance via poor mental health. It is important to emphasize, however, that we do not directly measure effects on grades, and that we do not rule out potential positive effects of Facebook on students’ academic performance due to channels unrelated to mental health, such as improved teamwork.<sup>34</sup> 

Figure 5 presents estimates of Equation (1) and shows how the introduction of Facebook affected each of the measures described in the previous paragraph. All the point estimates are positive and the coefficient for an equally-weighted index summarizing them is positive and significant, suggesting that, after the introduction of Facebook, students were more likely to report that their academic performance was impaired as a result of poor mental health. The effect size on the index is 0.067 standard deviation units. Consistent with our evidence suggesting that depression and anxiety-related disorders are the conditions most severely affected by the introduction of Facebook, we find the largest effect on the depression/anxietydisorder/seasonal-affect-disorder measure. The number of students who reported that those conditions impaired their academic performance increased by three percentage points over a baseline of 13%. Finally, the bottom-left panel in Figure 3 and column (3) of Table A.5 show that the negative effect of poor mental health on self-reported academic performance is especially pronounced among the students who are predicted to be most susceptible to mental illnesses.

---

[referencia=13d0780828065ceb score=0.344]
> 46Although the effects on physical health are statistically smaller than the effects on mental health, the point estimates in Table A.10 are positive and may be considered non-negligible. Such effects might be due to noise, but they might also be capturing actual effects of the introduction of Facebook on physical health. There are two main reasons why Facebook might affect students’ physical health. First, it could lead students to spend more time on their computers. Consistent with this narrative, the largest point estimate of Facebook’s effect on physical health in Figure A.8 is for back pain. Second, Facebook might affect students’ physical health indirectly as a result of its negative effect on mental health (Prince et al., 2007). Indeed, even respiratory diseases such as bronchitis have been linked to major depressive episodes (Hedden et al., 2017). 

43 

took the survey coincides with the semester in which Facebook was rolled out at her college. To address the first concern, we construct two additional indices: an index of poor mental health that includes observations for which some of the component variables are missing and an inverse-covariance weighted index that assigns a smaller weight to strongly correlated components (Anderson, 2008). Appendix Table A.11 shows that our results remain qualitatively similar using these alternative indices. To address the second concern, we construct various versions of the index of poor mental health, each time excluding a different component from the index. Appendix Figure A.9 shows that our estimates are robust to separately dropping each individual component of the index of poor mental health. To address the third concern, we run our TWFE and length-of-exposure models on a restricted dataset that excludes colleges belonging to each Facebook expansion group in turn. Appendix Table A.12 shows that the results remain fairly stable across the various restricted datasets.<sup>47</sup> Lastly, to address the fourth concern, Appendix Table A.13 shows that our results are qualitatively similar independently of whether we consider respondents who took the survey in the semester in which Facebook was rolled out at their colleges treated, untreated, or whether we assign them a treatment status of 0.5. Also, reassuringly, the coefficient on _t_ = 0 in Figure 2 is in between the magnitudes of _t_ = _−_ 1 and _t_ = 1 for all estimators.

---

[referencia=13d0780828065ceb score=0.298]
Second, the mechanisms whereby Facebook use can affect mental health might have been exacerbated rather than mitigated by many of the technological changes undergone by Facebook and related platforms in the last 15 years. Individuals now receive information about their social network directly in their news feeds, and the information is more relevant to them because it is ranked by an algorithm. The content on the platform is richer in that it often includes videos, and it can be accessed at any time or place using a smartphone. These changes might 44The effects might be mitigated if, over time, users learn how to interpret the content they are exposed to on Facebook. The effects could be exacerbated if, over time, users become dependent on and potentially even addicted to Facebook (Allcott et al., 2021). A change in the social norms around the content that people post on social media might also affect the relationship between Facebook use and mental health. 

30 

make Facebook even more engaging and might exacerbate the effects on mental health.<sup>45</sup> 

#### **8 Conclusion** 

In 2021, 4.3 billion individuals had a social media account, accounting for over half the world population and over 90% of internet users (We Are Social, 2021). The repercussions of the rise of social media are thus likely to be far-reaching. In this paper, we leveraged the staggered introduction of Facebook across U.S. colleges to estimate the impact of social media on mental health and found that the introduction of Facebook at a college had a negative effect on student mental health. 

Overall, our results are consistent with the hypothesis that social media might be partly responsible for the recent deterioration in mental health among teenagers and young adults. It is up to social media platforms, regulators, and future research to determine whether and how these effects can be alleviated.

---

[referencia=13d0780828065ceb score=0.278]
The results presented in this paper, which rely on the staggered roll-out of Facebook across U.S. college campuses in 2004-2006, should be interpreted with caution for several reasons. First, our estimates cannot speak directly to the effects of social media features—e.g., news pages—that were introduced after the time period we analyze. Similarly, our estimates 

3 

cannot speak directly to the possibility that years of experience with the platform might teach users ways to mitigate the negative effects on mental health.<sup>3</sup> Second, despite being the core component of most mental health diagnoses, self-reports may still suffer from measurement error due to recall bias, lack of incentives, and social image concerns.<sup>4</sup> Finally, we note that our estimates are local to college students, a population of direct interest in the discussion about the recent worsening of mental health trends among adolescents and young adults. Nevertheless, future research should test whether social media has a similar effect on the mental health of other demographic groups. 

Aside from these caveats, our findings are in line with the hypothesis that social media has a negative impact on mental health and played a role in the increase in mental illness among adolescents and young adults over the past two decades. Of course, our results do not imply that the overall welfare effects of social media are necessarily negative. Such calculation would require estimating the effects of social media along various other dimensions; furthermore, they would require taking into account potential positive effects, such as a reduction in the cost of connecting with friends and family across a distance. Nevertheless, we believe our results will be informative to social media users and policymakers alike.