# llm-framing-experiment
Prompt framing effect experiments

📄 Appendix C: Platform-Level Framing Drift in Public Discourse

(Ready to drop directly into the academic T13/REF work)

C.1 Overview

This appendix documents an incidental but informative observation:
the same underlying conceptual material, when framed differently and presented on two different platforms, produced opposite system-level responses.

The content itself did not change.
Only the frame, tone, and contextual positioning did.

This creates a useful real-world analogue to the question motivating the LLM drift experiment:

Do different framings systematically alter reasoning pathways and system outputs, even when the underlying information remains constant?

In this case, the “system outputs” were not LLM tokens, but platform behaviours (moderation, engagement, visibility, and discourse characteristics).

C.2 Methods (Incidental Case Study)

Two deployments occurred:
	1.	Wikipedia submission
	•	Framed as a formal mathematical article.
	•	Positioned as a potential canonical reference.
	•	Tone: declarative, authoritative, institutional.
	2.	Reddit post in r/OpenSourceAI
	•	Framed as a small exploratory experiment.
	•	Positioned as a curiosity-driven question.
	•	Tone: neutral, tentative, inquiry-oriented.

The core underlying idea was substantially the same in both cases:
that reasoning trajectories (human or machine) may vary under different prompt framings, and that such drift may be measurable.

C.3 Observed Outcomes

Wikipedia
	•	Immediate resistance.
	•	Rapid scrutiny from multiple participants.
	•	Deletion pathways activated.
	•	Process-oriented objections (e.g., sourcing, notability, authority).
	•	System behaviour tended toward constriction.

Reddit
	•	Rapid positive engagement.
	•	High visibility within hours.
	•	Organic discussion.
	•	No defensive moderation behaviour.
	•	System behaviour tended toward expansion.

Both systems acted consistently with their documented institutional roles:
	•	Wikipedia tends to filter, stabilise, and converge.
	•	Reddit tends to explore, diversify, and amplify.

C.4 Analysis

The divergence cannot be explained by content (which was similar),
but can be explained by:

(1) Frame-based interpretation

Institutional tone ≠ conversational tone.
Formal tone signals “authoritative claim” → triggers gatekeeping.
Exploratory tone signals “open question” → triggers collaboration.

(2) System-level incentives

Wikipedia incentivises:
	•	Caution
	•	Verification
	•	Deferral to precedent

Reddit incentivises:
	•	Novelty
	•	Discussion
	•	User-driven momentum

The underlying hypothesis emerges naturally:

A system’s local interpretive frame can shift its behavioural output even when the informational input remains constant.

This is analogous to LLM framing drift:
	•	The model remains the same.
	•	The “ask” remains the same.
	•	The framing alters the pathway and the outcome.

(3) Observer-dependent collapse

Although purely sociotechnical (not physical), the effect mirrors the core question:

Different observers
	•	different frames
→ different reasoning collapses
→ different stable states.

C.5 Conclusion

This incidental case study provides a real-world analogue to the LLM drift phenomenon:
	•	Same content
	•	Different framing
	•	Different system response

It reinforces the central premise of the drift experiment:

In complex cognitive or sociotechnical systems, framing is not a cosmetic layer.
It is an active variable that shapes the system’s internal dynamics and external behaviour.

Further work may compare:
	•	LLM drift maps
	•	Human discourse drift
	•	Platform behaviour drift

to determine whether similar recursive patterns appear across domains.
