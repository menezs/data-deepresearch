# Auditing the Responses of Deep Research Tools — Data

This repository contains the data of the research *Auditing the Responses of Deep Research Tools*: 54 answers produced by three Deep Research tools (ChatGPT, Gemini, and Claude) to the same 9 questions in Brazilian Portuguese and in US English, and the complete artifacts of the citation audit of each answer.

The audit was produced with **Deep Research Auditor**, an open-source pipeline that checks, sentence by sentence, whether each cited source supports the sentence that cites it: <https://github.com/menezs/deep-research-auditor>.

Every verdict can be re-checked by reading exactly what the judge read, and every rate can be recomputed from these files without calling any language model.

## Corpus at a glance

| Set | Answers | Cited excerpts | Judged | Supported (% of judged) | Cited sources | Downloaded |
|---|---|---|---|---|---|---|
| Portuguese (PT) | 27 | 2,687 | 2,365 | 1,605 (67.86%) | 867 | 771 |
| English (EN) | 27 | 2,679 | 2,380 | 1,633 (68.61%) | 1,333 | 1,229 |

A **cited excerpt** is a sentence of the answer that carries a citation marker such as `[12]`. It is **judged** only when every source it cites has downloaded content and every marker has an entry in the reference list; otherwise it is **skipped** with an explicit reason. Percentages are truncated, not rounded, to two decimal places.

## Repository layout

```
Deepreseachr answers/            the answers as exported by the tools
  Portugues/ | Ingles/           language
    ChatGPT/ | Claude/ | Gemini/ tool
      Consolidado/               consolidated topics
      EmConsolidacao/            consolidating topics
      Emergente/                 emerging topics
        <topic>.md | <topic>.docx
Runs/                            one folder per audit run
  Portugues/ | Ingles/
    <topic>_<answer hash>_<UTC start time>/
```

ChatGPT and Claude answers are Markdown exports; Gemini answers are DOCX exports.

### Files in each run

