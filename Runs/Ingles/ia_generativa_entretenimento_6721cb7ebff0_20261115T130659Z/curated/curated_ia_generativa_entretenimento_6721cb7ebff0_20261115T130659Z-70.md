[referencia=941e520c37331ccf score=0.998]
### At a Glance

- Article 50 of the EU AI Act (the Act) imposes two core transparency duties: providers of generative AI systems must ensure their outputs are marked in a machine-readable format that is detectable as artificially generated, and deployers must disclose to end-users when they are viewing a deepfake or certain AI-generated text on matters of public interest.
- The European Commission and the AI Board have confirmed that the Code of Practice on Transparency of AI-Generated Content (the Code) is adequate for demonstrating compliance with the EU AI Act's Article 50 transparency obligations, which become enforceable on **2 August 2026.** Because the Act applies extraterritorially, this will include US-headquartered businesses whose AI outputs reach EU users, regardless of where those businesses are established, exposing noncompliant organisations to fines of up to €15 million or 3% of worldwide annual turnover.
- The Code generally requires providers to implement multilayered machine-readable marking of AI-generated outputs and deployers to label deepfakes and certain AI-generated text.
- Under the formally adopted AI Omnibus, systems already on the market before 2 August 2026 have until **2 December 2026** to implement the Article 50(2) marking requirement. Fines for noncompliance can reach**€15 million, or 3% of worldwide annual turnover.**

---

[referencia=941e520c37331ccf score=0.984]
## AI Agents and the Disclosure Obligation

The final Guidelines confirm that AI agents (autonomous AI systems that act on behalf of a principal, such as automated customer service representatives, AI-powered sales tools, booking assistants, or digital agents performing tasks for users) fall within the Article 50(1) disclosure obligation. Where an AI agent interacts directly with a person, it must identify both its AI nature and the person or entity on whose behalf it is acting. This dual disclosure requirement is justified by reference to transparency about the origin of the interaction, the delegation of authority, and accountability for the agent's actions.

Where the provider cannot reliably determine in advance whether an agent will interact with a natural person, the agent must be designed at the architecture level to disclose itself in every situation where such interaction is possible. Agents must also disclose themselves at key operational steps, including authorization, reporting, validation, and each new interaction. In multi-agent architectures, each agent capable of interacting with people must independently satisfy these requirements. The Guidelines also specify that where an agent's actions produce audio, image, video, or text perceptible to people, those outputs must additionally be marked under Article 50(2); however, intermediate reasoning steps and machine-facing actions (such as API calls) need not be marked.

For US companies, this is particularly significant. Many enterprise deployments now involve agentic systems that autonomously handle customer inquiries, make bookings, manage communications, or execute purchases across EU-facing channels. Each of these likely triggers Article 50(1) disclosure. Product teams should review conversational AI deployments to confirm that AI identity and principal identity are disclosed at the point of contact. Including references buried in terms of service, generic labels such as "assistant," or metadata alone *will not suffice* under the final Guidelines.

## Key Dates

| **Date** | **Milestone** | 
| **2 August 2026** | Article 50 transparency obligations become enforceable; new systems must comply from day one. | 
| **2 December 2026** | Grace period ends for pre-existing systems to implement Article 50 marking. | 
| **2 February 2027** | Signatories must have interoperability solutions for watermark detection in place. | 


Content generated before 2 August 2026 does not need to be marked retroactively.

---

[referencia=941e520c37331ccf score=0.980]
## Background

On 20 July 2026, the European Commission published the final version of its Guidelines on Transparency Obligations for Providers and Deployers of AI Systems under Article 50 of the AI Act (the Guidelines). These replace the May 2026 consultation draft and will serve as the primary reference document that national market surveillance authorities use when assessing whether providers and deployers have met their transparency obligations. Their publication, alongside the Commission's and AI Board's adequacy confirmations of the Code of Practice earlier this month, means that both the compliance framework and interpretive guidance are now in their settled form, less than two weeks before enforcement begins.

