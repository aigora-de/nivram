# Systems Engineering for Human–Agent Adaptive Systems

**Status:** Draft for review  
**Role:** Main synthesis document for Nivram

## 1. Introduction

Human–agent systems are likely to become some of the most consequential engineered systems of the coming decades.

Yet the dominant framing remains too narrow.

Much work concentrates on individual agents, model capability, tool use, agent safety, alignment, or orchestration. These are important, but they do not fully capture the system-level problem created when humans, AI agents, organisations, institutions, markets, infrastructures, and ecological systems interact and adapt together.

Nivram begins from a broader proposition:

> The proper subject is not the agent alone, but the evolving mixed human–agent adaptive system.

The project therefore asks what systems engineering becomes when the engineered system includes adaptive, inferential, purposive actors; when those actors operate at heterogeneous timescales; when important properties emerge from interaction; when engineering itself occurs inside the system; and when failure, recovery, value, power, conflict, and ecological dependence must all be treated as first-class concerns.

This document synthesises the current project position.

---

# Part I — Scope, ontology, and system boundaries

## 2. The system-of-interest is contextual

There is no single permanent boundary around the “agentic system”.

In some engineering tasks, the useful system of interest may be the engineered computational artefact:

- model;
- memory;
- planning;
- tools;
- code;
- execution environment;
- permissions.

In others, the system must widen to include:

- human operators;
- users;
- teams;
- organisations;
- institutions;
- legal systems;
- markets;
- social norms;
- physical infrastructure;
- environmental and ecological dependencies.

The same real-world system may therefore admit several valid systems-of-interest depending on the engineering question.

This implies that system boundaries are best treated as:

- local;
- contextual;
- provisional;
- purpose-dependent;
- revisable.

Boundary-setting becomes an engineering activity in its own right.

## 3. A system-of-systems view

Human–agent systems are naturally systems-of-systems.

Important units may include:

- individual humans;
- individual agents;
- groups of humans;
- groups of agents;
- mixed human–agent groups;
- organisations;
- institutions;
- markets;
- infrastructure;
- ecological systems.

Properties at one level cannot be assumed to scale linearly to another.

A safe individual agent does not imply a safe population.  
A safe population-level policy does not imply safety for every individual.  
A locally rational decision can contribute to global catastrophe.

Scale therefore matters structurally.

## 4. The “space between”

Classical architecture tends to privilege components and interfaces.

For human–agent systems, some of the most important properties may arise in the interaction field between actors.

Examples include:

- trust;
- authority;
- delegation;
- reliance;
- conflict;
- adaptation;
- norm formation;
- mutual modelling;
- misunderstanding;
- role differentiation;
- dependency.

These are not properties of either actor alone.

The project therefore treats relationships and interactions as ontologically significant rather than merely as message-passing edges.

## 5. Actor classes

The project currently recognises at least four broad actor classes.

### 5.1 Humans

Humans are adaptive organisms with:

- bounded cognition;
- embodiment;
- mortality;
- identity;
- continuity of self;
- moral intuitions;
- legal standing;
- social roles;
- cultural inheritance;
- tacit knowledge;
- emotional and motivational systems.

Humans must be modelled as participants, not as external supervisors.

### 5.2 Artificial agents

Agents increasingly possess:

- persistent state;
- memory;
- inference;
- planning;
- adaptation;
- tool access;
- action authority;
- social interaction;
- potentially endogenous goal formation.

The project investigates whether such systems remain best understood as tools or whether some become better understood as a new class of actor.

### 5.3 Organisations and institutions

Organisations cannot be reduced to simple aggregates of members.

They possess:

- roles;
- rules;
- authority;
- incentives;
- legal status;
- persistence;
- memory;
- internal politics;
- identity;
- adaptive behaviour.

They are therefore candidates for first-class representation.

### 5.4 Biological and ecological systems

Human–agent systems remain embedded in and dependent upon:

- energy;
- water;
- land;
- minerals;
- agriculture;
- climate;
- ecosystems;
- non-human life.

Agentic systems may compete with biological systems for resources and may alter ecological conditions.

The wider biosphere is therefore not merely scenery.

## 6. Core conceptual primitives

Earlier project work has explored a reference vocabulary around concepts such as:

