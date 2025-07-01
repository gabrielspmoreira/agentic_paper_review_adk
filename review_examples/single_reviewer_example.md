As an expert academic reviewer for KDD, I've thoroughly evaluated your paper, "NV-Retriever: Improving text embedding models with effective hard-negative mining." KDD emphasizes novelty, technical depth, rigorous empirical validation, and practical impact. Your paper presents a compelling empirical study, and my review will focus on the scientific method, experimental validation, reproducibility, and the claims made.

**Summary of the Paper**

This paper introduces "positive-aware" hard-negative mining methods, namely TopK-MarginPos and TopK-PercPos, to improve the fine-tuning of text embedding models using contrastive learning. The core idea is to filter hard-negatives based on their relevance score relative to the positive passage's score, aiming to remove false negatives and stabilize training. The authors conduct extensive ablation studies on various aspects, including different teacher models, ensembling strategies, mining method configurations, and sampling approaches. Finally, they demonstrate the effectiveness of their proposed methods at scale, claiming the NV-Retriever-v1 model achieved state-of-the-art results on the MTEB Retrieval benchmark upon publication.

**Strengths**

1.  **Clear and Novel Contribution**: The introduction of "positive-aware" hard-negative mining methods (TopK-MarginPos and TopK-PercPos) is a clear and practically impactful novelty. The algorithms are well-defined, enhancing the clarity of the proposed approach.
    
2.  **Excellent Empirical Validation**: This is a major strength of the paper and directly aligns with KDD's emphasis on rigorous empirical methods.
    
    *   **Comprehensive Ablation Studies**: The paper provides incredibly detailed and multi-faceted ablation studies. This includes:
        
        *   Evaluating the impact of various teacher models (RQ1, Table 1).
            
        *   Investigating hard-negative ensembling strategies (RQ2, Table 2, Appendix A).
            
        *   An in-depth comparison and configuration tuning of different mining methods (RQ3.a, Figures 1 & 2, Table 3), including traditional methods (Naive Top-K, Top-K shifted by N, TopK-Abs) against the proposed ones.
            
        *   Replication of mining method experiments with a larger base model (Mistral-7B-v0.1, Table 4) to demonstrate generalization.
            
    *   **Large-Scale Evaluation**: The final demonstration of NV-Retriever-v1 on the full MTEB Retrieval benchmark (Table 5) is a strong testament to the methods' efficacy at scale. Claiming the #1 spot on a widely recognized leaderboard is a significant achievement and impact.
        
    *   **Insightful Analysis**: Figures 3 and 4 visually demonstrate the impact of positive-aware mining on false negative reduction, score separation, and cross-entropy loss stabilization. This provides valuable intuition and concrete evidence for the benefits claimed.
        
3.  **Strong Reproducibility**: The paper excels in providing details necessary for reproducibility.
    
    *   Algorithms for the proposed methods are explicitly given.
        
    *   Detailed experimental setups are described, including base models, teacher models, specific datasets (Table 7), hyperparameters (Table 8 & 9), and libraries (Hugging Face Transformers, PEFT).
        
    *   The computational cost is estimated, which is highly useful for practical implementation and resource planning.
        
    *   Footnotes provide direct links to the specific models on Hugging Face, which is commendable.
        
4.  **Practical Relevance and Impact**: Hard-negative mining is a critical and often under-explored aspect of training effective embedding models. This work provides concrete, high-performing strategies that are directly applicable by practitioners, addressing a significant pain point in current text embedding model development.
    

**Weaknesses**

1.  **Unsubstantiated Claim of "Faster Training"**: The abstract states that the methods lead to "faster training." While the paper suggests "more efficient fine-tuning" by using better negatives, no direct evidence (e.g., convergence curves, wall-clock training time comparisons for different mining methods) is provided to support a claim of _faster_ training. If the benefit is primarily improved final accuracy or stability, the wording should be adjusted.
    