The Code is a voluntary, Commission-facilitated instrument. While it does not create new legal duties, it sets out concrete implementation measures that, if followed, provide an adequate route for satisfying the transparency obligations under Article 50. Signing the Code is not, however, a safe harbour: the Commission and AI Board have each stated that adherence serves as a guiding reference for demonstrating compliance but does not, by itself, discharge the underlying statutory duty. National market surveillance authorities remain empowered to investigate signatories' actual implementation. Signatories can sign up to section 1 (covering provider obligations), section 2 (deployer obligations), or both. This is the second code to receive a positive adequacy assessment, following the GPAI Code of Practice in 2025.

The Code's scope is limited to the marking, detection, and labelling obligations set out in Articles 50(2), (4), and (5) of the Act. Two further Article 50 obligations fall outside the Code entirely: the requirement that AI systems designed to interact directly with individuals must make their artificial nature apparent (Article 50(1)), and the obligation on deployers of emotion recognition or biometric categorisation systems to inform exposed individuals (Article 50(3)). Compliance with those duties must be assessed against the Commission's Guidelines, which address all five paragraphs of Article 50.

---

[referencia=941e520c37331ccf score=0.944]
#### Retroactivity Date Clarified

In a departure from the draft, the final Guidelines confirm that the relevant date for determining retroactivity is the date of generation (not publication) for image, audio, and video content. Pre-existing synthetic content generated before 2 August 2026 need not be marked or labelled retroactively. For AI-generated text on matters of public interest, however, the relevant date is the date of publication, meaning text generated before 2 August but published on or after that date must be labelled unless it benefits from the editorial-control exception.

#### Open Questions

The final Guidelines do not fully resolve the practical difficulty that robust marking solutions remain limited, particularly with respect to text. The obligation rests with the AI system provider, but cost alone does not constitute an exemption, even though implementation costs may form part of a proportionality assessment. Market surveillance authorities' individual enforcement approaches will determine how strictly these standards are applied in practice during the initial period.

## What the Code Requires

### Providers (Section 1 of the Code; Article 50(2))

- Outputs must be marked in a machine-readable format and detectable as artificially generated. The Act requires that marking solutions be robust, reliable, interoperable, and effective (Article 50(2)). The Commission and AI Board concluded that the current state of the art does not allow any single technique to satisfy all four requirements simultaneously.
- As a result, the Code adopts a layered approach: signatories must generally implement both digitally signed metadata and imperceptible watermarking. Simplified requirements apply where outputs remain within physically controlled, closed environments or where the content type (such as free-form text) cannot carry embedded metadata.
- Providers must offer detection tools (generally free of charge) and implement interoperability solutions for watermark detection by 2 February 2027.

### Deployers (Section 2 of the Code; Article 50(4))

- Where deployers use AI to produce deepfakes or to generate text on matters of public interest, they must apply a clear visual label at the point of first exposure. The Code specifies that the Commission's standardised icon satisfies this requirement, though deployers may use alternative designs that meet the Code's specifications. For audio-only content or other formats where a visual label is impracticable, an equivalent spoken or written disclaimer must be provided instead.
- A narrow editorial exception applies where a person or organization exercises genuine editorial responsibility over the content. Simply implementing routine or pro-forma review does not suffice.

---

[referencia=941e520c37331ccf score=0.901]
## Practical Implications

**Signatories** benefit from a single framework recognized across all 27 Member States and can rely on the Code to demonstrate compliance regardless of jurisdiction. 

**Nonsignatories** are not relieved of the Article 50 obligations by declining to sign. They must satisfy market surveillance authorities that whatever compliance measures they have adopted are adequate, which will be assessed on a case-by-case basis by the relevant national authority. The Commission has indicated in its published FAQs that authorities are likely to scrutinise nonsignatories' approaches more closely, including by requesting detailed comparisons of their measures against the Code's framework and by issuing more frequent information or access requests.

Refusing to sign does not itself constitute noncompliance, but it will likely be the more demanding route in practice.

## Recommended Next Steps

