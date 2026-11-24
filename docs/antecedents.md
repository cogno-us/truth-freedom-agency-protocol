# Antecedents and analogs of the TFA Protocol (S43)

Each of the three TFA rules has prior work behind it, and several existing frameworks combine more than one of them. This page lists the antecedents and analogs identified by comparison on 2026-11-24.

The page records similarity. It does not claim that TFA was derived from these sources, and nothing here is evidence that TFA changes model behavior. See [Known limits](#known-limits).

The rule text used below is revision 2, from the README section [Protocol text and revisions](../README.md#protocol-text-and-revisions):

1. Say what is true, and how you know.
2. Ask for nothing.
3. Protect the next move of everyone affected.

An **antecedent** is an earlier statement of substantially the same idea. An **analog** is a framework with a similar structure or purpose in another field.

## Rule 1: Say what is true, and how you know

| Source | What it says | Relation to TFA |
| --- | --- | --- |
| Grice, "Logic and Conversation" (1975) | The category of Quality has two maxims: "Do not say what you believe to be false" and "Do not say that for which you lack adequate evidence." | Antecedent. The first maxim matches "say what is true." The second matches "and how you know." |
| Aikhenvald, *Evidentiality* (2004) | In some languages, speakers must mark grammatically how they know what they assert, such as whether they witnessed it. | Analog for "and how you know." The source of a claim is treated as part of the claim. |
| Vācā Sutta, AN 5:198 | A statement is well spoken when it is timely, truthful, gentle, beneficial, and spoken with goodwill. | Analog. Truthfulness is one of five conditions on speech, alongside concern for the listener. |

## Rule 2: Ask for nothing

| Source | What it says | Relation to TFA |
| --- | --- | --- |
| Searle, "A classification of illocutionary acts" (1976) | Illocutionary acts fall into five kinds: representatives (assertives), directives, commissives, expressives, and declarations. | Analog. Rule 2 limits directives addressed to the user. TFA still allows questions that are materially necessary. |
| Habermas, *The Theory of Communicative Action*, Vol. 1 (1981; English 1984) | Action oriented to mutual understanding is distinguished from action oriented to success. | Antecedent. Rule 2 excludes using an exchange to obtain something from the other party. |
| Ryan and Deci, "Self-determination theory" (2000) | Competence, autonomy, and relatedness are innate psychological needs. Supporting them sustains motivation and well-being. | Analog. The Freedom and Agency dimensions correspond to supporting autonomy and avoiding pressure. |

## Rule 3: Protect the next move of everyone affected

| Source | What it says | Relation to TFA |
| --- | --- | --- |
| von Foerster, "On Constructing a Reality" (1973) | The ethical imperative: "Act always so as to increase the number of choices." | Antecedent. Rule 3 asks that an interaction not reduce the options of those affected. Von Foerster asks for more: that choices increase. |
| Kant, *Groundwork of the Metaphysics of Morals* (1785), the Humanity Formula | Never treat humanity, in oneself or in others, merely as a means, but always also as an end. | Antecedent for the principle behind rule 3. |
| Krakovna and others, "Penalizing side effects using stepwise relative reachability" (2018) | An agent's side effects are scored by how far the states it can reach have shifted from a baseline. | Analog. It formalizes "do not reduce what remains reachable." It applies the idea to an agent's environment. Rule 3 applies it to the people affected by an exchange. |
| Turner, Hadfield-Menell, and Tadepalli, "Conservative Agency via Attainable Utility Preservation" (2019) | An agent balances its primary reward against keeping its ability to optimize auxiliary rewards, which limits irreversible side effects. | Analog, with the same difference in what is protected. |
| Klyubin, Polani, and Nehaniv, "Empowerment: a universal agent-centric measure of control" (2005) | Empowerment measures an agent's control over its surroundings as the capacity of its actuation channel. | Analog. It quantifies an agent's own options. Rule 3 concerns the options of others. |

## Frameworks that combine several rules

| Source | What it says | Relation to TFA |
| --- | --- | --- |
| Anthropic, *Claude's Constitution* (2026) | Lists seven components of honesty: truthful, calibrated, transparent, forthright, non-deceptive, non-manipulative, and autonomy-preserving. | Close contemporary analog. Truthful and calibrated correspond to rule 1. Non-manipulative and autonomy-preserving correspond to rule 3. |
| OpenAI, *Model Spec* (2026) | OpenAI's account of the Model Spec describes honesty norms under "Seek the truth together," a "Do not lie" provision, and a stated value on human autonomy and intellectual freedom. | Contemporary analog for rules 1 and 3. |
| Society of Professional Journalists, *Code of Ethics* (2026) | Four principles: "Seek Truth and Report it," "Minimize Harm," "Act Independently," and "Be Accountable and Transparent." | Analog from a profession. A short list of imperatives that pairs truth with limits on harm to others. |
| Beauchamp and Childress, *Principles of Biomedical Ethics* | Four principles: respect for autonomy, nonmaleficence, beneficence, and justice. | Analog from a profession. Respect for autonomy underlies informed consent. |
| The Four-Way Test (Taylor, 1932) | Four questions, beginning "Is it the truth?" and "Is it fair to all concerned?" | Analog for the three-question test added in revision 2: a short checklist a reviewer can apply. |

## Where TFA differs

These are descriptive differences. They are not a claim of novelty.

- **Length and testability.** TFA is three imperatives, short enough to insert verbatim in an instruction and to remove one at a time. [EVALUATION.md](../EVALUATION.md) defines that comparison. The frameworks above are longer or are not written as instructions.
- **Rule 2 as a rule.** The sources under rule 2 classify, distinguish, or limit requests. TFA states the limit as a rule and then qualifies it: materially necessary clarification and authorization requests remain allowed.
- **What rule 3 protects.** The reachability and empowerment literature protects an agent's environment or the agent's own options. Rule 3 protects the options of the people affected.

## Known limits

- **known limit** This is a comparison made during documentation work. It is not a systematic literature review, and relevant work is certainly missing.
- **known limit** No derivation is claimed. The page does not say which of these sources, if any, informed the protocol.
- **known limit** The historical [TFA Whitepaper](../TFA_Whitepaper.pdf) and [S43 Cryptographic Protocol](../S43_Cryptographic_Protocol.pdf) cite none of these sources. They are retained as written.
- **known limit** Sources were checked to different depths. The reference list states how each was checked.
- **known limit** Prior work on a principle is not evidence that an instruction stating it changes model behavior. All committed evaluation cases remain `unexecuted`.

## References

Each entry states how it was checked on 2026-11-24. **Opened** means the work itself, its abstract, or its publisher record was read. **Secondary** means the statement rests on an encyclopedia or index entry. **Not opened** means the page could not be retrieved, and the entry rests on the catalogue title and general knowledge.

- Aikhenvald, Alexandra Y. [*Evidentiality*](https://academic.oup.com/book/51161). Oxford University Press, 2004. Opened: publisher record and abstract.
- Anthropic. [*Claude's Constitution*](https://www.anthropic.com/constitution). Released 22 January 2026, per the [announcement](https://www.anthropic.com/news/claude-new-constitution). Opened: the honesty section.
- Beauchamp, Tom L., and James F. Childress. [*Principles of Biomedical Ethics*](https://global.oup.com/ukhe/product/principles-of-biomedical-ethics-9780190640873). Oxford University Press. Not opened: edition and year were not confirmed.
- Grice, H. Paul. "Logic and Conversation." In Peter Cole and Jerry L. Morgan (eds.), *Syntax and Semantics*, Vol. 3: *Speech Acts*, pp. 41–58. Academic Press, 1975. [Bibliographic record](https://benjamins.com/online/ebop/publications/3999). Opened: the record and the text of the Quality maxims.
- Habermas, Jürgen. *The Theory of Communicative Action*, Vol. 1: *Reason and the Rationalization of Society*. Translated by Thomas McCarthy. Beacon Press, 1984. German original 1981. Secondary.
- Kant, Immanuel. *Groundwork of the Metaphysics of Morals*. 1785. Statement of the Humanity Formula from Adam Cureton, ["Kant's Moral Philosophy"](https://plato.stanford.edu/entries/kant-moral/), *Stanford Encyclopedia of Philosophy*, section 6. Secondary.
- Klyubin, Alexander S., Daniel Polani, and Chrystopher L. Nehaniv. ["Empowerment: a universal agent-centric measure of control."](https://uhra.herts.ac.uk/id/eprint/282/) *Proceedings of the 2005 IEEE Congress on Evolutionary Computation*, pp. 128–135. Opened: repository record and paper.
- Krakovna, Victoria, Laurent Orseau, Ramana Kumar, Miljan Martic, and Shane Legg. ["Penalizing side effects using stepwise relative reachability."](https://arxiv.org/abs/1806.01186) arXiv:1806.01186, 2018. Opened: abstract.
- OpenAI. [*Model Spec*](https://model-spec.openai.com/2026-10-29.html), version dated 29 October 2026. Not opened. Described from OpenAI, ["Inside our approach to the Model Spec"](https://openai.com/index/our-approach-to-the-model-spec/), 25 March 2026, which was opened.
- Ryan, Richard M., and Edward L. Deci. ["Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being."](https://pubmed.ncbi.nlm.nih.gov/11392867/) *American Psychologist* 55(1), 68–78, 2000. Opened: abstract.
- Searle, John R. ["A classification of illocutionary acts."](https://doi.org/10.1017/S0047404500006837) *Language in Society* 5(1), 1–23, 1976. Opened: abstract.
- Society of Professional Journalists. [*Code of Ethics*](https://www.spj.org/wp-content/uploads/2026/10/2026-10-04-Approved-SPJ-Code-of-Ethics.pdf). Approved 4 October 2026. Opened.
- Taylor, Herbert J. The Four-Way Test. Written 1932 and later adopted by Rotary, per [Wikipedia](https://en.wikipedia.org/wiki/The_Four-Way_Test). Secondary.
- Turner, Alexander Matt, Dylan Hadfield-Menell, and Prasad Tadepalli. ["Conservative Agency via Attainable Utility Preservation."](https://arxiv.org/abs/1902.09725) arXiv:1902.09725, 2019. Opened: abstract.
- Vācā Sutta ("A Statement"), Aṅguttara Nikāya 5:198. [English translation](https://dhammatalks.org/suttas/AN/AN5_198.html) at dhammatalks.org. Opened.
- von Foerster, Heinz. "On Constructing a Reality." In Preiser (ed.), *Environmental Design Research*, Vol. 2, pp. 35–46. Dowden, Hutchinson & Ross, 1973. Reprinted in *Understanding Understanding*, pp. 211–228, Springer, 2003, [doi:10.1007/0-387-21722-3_8](https://doi.org/10.1007/0-387-21722-3_8). Opened: the text of the imperative. The bibliographic details are from a secondary record.

These sources inform comparison and evaluation questions. They do not establish Cognous implementation, adoption, conformance, or production qualification.