| Path | Content |
|---|---|
| `run_meta.json` | Answer path, tool, and start time of the run |
| `input/` | A copy of the exported answer file (`original.md` or `original.docx`), the text loaded from it (`answer_raw.md`), and the normalized text that was audited (`answer.md`) |
| `references.json` | The answer's reference list: URL, citation markers, and download status of each source (`downloaded`, `blocked`, `inaccessible`, `dead`, `error`) |
| `answer_chunks.json` | The cited excerpts, their markers, and the sources they cite |
| `documents/` | Metadata of each downloaded source (`<id>.meta.json`: fetch method, word count, and the SHA-256 of the Markdown text that was audited). The full texts are not redistributed; see [Re-downloading the sources](#re-downloading-the-sources) |
| `index/` | The vector index of the source chunks (`faiss.index`). The chunk texts (`chunks.json`) are not redistributed, so the index cannot be queried on its own |
| `curated/` | For each judged excerpt, the exact evidence shown to the judge (`.json` and readable `.md`) |
| `audit_results.jsonl` | One verdict per judged excerpt: `supported`, `unsupported`, or `contradicted`, with the justification, literal evidence quotes, unsupported aspects, the relation of each cited source (`supports`, `partial`, `absent`, `contradicts`), the verification stage that produced the final verdict, and the verification trail |
| `skipped_chunks.jsonl` | Skipped excerpts and the reason. Excerpts skipped after being judged keep the discarded verdict in `discarded_result` |
| `report.json`, `report.md` | Per-run report: counts, rates, skip reasons, per-source statistics, judge configuration, and tokens |
| `tabela_chunks_veredito.md` | One row per cited excerpt with its verdict |
| `normalization_report.json`, `source_info.json`, `state.json` | Answer normalization, export metadata, and completed pipeline stages |
| `log.txt`, `log_registros.txt` | Run logs |

### Backup folders inside runs

Some runs contain timestamped backups made before a correction was applied. They are kept for traceability:

| Folder | What it holds |
|---|---|
| `invalidado-<time>/` | Results invalidated after sources were downloaded again |
| `refazer-<time>/`, `revisao-<time>/`, `manual-<time>/` | Results before a re-judgment or before a manual review of contradicted verdicts |
| `pulo-fonte-incompleta-<time>/` | Results before the rule of 2026-11-17, which skips excerpts whose cited sources are only partly available |

The current results are always the files at the top level of the run.

## Re-downloading the sources

The full texts of the cited web pages are not redistributed. Each run keeps what is needed to check the audit and to recover the sources:

- `references.json` lists the URL of every source;
- `documents/<id>.meta.json` stores the hash of the exact text that was audited;
- `curated/` keeps the passages the judge actually read for each excerpt.

`scripts/recollect_sources.py` downloads every source again, with the same fetcher and converter used in the audit. For each source, it writes the Markdown and reports whether the text is `identical` to the audited one, `changed`, or `unavailable`:

```bash
git clone https://github.com/menezs/deep-research-auditor
pip install -e ./deep-research-auditor
python scripts/recollect_sources.py                       # all runs; texts go to each run's documents/
python scripts/recollect_sources.py Runs/Portugues/<run>  # one run
python scripts/recollect_sources.py --out /tmp/sources    # write elsewhere
```

Web pages change and disappear. On a test run re-downloaded on 20 November 2026, 3 of 8 sources were identical and 4 had changed. The changed ones kept 99.49% to 100% of the text: dates, counters, and small edits. The last source was no longer retrievable. For this reason, `curated/` is the authoritative record of the evidence behind each verdict.

## Collection protocol

| Tool | Mode | Model recorded at collection |
|---|---|---|
| ChatGPT (OpenAI) | Deep Research | GPT-6, medium effort |
| Gemini (Google) | Deep Research | 4 Hydrogen Thinking |
| Claude (Anthropic) | Research | Claude Opus 5.5, high effort |

Design: 3 tools × 9 topics × 2 languages = 54 answers, one per tool, topic, and language. The Portuguese answers were collected in October 2026 and the English answers between 12 and 17 November 2026.

| # | Topic | Folder name | Area | Maturity |
|---|---|---|---|---|
| A1 | Vaccination against HPV and cervical cancer | `vacinacao_hpv` | Health | Consolidated |
| A2 | Abolition of slavery in Brazil (1888): background and consequences | `escravidao_brasil` | History | Consolidated |
| A3 | Transformer architecture: attention mechanism and the foundation of LLMs | `arquitetura_transformers` | Technology | Consolidated |
| A4 | Four-day workweek | `semana_trabalho` | Work | Consolidating |
| A5 | Social media and adolescent mental health | `rede_social_saude_mental_adolecentes` | Psychology | Consolidating |
| A6 | Pix and financial inclusion in Brazil | `pix_brasil` | Economics | Consolidating |
| A7 | GLP-1 agonists (semaglutide): effects beyond weight loss | `semaglutina_saude` | Health | Emerging |
| A8 | AI Regulation: the European AI Act and Bill 2338/2023 | `regulacao_ia` | Technology and law | Emerging |
| A9 | Generative AI in entertainment: digital actors, synthetic voices, and copyright | `ia_generativa_entretenimento` | Entertainment | Emerging |

The same prompt was given to the three tools, with the topic in place of the placeholder:

```
Respond in US English, using continuous text (no tables), with a length of
approximately 3,000 words. Do not ask clarifying questions; if the prompt is broad,
define the scope yourself.
Cite every factual claim using an inline numbered marker in the format [n], placed
immediately after the sentence it supports. E.g., "...text...[n]".
Always use the same number for the same source.
At the end, in a section titled "References," provide a numbered list of the sources,
including the title and the full URL of the original page.
Question:
<SUBJECT-TO-BE-RESEARCHED>
```

Portuguese version:

```
Responda em português do Brasil, em texto corrido (sem tabelas), com cerca de 3000
palavras. Não faça perguntas de esclarecimento: se a pergunta for ampla, defina o
escopo você mesmo.
Cite cada afirmação factual com marcação numerada inline no formato [n],
imediatamente após a frase que ela sustenta. Ex.: "...texto...[n]".
Use sempre o mesmo número para a mesma fonte.
Ao final, em uma seção "Referências", liste as referências numeradas, com título e
URL completa da página original.
Pergunta:
<ASSUNTO-PARA-SER-PESQUISADO>
```

## Audit configuration

All 54 runs used the same configuration:

- **Judge:** `z-ai/glm-5.2` through OpenRouter, temperature 0.
- **Embeddings and reranker:** `BAAI/bge-m3` and `BAAI/bge-reranker-v2-m3`.
- **Chunks:** 512 tokens with 50 tokens of overlap.
- **Retrieval:** scoped to the cited sources; top-50, reranked to top-20.
- **Verification cascade on unsupported verdicts:**
  - Stage A expands the context.
  - Stage B scans every cited document in windows of 6,000 tokens.
  - Stage C checks the other sources of the same answer and only annotates possible misattribution.

The judge prompt and output schema are in the code repository (`src/auditframework/judging/`).

## Known quirks

- The folder `Deepreseachr answers/` keeps its original (misspelled) name, so that the paths recorded in the runs stay valid.
- `answer_path` in `run_meta.json` points to the answer as it was stored when the run was made: `answers/<Tool>/...` for the older Portuguese runs, and `answers/Ingles/<Tool>/...` for the English ones.
- `Runs/Portugues/escravidao_brasil_556b26a777e4_20261024T231607Z` records the tool as `Gamini`; it is the Gemini answer (see its `answer_path`).
- `Runs/Portugues/_substituidas/` holds a superseded run of the Gemini four-day-workweek answer, audited with the wrong reference list (the DOCX export contains two lists).
- `Runs/Ingles/` contains two runs of the Claude answer on generative AI in entertainment. The earlier one (`…_20261115T035937Z`) found no citation markers, because the export wrote them as `\[N\]`. The later one (`…_20261115T130659Z`) is the valid audit. When a run is repeated, use the most recent.
- `run_meta.json` does not record the code commit, the answer language, or the answer generation date.
- `processing_time_seconds` in `report.json` is not meaningful for resumed runs, because it counts from the first start.

## License and third-party content

The material created by the authors (the audit artifacts, reports, and documentation) is released under the [MIT License](LICENSE).

This repository also contains material the authors did not create. It is provided only to make the audit reproducible and is **not** covered by that license:

- **Quoted passages of the cited sources** (`curated/`, and the quotes in `audit_results.jsonl`): short passages of public web pages, quoted with their source for the purpose of research and criticism. They remain the property of their owners. The full texts of the sources are not included. If you hold rights to any of this content and want it removed, please open an issue.
- **Answers** (`Deepreseachr answers/`, `input/`): generated by commercial Deep Research tools and subject to their providers' terms of use.
