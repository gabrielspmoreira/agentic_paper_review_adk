# Meta-Review
Dear Authors, We have carefully read your paper, "NV-Retriever: Improving text embedding models with effective hard-negative mining," along with the detailed reviews from the program committee. There is a strong consensus among the reviewers regarding the high quality and significant practical impact of your work, particularly for a conference like KDD, which values impactful and scalable data mining techniques.

**Overall Recommendation:**

**Accept** The committee finds your paper to be a valuable contribution to the field of text embeddings and information retrieval. Your proposed "positive-aware" hard-negative mining methods (TopK-MarginPos and TopK-PercPos) are considered novel, intuitive, and highly effective. The rigorous empirical validation, including comprehensive ablation studies across various teacher and base models, and the insightful analysis of how these methods reduce false negatives and stabilize training, are major strengths. Most notably, the successful application of these methods to achieve state-of-the-art results with NV-Retriever-v1 on the MTEB Retrieval leaderboard provides compelling evidence of the practical utility and impact of your research at scale, aligning perfectly with KDD's emphasis on real-world effectiveness. However, the reviewers have also identified several areas for improvement that should be addressed in your camera-ready version to further enhance the paper's scientific rigor and reproducibility.

**Key Strengths (Consensus among Reviewers):** 

1. **Addresses a Critical Practical Problem:** All reviewers commend the paper for tackling a fundamental and widely recognized challenge in text retrieval and contrastive learning: effective hard-negative mining and the critical mitigation of false negatives. 

2. **Novel and Intuitive Heuristics:** The "positive-aware" concept, which leverages the positive relevance score as an anchor for filtering false negatives, is praised as a novel, conceptually sound, and practically relevant contribution. 

3. **Strong Empirical Validation and SOTA Achievement:** The paper's most compelling strength is its comprehensive and rigorous empirical evaluation. The thorough ablation studies across teacher models, mining methods, and configurations demonstrate consistent performance improvements. Crucially, the deployment of these methods to train NV-Retriever-v1, which achieved 1st place on the MTEB Retrieval leaderboard, is a significant highlight, showcasing real-world applicability and state-of-the-art performance. 

4. **Insightful Analysis:** The use of LLM-as-a-judge to quantify false negative reduction and the visualization of score and loss distributions provide valuable mechanistic insights into *why* the proposed methods are effective, going beyond mere performance reporting. 

5. **Well-Structured and Clear Writing:** Reviewers generally found the paper to be well-organized, with a logical flow from problem statement to methodology, experiments, and conclusions.

**Key Weaknesses and Areas for Improvement (for Camera Ready):** 

1. **Reproducibility (Critical):** A primary concern, highlighted by Reviewer 3, is the **absence of publicly available code** for the proposed mining methods and the full training pipeline of NV-Retriever-v1. While the appendix provides detailed hyperparameters, re-implementing the exact mining logic and ensuring all subtle choices for SOTA results would be challenging.
**For the camera-ready version, it is essential to provide publicly available code (e.g., via GitHub link) to enable reproducibility.** 

2. **Statistical Significance Testing:** Reviewer 3 points out the lack of statistical significance tests for reported performance differences (e.g., NDCG@10 scores). Given that some improvements might be subtle, demonstrating statistical significance would greatly strengthen your empirical claims.

**Please conduct and report statistical significance tests for key comparisons in your ablation studies.** 

3. **Theoretical Depth/Intuition:** Reviewers 1 and 3 note that while the methods are empirically effective heuristics, the paper could benefit from a deeper theoretical discussion or intuition. *

**Justification for Optimal Parameters:** While the optimal margin/percentage (0.05 and 95\%) are empirically derived, providing more theoretical intuition or connecting them to properties of embedding spaces or contrastive loss functions would be valuable. *

**Impact on Loss Landscape:** Expand on how these filtering methods *theoretically* impact the loss landscape, potentially linking it to concepts like gradient variance reduction or better-conditioned optimization, as suggested by Reviewer 3. 4.

