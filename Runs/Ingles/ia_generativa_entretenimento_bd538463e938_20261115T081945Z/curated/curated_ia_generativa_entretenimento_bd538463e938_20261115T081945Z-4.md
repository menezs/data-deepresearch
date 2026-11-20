[referencia=141fa255b5f5db2d score=0.976]
# **Production-Ready Face Re-Aging for Visual Effects**

### We demonstrate how the simple U-Net, surprisingly, allows us to advance the state of the art for re-aging real faces on video, with unprecedented temporal stability and preservation of facial identity across variable expressions, viewpoints, and lighting conditions.

**November 30, 2022 ACM SIGGRAPH Asia (2022)**


#### Authors

Gaspard Zoss (DisneyResearch|Studios)

Prashanth Chandran (DisneyResearch|Studios/ETH Joint PhD)

Eftychios Sifakis (DisneyResearch|Studios)

Markus Gross (DisneyResearch|Studios/ETH Zurich)

Paulo Gotardo (DisneyResearch|Studios)

Derek Bradley (DisneyResearch|Studios)

---

[referencia=141fa255b5f5db2d score=0.974]
### Production-Ready Face Re-Aging for Visual Effects

Photorealistic digital re-aging of faces in video is becoming increasingly common in entertainment and advertising. But the predominant 2D painting workflow often requires frame-by-frame manual work that can take days to accomplish, even by skilled artists. Although research on facial image re-aging has attempted to automate and solve this problem, current techniques are of little practical use as they typically suffer from facial identity loss, poor resolution, and unstable results across subsequent video frames. In this paper, we present the first practical, fully-automatic and production-ready method for re-aging faces in video images. Our first key insight is in addressing the problem of collecting longitudinal training data for learning to re-age faces over extended periods of time, a task that is nearly impossible to accomplish for a large number of real people. We show how such a longitudinal dataset can be constructed by leveraging the current state-of-the-art in facial re-aging that, although failing on real images, does provide photoreal re-aging results on synthetic faces. Our second key insight is then to leverage such synthetic data and formulate facial re-aging as a practical image-to-image translation task that can be performed by training a well-understood U-Net architecture, without the need for more complex network designs. We demonstrate how the simple U-Net, surprisingly, allows us to advance the state of the art for re-aging real faces on video, with unprecedented temporal stability and preservation of facial identity across variable expressions, viewpoints, and lighting conditions. Finally, our new face re-aging network (FRAN) incorporates simple and intuitive mechanisms that provides artists with localized control and creative freedom to direct and fine-tune the re-aging effect, a feature that is largely important in real production pipelines and often overlooked in related research work.