2.  **Lack of Statistical Significance Analysis**: While the experimental results show improved average NDCG@10 scores, especially in Tables 3 and 4, the differences between top-performing methods can be very small (e.g., 0.5856 vs 0.5857 in Table 3). Without statistical significance tests (e.g., confidence intervals, p-values from multiple runs), it's hard to definitively conclude whether these small differences are truly robust or merely due to experimental variance.
    
3.  **Limited Ablation on Number of Hard-Negatives**: The paper extensively ablates the _type_ of hard-negative mining and _sampling strategies_ within a given top-k pool, but the initial number of hard-negatives (e.g., 4, 5, 8) is a fixed choice for most ablations. An ablation on the _absolute number_ of hard-negatives chosen (e.g., comparing 1, 2, 4, 8, 16 hard-negatives) would further strengthen the experimental rigor and provide guidance on this important hyperparameter.
    
4.  **Clarity on Mistral-7B-v0.1 Hard-Negative Constraint**: In Section 4.3.4, it's mentioned that only "1 hard-negative per example" was used for the Mistral-7B-v0.1 base model due to "memory errors." It would be beneficial to clarify if this memory limitation is during the _mining process_ (teacher model inference) or the _fine-tuning training_ of the base model. This distinction is important, as it might imply that the optimal number of negatives is model-dependent, which could influence the direct applicability of findings from the e5-large-unsupervised ablations.
    
5.  **Potential Limitations of LLM-as-a-Judge**: While the use of LLM-as-a-judge for false negative analysis (Figure 3) is a novel and insightful approach, a brief discussion acknowledging potential biases or limitations of LLMs in such classification tasks would add to the scientific rigor.
    

**Questions and Suggestions for Improvement**

1.  **Clarify "Faster Training"**: Please either provide empirical evidence (e.g., convergence plots, wall-clock time comparisons) to support the "faster training" claim or rephrase it to reflect the observed benefits (e.g., "more efficient fine-tuning," "more stable training," "higher accuracy").
    
2.  **Add Statistical Significance**: Consider performing multiple runs for key comparisons and reporting mean and standard deviation, or employing statistical tests (e.g., t-tests, bootstrapping) to demonstrate the significance of performance improvements, especially for smaller differences in NDCG@10.
    
3.  **Ablation on Number of Negatives**: Could you include an ablation study on the _number_ of hard-negatives used (e.g., 1, 2, 4, 8) to provide more comprehensive guidance on this hyperparameter? This could be especially relevant given the memory constraints for larger models.
    
4.  **Detail Memory Constraints**: Please elaborate on the "memory errors" when using more than 1 hard-negative for Mistral-7B-v0.1. Is it a constraint during negative mining (inference on teacher model) or during the subsequent fine-tuning (training of the base model)? This clarification would help readers understand the implications for applying your methods to different model sizes.
    
5.  **Acknowledge LLM-as-a-Judge Limitations**: Add a brief note on the potential limitations or biases of using LLMs for judging false negatives, given the current stage of LLM development.
    
6.  **Minor Typographical Errors**: Proofread the paper for minor typos or grammatical inconsistencies (e.g., "constastive learning," "PercRelevant" in Figure 3, inconsistent formatting of sub-sections like 4.3.1).
    

**Overall Recommendation**

This paper presents a **strong empirical study** with a clear, practically relevant contribution to the field of text embeddings. The proposed positive-aware hard-negative mining methods are novel and well-supported by extensive and detailed ablation studies. The large-scale results on MTEB Retrieval, demonstrating state-of-the-art performance, are particularly impactful and highly align with KDD's focus on practical utility and strong empirical validation. The reproducibility aspects are also commendable.

While there are minor areas for refinement related to statistical rigor, unsubstantiated claims, and further experimental details, these do not detract significantly from the overall quality and contribution of the work.

Given the paper's strengths, particularly its robust empirical validation and high practical impact, I recommend **Acceptance** at KDD. Addressing the minor weaknesses would further enhance the paper's already high quality.