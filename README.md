LLM Framing Experiment

A controlled investigation into prompt-conditioning effects in large language models.

Abstract

This repository presents an exploratory empirical study examining how prompt framing—specifically emotional tone and contextual priming—affects output variability in large language models (LLMs). Although LLMs operate deterministically given the same model and sampling parameters, the degree to which framing functions as an independent conditioning signal remains insufficiently characterised. This project provides a transparent, reproducible method for collecting outputs under controlled framings and for analysing lexical and semantic drift.

⸻

Research Question

To what extent does a change in prompt framing (e.g., neutral, excited, concerned) influence linguistic or conceptual variation in LLM outputs when the underlying task instruction remains constant?

This question is treated purely as a computational and statistical inquiry, without metaphysical or anthropomorphic interpretation.

⸻

Methodology

Prompt Structure

Each task consists of an identical instruction preceded by one of three framing contexts:
	1.	Neutral
	2.	Excited
	3.	Concerned

Task content remained unchanged; only framing was manipulated.

Data Collection

For each task–frame combination, the LLM generated a response using consistent parameters.
Outputs were stored in structured JSON for reproducibility.

Analysis

Three initial metrics were employed:
	•	Lexical Drift:
Word-level overlap measured via Jaccard similarity.
	•	Semantic Drift:
Vector-space similarity using TF-IDF and cosine distance.
	•	Structural Variation:
Differences in emphasis, elaboration, and reasoning tendencies.

The repository includes analysis scripts that compute drift scores, generate summary reports, and produce replicable observations.

⸻

Findings (Preliminary)

Preliminary results demonstrate that framing produces:
	•	systematic lexical variation
	•	shifts in structural and interpretive choices
	•	changes in conceptual salience
	•	increased divergence in specific categories (e.g., ethics, creativity)

These observations are consistent with the hypothesis that framing acts as a conditioning signal that nudges the model toward distinct activation pathways within its latent space.

⸻

Repository Contents
	•	The full dataset of collected model outputs
	•	Scripts to run controlled experiments
	•	Analysis utilities for computing drift metrics
	•	Summary generation tools
	•	Documentation and methodological notes

This repository is intentionally lightweight to encourage replication, critique, and extension.

⸻

Significance

Framing effects have implications for:
	•	reproducible research
	•	interpretability and reasoning analysis
	•	prompt engineering
	•	bias and variance studies
	•	reliability of LLM-assisted workflows

Quantifying these effects is increasingly important as LLMs are deployed in sensitive domains.

⸻

Contributing

Replication, extension, and critique are welcome.
Users may add new framing conditions, incorporate additional models, or propose improved metrics.

⸻

Licence

(Public Domain Dedication + Anti-Enclosure Covenant — Version 1.0, 2025)

1. Public Domain Dedication (CC0 1.0 Universal)

The authors permanently dedicate all material in this repository—including methods, processes, workflows, experimental designs, scripts, documentation, data formats, and results—to the public domain under CC0 1.0.

All copyright and related rights are waived to the fullest extent permitted by law.
This dedication is irrevocable.

⸻

2. Anti-Enclosure Covenant (Non-Assert Clause)

To ensure this work remains free:

No individual or organisation may:
	•	patent the method or any derivative of it
	•	claim exclusive ownership over the process, framework, or workflow
	•	assert proprietary rights over any conceptual or methodological component
	•	restrict others from using or reusing any part of this work

By using this material, you agree not to pursue or support any legal action aimed at monopolising the underlying process.

⸻

3. Permitted Uses

You may freely:
	•	use, modify, distribute, or build upon the work
	•	publish research based on it
	•	create tools, visualisations, or improved versions
	•	incorporate the technique into other systems

No attribution is required, though appreciated in academic contexts.
You may commercialise implementations, but not the method itself.

⸻

4. No Warranty

This work is provided “as is,” without warranty of any kind.

⸻

5. Summary (Plain-Language Version)

The method belongs to everyone, forever.
You can use it freely.
You just can’t lock it away.