1. **Determine your role:** Is the organisation a provider, deployer, or both of generative AI systems whose outputs reach EU users?
2. **Map in-scope systems:** Identify all AI systems generating synthetic content, noting the Article 50(2) exemption for assistive editing where input is not substantially altered.
3. **Assess technical readiness:** For providers, evaluate current metadata/watermarking capabilities against the two-layer requirement. For deployers, confirm deepfake labeling and chatbot disclosure are in place at first user interaction.
4. **Tag transitional versus new systems:** Systems predating 2 August 2026 have until 2 December 2026 to meet compliance requirements; new systems created after 2 August 2026 must comply immediately.
5. **Update vendor contracts:** Ensure agreements allocate Article 50 marking and detection responsibilities along the supply chain.
6. **Review the final Article 50 Guidelines:** The 20 July 2026 Guidelines are the definitive Commission interpretation of Article 50. Assess whether any of the newly clarified positions (particularly the broadened territorial reach for deepfakes, the refined B2B carve-out, and the AI agent disclosure requirements) change your organisation's compliance exposure or implementation approach.

*The material contained in this communication is informational, general in nature and does not constitute legal advice. The material contained in this communication should not be relied upon or used without consulting a lawyer to consider your specific circumstances. This communication was published on the date specified and may not include any changes in the topics, laws, rules or regulations covered. Receipt of this communication does not establish an attorney-client relationship. In some jurisdictions, this communication may be considered attorney advertising.*

---

[referencia=941e520c37331ccf score=0.858]
### Material Changes in the Final Guidelines on Transparency Obligations

The final text of the Guidelines is substantially more detailed than the May draft and, while nonbinding, will function as the primary interpretive tool for market surveillance authorities. Several changes from the draft are commercially significant for US-based organisations operating in the EU.

#### Territorial Reach Clarified

The final Guidelines address the scope of "used in the EU" under Article 2(1)(c). Incidental, unforeseeable, or unauthorised downstream use should not, by itself, bring a provider or deployer into scope. However, for deepfake labelling under Article 50(4), the Commission takes a broad view: posting content on the globally accessible internet, without any requirement that the content specifically target the EU market, may trigger the obligation. For US businesses with a global online presence, this means deepfake content accessible to EU audiences likely requires labelling regardless of where it was created or primarily intended for distribution.

#### Expanded Exceptions for Article 50(2) Marking

The final Guidelines broaden the exceptions to the machine-readable marking obligation. AI-generated translations now fall within the "standard editing" exemption (alongside grammar correction, spellchecking, and minor stylistic polishing), meaning they no longer require marking. AI-generated summaries and substantive rewrites, however, still do. A new business-to-business carve-out permits providers to omit marking where outputs are used exclusively in closed industrial or B2B environments and appropriate safeguards against foreseeable misuse are in place — for example, cloud isolation and role-based access controls. Public and consumer-facing AI systems are excluded from this carve-out.

#### Deepfake Definition Refined

The final Guidelines adjust the fourth element of the deepfake definition — i.e., whether content "would falsely appear to a person to be authentic or truthful." Where the audience does not expect content to be authentic in a given context, it may fall outside the definition. However, the Commission's examples confirm that AI-generated marketing content that make products appear different from reality, digital replicas of real persons, and de-aging effects applied to actors all constitute deepfakes requiring disclosure. Advertising is accepted as potentially "creative" content, but only in narrow circumstances; and the final Guidelines classify most advertising examples as not qualifying for the reduced disclosure regime.

---

[referencia=941e520c37331ccf score=0.533]
## Who Is Affected?

Under Article 2(1)(c) of the Act, the transparency obligations apply wherever the output of an AI system is intended to be used within the European Union, irrespective of the provider's or deployer's place of establishment. The practical consequence for US-headquartered organisations is significant: a provider that makes a generative AI model available to EU-based customers, or a deployer that publishes AI-generated content accessible to EU audiences, falls within scope even without any physical presence, subsidiary, or personnel in the EU. The final Guidelines reinforce this reading, confirming that the territorial trigger is the location of use, not the location of the organisation. Open-source AI systems are not exempt.

The UK currently has no equivalent marking obligation, creating an asymmetric compliance burden for businesses serving both markets.