**Clarity of Figures and Tables:** Reviewers 2 and 3 noted that some figures (e.g., Figure 1's x-axis labels) and tables (e.g., Appendix A, Table 6) are dense and difficult to read.

**Please improve the legibility of these figures and tables in the camera-ready version.** 

5. **LLM-as-a-Judge Validation:** Reviewer 3 asks for further discussion on the reliability and potential biases of using an LLM-as-a-judge for false negative classification.

**Please elaborate on the validation of your LLM-as-a-judge methodology, discussing its estimated accuracy or potential limitations.** 6.

**Minor Grammatical Errors and Typos:** Reviewers 2 and 3 identified several minor grammatical errors and typos.

**Please proofread the paper thoroughly to address these.** We are confident that addressing these points will further elevate the quality and impact of your already strong paper. We look forward to your revised submission. Sincerely, The KDD Meta-Reviewer ---

# Transcribed Reviews:

## Reviewer 1

**Paper Title:** NV-Retriever: Improving text embedding models with effective hard-###negative mining

**Reviewer Expertise:** Expert in Information Retrieval, Text Embeddings, Contrastive Learning, and Large Language Models. ---

**Detailed Review** This paper introduces a family of "positive-aware" hard-negative mining methods, namely TopK-MarginPos and TopK-PercPos, aimed at improving text embedding models by more effectively identifying and removing false negatives during contrastive learning. The authors demonstrate the efficacy of these methods at scale, culminating in the NV-Retriever-v1 model which achieved state-of-the-art results on the MTEB Retrieval benchmark. The work aligns well with KDD's emphasis on practical, scalable, and impactful data mining techniques. My primary focus as a reviewer is on the paper's positioning within the existing literature, evaluation of citations, the 'related work' section, and how this work differentiates from prior art, including any crucial missed citations or misrepresentations.

**Positioning within Existing Literature and Differentiation:** The paper effectively positions its core contribution as addressing a critical, yet often underexplored or poorly detailed, aspect of fine-tuning text embedding models: the selection of high-quality hard-negative passages. The authors rightly point out that while many state-of-the-art models topping leaderboards like MTEB leverage hard-negative mining, their methodologies are rarely described in detail. This provides a strong motivation for the current work. 1.

**Clarity of Novelty:** The proposed "positive-aware" methods (TopK-MarginPos and TopK-PercPos) are clearly articulated. The core differentiator is their use of the *positive relevance score as an anchor* to filter potential false negatives. This is a principled approach that logically extends prior heuristic-based methods. The paper successfully argues why existing methods like "Top-K shifted by N" and "TopK-Abs" have limitations (e.g., ignoring positive relevance, arbitrary thresholds), thereby highlighting the novelty and necessity of their proposed approach. 2.

**Related Work Section (Section 2.1 & 2.2):** *

**Strengths:** The related work section provides a good overview of text embedding models, contrastive learning fundamentals (SimCLR, DPR), and prominent recent models (E5, E5-Mistral, GTE, Jina). It correctly identifies the role of hard-negative mining and its challenges, particularly the issue of false negatives, citing relevant works like [25] (RocketQA) which also address denoising. The discussion of in-batch negatives, memory banks, and incremental mining methods (ANCE, NGAME) helps set the context. The claim that many top models don't detail their mining strategy is a valid and important observation that motivates this work. *

**Differentiation within Related Work:** The paper dedicates a subsection (2.2.1) to "False negatives," discussing prior attempts at denoising using cross-encoders [25] or LLMs [15], and previous ablation studies on thresholds [19] and sampling ranges [18]. This directly sets up the comparison for their own methods, which is well done. 3.

**Adequacy of Citations and Potential Missed Works:** *

**Coverage:** The paper provides a comprehensive set of citations for foundational work in contrastive learning, dense retrieval, and recent SOTA embedding models. This demonstrates a solid understanding of the landscape. *

**Direct Comparison:** While the paper mentions RocketQA [25] and its use of cross-encoders for denoising, it states these methods "might be costly to run on large train sets." While this implicitly positions the proposed method as more efficient (as it relies on a teacher retrieval model and score-based filtering, not necessarily a separate cross-encoder pass per negative), a more explicit discussion or comparison on the computational efficiency of *denoising* itself would strengthen this point. How do the computational requirements of their filtering (running a teacher retrieval model once to get candidates, then simple score comparisons) stack up against re-ranking with a cross-encoder on potentially thousands of candidates per query? This is a point for KDD's practical emphasis. *

**LLM-based Negative Generation:** The paper uses LLM-as-a-judge for *analysis* of false negatives (Section 4.5.1), which is a nice touch. However, recent trends have also explored using LLMs *to generate* hard negatives directly or to re-rank candidates based on their semantic similarity/dissimilarity to the query/positive. While the paper focuses on mining from an existing corpus, acknowledging or briefly discussing these emerging methods as a broader context for hard-negative generation would be beneficial. For instance, methods that prompt LLMs to synthesize plausible but incorrect answers as hard negatives could be seen as an alternative. This is not a critical omission given the paper's specific scope but could enrich the related work by painting a fuller picture of current research directions in negative selection. 4.

**Misrepresentation of Previous Work:** I found no instances of misrepresentation of previous work. The limitations described for "Top-K shifted by N" and "TopK-Abs" are fair and accurate based on their described mechanisms. The claim that other SOTA models don't detail their mining strategy is generally true in practice, making this work a valuable contribution to transparency and reproducibility.

**Empirical Validation of Differentiation:** The paper's experimental setup and ablation studies are critical in substantiating the claims of superiority. *

**Ablation Study (Section 4.3):** The comprehensive ablation study on different mining methods (Naive Top-K, Top-K shifted by N, TopK-Abs, TopK-MarginPos, TopK-PercPos) across various configurations (Figure 1, Table 3, Table 4) is a significant strength. It clearly demonstrates that TopK-PercPos consistently outperforms prior methods and identifies optimal configurations. *

**False Negative Reduction (Section 4.5.1, Figure 3):** The use of LLM-as-a-judge to quantify false negative rates provides compelling evidence for the effectiveness of the proposed positive-aware methods in reducing false negatives (50-57% reduction compared to Naive Top-K). This directly validates the theoretical advantage. *

**Loss Stabilization (Section 4.5.2, Figure 4):** The visualization of score and loss distributions further supports the claim that positive-aware mining leads to better separation of positive/negative scores and more stable training by limiting the max cross-entropy loss.

**Relevance to KDD:** The paper addresses a highly relevant problem for KDD: improving large-scale information retrieval systems. The focus on "effective hard-negative mining" is crucial for enhancing the performance of dense retrieval models, which are foundational for applications like RAG and semantic search. The demonstration of achieving SOTA on MTEB with NV-Retriever-v1, a model developed with practical deployment in mind (NVIDIA authors, large-scale training, computational cost details), strongly aligns with KDD's emphasis on practical impact and scalable solutions. The detailed analysis of teacher models, ensembling, and mining configurations provides valuable insights for practitioners.

**Conclusion:** This paper presents a strong contribution to the field of text embeddings and contrastive learning by introducing novel, principled hard-negative mining methods. The clear articulation of the problem, well-defined novel contributions, and rigorous empirical validation—including detailed ablation studies and an analysis of false negative reduction—are commendable. The paper's positioning within the existing literature is generally robust, clearly differentiating its approach from prior art. While there could be a slightly more direct comparative discussion on computational costs with cross-encoder denoising and a brief acknowledgment of LLM-based negative generation as a broader trend, these are minor points for an otherwise excellent paper. The work has significant practical implications for building high-performing retrieval systems and aligns very well with the KDD conference's themes. ---

**Recommendation:** Accept. ---

## Reviewer 2

**Paper Title:** NV-Retriever: Improving text embedding models with effective hard-negative mining

**Overall Recommendation:** Strong Accept, pending minor revisions.

**Summary:** This paper addresses a crucial challenge in training dense text embedding models: effective hard-negative mining for contrastive learning, specifically focusing on the issue of false negatives. The authors propose a novel family of "positive-aware" mining methods, TopK-MarginPos and TopK-PercPos, which leverage the positive relevance score to filter out potential false negatives. Through extensive ablation studies, they demonstrate the superior performance of their methods compared to traditional mining strategies across various teacher and base models. The paper culminates in the successful application of these methods to train NV-Retriever-v1, which achieved 1st place on the MTEB Retrieval leaderboard when published in July 2024, showcasing significant state-of-the-art results. The paper also provides valuable insights into how these methods reduce false negatives and stabilize the training loss.

**Strengths:** 

1. **High Potential Impact:** The paper tackles a fundamental and widely recognized problem in text retrieval and contrastive learning – the selection of high-quality hard negatives and the mitigation of false negatives. The proposed methods are generic, simple to implement, and demonstrably effective, making them highly impactful for both research and practical applications in the field of text embeddings. 

2. **Strong Empirical Results and State-of-the-Art Achievement:** The paper presents compelling evidence of its methods' effectiveness. The ablation studies are thorough, comparing the proposed positive-aware methods against several baselines and demonstrating consistent improvements in retrieval accuracy (NDCG@10). Crucially, the application of these methods directly led to the NV-Retriever-v1 model achieving 1st place on the MTEB Retrieval leaderboard, a highly respected benchmark. This concrete SOTA result significantly elevates the paper's impact. 

3. **Clear Motivation and Contribution:** The introduction clearly articulates the problem, the limitations of existing hard-negative mining techniques (especially regarding false negatives), and the paper's three distinct contributions. The core idea of "positive-aware" mining is well-motivated and logically follows from the identified challenges. 

4. **Insightful Analysis:** Beyond just reporting performance gains, the paper provides excellent analyses of *why* the proposed methods work. Figures 3 and 4, which visualize the reduction of false negatives and the stabilization of score/loss distributions, offer valuable mechanistic insights that enhance the understanding and utility of the proposed techniques. 

5. **High Reproducibility:** The paper includes a detailed appendix covering model architecture, training datasets, hyperparameters, and computational costs. This level of detail, combined with the clear algorithms for the mining methods, makes the work highly reproducible, which is commendable for a top-tier conference like KDD. 

6. **Well-Structured Writing:** Generally, the paper is very well-organized, with a logical flow from problem statement to methodology, experiments, and conclusions. The research questions are clearly defined and addressed sequentially through the experimental sections.

**Weaknesses and Areas for Improvement (Minor Revisions):** 

1. **Clarity of Figure 1:** The most significant weakness is the clarity of Figure 1 (ablation study of mining methods configurations). The x-axis labels on subplots (b), (c), and (d) are severely overlapping and unreadable due to high density. The numerical data points on the plots are also very small. This figure is crucial for understanding the ablation results, and its current state significantly detracts from the paper's clarity. This must be fixed, perhaps by simplifying the x-axis tick marks, rotating labels, or presenting the information in a clearer tabular format if a plot cannot be made legible. 

2. **Minor Grammatical and Typos:** There are several minor grammatical errors and typos that should be addressed through a thorough proofread. Examples include: * "constrastive learning" (Abstract, Section 5) should be "contrastive learning". * "particularily" (Abstract) should be "particularly". * Inconsistent hyphenation for "fine-tuning" (e.g., "finetune" vs. "fine-tuned"). * "affect the accuracy is to the choice" (Section 4.4) is slightly awkward phrasing and could be rephrased for conciseness. These are minor but detract from the polish expected at KDD. 

3. **Appendix A Table Readability:** While the content of Table 6 in Appendix A is useful, its formatting is very dense, making it challenging to read and interpret the Jaccard similarity values. Consider increasing spacing or using different formatting to improve readability.

**Conclusion:** This paper presents a highly impactful contribution to the field of text embeddings and information retrieval. The proposed positive-aware hard-negative mining methods are innovative, effective, and well-supported by rigorous experimentation and compelling results, including achieving state-of-the-art performance on a major benchmark. The work also offers valuable insights into the mechanisms by which these methods improve training. Addressing the clarity issues in Figure 1 and performing a thorough proofread will significantly enhance the paper's overall quality. Given its strong technical contributions and clear impact, I recommend this paper for acceptance at KDD. --- *Review for KDD Conference*

## Reviewer 3

**Paper Title:** NV-Retriever: Improving text embedding models with effective hard-negative mining

**Overall Recommendation:** Borderline Accept.

**Summary:** This paper addresses a critical practical challenge in training text embedding models for retrieval: the selection of high-quality hard-negative passages for contrastive learning, particularly focusing on the pervasive issue of false negatives. The authors propose a "positive-aware" family of hard-negative mining methods (TopK-MarginPos and TopK-PercPos) that leverage the relevance score of positive passages as an anchor to filter out potential false negatives. Through extensive ablation studies, they investigate various aspects of hard-negative mining, including the choice of teacher models, ensembling strategies, and method configurations. The culmination of this research is the development of NV-Retriever-v1, which achieved state-of-the-art results on the MTEB Retrieval benchmark, demonstrating the practical efficacy of the proposed mining techniques at scale.

**Strengths:** 

1. **Addresses a Significant Practical Problem:** The paper tackles a crucial and widely recognized challenge in contrastive learning for information retrieval—effective hard-negative mining and false negative mitigation. This is highly relevant to the KDD community, which values practical solutions to real-world data mining problems. 

2. **Novel Heuristics for False Negative Removal:** The "positive-aware" concept (TopK-MarginPos and TopK-PercPos) is a novel and intuitive heuristic approach to filter false negatives. By anchoring the negative selection on the positive relevance score, the methods offer a sensible way to prevent highly relevant, but unlabeled, passages from being treated as negatives. 

3. **Extensive and Rigorous Empirical Evaluation:** The paper presents an exceptionally thorough empirical study. This includes: * Ablation on various teacher models, demonstrating their impact on fine-tuned model accuracy. * Analysis of ensembling strategies for hard-negatives. * Detailed ablation on the proposed mining methods' configurations (margins, percentages), providing valuable insights into optimal settings. * Validation across different base models (e5-large-unsupervised and Mistral-7B-v0.1). * Demonstration of scalability and state-of-the-art performance with NV-Retriever-v1 on the full MTEB benchmark, underscoring the practical impact. 

4. **In-depth Analysis and Insights:** The paper goes beyond just reporting performance gains by providing insightful analyses, such as the LLM-as-a-judge evaluation for false negative reduction (Figure 3) and visualizations of score and loss distributions (Figure 4). These help to elucidate *why* the proposed methods are effective, providing a deeper understanding of their mechanism. 

5. **Reproducibility:** The paper provides detailed experimental setups, hyperparameters, and dataset information, significantly aiding reproducibility.

**Weaknesses (with an emphasis on theoretical and 'pure science' contribution):** 

1. **Limited Theoretical Depth and "Pure Science" Contribution:** While the proposed "positive-aware" methods are empirically effective and intuitively sound heuristics, the paper's primary contribution is heavily skewed towards empirical validation and engineering excellence rather than fundamental theoretical advancements. *

**Lack of Novel Mathematical Formulation or Proofs:** The core of the contribution lies in algorithmic filtering rules (Algorithms 2 and 3) that are essentially conditional statements based on empirically chosen thresholds. There are no new mathematical formulations of contrastive loss, no formal proofs of convergence under these mining strategies, nor a deep theoretical analysis of how these specific filtering criteria (e.g., subtracting a fixed margin or using a percentage of positive score) optimally modify the underlying data distribution or the gradient landscape in a provably beneficial way. *

**Heuristic Nature of Optimal Parameters:** The optimal `abs_margin` (0.05) and `perc_margin` (95%) are determined purely empirically through ablation. A more "pure science" contribution would attempt to derive or provide a theoretical justification for why these specific values, or a range around them, are theoretically optimal, perhaps linking them to properties of the embedding space, noise characteristics, or the theoretical bounds of contrastive learning. *

**Assumptions Without Formal Grounding:** The methods operate on the assumption that the teacher model's positive relevance score is a sufficiently reliable anchor for filtering false negatives. While empirically shown to be effective, there's no formal model of false negatives or how these heuristics optimally mitigate their effects from a statistical or information-theoretic perspective. *

**Comparison to Deeper Theoretical Works:** The paper primarily compares its mining methods to other common practical heuristics (Top-K shifted by N, TopK-Abs) or acknowledges the complexity of incremental mining methods like ANCE/NGAME. A "pure science" review would demand engagement with more theoretically grounded approaches to negative sampling or robust contrastive learning if they exist, and a theoretical argument as to why the simpler, positive-aware heuristics are superior. 2.

**Generality of Heuristics:** While the methods performed well across two different base models, the question remains whether the *optimal* margin/percentage configurations (e.g., 95% for TopK-PercPos) are universal or task/dataset-specific. A more robust theoretical framework might offer guidance on how to determine these parameters without exhaustive ablation for every new application.

**Detailed Comments and Questions:** 

1. **Theoretical Justification for Margins:** Could the authors elaborate on any theoretical intuition or analysis that led to the specific `abs_margin` and `perc_margin` parameters? For instance, is there a connection to noise models, margin theory in SVMs, or properties of the embedding space that makes 0.05 and 95% particularly effective? 

2. **Impact on Loss Landscape:** Figure 4.c shows that TopK-PercPos "limits the max. cross-entropy loss, making training more stable." Can the authors provide a more formal analysis or discussion of how this filtering *theoretically* impacts the loss landscape, potentially linking it to concepts like gradient variance reduction or better-conditioned optimization? 

3. **Sensitivity to Teacher Model Quality:** The paper shows the effectiveness of different teacher models. Is there a theoretical minimum quality a teacher model must possess for these "positive-aware" methods to be effective? For instance, if the `p.rel_score` is unreliable, how would the methods perform? 

4. **Beyond Dot Product/Cosine Similarity:** The InfoNCE loss is general to any `sim()` function. Do the proposed filtering methods have specific dependencies on dot product or cosine similarity, or are they generalizable to other similarity metrics without loss of efficacy? 

5. **False Negative Definition:** The LLM-as-a-judge provides an empirical classification of "false negatives." Could the paper more formally define what constitutes a "false negative" in the context of retrieval datasets, perhaps leveraging statistical properties of relevance scores?

**Minor Comments / Typos:** * Page 1, Abstract: "placed 1st when it was published to the MTEB Retrieval on July, 2024." -> "placed 1st on the MTEB Retrieval leaderboard when it was published in July 2024." for clarity and consistency with later text. * Page 2, Section 2.2: "In [25] they found that naive mining of hard-negatives may select many false negatives." This sentence appears to be missing a verb or slightly awkward phrasing. Perhaps "In [25], it was found that..." or "The authors in [25] found that...". * Page 2, Section 2.2: "particularly in papers [12, 17, 17, 23, 34]" - repeated [17]. * Page 3, Algorithm 2: The return statement `return (n.rel_score < p.rel_score - abs_margin)` should probably be a boolean, e.g., `return n.rel_score < (p.rel_score - abs_margin)`. Same for Algorithm 3. * Page 3, Section 3.1: Equation 1 uses `Edi∈ {d+}udy` which looks like a OCR error, it should probably be a sum over `i`. Please confirm and correct the mathematical notation. * Page 4, Table 1: The header "HotpotQA" and "FIQA" should probably align better with the data rows. * Page 7, Figure 3: Consider making the bar labels on the x-axis (nq, squad, stack) more prominent or adding grid lines for easier readability. This paper represents excellent applied research with strong empirical results and valuable practical insights. However, given the explicit emphasis in the review instructions on "THEORETICAL and a 'pure science' contribution," it falls somewhat short in terms of introducing new mathematical frameworks, formal proofs, or deep theoretical derivations for its proposed methods. The contributions are highly effective heuristics, rather than foundational theoretical breakthroughs. For KDD, which balances both, it is a very strong paper on the empirical and practical side, but less so on the pure theoretical side. --- This paper introduces a family of "positive-aware" hard-negative mining methods, TopK-MarginPos and TopK-PercPos, designed to improve text embedding models fine-tuning by explicitly filtering out potential false negatives. The authors conduct a comprehensive empirical study, investigating the impact of different teacher models, ensembling strategies, and various configurations of their proposed mining methods. A key claim is that these methods are instrumental in achieving state-of-the-art results for the NV-Retriever-v1 model on the MTEB Retrieval benchmark. As a reviewer for KDD, my primary focus is on the scientific method and experimental validation, including reproducibility, baseline selection, and statistical rigor. This paper presents strong empirical results and a well-structured experimental design to support its claims. 

**Strengths**

1. **Clear Problem Statement and Novel Contribution:** The paper clearly identifies the critical challenge of hard-negative mining for contrastive learning in text embedding models, particularly the issue of false negatives. The proposed "positive-aware" methods (TopK-MarginPos and TopK-PercPos) offer a novel and intuitive approach to address this by leveraging the positive relevance score as an anchor for filtering. This is a conceptually sound and practically relevant contribution. 

2. **Comprehensive Experimental Design:** The paper excels in its systematic experimental validation, structured around three well-defined research questions (RQ1-RQ3). *

**Diverse Teacher Models (RQ1):** The investigation into how different teacher models impact hard-negative quality is thorough and provides valuable insights into the sensitivity of fine-tuned models to mining choices. *

**Extensive Ablation Studies (RQ3.a):** The detailed ablation study on various hard-negative mining methods and their configurations (thresholds, sampling) is a significant strength. Figure 1 and Table 3 clearly demonstrate the effectiveness and optimal parameters of the proposed methods compared to existing ones like TopK-Abs and TopK-shifted by N. *

**Generalizability:** The replication of mining experiments with a larger base model (Mistral-7B-v0.1, Table 4) demonstrates that the findings generalize beyond a single base model, enhancing the robustness of the conclusions. *

**Scaling to SOTA (RQ3.b):** The application of the proposed mining methods to train the NV-Retriever-v1 model, achieving first place on the MTEB Retrieval leaderboard, provides compelling evidence of their practical utility and impact at scale. This aligns well with KDD's emphasis on real-world effectiveness. 

3. **Insightful Analysis of Mining Effects:** The paper goes beyond just reporting performance metrics. The use of LLM-as-a-judge to quantify false negative rates (Figure 3) and the visualization of score and loss distributions (Figure 4) provide crucial insights into *why* the proposed methods are effective – they genuinely reduce false negatives and stabilize the training process. This level of analysis strengthens the scientific contribution. 

4. **Well-Chosen Baselines:** The paper compares its proposed mining methods against relevant and common baselines (Naive Top-K, Top-K shifted by N, TopK-Abs). For the SOTA comparison, NV-Retriever-v1 is benchmarked against other top-performing models on MTEB, providing a fair comparison. 

**Weaknesses**

1. **Reproducibility Concerns (Lack of Code):** A significant weakness for a top-tier conference like KDD is the absence of publicly available code for the proposed mining methods and the full training pipeline of NV-Retriever-v1. While hyperparameters are detailed and base/teacher models are referenced, reimplementing the exact mining logic and ensuring all subtle choices (e.g., specific instruction prompts, dataset blends, sampling logic for hard-negatives within the pipeline) would be extremely challenging. This severely impacts the reproducibility of the core contribution and the SOTA results. 

2. **Lack of Statistical Significance Testing:** The paper presents various performance numbers (NDCG@10) but does not report any statistical significance tests (e.g., t-tests, ANOVA) to ascertain if the observed improvements are statistically meaningful or merely due to random variations. Given that some differences in performance are relatively small (e.g., between TopK-MarginPos and TopK-PercPos, or between different ensembling strategies), statistical testing is crucial for robust scientific claims. 

3. **Limited Theoretical Justification for "Positive-Awareness":** While the empirical results clearly show the benefit of relating the negative threshold to the positive score, the paper could benefit from a deeper theoretical discussion on *why* this relative approach is superior to absolute thresholds. Is there a specific property of embedding spaces or contrastive loss functions that makes this relative filtering more effective? 

4. **LLM-as-a-Judge Validation:** The use of an LLM-as-a-judge for false negative classification is an interesting approach. However, its reliability and potential biases as a ground-truth source are not discussed or validated. What is the confidence in the LLM's classification accuracy, and how might its limitations impact the analysis in Section 4.5.1? Further details or a small human-annotated validation set for the LLM's classifications would strengthen this analysis. 

5. **Clarity on Sampling (Section 4.3.2):** The benefits of the sampling strategies (Sampled Top-k, Top-1+sampled top-k) are less clearly articulated compared to the margin/percentage filtering methods. Figure 2.a shows a drop in accuracy for Sampled Top-k, and the justification for Top-1+sampled top-k's modest improvement with Mistral-7B-v0.1 is rather weak ("it might help in some cases"). This section feels less conclusive. 

**Questions/Comments for Authors**

1. **Reproducibility (Code Release):** Given the emphasis of KDD on reproducibility, are there plans to release the code for the positive-aware mining methods and the full NV-Retriever-v1 training pipeline? This would significantly enhance the paper's impact and allow other researchers to build upon your work. 

2. **Statistical Significance:** Could you perform and report statistical significance tests (e.g., pairwise t-tests) for the differences in NDCG@10 scores, especially for the ablation studies where improvements might be subtle? This would strengthen the empirical claims. 

3. **LLM-as-a-Judge Reliability:** Could you elaborate on the validation of your LLM-as-a-judge methodology? What are its estimated accuracy and potential limitations in identifying false negatives? A small-scale human annotation agreement study or a more detailed prompt engineering discussion could be valuable. 

4. **Theoretical Intuition:** Can you provide more theoretical intuition or a formal argument for why relating the negative threshold to the positive score (as in TopK-MarginPos and TopK-PercPos) is consistently more effective than absolute thresholds (TopK-Abs)? 

5. **Sampling Strategies:** Could you elaborate on the specific scenarios or model types where the sampling strategies (e.g., Top-1+sampled top-k) are expected to provide a more significant benefit, beyond the empirical observation for the Mistral base model? What might be the underlying mechanisms? 

**Recommendation** 

This paper presents a valuable and empirically strong contribution to the field of text embedding fine-tuning, particularly for hard-negative mining. The proposed positive-aware methods are intuitive and demonstrate clear performance gains, leading to state-of-the-art results for NV-Retriever-v1. The comprehensive ablation studies and insightful analysis of false negative reduction are major strengths. However, the lack of public code release is a significant concern for a conference like KDD, which prioritizes reproducibility. The absence of statistical significance testing also weakens some of the empirical claims. Given the strength of the empirical results and the clear contribution, I lean towards

**Weak Accept**. However, I strongly urge the authors to address the reproducibility and statistical significance points in a revised version, as these are critical for a top-tier KDD paper.