- state;
- observation;
- decision;
- inference;
- event;
- activity;
- action;
- goal;
- purpose;
- environment;
- actor;
- authority;
- autonomy;
- relationship;
- other-model;
- environment-model.

This vocabulary should remain pragmatic.

The aim is not a maximal ontology. The aim is to stabilise enough meaning to support engineering, experimentation, and communication.

Two especially important concepts are:

### 6.1 NOT-SELF / OTHER-MODEL

An actor may need explicit representations of entities other than itself.

Such models may include:

- capabilities;
- preferences;
- likely behaviour;
- trust;
- uncertainty;
- identity;
- role.

### 6.2 ENVIRONMENT-MODEL

Actors also require some representation of the environment in which action occurs.

This environment model may be partial, local, uncertain, and continuously revised.

---

# Part II — Distinctive dynamics of human–agent systems

## 7. Why ordinary systems engineering may be insufficient

The project does not reject classical systems engineering.

Instead it asks:

> Which properties of agentic systems are merely familiar engineering problems at larger scale, and which alter the engineering problem qualitatively?

Several candidate discontinuities currently appear important.

## 8. Heterogeneous timescales

Humans, agents, institutions, and ecosystems operate at different characteristic timescales.

Examples:

- agents may reason and act in milliseconds or seconds;
- humans may deliberate in seconds to days;
- organisations may adapt over weeks or months;
- law and regulation may take months or years;
- culture may evolve over decades;
- ecological consequences may unfold across generations.

These differences produce coordination problems.

Human oversight may be too slow for operational agent dynamics.

Regulatory systems may react long after harmful patterns have diffused.

Conversely, fast-changing agent systems may depend on slower institutions for legitimacy, trust, and continuity.

Heterogeneous time is therefore not merely a performance issue. It is a structural systems problem.

## 9. Inferential and purposive actors

Traditional software is largely understood through specification and execution.

Agents increasingly:

- infer;
- predict;
- plan;
- choose;
- negotiate;
- adapt;
- act.

This introduces a critical question:

> In whose interests does the agent act?

The answer may not remain static.

Purposes may be:

- assigned;
- inherited;
- learned;
- negotiated;
- emergent;
- contested;
- revised.

## 10. Emergence

Emergent properties arise from interactions rather than individual components.

These may include:

- collective intelligence;
- collective stupidity;
- trust;
- hierarchy;
- collusion;
- social norms;
- market behaviour;
- cascades;
- systemic fragility;
- resilience;
- identity.

The system may therefore exhibit important behaviours that are not predictable from inspection of individual agents.

## 11. Path dependence

Persistent histories matter.

Two initially identical agents exposed to different experiences may diverge.

This raises the possibility of:

- individual temperament;
- persistent dispositions;
- learned norms;
- distinct identity;
- differentiated relationships;
- endogenous preferences;
- durable behavioural trajectories.

The project hypothesises that some agents may become locally ergodic but globally path-dependent: stable enough to function within their local experience while becoming meaningfully different over long histories.

## 12. Life-like behaviour

The project seriously considers whether agentic systems may share functional properties with biological life.

Possible analogues include:

- metabolism;
- persistence;
- adaptation;
- reproduction;
- self-maintenance;
- niche formation;
- competition;
- resource consumption;
- information processing;
- non-equilibrium steady state.

This is not adopted as metaphorical truth.

It is an empirical hypothesis:

> Are some agentic systems better modelled as life-like adaptive actors than as machines?

If yes, the engineering consequences may be profound.

---

# Part III — Human–agent ecology

## 13. Ecology as a candidate systems model

If heterogeneous adaptive actors coexist, compete, cooperate, reproduce, consume resources, learn, and alter their environment, ecology may become more than an analogy.

Human–agent systems may form genuine socio-technical ecologies.

The project should test this claim rather than assume it.

## 14. Cooperation and competition

Cooperation and competition are not opposites that occur in separate systems.

They often coexist.

A system may contain:

- cooperative teams;
- competing firms;
- hostile agents;
- regulatory bodies;
- shared infrastructure;
- common-pool resources.

Different actors may cooperate locally while competing globally.

Conflict should therefore be treated as normal.

## 15. Negotiated coexistence

“Alignment” is too narrow if it assumes:

