[referencia=7f813a7301265048 score=0.031]
## Footnotes

<sup>1</sup>

∗The unit of HbA1c was not specified in the original GWAS dataset (ebi-a-GCST90014006 from the IEU OpenGWAS platform), and therefore β estimates are reported as unitless effect sizes.

**Publisher’s note**

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Contributor Information

Zhenyu Wang, Email: wangzhenyu@yeah.net.

Yanli Wang, Email: wangyanli_0405@hotmail.com.

---

[referencia=7f813a7301265048 score=0.025]
### Selection of instrumental variables

Complete results are presented in the Supplementary Tables. In total, six cis-eQTL SNPs were selected as genetic proxies for GLP1RAs. SNPs associated with diseases and traits were recorded in LDLink (R² = 0.3, 100,000 bp window). The rs10305420 SNP, associated with “smoking initiation,” was removed prior to MR analysis. The F-statistics of all cis-eQTL SNPs were greater than 10, indicating no bias was caused by weak IVs (Table 2). Positive control analysis confirmed that GLP1RAs reduced the risk of T2D (odds ratio [OR] [95% confidence interval (CI)] = 0.874 [0.791–0.966], *P* = 0.008), HbA1c (β [95% CI] = -0.046 [-0.085 to -0.007], *P* = 0.0221<sup>∗</sup>, and BMI (β [95% CI] = -0.037 SD [-0.061 to -0.014], *P* = 0.002), validating the reliability of our genetic proxies for GLP1RAs (Supplementary Table 2). Furthermore, no outliers were detected by MR-PRESSO in the sensitivity analysis of the positive control study (*P* > 0.05) (Supplementary Table 4). Although heterogeneity and horizontal pleiotropy were observed for HbA1c, these findings were acceptable, as we used the IVW method for the main analysis [28]. The Cochrane’s Q-test showed no statistical heterogeneity in T2D (*P* = 0.257) and BMI (*P* = 0.271) (Supplementary Table 5). Similarly, no evidence of horizontal pleiotropy was detected in the MR-Egger intercept test for T2D (*P* = 0.151) and BMI (*P* = 0.717), further validating the effectiveness of the identified genetic instruments (Supplementary Table 6).

---

[referencia=7f813a7301265048 score=0.015]
#### Table 2.

| SNP | Chr | Z-score | effect allele | other allele | *N* | BP | eaf | beta | se | *p* -value | *R*<sup>2</sup> | F | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rs1018437 | 6 | -7.348 | C | T | 29,621 | 38,814,743 | 0.437 | -0.061 | 0.008 | 2.02E-13 | 0.002 | 53.987 | 
| rs114977861 | 6 | 6.356 | C | T | 3243 | 38,971,093 | 0.013 | 0.694 | 0.109 | 2.07E-10 | 0.012 | 40.371 | 
| rs1738241 | 6 | -6.843 | T | C | 29,623 | 38,762,555 | 0.440 | -0.057 | 0.008 | 7.73E-12 | 0.002 | 46.829 | 
| rs4714209 | 6 | 7.250 | T | C | 29,294 | 39,023,359 | 0.253 | 0.069 | 0.009 | 4.18E-13 | 0.002 | 52.553 | 
| rs9283907 | 6 | 8.788 | A | G | 29,294 | 39,026,703 | 0.151 | 0.101 | 0.012 | 1.52E-18 | 0.003 | 77.223 | 
| rs9380816 | 6 | 5.693 | C | T | 29,623 | 38,956,892 | 0.438 | 0.047 | 0.008 | 1.25E-08 | 0.001 | 32.410 |

---

[referencia=7f813a7301265048 score=0.007]
## Result

---

[referencia=7f813a7301265048 score=0.007]
## Method

### Study design

To ensure reliable results in this drug-target MR analysis, we selected IVs that meet three key assumptions for GLP1RA: (1) genetic variants are strongly associated with the exposure; (2) genetic variants are not correlated with confounders; (3) genetic variants influence the outcome exclusively through the exposure, meaning horizontal pleiotropy is not allowed (Fig. 1). In this study, confounders including smoking, occupational dust, toxic chemicals, and air pollution. A positive control analysis was conducted to further evaluate the association of IVs with T2D, HbA1c, and BMI, thereby ensuring the reliability of the selected IVs. This MR study adhered to the STROBE-MR (Strengthening the Reporting of Observational Studies in Epidemiology using Mendelian Randomization) guidelines [24]. The overall design of this study is illustrated in Fig. 1.

---

[referencia=7f813a7301265048 score=0.007]
### Positive control analyses

Positive control analyses were conducted to validate the genetic instruments for GLP1RAs. Genetic association estimates for BMI were obtained from the UK Biobank, using the GWAS pipeline developed by the Medical Research Council Integrated Epidemiology Unit (MRC IEU) (*n* = 454,884). Genetic estimates for T2D and HbA1c were obtained from the FinnGen Consortium (*n* = 55,418 cases, 405,261 controls) and the IEU (*n* = 389,889), respectively.

### Statistical analyses

Drug-target MR analysis was performed using the “TwoSampleMR” R package (version 4.4.1). There is no overlap in individual participants between the exposure and outcome cohorts. We assessed the associations between cis-eQTLs and outcomes using the random-effects inverse variance weighted (IVW) method, which assumes no directional or horizontal pleiotropy, and supplemented this with the weighted median (WM) estimator and MR-Egger regression to account for potential pleiotropy. To validate our findings, sensitivity analyses for heterogeneity and pleiotropy were conducted using Cochran’s Q-test, MR-Egger intercept, and MR Pleiotropy RESidual Sum and Outlier (MR-PRESSO) tests. Significant pleiotropic effects were indicated by non-zero MR-Egger intercepts, with a significance threshold of *P* < 0.05. The MR-PRESSO tests corrected for horizontal pleiotropy by removing outliers and testing for significant differences in estimates post-correction. Additionally, we performed leave-one-out analyses and used funnel plots to evaluate potential biases and directional pleiotropy in the MR estimates.

To correct for multiple testing, the Benjamini-Hochberg method was applied to adjust for the false discovery rate (FDR). Results were considered robust when MR analyses achieved FDR-adjusted statistical significance (*P* < 0.05) or nominal *P* < 0.05 in two or more MR methods.

---

[referencia=7f813a7301265048 score=0.005]
### Strengths

First, we rigorously selected IVs and validated the robustness of the genetic instruments using multiple databases, ensuring a comprehensive evaluation from various perspectives. Using the novel approach of drug target MR, we confirmed the genetic benefits of GLP1RAs on certain lung diseases, free from confounding factors or reverse causality. Second, patients with concurrent COPD and T2D are at an increased risk of frequent exacerbations. While previous studies on GLP1RAs in COPD have primarily been limited to cohort and retrospective designs, this study mimics an RCT, providing higher-quality evidence to guide treatment decisions for COPD patients with T2D. Our MR analysis, combined with previous observational studies, underscores the protective role of GLP1RAs in pulmonary disease. Further research is needed to investigate the role of GLP1RAs within the cardiopulmonary-endocrine-metabolic axis and explore the underlying mechanisms.

### Limitations

First, DTMR cannot fully replace RCTs, as it only examines the overall association between GLP1RAs and diseases without evaluating the effects of specific drug subclasses (e.g., semaglutide, liraglutide). Second, our study population was restricted to individuals of European ancestry, which may limit the generalizability of the findings. Future multi-ancestry analyses should be conducted when adequately powered GWAS of COPD-related outcomes become available in non-European populations (e.g., Biobank Japan), enabling more rigorous validation of our results across diverse genetic backgrounds. Of note, MR analysis can only explain partial genetic effects. Therefore, the results should be interpreted with caution, and further multicenter, randomized, double-blind, placebo-controlled trials are necessary to confirm the causal effects of GLP1RAs on the development and prognosis of pulmonary diseases.

## Conclusion

This study supports a causal relationship between genetically predicted GLP1RAs and a lower risk of early-onset COPD, COPD-related respiratory insufficiency and COPD-related diseases, including acute bronchitis and asthma. These findings provide new insights into the potential benefits of GLP1RAs in patients with T2D and comorbid pulmonary diseases and highlight the need for further studies to explore their clinical utility in COPD management.

## Electronic supplementary material

Below is the link to the electronic supplementary material.

---

[referencia=7f813a7301265048 score=0.005]
## Electronic supplementary material

Below is the link to the electronic supplementary material.

## Acknowledgements

We acknowledge the participants and investigators of the FinnGen study and sincerely thank the eQTLGen Consortium, FinnGen consortium, and Ieu Open GWAS Project for publicly providing all the data for this MR analysis.

## Abbreviations

- SNP
- Single nucleotide polymorphisms
- GWAS
- Genome-wide association study
- MR
- Mendelian randomization
- COPD
- Chronic obstructive pulmonary disease
- GLP1RAs
- Glucagon-like peptide-1 receptor agonists
- GLP-1
- Glucagon-like peptide-1
- T2D
- Type 2 diabetes
- cis-eQTLs
- Cis-expression quantitative trait loci
- FDA
- Food and drug administration
- BMI
- Body mass index
- RCTs
- Randomized controlled trials
- IVs
- Instrumental variables
- STROBE-MR
- Strengthening the reporting of observational studies in epidemiology using Mendelian randomization
- MAF
- Minor allele frequency
- LD
- Linkage disequilibrium
- ICD
- International classification of diseases
- MRC IEU
- Medical research council integrated epidemiology unit
- IVW
- Inverse variance weighted
- WM
- Weighted median estimator
- MR-PRESSO
- MR pleiotropy residual sum and outlier
- DALYs
- Disability-adjusted life years

## Author contributions

SL, LL designed this study; SL, JZ analyzed the data; SL was a major contributor in writing the manuscript; YF, ZW, YW provided the methodological suggestions and revised the manuscript. All authors read and approved the final manuscript.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Data availability

Data is provided within the manuscript or supplementary information files.

## Declarations

### Ethics approval and consent to participate

This study used publicly available de-identified data. Ethical approval and informed consent were obtained in each original study. No additional ethical approval was required.

### Consent for publication

Not applicable.

### Competing interests

The authors declare no competing interests.

---

[referencia=7f813a7301265048 score=0.005]
## References

---

[referencia=7f813a7301265048 score=0.004]
#### Table 1.

| Positive control | ID | *N* cases | *N* controls | Sample size | Publication Year | 
|---|---|---|---|---|---|
| T2D | finngen_r12_T2D_wide | 55,418 | 405,261 | 460,679 | 2024 | 
| HbA1c | ebi-a-GCST90014006 | NA | NA | 389,889 | 2021 | 
| BMI | ukb-b-2303 | NA | NA | 454,884 | 2018 | 
| **Outcome** | **ID** | ***N*****cases** | ***N*****controls** | **Consortium** |  **Publication**   **Year** | 
| COPD | finngen_R12_J10_COPD | 24,138 | 409,070 | FinnGen 12 | 2024 | 
| Early onset COPD | finngen_R12_COPD_EARLY | 9,491 | 477,322 | FinnGen 12 | 2024 | 
| Later onset COPD | finngen_R12_COPD_LATER | 13,535 | 215,585 | FinnGen 12 | 2024 | 
| COPD-related respiratory insufficiency | finngen_R12_COPD _INSUFFICIENCY | 4,541 | 477,322 | FinnGen 12 | 2024 | 
| Acute bronchitis | finngen_R12_J10_BRONCHITIS | 20,762 | 471,806 | FinnGen 12 | 2024 | 
| Chronic lower respiratory diseases | finngen_R12_J10_LOWCHRON | 91,278 | 409,070 | FinnGen 12 | 2024 | 
| Asthma | finngen_R12_ASTHMA_NAS | 30,770 | 270,290 | FinnGen 12 | 2024 | 
| Other symptoms and signs involving the circulatory and respiratory systems | finn-b-R18_OTHER_SYMPTOMS _SIGNS_INVOLVI_CIRCULATO _RESPI_SYSTEMS | 719 | 163,123 | IEU | 2024 |

---

[referencia=bc87b595fa04d0f2 score=0.003]
In the semaglutide new-user cohort (n = 22,537), semaglutide initiation was associated with fewer airway exacerbations compared with sulfonylureas (weighted hazard ratio [wHR], 0.76; 95% CI, 0.60-0.96).<sup>1</sup> The association was stronger at higher doses, with a wHR of 0.75 (95% CI, 0.58-0.95) at low doses and 0.28 (95% CI, 0.08-1.01) at medium or high doses, and was more pronounced in asthma (wHR, 0.20; 95% CI, 0.05-0.78) than in COPD (wHR, 0.76; 95% CI, 0.58-1.00).<sup>1</sup>

### Were effects more asthma-specific and drug-specific?

No significant associations with airway exacerbations were observed for liraglutide, dulaglutide, or exenatide, regardless of dose or underlying lung disease, despite similarly sized new-user cohorts for each individual agent.<sup>1</sup> Investigators said only semaglutide showed a significant reduction in airway exacerbations, with evidence of a dose-response relationship and an association substantially stronger in asthma than in COPD.<sup>1</sup>

---

[referencia=7f813a7301265048 score=0.003]
### Results

After Benjamini-Hochberg correction for multiple testing, MR analyses indicated that genetically predicted GLP1RAs were significantly associated with lower risks of COPD (OR [95% CI] = 0.838 [0.74–0.948], *P* = 0.013), early-onset COPD (< 65 years) (OR [95% CI] = 0.751[0.622–0.906], *P* = 0.01), COPD-related respiratory insufficiency (OR [95% CI] = 0.720[0.55–0.944], *P* = 0.024), acute bronchitis (OR [95% CI] = 0.787 [0.693–0.893], *P* = 0.002), asthma (OR [95% CI] = 0.872 [0.782–0.973], *P* = 0.023), and other symptoms and signs involving the circulatory and respiratory systems (OR [95% CI] = 0.426 [0.217–0.834], *P* = 0.023). No significant association was observed for later-onset COPD (**≥** 65 years) (OR [95% CI] = 0.921 [0.783–1.082], *P* = 0.315) or chronic bronchitis risk (OR [95% CI] = 0.950 [0.889–1.016], *P* = 0.146).

### Conclusions

Genetically predicted GLP1RAs are associated with a lower risk of early-onset COPD, COPD-related respiratory insufficiency, acute bronchitis, and asthma. These findings highlight potential benefits of GLP1RAs in T2D patients with coexisting pulmonary diseases and support the need for further investigation in COPD management.

### Supplementary Information

The online version contains supplementary material available at 10.1186/s13098-025-01866-7.

**Keywords:** GLP1RAs, Drug target, Mendelian randomization, Chronic obstructive pulmonary disease

---

[referencia=7f813a7301265048 score=0.002]
- 31.Emdin CA, Khera AV, Kathiresan S, Mendelian Randomization. JAMA. 2017;318(19):1925–6. 10.1001/jama.2017.17219 [DOI] [PubMed] [Google Scholar]
- 32.Safiri S, Carson-Chahhoud K, Noori M, Nejadghaderi SA, Sullman MJM, Ahmadian-Heris J, et al. Burden of chronic obstructive pulmonary disease and its attributable risk factors in 204 countries and territories, 1990–2019: results from the global burden of disease study 2019. BMJ (Clinical Res ed). 2022;378:e069679. 10.1136/bmj-2021-069679 [DOI] [PMC free article] [PubMed] [Google Scholar]
- 33.Rosoff DB, Bell AS, Jung J, Wagner J, Mavromatis LA, Lohoff FW. Mendelian randomization study of PCSK9 and HMG-CoA reductase Inhibition and cognitive function. J Am Coll Cardiol. 2022;80(7):653–62. 10.1016/j.jacc.2022.05.041 [DOI] [PubMed] [Google Scholar]
- 34.Davies NM, Holmes MV, Davey Smith G. Reading Mendelian randomisation studies: a guide, glossary, and checklist for clinicians. BMJ (Clinical Res ed). 2018;362:k601. 10.1136/bmj.k601 [DOI] [PMC free article] [PubMed] [Google Scholar]
- 35.Eisner MD, Blanc PD, Sidney S, Yelin EH, Lathon PV, Katz PP, et al. Body composition and functional limitation in COPD. Respir Res. 2007;8(1):7. 10.1186/1465-9921-8-7 [DOI] [PMC free article] [PubMed] [Google Scholar]

---

[referencia=7f813a7301265048 score=0.002]
Notably, COPD often coexists with asthma and bronchitis, with interconnected symptoms and pathophysiology collectively referred to as airway diseases [12]. Evidence from a prospective UK Biobank study indicates that diabetes, prediabetes, and prolonged diabetes duration are associated with an increased risk of COPD and mortality [13]. A population-based cohort study found that GLP1RA use was associated with a lower risk of moderate or severe exacerbations compared with dipeptidyl peptidase 4 inhibitors in patients with COPD and T2D. These findings were further supported by a recent meta-analysis [14]. GLP1RAs may benefit patients with COPD via multiple pulmonary mechanisms, including the attenuation of inflammation, mitigation of oxidative stress, regulation of the protease–antiprotease balance, preservation of airway mucus homeostasis, and modulation of airway remodeling [15]. Interestingly, a study involving 968 patients with COPD suggested that higher body mass index (BMI) was independently predictive of lower mortality, with better outcomes observed in obese patients compared with normal weight [16], drawing attention to the “obesity paradox”. However, a recent meta-analysis [17] identified a U-shaped relationship between BMI and COPD risk, where only mild to moderate obesity appeared protective, while BMI > 35 increased risk. Given potential confounding in observational studies, the causality between GLP1RAs and COPD, as well as related diseases, needs further elucidation [18, 19].

Mendelian randomization (MR) mimics the random distribution of genetic variants during gametogenesis, offering an alternative to randomized controlled trials (RCTs) for investigating causal relationships between exposures and outcomes [20]. Drug-target MR, a derivative of MR, utilizes genetic variations significantly associated with drug targets as instrumental variables (IVs) to model the pharmacological effects of drugs on these targets and explore causal relationships between drugs and diseases [21]. Considering the gradual progression of COPD, utilizing drug-target MR analysis offers advantages in evaluating drug repurposing potential and predicting associated adverse effects [22, 23]. In this study, we use recently released data to evaluate the causal effect of GLP1RAs on COPD and related diseases (bronchitis and asthma) through drug-target MR analysis to address gaps in this area.

---

[referencia=7f813a7301265048 score=0.001]
### Causal effect in the main analysis

The MR analysis showed a decreased risk of COPD (OR [95% CI] = 0.838[0.74–0.948], *P* = 0.0048), early onset COPD (OR [95% CI] = 0.751[0.622–0.906], *P* = 0.0027), COPD-related respiratory insufficiency (OR [95% CI] = 0.72[0.55–0.944], *P* = 0.0173), acute bronchitis (OR [95% CI] = 0.787[0.693–0.893], *P* = 0.0002), asthma (OR [95% CI] = 0.872[0.782–0.973], *P* = 0.0144), and other symptoms and signs (OR [95% CI] = 0.426[0.217–0.834], *P* = 0.0128), with the increased expression of *GLP1R* gene. After Benjamini-Hochberg correction, the IVW-MR analysis still indicated that GLP1RAs were significantly associated with a lower risk of these diseases (*P* < 0.05) (Fig. 2). No supporting evidence was found to substantiate the association between GLP1R expression and later-onset COPD (OR [95% CI] = 0.921[0.783–1.082], *P* = 0.3149) or chronic bronchitis (OR [95% CI] = 0.95[0.889–1.016], *P* = 0.1329) (Fig. 2, Supplementary Table 3). The scatter plot, funnel plot, and leave-one-out plot for genetically predicted GLP1RAs on outcomes further validated the robustness of our findings (Supplementary Figures).

---

[referencia=7f813a7301265048 score=0.001]
### Causal effect in the sensitivity analyses

Sensitivity analyses were overall broadly consistent. Cochrane’s Q test suggested no evidence of heterogeneity in COPD (*P* = 0.958), early-onset COPD (*P* = 0.987), later-onset COPD (*P* = 0.875), COPD-related respiratory insufficiency (*P* = 0.87), acute bronchitis (*P* = 0.829), chronic lower respiratory diseases (*P* = 0.672), asthma (*P* = 0.84), other symptoms and signs (*P* = 0.843) (Supplementary Table 5), nor did MR-Egger intercept test observe horizontal pleiotropy in outcomes (*P* > 0.05) (Supplementary Table 6). Similarly, no evidence of horizontal pleiotropy was detected in the MR-PRESSO global test (*P* > 0.05) (Supplementary Table 4). Excluding each SNP individually did not significantly affect the risk estimates of genetically predicted GLP1RAs on outcome risk, suggesting that potential driving SNPs are unlikely to introduce bias in the causal association.

---

[referencia=7f813a7301265048 score=0.001]
Obesity is a key modifier of COPD, particularly among younger patients [35]. While mild-to-moderate obesity has been associated with improved survival—commonly referred to as the “obesity paradox”—severe obesity (BMI > 35) increases the risk of COPD and related complications [17]. This may reflect differences in muscle mass, systemic inflammation, and metabolic health. Obese individuals are predisposed to airflow limitation, which exacerbates the risks associated with persistent smoking, sedentary lifestyle, and reduced physical activity—factors that collectively contribute to the development and progression of COPD. Additionally, obesity may intensify systemic inflammation, increasing the likelihood of emergency healthcare utilization [36]. GLP1RAs not only facilitate weight reduction and glycemic control but also exert potent anti-inflammatory effects. Mechanistically, GLP1RAs suppress leptin [37]—a pro-inflammatory adipokine overexpressed in COPD airways that impairs lung function [38, 39] and enhances infection risk. This directly explains the reduced acute bronchitis risk (OR = 0.787, *P* = 0.0002) in our MR analysis, as leptin-driven inflammation primes the lung for injury [38]. Therefore, the protective effect of GLP1RAs against COPD exacerbations observed in our study is likely driven not only by weight reduction, but also by their ability to mitigate obesity-related inflammation, improve metabolic dysfunction and pulmonary damage. These findings underscore the complex interplay between BMI, body composition, and COPD outcomes, highlighting the need for further studies to clarify the role of GLP1RAs in COPD across different levels of obesity.

---

[referencia=7f813a7301265048 score=0.001]
- 21.Zheng J, Haberland V, Baird D, Walker V, Haycock PC, Hurle MR, et al. Phenome-wide Mendelian randomization mapping the influence of the plasma proteome on complex diseases. Nat Genet. 2020;52(10):1122–31. 10.1038/s41588-020-0682-6 [DOI] [PMC free article] [PubMed] [Google Scholar]
- 22.Schmidt AF, Finan C, Gordillo-Marañón M, Asselbergs FW, Freitag DF, Patel RS, et al. Genetic drug target validation using Mendelian randomisation. Nat Commun. 2020;11(1):3255. 10.1038/s41467-020-16969-0 [DOI] [PMC free article] [PubMed] [Google Scholar]
- 23.Yang Y, Chen B, Zheng C, Zeng H, Zhou J, Chen Y, et al. Association of glucose-lowering drug target and risk of Gastrointestinal cancer: a Mendelian randomization study. Cell Bioscience. 2024;14(1):36. 10.1186/s13578-024-01214-8 [DOI] [PMC free article] [PubMed] [Google Scholar]
- 24.Skrivankova VW, Richmond RC, Woolf BAR, Yarmolinsky J, Davies NM, Swanson SA, et al. Strengthening the reporting of observational studies in epidemiology using Mendelian randomization: the STROBE-MR statement. JAMA. 2021;326(16):1614–21. 10.1001/jama.2021.18236 [DOI] [PubMed] [Google Scholar]
- 25.Papadimitriou N, Dimou N, Tsilidis KK, Banbury B, Martin RM, Lewis SJ, et al. Physical activity and risks of breast and colorectal cancer: a Mendelian randomisation analysis. Nat Commun. 2020;11(1):597. 10.1038/s41467-020-14389-8 [DOI] [PMC free article] [PubMed] [Google Scholar]

---

[referencia=7f813a7301265048 score=0.001]
Preventing acute exacerbations is a primary goal in COPD management. Our MR analysis demonstrated that genetically proxied GLP1RAs were significantly associated with a reduced risk of acute bronchitis, a key trigger of exacerbations (OR [95% CI] = 0.787 [0.693–0.893], *P* = 0.0002). This is consistent with previous clinical observations in patients with COPD and T2D, where GLP1RAs reduced the incidence of respiratory exacerbations [46]. One potential mechanism underlying this protective effect is improved glycemic control: hyperglycemia is known to impair neutrophil function and compromise host defenses [47], increasing susceptibility to infection and inflammation-related exacerbation. GLP1RAs, by lowering glucose levels, may mitigate these immunometabolic disruptions.

In addition to their antidiabetic effects, GLP1RAs exhibit direct anti-inflammatory and airway-modulating properties. Preclinical studies have shown that GLP1RAs attenuate airway inflammation and hyperresponsiveness [48]. For example, exendin-4 restores the expression of forkhead box protein A2 (FOXA2), a transcriptional regulator of mucin homeostasis, thereby reducing mucin production and bacterial burden in the lungs [49]. These actions likely contribute to the reduced bronchitis risk observed in our analysis. Similarly, we found that GLP1RAs were associated with lower asthma risk, which may be mechanistically linked to reduced IL-33 [50] and IL-13 expression, decreased airway inflammation [51], and improved mucosal immune regulation [48]. Notably, GLP1RAs have shown the ability to modulate both allergic and viral airway inflammation in animal [52] and ex vivo models [53], suggesting their potential utility across a spectrum of airway inflammatory conditions.

Taken together, these findings suggest that GLP1RAs reduce inflammation and mitigate risk factors for pulmonary infections and asthma, ultimately decreasing the likelihood of developing COPD. In patients with T2D comorbid active COPD, acute bronchitis, or asthma, GLP1RAs may represent a more favorable therapeutic option compared to other antidiabetic agents, especially in those with concomitant severe obesity. Further studies are needed not only to verifying real-world clinical efficacy, but also to uncover the underlying mechanisms and investigate novel routes of administration, such as inhaled formulations.

---

[referencia=7f813a7301265048 score=0.001]
### Outcome

To minimize ancestry mismatches, we restricted the analytical cohort to individuals of European descent. The genome-wide association study (GWAS) data for outcomes were obtained from the FinnGen Consortium (https://r12.finngen.fi/) [27], released in November 2024. The diagnostic criteria for outcomes were based on the International Classification of Diseases (ICD) standards. Specifically, “COPD” was defined as “ICD 10-J10: A chronic and progressive lung disorder mainly includes chronic obstructive bronchitis and emphysema”; “early-onset COPD” was defined as “ICD 10-J44: other COPD, COPD age < 65”; “later-onset COPD” was defined as “ICD 10-J44: other COPD, COPD age **≥** 65”; “acute bronchitis” was defined as “ICD 10-J20: acute bronchitis”; “chronic lower respiratory diseases (CLRD)” was defined as “ICD 10-J40 ~ J47: chronic lower respiratory disease”; “asthma” was defined as “ICD 10-J45.9: other and unspecified asthma”. The sample size of outcomes was shown in Fig. 1. Further details on data sources are provided in Table 1.