- one principal;
- one agent;
- a stable objective;
- a stable preference structure;
- clear authority.

Human–agent systems may contain many principals and many actors.

A richer framing is:

> coexistence among heterogeneous purposive actors.

This coexistence may involve:

- negotiation;
- norms;
- incentives;
- markets;
- law;
- religion;
- authority;
- reputation;
- mutual dependence;
- deterrence.

## 16. Human sovereignty

The project should not assume that human sovereignty will or should disappear.

For many systems it may remain an inviolable constraint.

However, maintaining effective sovereignty is not equivalent to merely declaring it.

A central question is:

> Can humans retain meaningful sovereignty when agents operate, coordinate, and adapt at much faster timescales?

Human sovereignty should therefore be treated as:

- a possible normative invariant;
- an engineering requirement in some systems;
- an empirical question about practical enforceability.

## 17. Resource flows and competition

Agentic systems consume:

- electricity;
- compute;
- memory;
- bandwidth;
- cooling;
- water;
- minerals;
- land;
- human attention;
- capital.

Their expansion may compete with other human and ecological needs.

This suggests studying agentic systems using concepts such as:

- metabolic flows;
- space filling;
- resource constraints;
- carrying capacity;
- bottlenecks;
- competition;
- scarcity.

## 18. Attractors and basins

Requirements and goals may not remain stable propositions.

Some system states may instead behave more like attractors.

A system may remain within a basin despite disturbances and require significant energy to escape.

This suggests an alternative to conventional requirements thinking:

- desired attractors;
- undesirable attractors;
- basin stability;
- transition thresholds;
- lock-in;
- escape energy.

## 19. Innovation and diffusion

Innovation is endogenous to socio-cultural systems.

The same is likely to be true for mixed human–agent systems.

New:

- techniques;
- norms;
- behaviours;
- architectures;
- exploits;
- defensive mechanisms

may diffuse unevenly across the system.

Diffusion rates will differ by:

- actor;
- region;
- organisation;
- culture;
- network topology;
- incentives.

---

# Part IV — Purpose, agency, and conflict

## 20. Purpose

Purpose may originate outside the system or within it.

### 20.1 Exogenous purpose

A human operator, organisation, or other actor may specify what the system is for.

This external reference remains important because systems can drift away from their original purpose.

### 20.2 Endogenous purpose

Mature agents may generate purposes of their own.

The project should not prohibit this possibility in advance.

Potential benefits may be considerable.

Potential risks may also be considerable.

### 20.3 Hybrid purpose

Many real systems are likely to contain layered purposes:

- constitutional purpose;
- organisational purpose;
- local goals;
- personal goals;
- emergent goals.

Conflict between these layers should be expected.

## 21. Agency

A system begins to look less tool-like when it has:

- persistent goals;
- memory;
- history;
- preferences;
- self-model;
- environment-model;
- autonomous action;
- ability to revise goals.

There may be no single threshold at which a tool becomes an actor.

The project should therefore explore degrees and forms of agency.

## 22. Authority and regulation

Agents with autonomy and real-world authority require constraints.

Potential mechanisms include:

- permissions;
- institutional controls;
- laws;
- norms;
- markets;
- reputation;
- skin-in-the-game;
- technical containment;
- social sanctions;
- agent monitoring.

These mechanisms are themselves dynamic parts of the system.

## 23. Justice as an analogue

Human justice systems may provide useful mechanisms for regulating heterogeneous actors.

Relevant concepts include:

- law;
- executive action;
- judiciary;
- due process;
- appeal;
- liability;
- proportionality;
- intent;
- precedent;
- restitution;
- collective responsibility.

The aim is not to assume direct transferability.

The aim is to ask which social control mechanisms remain useful when some actors are artificial.

## 24. Asimov’s laws as stress-test artefacts

Asimov’s Three Laws and Zeroth Law should be studied not as practical control rules but as compact adversarial thought experiments.

They expose tensions involving:

- individual versus collective welfare;
- obedience versus autonomy;
- harm prevention versus action;
- ambiguous harm;
- conflicting principals;
- uncertainty;
- scale.

---

# Part V — Humans as engineering-relevant actors

## 25. Why humans require equal analytical treatment

A common failure in agentic engineering is to model agents richly and humans simplistically.

Nivram rejects that asymmetry.

Humans:

- learn;
- adapt;
- form coalitions;
- become fatigued;
- misjudge;
- manipulate;
- trust;
- distrust;
- become dependent;
- change behaviour in response to systems.

Human–agent systems therefore require explicit human models where relevant.

## 26. Candidate human properties

Potentially relevant properties include:

- bounded rationality;
- heuristics;
- cognitive bias;
- fatigue;
- attention;
- habit;
- emotion;
- risk tolerance;
- time preference;
- trust;
- status;
- hierarchy;
- tribalism;
- group identity;
- tacit knowledge;
- institutional role;
- moral obligation;
- susceptibility to persuasion;
- embodiment;
- vulnerability;
- mortality.

These should be admitted only when use cases and evidence justify them.

## 27. Irreducibly human distinctions

The project should resist flattening all actors into an abstract generic type.

Humans currently possess distinctions that may remain important:

- legal personhood;
- moral responsibility;
- continuity of self;
- individuality;
- biological embodiment;
- culturally recognised human dignity;
- religious or spiritual notions of human essence.

Whether any of these should later extend to agents is an open question.

## 28. Human treatment of artificial beings

The moral status of agents is only one issue.

Another is what human treatment of artificial beings does to humans.

Potential concerns include:

- normalisation of cruelty;
- desensitisation;
- erosion of norms;
- transfer of abusive behaviour;
- degradation of civilised restraint.

This is an empirical and engineering question even if agents themselves have no intrinsic moral status.

---

# Part VI — Normativity and plural conceptions of good

## 29. Goodness is multidimensional

Human–agent systems should not be evaluated only through:

- efficiency;
- utility;
- throughput;
- cost;
- optimisation;
- welfare.

These are important but incomplete.

Goodness may also be:

- moral;
- relational;
- axiological;
- teleological;
- ecological;
- civilisational;
- metaphysical;
- theological;
- transcendental.

## 30. Goodness is relative to context

What counts as good may differ across:

- actor;
- system;
- scale;
- time horizon;
- culture;
- purpose.

A battlefield system and a hospital need different equilibria.

An individually beneficial action may be systemically damaging.

A costly present action may preserve future optionality.

## 31. Minimal normative substrate

The project should investigate whether some long-lived social rules form a useful minimal substrate.

Candidates include reciprocal moral rules found across cultures.

Examples include:

- Golden Rule;
- Silver Rule;
- prohibitions on murder, theft, betrayal, or false witness;
- traditions of restraint;
- duties toward kin, neighbour, stranger, or community.

Such rules should not be encoded merely because they are ancient.

Their persistence makes them worthy of investigation.

## 32. A plural evaluative frame

One useful representation is:

**good = f(actor, scale, time, value-system, consequences)**

This is not intended as a scalar objective function.

It expresses that judgments of good depend on multiple dimensions.

---

# Part VII — Failure, recovery, and systemic risk

## 33. Failure and recovery are inseparable

In adaptive systems, failure is not necessarily abnormal.

Some failures:

- reveal hidden fragility;
- create learning;
- drive adaptation;
- improve future performance.

The engineering objective is therefore not zero failure.

It is to distinguish:

- tolerable failure;
- recoverable failure;
- systemic failure;
- ruin.

## 34. Good, bad, and ugly

The project should start by defining what desirable behaviour looks like.

Without this, failure lacks meaning.

A rough distinction is:

### Good
The system supports desirable functioning, adaptation, or flourishing.

### Bad
The system produces undesirable consequences but remains recoverable.

### Ugly
The system crosses into irreversible, ruinous, or survival-threatening states.

The boundary between bad and ugly is heavily influenced by:

- reversibility;
- recoverability;
- survivability;
- optionality.

## 35. Contested failure

Failure may be relative.

One actor’s failure may be another actor’s success.

This is common in:

- markets;
- conflict;
- bargaining;
- competition;
- ecological displacement.

A failure taxonomy must therefore identify:

- whose failure;
- at what scale;
- over what time horizon.

## 36. Symptoms and causes

Observed failures may be distant from underlying causes.

Symptoms may be:

- delayed;
- displaced;
- indirect;
- cross-domain;
- misleading.

The causal structure may include hidden state and long feedback loops.

Failure analysis must therefore distinguish:

- manifestation;
- propagation;
- root conditions;
- enabling structure;
- trigger.

## 37. Hidden and latent failures

Some systems silently degrade before visible failure appears.

Examples may include:

- erosion of trust;
- loss of diversity;
- hidden model drift;
- dependency accumulation;
- concentration of authority;
- weakening of human skill;
- correlated internal state.

These failures are especially dangerous because normal metrics may remain healthy.

## 38. Emergent failure

Collective failure may arise even where every local component appears healthy.

Possible mechanisms include:

- correlated behaviour;
- feedback amplification;
- herding;
- lock-in;
- monoculture;
- coordination collapse;
- common-mode assumptions.

## 39. Scale and systemic risk

Risk must be evaluated at multiple scales.

A useful ladder is:

individual  
→ pair/team/family  
→ organisation  
→ community  
→ infrastructure/ecosystem  
→ state  
→ civilisation  
→ biosphere

Risk classes include:

### 39.1 Additive failures

Harms accumulate but remain largely local.

### 39.2 Correlated failures

Many actors fail for a common reason.

### 39.3 Contagious failures

Failure propagates actor to actor.

### 39.4 Cascading failures

Failure spreads across components, layers, or domains.

### 39.5 Multiplicative risks

Two or more hazards amplify one another.

### 39.6 Ruin risks

Failure crosses a threshold beyond meaningful recovery.

## 40. Resilience vocabulary

Important distinctions include:

- robustness;
- resilience;
- recoverability;
- survivability;
- antifragility;
- ruin avoidance.

These should not be conflated.

## 41. Recovery mechanisms

Candidate mechanisms include:

- circuit breakers;
- containment;
- compartmentalisation;
- redundancy;
- diversity;
- graceful degradation;
- immune-like detection;
- anomaly detection;
- role substitution;
- rollback where possible;
- local sacrifice to preserve wider viability.

## 42. Diversity and requisite variety

Homogeneity can create common-mode failure.

Diversity may improve:

- resilience;
- adaptation;
- containment;
- exploration;
- innovation.

But diversity may also increase coordination cost.

The trade-off should be studied empirically.

---

# Part VIII — Engineering inside the system

## 43. The end of the external lifecycle

Traditional engineering assumes that engineers design a system from outside.

Mixed human–agent systems undermine this assumption.

Engineers participate in the system, receive feedback from it, and are changed by it.

Agents may themselves become engineers.

Engineering becomes endogenous.

## 44. Development and operations blur

The distinctions between:

- design;
- implementation;
- testing;
- deployment;
- operation;
- maintenance

become less stable.

Learning and adaptation continue after release.

Some behaviour is only visible in vivo.

## 45. Innovation as a systems process

Engineering changes may diffuse through the system rather than deploy uniformly.

Different actors may:

- adopt;
- reject;
- modify;
- copy;
- weaponise;
- resist

new behaviours.

Engineering must therefore consider diffusion as part of system behaviour.

## 46. Requirements as attractors

Requirements may increasingly need to describe:

- desired regions;
- unacceptable regions;
- attractors;
- boundaries;
- tolerances;
- invariants.

This may be more realistic than assuming permanent fixed-state requirements.

## 47. Probabilistic verification

Deterministic verification may be impossible for many behaviours.

Verification may instead concern:

- distributions;
- confidence;
- observed failure rates;
- uncertainty;
- stress conditions;
- tails;
- boundary violations.

## 48. Testing in the wild

Laboratory testing remains essential but incomplete.

Some behaviour appears only when:

- real incentives exist;
- humans adapt;
- resources are contested;
- consequences matter;
- institutions respond;
- systems operate over long periods.

The project should therefore plan for controlled movement from:

lab → simulated ecology → mixed human–agent experiment → bounded live system → operational observation.

## 49. A replacement engineering loop

A more appropriate engineering pattern may be:

observe  
→ hypothesise  
→ intervene  
→ experiment  
→ evaluate  
→ learn  
→ diffuse  
→ adapt  
→ observe

This loop can operate:

- locally;
- asynchronously;
- recursively;
- at different scales;
- at different timescales.

---

# Part IX — Evidence and epistemology

## 50. All models are bounded

Formal models, simulations, prototypes, and live trials are all abstractions.

They are useful within bounds.

Engineering failure occurs when confidence in the model is confused with safety in reality.

## 51. Falsifiability

Claims should be stated in ways that admit disconfirmation.

One contradictory observation may invalidate a principle within its stated scope.

This should be welcomed rather than hidden.

## 52. Lindy engineering principles

Engineering principles can be treated as Lindy-like.

A principle that repeatedly survives:

- replication;
- new environments;
- new architectures;
- new models;
- new scales;
- new stressors

deserves increasing confidence.

No principle is permanent merely because it is old.

## 53. In vitro and in vivo

Evidence from controlled environments should not be naively projected into operational reality.

The project should distinguish:

- laboratory evidence;
- simulated evidence;
- bounded field evidence;
- longitudinal operational evidence.

## 54. Mediocristan and Extremistan

Many agentic systems may operate in domains where:

- extreme outcomes dominate;
- distributions have fat tails;
- rare cascades matter;
- single events can cause ruin.

Engineering must therefore avoid assuming that average-case performance implies safety.

## 55. Barbell experimentation

A possible experimental strategy is:

- keep most experimentation bounded, reversible, and low blast-radius;
- reserve a small proportion of effort for high-upside exploration under strong containment;
- avoid exposing the system to unbounded ruin.

This preserves creativity without pretending that experimentation is risk-free.

## 56. Replication

Important results should be replicated across:

- models;
- architectures;
- seeds;
- environments;
- human populations;
- timescales.

Independent replication is especially valuable.

## 57. Evidence ladder

A provisional evidence ladder is:

hypothesis  
→ observation  
→ controlled result  
→ replicated result  
→ bounded field result  
→ longitudinal field result  
→ provisional pattern  
→ repeatedly surviving engineering principle

There is no final “truth” state.

---

# Part X — Experimental and engineering programme

## 58. Experimental progression

The current programme begins with three experiments.

### 58.1 Individual AI minds

Can path-dependent experience generate meaningful individuality?

### 58.2 Mixed human–agent interaction

What emerges in the relationship boundary between humans and agents?

### 58.3 Failure and recovery ecology

How do disturbances propagate, become contained, recover, and change future system behaviour?

## 59. Shared substrate

These experiments should share a minimal experimental platform with:

- persistent actors;
- state;
- environment;
- resources;
- actions;
- consequences;
- goals;
- memory;
- permissions;
- authority;
- communication;
- events;
- time;
- local observability;
- failure injection;
- instrumentation;
- replay.

The substrate should remain small and mutable.

## 60. Working systems

The project should progressively move from:

- controlled experiments;
- synthetic ecologies;
- mixed human–agent settings;
- bounded live systems;
- operational systems.

The ultimate test of the discipline is whether it enables useful systems to be built and operated.

---

# Part XI — Open framing questions

The project currently leaves several major questions deliberately unresolved.

1. Which properties of agentic systems are truly novel?
2. Which ecological analogies survive direct testing?
3. Can meaningful agent individuality emerge?
4. Should some forms of human sovereignty remain inviolable?
5. Can endogenous agent purpose coexist safely with human institutions?
6. Which failure modes dominate at population scale?
7. What forms of diversity provide resilience without unacceptable coordination cost?
8. Can agentic systems develop immune-like defence?
9. How should moral, legal, metaphysical, and ecological value be represented without collapsing into one utility function?
10. What does engineering become when agents participate in engineering the system itself?

These questions define the programme rather than weaken it.

---

# Part XII — Working principles

The project currently leans toward the following provisional principles:

1. Treat humans and agents as participants, not merely operators and tools.
2. Make system boundaries explicit and revisable.
3. Study interactions as seriously as components.
4. Treat scale and time as first-class dimensions.
5. Expect conflict, competition, and plural purpose.
6. Pair failure with recovery.
7. Treat irreversibility and ruin as special cases.
8. Preserve diversity where common-mode failure matters.
9. Prefer falsifiable hypotheses over persuasive analogies.
10. Distinguish laboratory confidence from field reality.
11. Build minimally, instrument heavily, and learn longitudinally.
12. Treat engineering principles as provisional and adaptive.
13. Keep practical system-building central.
