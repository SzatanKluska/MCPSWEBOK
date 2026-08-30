# SWEBOK Guide v4.0 — mapa literatury

Wygenerowano: 2026-08-28. Źródło: `KnowledgeBasePipeline/RawMaterials/swebok/chapterN/swebok-v4-chN.pdf` (18 rozdziałów = 18 obszarów wiedzy).

Dokument odwzorowuje trzy warstwy powiązań SWEBOK → literatura:

1. **Bibliografia rozdziału** — sekcja `REFERENCES`, pozycje `[n]` / `[n*]`.
2. **Macierz tematów** — sekcja `MATRIX OF TOPICS VS. REFERENCE MATERIAL`: dla każdego podrozdziału wskazuje pozycję literatury **i miejsce w niej** (rozdział / sekcja / strony).
3. **Cytowania w treści** — odsyłacze `[n*, cXsY]` występujące w nagłówkach i akapitach rozdziału, przypisane do najbliższego podrozdziału. Uzupełniają macierz (m.in. o pozycje bez gwiazdki).

## Jak czytać lokalizatory

| Zapis w SWEBOK | Znaczenie | Przykład |
|---|---|---|
| `[n]` / `[n*]` | numer pozycji na liście `REFERENCES` danego rozdziału; gwiazdka oznacza **materiał rekomendowany** (kolumna macierzy tematów) | `[1*]` = Wiegers & Beatty, *Software Requirements* |
| `cN` | rozdział (*chapter*) N cytowanej pozycji | `c12` → rozdział 12 |
| `cN-M` | rozdziały od N do M | `c8-9` → rozdziały 8–9 |
| `sN.M` | sekcja (*section*) N.M | `s4.1.1` → sekcja 4.1.1 |
| `pN` | strona (*page*) N | `p9` → s. 9 |
| `ppN-M` | strony od N do M | `pp5-6` → s. 5–6 |
| `cNsM` | rozdział N, sekcja M | `c9s3` → rozdz. 9, sekcja 3 |
| `cNpM` / `cNppM-K` | rozdział N, strona/strony M(-K) | `c1pp5-6` → rozdz. 1, s. 5–6 |
| `App` / `Appendix X` | dodatek | `App A` → dodatek A |
| `Part IV` | część IV | |
| `X` lub `*` w komórce macierzy | pozycja dotyczy tematu jako całość (bez wskazania miejsca) | |
| `ff` | „i dalsze" (strony/rozdziały) | `p69ff` → od s. 69 dalej |

Lokalizatory odnoszą się do **numeracji cytowanej książki/artykułu**, nie do stron SWEBOK.


## Spis obszarów wiedzy

- [KA 01 — Software Requirements](#ka-01--software-requirements)
- [KA 02 — Software Architecture](#ka-02--software-architecture)
- [KA 03 — Software Design](#ka-03--software-design)
- [KA 04 — Software Construction](#ka-04--software-construction)
- [KA 05 — Software Testing](#ka-05--software-testing)
- [KA 06 — Software Engineering Operations](#ka-06--software-engineering-operations)
- [KA 07 — Software Maintenance](#ka-07--software-maintenance)
- [KA 08 — Software Configuration Management](#ka-08--software-configuration-management)
- [KA 09 — Software Engineering Management](#ka-09--software-engineering-management)
- [KA 10 — Software Engineering Process](#ka-10--software-engineering-process)
- [KA 11 — Software Engineering Models and Methods](#ka-11--software-engineering-models-and-methods)
- [KA 12 — Software Quality](#ka-12--software-quality)
- [KA 13 — Software Security](#ka-13--software-security)
- [KA 14 — Software Engineering Professional Practice](#ka-14--software-engineering-professional-practice)
- [KA 15 — Software Engineering Economics](#ka-15--software-engineering-economics)
- [KA 16 — Computing Foundations](#ka-16--computing-foundations)
- [KA 17 — Mathematical Foundations](#ka-17--mathematical-foundations)
- [KA 18 — Engineering Foundations](#ka-18--engineering-foundations)

---

## KA 01 — Software Requirements

Plik źródłowy: `chapter1/swebok-v4-ch1.pdf` · macierz tematów na stronach PDF: 21, 22

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | K. E. Wiegers and J. Beatty, Software Requirements, 3rd ed., Redmond, WA: Microsoft Press, 2013. |
| `[2*]` | ★ | I. Sommerville, Software Engineering, 10th ed., New York: Addison-Wesley, 2016. |
| `[3*]` | ★ | S. Tockey, Return on Software: Maximizing the Return on Your Software Investment, Boston, MA: Addison- Wesley, 2005. |
| `[4*]` | ★ | J. M. Wing, “A Specifier’s Introduction to Formal Methods,” Computer, vol. 23, no. 9, 1990, pp. 8, 10-23. |
| `[5]` |  | P. Laplante and M. Kassab, Requirements Engineering for Software and Systems, 4th ed., Boca Raton, FL: CRC Press, 2022. |
| `[6]` |  | S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right, Upper Saddle River, NJ: Addison- Wesley, 2013. |
| `[7]` |  | T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering, and Software Engineering Using Planguage, Oxford, UK: Elsevier Butterworth- Heinemann, 2005. |
| `[8]` |  | E. Yourdon, Modern Structured Analysis, Englewood Cliffs, NJ: Prentice- Hall, 1989. |
| `[9]` |  | S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019. |
| `[10]` |  | S. Ambler, Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process, Hoboken, NJ: Wiley, 2002. |
| `[11]` |  | A. Cockburn, Writing Effective Use Cases, Upper Saddle River, NJ: Addison-Wesley, 2000. |
| `[12]` |  | L. Constantine and L. Lockwood, Software for Use, Reading, MA: Addison-Wesley, 2000. |
| `[13]` |  | J. Wood and D. Silver, Joint Application Development, New York, NY: Wiley, 1995. |
| `[14]` |  | E. Gottesdiener, Requirements by Collaboration, Boston, MA: Addison- Wesley, 2002. |
| `[15]` |  | J. Terninko, Step by Step QFD, 2nd ed., Boca Raton, FL: CRC Press, 1997. |
| `[16]` |  | G. Salvendy, Handbook of Human Factors, 4th ed., Hoboken, NJ: Wiley, 2012. |
| `[17]` |  | T. Brown and B. Katz, Change by Design: How Design Thinking Transforms Organizations and Inspires Innovation, Revised and updated ed., New York, NY: Harper Collins, 2019. |
| `[18]` |  | S. McMenamin and J. Palmer, Essential Systems Analysis, New York, NY: Yourdon Press, 1984. |
| `[19]` |  | J. Smart, BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle, Shelter Island, NY: Manning Publications, 2015. |
| `[20]` |  | D. Weiss and C. Lai, Software Product- Line Engineering: A Family-Based Software Development Process, Reading, MA: Addison-Wesley, 1999. |
| `[21]` |  | K. Wiegers, Software Development Pearls: Lessons from Fifty Years of Software Experience, Boston, MA: Addison-Wesley Professional, 2021. |
| `[22]` |  | S. McConnell, Rapid Development, Redmond, WA: Microsoft Press, 1996. |
| `[23]` |  | O. Gotel and C. W. Finkelstein, “An Analysis of the Requirements Traceability Problem,” presented at the Proceedings of the 1st International Conference on Requirements Engineering, 1994. |
| `[24]` |  | INCOSE, Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities, 3.2.2 ed., San Diego, US: International Council on Systems Engineering, 2012. |
| `[25]` |  | R. Fisher and W. Ury, Getting to Yes, 3rd ed., New York, NY: Penguin, 2011. |
| `[26]` |  | ISO/IEC/IEEE 29148 “Systems and software engineering – Life cycle processes – Requirements engi- neering,” International Standards Organization, 2018. |
| `[27]` |  | ISO/IEC 25010: “System and software engineering – Systems and software Quality Requirements and Evaluation (SQuaRE) – System and software quality models,” International Standards Organization, 2011. |
| `[28]` |  | ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” 2nd ed. 2017. |
| `[29]` |  | N. Ahmad, Effects of Electronic Communication on the Elicitation of Tacit Knowledge in Interview Techniques for Small Software Developments, doctoral thesis, University of Huddersfield, 2021. |
| `[30]` |  | IIBA, A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide) v3, International Institute of Business Analysis, Toronto, Ontario, Canada, 2015. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Definition of a Software Requirement | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp5-6` | rozdz. 1, s. 5-6 |
| 1.1. Definition of a Software Requirement | `[2*]` I. Sommerville, Software Engineering | `c4p102` | rozdz. 4, s. 102 |
| 1.2. Categories of Software Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp7-12` | rozdz. 1, s. 7-12 |
| 1.2. Categories of Software Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1` | sekcja 4.1 |
| 1.3. Software Product Requirements and Software Project Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp14-15` | rozdz. 1, s. 14-15 |
| 1.4. Functional Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1p9` | rozdz. 1, s. 9 |
| 1.4. Functional Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1.1` | sekcja 4.1.1 |
| 1.5. Nonfunctional Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp10-11` | rozdz. 1, s. 10-11 |
| 1.5. Nonfunctional Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1.2` | sekcja 4.1.2 |
| 1.11. Software Requirements Activities | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp15-18` | rozdz. 1, s. 15-18 |
| 1.11. Software Requirements Activities | `[2*]` I. Sommerville, Software Engineering | `s4.2` | sekcja 4.2 |
| 2.1. Requirements Sources | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c6` | rozdz. 6 |
| 2.1. Requirements Sources | `[2*]` I. Sommerville, Software Engineering | `s4.3` | sekcja 4.3 |
| 2.2. Common Requirements Elicitation Techniques | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c7` | rozdz. 7 |
| 2.2. Common Requirements Elicitation Techniques | `[2*]` I. Sommerville, Software Engineering | `s4.3` | sekcja 4.3 |
| 3.1. Basic Requirements Analysis | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c8-9` | rozdz. 8-9 |
| 3.2. Economics of Quality of Service Constraints | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c1-27` | rozdz. 1-27 |
| 3.3. Formal Analysis | `[2*]` I. Sommerville, Software Engineering | `s12.3.2-12.3.3` | sekcja 12.3.2-12.3.3 |
| 4.1. Unstructured Natural Language Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c11` | rozdz. 11 |
| 4.1. Unstructured Natural Language Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s4.4.1` | sekcja 4.4.1 |
| 4.2. Structured Natural Language Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c8` | rozdz. 8 |
| 4.2. Structured Natural Language Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s4.4.2` | sekcja 4.4.2 |
| 4.3. Acceptance Criteria-Based Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s3.2.3`, `s8.2` | sekcja 3.2.3; sekcja 8.2 |
| 4.4. Model-Based Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c12` | rozdz. 12 |
| 4.4. Model-Based Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 |
| 4.4. Model-Based Requirements Specification | `[4*]` J. M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 |
| 4.5. Additional Attributes of Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c27pp462-463` | rozdz. 27, s. 462-463 |
| 5.1. Requirements Reviews | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c17pp332-342` | rozdz. 17, s. 332-342 |
| 5.1. Requirements Reviews | `[2*]` I. Sommerville, Software Engineering | `c4p130` | rozdz. 4, s. 130 |
| 5.3. Prototyping | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c17p342` | rozdz. 17, s. 342 |
| 5.3. Prototyping | `[2*]` I. Sommerville, Software Engineering | `c4p130` | rozdz. 4, s. 130 |
| 6.2. Requirements Change Control | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c28` | rozdz. 28 |
| 6.2. Requirements Change Control | `[2*]` I. Sommerville, Software Engineering | `s4.6` | sekcja 4.6 |
| 7.1. Iterative Nature of the Requirements Process | `[2*]` I. Sommerville, Software Engineering | `s4.2` | sekcja 4.2 |
| 7.2. Requirements Prioritization | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c16` | rozdz. 16 |
| 7.3. Requirements Tracing | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c29` | rozdz. 29 |
| 7.4. Requirements Stability and Volatility | `[2*]` I. Sommerville, Software Engineering | `s4.6` | sekcja 4.6 |
| 7.5. Measuring Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c19` | rozdz. 19 |
| 7.6. Requirements Process Quality and Improvement | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c31` | rozdz. 31 |
| 8.1. Requirements Management Tools | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c30pp506-510` | rozdz. 30, s. 506-510 |
| 8.2. Requirements Modeling Tools | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c30p506` | rozdz. 30, s. 506 |
| 8.2. Requirements Modeling Tools | `[2*]` I. Sommerville, Software Engineering | `s12.3.3` | sekcja 12.3.3 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (19)</summary>

- 1. Software Requirements Fundamentals
- 1.6. Technology Constraints
- 1.7. Quality of Service Constraints
- 1.8. Why Categorize Requirements This Way?
- 1.9. System Requirements and Software Requirements
- 1.10. Derived Requirements
- 2. Requirements Elicitation
- 3. Requirements Analysis
- 3.4. Addressing Conflict in Requirements
- 4. Requirements Specification
- 4.6. Incremental and Comprehensive Requirements Specification
- 5. Requirements Validation
- 5.2. Simulation and Execution
- 6. Requirements Management Activities
- 6.1. Requirements Scrubbing
- 6.3. Scope Matching
- 7. Practical Considerations
- 8. Software Requirements Tools
- 8.3. Functional Test Case Generation Tools

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Definition of a Software Requirement | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp5-6` | rozdz. 1, s. 5-6 | 2 |
| 1.1. Definition of a Software Requirement | `[2*]` I. Sommerville, Software Engineering | `c4p102` | rozdz. 4, s. 102 | 2 |
| 1.1. Definition of a Software Requirement | `[28]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 2 |
| 1.1. Definition of a Software Requirement | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 3 |
| 1.1. Definition of a Software Requirement | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c1` | rozdz. 1 | 3 |
| 1.1. Definition of a Software Requirement | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 3 |
| 1.2. Categories of Software Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp7-12` | rozdz. 1, s. 7-12 | 3 |
| 1.2. Categories of Software Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1` | sekcja 4.1 | 3 |
| 1.2. Categories of Software Requirements | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 3 |
| 1.2. Categories of Software Requirements | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c1` | rozdz. 1 | 3 |
| 1.2. Categories of Software Requirements | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 3 |
| 1.3. Software Product Requirements and Software Project Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp14-15` | rozdz. 1, s. 14-15 | 3 |
| 1.4. Functional Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1p9` | rozdz. 1, s. 9 | 4 |
| 1.4. Functional Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1.1` | sekcja 4.1.1 | 4 |
| 1.4. Functional Requirements | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 4 |
| 1.4. Functional Requirements | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c10` | rozdz. 10 | 4 |
| 1.4. Functional Requirements | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 4 |
| 1.5. Nonfunctional Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp10-11` | rozdz. 1, s. 10-11 | 4 |
| 1.5. Nonfunctional Requirements | `[2*]` I. Sommerville, Software Engineering | `s4.1.2` | sekcja 4.1.2 | 4 |
| 1.5. Nonfunctional Requirements | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 4 |
| 1.5. Nonfunctional Requirements | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c11` | rozdz. 11 | 4 |
| 1.5. Nonfunctional Requirements | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 4 |
| 1.6. Technology Constraints | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 4 |
| 1.7. Quality of Service Constraints | `[27]` ISO/IEC 25010: “System and software engineering – Systems and software Quality Requirements a… |  |  | 4 |
| 1.7. Quality of Service Constraints | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 4 |
| 1.7. Quality of Service Constraints | `[2*]` I. Sommerville, Software Engineering | `c13` | rozdz. 13 | 5 |
| 1.8. Why Categorize Requirements This Way? | `[18]` S. McMenamin and J. Palmer, Essential Systems Analysis, New York, NY: Yourdon Press | `c1-4` | rozdz. 1-4 | 5 |
| 1.8. Why Categorize Requirements This Way? | `[8]` E. Yourdon, Modern Structured Analysis, Englewood Cliffs, NJ: Prentice- Hall |  |  | 5 |
| 1.8. Why Categorize Requirements This Way? | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 5 |
| 1.8. Why Categorize Requirements This Way? | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c6` | rozdz. 6 | 5 |
| 1.9. System Requirements and Software Requirements | `[24]` INCOSE, Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities |  |  | 5 |
| 1.9. System Requirements and Software Requirements | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 5 |
| 1.10. Derived Requirements | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 6 |
| 1.11. Software Requirements Activities | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c1pp15-18` | rozdz. 1, s. 15-18 | 6 |
| 1.11. Software Requirements Activities | `[2*]` I. Sommerville, Software Engineering | `s4.2` | sekcja 4.2 | 6 |
| 1.11. Software Requirements Activities | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c1` | rozdz. 1 | 6 |
| 1.11. Software Requirements Activities | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right |  |  | 6 |
| 1.11. Software Requirements Activities | `[2*]` I. Sommerville, Software Engineering |  |  | 6 |
| 2. Requirements Elicitation | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c6-7` | rozdz. 6-7 | 6 |
| 2. Requirements Elicitation | `[2*]` I. Sommerville, Software Engineering | `s4.3` | sekcja 4.3 | 6 |
| 2. Requirements Elicitation | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c2-3` | rozdz. 2-3 | 6 |
| 2. Requirements Elicitation | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c3-7` | rozdz. 3-7 | 6 |
| 2.1. Requirements Sources | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c6` | rozdz. 6 | 6 |
| 2.1. Requirements Sources | `[2*]` I. Sommerville, Software Engineering | `s4.3` | sekcja 4.3 | 6 |
| 2.1. Requirements Sources | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c3` | rozdz. 3 | 7 |
| 2.1. Requirements Sources | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c3` | rozdz. 3 | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c7` | rozdz. 7 | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[2*]` I. Sommerville, Software Engineering | `s4.3` | sekcja 4.3 | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[13]` J. Wood and D. Silver, Joint Application Development, New York, NY: Wiley |  |  | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[14]` E. Gottesdiener, Requirements by Collaboration, Boston, MA: Addison- Wesley |  |  | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c15` | rozdz. 15 | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[15]` J. Terninko, Step by Step QFD |  |  | 7 |
| 2.2. Common Requirements Elicitation Techniques | `[16]` G. Salvendy, Handbook of Human Factors |  |  | 8 |
| 2.2. Common Requirements Elicitation Techniques | `[17]` T. Brown and B. Katz, Change by Design: How Design Thinking Transforms Organizations and Insp… |  |  | 8 |
| 2.2. Common Requirements Elicitation Techniques | `[27]` ISO/IEC 25010: “System and software engineering – Systems and software Quality Requirements a… |  |  | 8 |
| 2.2. Common Requirements Elicitation Techniques | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c3` | rozdz. 3 | 8 |
| 2.2. Common Requirements Elicitation Techniques | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c4-7` | rozdz. 4-7 | 8 |
| 3. Requirements Analysis | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c8-9` | rozdz. 8-9 | 8 |
| 3.1. Basic Requirements Analysis | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c8-9` | rozdz. 8-9 | 8 |
| 3.1. Basic Requirements Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4` | rozdz. 4 | 8 |
| 3.2. Economics of Quality of Service Constraints | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment |  |  | 8 |
| 3.2. Economics of Quality of Service Constraints | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 8 |
| 3.2. Economics of Quality of Service Constraints | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c14` | rozdz. 14 | 9 |
| 3.3. Formal Analysis | `[2*]` I. Sommerville, Software Engineering | `s12.3.2-12.3.3` | sekcja 12.3.2-12.3.3 | 9 |
| 3.3. Formal Analysis | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c6` | rozdz. 6 | 9 |
| 3.4. Addressing Conflict in Requirements | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c17` | rozdz. 17 | 10 |
| 3.4. Addressing Conflict in Requirements | `[25]` R. Fisher and W. Ury, Getting to Yes |  |  | 10 |
| 3.4. Addressing Conflict in Requirements | `[20]` D. Weiss and C. Lai, Software Product- Line Engineering: A Family-Based Software Development… |  |  | 10 |
| 4. Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c10-14`, `c20-26` | rozdz. 10-14; rozdz. 20-26 | 10 |
| 4. Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s4.4`, `c5` | sekcja 4.4; rozdz. 5 | 10 |
| 4. Requirements Specification | `[26]` ISO/IEC/IEEE 29148 “Systems and software engineering – Life cycle processes – Requirements en… |  |  | 11 |
| 4. Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c10-14` | rozdz. 10-14 | 11 |
| 4. Requirements Specification | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c4` | rozdz. 4 | 11 |
| 4. Requirements Specification | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c16` | rozdz. 16 | 11 |
| 4.1. Unstructured Natural Language Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c11` | rozdz. 11 | 11 |
| 4.1. Unstructured Natural Language Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s4.4.1` | sekcja 4.4.1 | 11 |
| 4.1. Unstructured Natural Language Requirements Specification | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c4` | rozdz. 4 | 12 |
| 4.1. Unstructured Natural Language Requirements Specification | `[26]` ISO/IEC/IEEE 29148 “Systems and software engineering – Life cycle processes – Requirements en… |  |  | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c8` | rozdz. 8 | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s4.4.2` | sekcja 4.4.2 | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[11]` A. Cockburn, Writing Effective Use Cases, Upper Saddle River, NJ: Addison-Wesley |  |  | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c4` | rozdz. 4 | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c12`, `c16` | rozdz. 12; rozdz. 16 | 12 |
| 4.2. Structured Natural Language Requirements Specification | `[7]` T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering | `c2-5` | rozdz. 2-5 | 12 |
| 4.3. Acceptance Criteria-Based Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `s3.2.3`, `s8.2` | sekcja 3.2.3; sekcja 8.2 | 12 |
| 4.3. Acceptance Criteria-Based Requirements Specification | `[19]` J. Smart, BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle |  |  | 13 |
| 4.3. Acceptance Criteria-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c1`, `c12` | rozdz. 1; rozdz. 12 | 14 |
| 4.4. Model-Based Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c12` | rozdz. 12 | 14 |
| 4.4. Model-Based Requirements Specification | `[2*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 | 14 |
| 4.4. Model-Based Requirements Specification | `[4*]` J. M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer |  |  | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c1-2` | rozdz. 1-2 | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c8` | rozdz. 8 | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c7` | rozdz. 7 | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c9` | rozdz. 9 | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c10` | rozdz. 10 | 14 |
| 4.4. Model-Based Requirements Specification | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c12-13` | rozdz. 12-13 | 14 |
| 4.4. Model-Based Requirements Specification | `[8]` E. Yourdon, Modern Structured Analysis, Englewood Cliffs, NJ: Prentice- Hall |  |  | 14 |
| 4.4. Model-Based Requirements Specification | `[10]` S. Ambler, Agile Modeling: Effective Practices for eXtreme Programming and the Unified Process |  |  | 14 |
| 4.4. Model-Based Requirements Specification | `[18]` S. McMenamin and J. Palmer, Essential Systems Analysis, New York, NY: Yourdon Press |  |  | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c6-12` | rozdz. 6-12 | 14 |
| 4.4. Model-Based Requirements Specification | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `Appendix L` | dodatek L | 14 |
| 4.4. Model-Based Requirements Specification | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c7` | rozdz. 7 | 14 |
| 4.5. Additional Attributes of Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c27pp462-463` | rozdz. 27, s. 462-463 | 14 |
| 4.5. Additional Attributes of Requirements | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c16` | rozdz. 16 | 15 |
| 4.5. Additional Attributes of Requirements | `[20]` D. Weiss and C. Lai, Software Product- Line Engineering: A Family-Based Software Development… |  |  | 15 |
| 4.5. Additional Attributes of Requirements | `[7]` T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering |  |  | 15 |
| 5. Requirements Validation | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c17` | rozdz. 17 | 15 |
| 5. Requirements Validation | `[2*]` I. Sommerville, Software Engineering | `s4.5` | sekcja 4.5 | 15 |
| 5. Requirements Validation | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c5` | rozdz. 5 | 15 |
| 5. Requirements Validation | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c17` | rozdz. 17 | 15 |
| 5. Requirements Validation | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c12` | rozdz. 12 | 15 |
| 5.1. Requirements Reviews | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c17pp332-342` | rozdz. 17, s. 332-342 | 15 |
| 5.1. Requirements Reviews | `[2*]` I. Sommerville, Software Engineering | `c4p130` | rozdz. 4, s. 130 | 15 |
| 5.2. Simulation and Execution | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c12` | rozdz. 12 | 16 |
| 5.3. Prototyping | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c17p342` | rozdz. 17, s. 342 | 16 |
| 5.3. Prototyping | `[2*]` I. Sommerville, Software Engineering | `c4p130` | rozdz. 4, s. 130 | 16 |
| 6. Requirements Management Activities | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c27-28` | rozdz. 27-28 | 16 |
| 6. Requirements Management Activities | `[2*]` I. Sommerville, Software Engineering | `s4.6` | sekcja 4.6 | 16 |
| 6. Requirements Management Activities | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c9` | rozdz. 9 | 16 |
| 6.1. Requirements Scrubbing | `[22]` S. McConnell, Rapid Development, Redmond, WA: Microsoft Press, 1996 | `c14`, `c32` | rozdz. 14; rozdz. 32 | 16 |
| 6.2. Requirements Change Control | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c28` | rozdz. 28 | 17 |
| 6.2. Requirements Change Control | `[2*]` I. Sommerville, Software Engineering | `s4.6` | sekcja 4.6 | 17 |
| 6.2. Requirements Change Control | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c9` | rozdz. 9 | 17 |
| 6.2. Requirements Change Control | `[22]` S. McConnell, Rapid Development, Redmond, WA: Microsoft Press, 1996 | `c17` | rozdz. 17 | 17 |
| 6.3. Scope Matching | `[22]` S. McConnell, Rapid Development, Redmond, WA: Microsoft Press, 1996 | `c14` | rozdz. 14 | 17 |
| 7.1. Iterative Nature of the Requirements Process | `[2*]` I. Sommerville, Software Engineering | `s4.2` | sekcja 4.2 | 17 |
| 7.1. Iterative Nature of the Requirements Process | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c2`, `c9` | rozdz. 2; rozdz. 9 | 17 |
| 7.2. Requirements Prioritization | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c16` | rozdz. 16 | 17 |
| 7.2. Requirements Prioritization | `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right | `c17` | rozdz. 17 | 18 |
| 7.3. Requirements Tracing | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c29` | rozdz. 29 | 18 |
| 7.3. Requirements Tracing | `[23]` O. Gotel and C. W. Finkelstein, “An Analysis of the Requirements Traceability Problem |  |  | 19 |
| 7.4. Requirements Stability and Volatility | `[2*]` I. Sommerville, Software Engineering | `s4.6` | sekcja 4.6 | 19 |
| 7.4. Requirements Stability and Volatility | `[20]` D. Weiss and C. Lai, Software Product- Line Engineering: A Family-Based Software Development… |  |  | 19 |
| 7.4. Requirements Stability and Volatility | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c4` | rozdz. 4 | 19 |
| 7.5. Measuring Requirements | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c19` | rozdz. 19 | 19 |
| 7.5. Measuring Requirements | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c23` | rozdz. 23 | 19 |
| 7.6. Requirements Process Quality and Improvement | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c31` | rozdz. 31 | 19 |
| 8. Software Requirements Tools | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c30` | rozdz. 30 | 20 |
| 8.1. Requirements Management Tools | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c30pp506-510` | rozdz. 30, s. 506-510 | 20 |
| 8.1. Requirements Management Tools | `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems | `c8` | rozdz. 8 | 20 |
| 8.2. Requirements Modeling Tools | `[1*]` K. E. Wiegers and J. Beatty, Software Requirements | `c30p506` | rozdz. 30, s. 506 | 20 |
| 8.2. Requirements Modeling Tools | `[2*]` I. Sommerville, Software Engineering | `s12.3.3` | sekcja 12.3.3 | 20 |
| 8.3. Functional Test Case Generation Tools | `[9]` S. Tockey, How to Engineer Software, Hoboken, NJ: Wiley, 2019 | `c12` | rozdz. 12 | 20 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[30]` IIBA, A Guide to the Business Analysis Body of Knowledge® (BABOK® Guide) v3, International Institute of Business Analysis, Toronto, Ontario, Canada, 2015.
- `[5]` P. Laplante and M. Kassab, Requirements Engineering for Software and Systems, 4th ed., Boca Raton, FL: CRC Press, 2022.
- `[1*]` K. E. Wiegers and J. Beatty, Software Requirements, 3rd ed., Redmond, WA: Microsoft Press, 2013.
- `[6]` S. Robertson and J. Robertson, Mastering the Requirements Process: Getting Requirements Right, Upper Saddle River, NJ: Addison- Wesley, 2013.
- `[7]` T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering, and Software Engineering Using Planguage, Oxford, UK: Elsevier Butterworth- Heinemann, 2005.
- `[21]` K. Wiegers, Software Development Pearls: Lessons from Fifty Years of Software Experience, Boston, MA: Addison-Wesley Professional, 2021.
- `[25]` R. Fisher and W. Ury, Getting to Yes, 3rd ed., New York, NY: Penguin, 2011.
- `[29]` N. Ahmad, Effects of Electronic Communication on the Elicitation of Tacit Knowledge in Interview Techniques for Small Software Developments, doctoral thesis, University of Huddersfield, 2021.

---

## KA 02 — Software Architecture

Plik źródłowy: `chapter2/swebok-v4-ch2.pdf` · macierz tematów na stronach PDF: 12, 13

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | M. Ali Babar, and I. Gorton, “Software Architecture Review: The State of the Practice”, IEEE Computer, July 2009. |
| `[2*]` | ★ | L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion, 2021. |
| `[3]` |  | L. Bass, J. Ivers, M.H. Klein, and P.Merson, Reasoning Frameworks, CMU/SEI-2005-TR-007, 2005. |
| `[4*]` | ★ | F. Brooks, The Design of Design, Addison-Wesley, 2010. |
| `[5]` |  | S. Brown, Software Architecture for Developers, 2018, http://leanpub.com/ software-architecture-for-developers. |
| `[6*]` | ★ | D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems, 3rd Edition, CRC Press, 2021. |
| `[7]` |  | F. Buschmann, R. Meunier, H. Rohnert, P. Sommerlad, and M. Stal, Pattern Oriented Software Architecture, John Wiley & Sons, 1996. |
| `[8]` |  | H. Cervantes, R Kazman, Designing Software Architectures: A Practical Approach, 2nd ed., Addison-Wesley, 2024. |
| `[9]` |  | P. Clements et al., Documenting Software Architecture: Views and Beyond, 2nd edi- tion Addison-Wesley, 2011. |
| `[10]` |  | P. Clements, R. Kazman, M. Klein, Evaluating Software Architectures, Addison-Wesley, 2001. |
| `[11]` |  | M.E. Conway, “How Do Committees Invent?” Datamation, 14(4), 28-31, 1968. |
| `[12]` |  | E.W. Dijkstra, “On the role of scientific thought”, 1974, available at https://www. cs.utexas.edu/users/EWD/transcriptions/ EWD04xx/EWD447.html. |
| `[13]` |  | T. Earl, SOA Design Patterns, Prentice-Hall, 2009 |
| `[14]` |  | P. Eeles, and P. Cripps, The Process of Software Architecting, Addison Wesley, 2010. |
| `[15]` |  | M. Erder, P. Pureur and E. Woods, Continuous Architecture in Practice: Software Architecture in the Age of Agility and DevOps, Addison-Wesley, 2021. |
| `[16]` |  | G. Fairbanks, Just Enough Software Architecture: A Risk-Driven Approach, Marshall & Brainerd, 2010. |
| `[17]` |  | E. Fernandez-Buglioni, Security Patterns in Practice: Designing Secure Architectures Using Software Patterns, Wiley, 2013. |
| `[18]` |  | R.T. Fielding and R.N. Taylor, Principled design of the modern web architecture, ACM Transactions on Internet Technology, 2(2), 115–150, 2002. |
| `[19]` |  | M. Fowler, D. Rice, M. Foemmel, E.Hieatt, R. Mee and R. Stafford, Patterns of Enterprise Application Architecture, Addison-Wesley, 2003. |
| `[20]` |  | C. Hofmeister, P.B. Kruchten, R.L. Nord, H. Obbink, A. Ran, and P. America, “A general model of soft- ware architecture design derived from five industrial approaches”, The Journal of Systems and Software, 80, 106–126, 2007. |
| `[21]` |  | C. Hofmeister, R.L. Nord, and D. Soni, Applied Software Architecture, Addison- Wesley, 2000. |
| `[22]` |  | ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, 2nd ed. 2017. |
| `[23]` |  | ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description. |
| `[24]` |  | R. Kazman, S. Haziyev, A. Yakuba, and D.A. Tamburri, Managing Energy Consumption as an Architectural Quality Attribute, IEEE Software, 35(5), 102–107, 2018 |
| `[25]` |  | P.B. Kruchten, The “4+1” View Model of Architecture, IEEE Software 12(6), 1995. |
| `[26]` |  | P.B. Kruchten, R.L. Nord, and I.Ozkaya, Managing Technical Debt: Reducing Friction in Software Development. Addison-Wesley, 2019. |
| `[27]` |  | Z. Li, P. Liang and P. Avgeriou, Architecture viewpoints for doc- umenting architectural technical debt. Software Quality Assurance, Elsevier, 2016. |
| `[28]` |  | Alan MacCormack, John Rusnak & Carliss Baldwin, Exploring the Duality between Product and Organizational Architectures: A Test of the ‘Mirroring’ Hypothesis. Research Policy, 41:1309–1324, 2012 |
| `[29*]` | ★ | M.W. Maier and E. Rechtin, The Art of Systems Architecting, 3rd edition, CRC Press, 2021. |
| `[30]` |  | N. Medvidović, D.S. Rosenblum, D.F. Redmiles and J.E. Robbins, Modeling software architectures in the Unified Modeling Language, ACM Transactions on Software Engineering and Methodology, 11(1), 2–57, 2002 |
| `[31]` |  | H. Obbink et al., Report on Software Architecture Review and Assessment (SARA), version 1.0, available at https:// philippe.kruchten.com/architecture/ SARAv1.pdf, 2002. |
| `[32]` |  | D.L. Parnas, “On the criteria to be used in decomposing systems into modules”, Communications of the ACM 15(12), 1053-1058, 1972. |
| `[33]` |  | D.L. Parnas and D.M. Weiss, “Active Design Reviews: Principles and Practices”, Proceedings of 8th International Conference on Software Engineering, 215-222, 1985. |
| `[34]` |  | D. Perry, A. Wolf, Foundations for the study of software architecture, ACM SIGSOFT Software Engineering Notes, 17(4), 40–52, 1992 |
| `[35]` |  | E. Poort, H. van Vliet, RCDA: Architecting as a Risk- and Cost Management Discipline, Journal of Systems and Software, https://www.cs.vu.nl/~hans/publications/y2012 /JSS-RCDA.pdf, 2012 |
| `[36]` |  | R. Prieto-Diaz and J.M. Neighbors, “Module Interconnection Languages”, Journal of Systems and Software, 6(4), 307–334, 1986. |
| `[37]` |  | C. Richardson, Microservices Patterns, Manning Publications, 2019 |
| `[38*]` | ★ | N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using Viewpoints and Perspectives, 2nd edition, Addison- Wesley, 2011. |
| `[39]` |  | M. Shaw and D. Garlan, Software Architecture: Perspectives on an Emerging Discipline, Prentice Hall, 1996. |
| `[40*]` | ★ | I. Sommerville, Software Engineering, 10th edition, 2016. |
| `[41*]` | ★ | R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations, Theory, and Practice, Wiley, 2009 |
| `[42]` |  | R. Weinreich and G. Buchgeher, Towards supporting the software archi- tecture life cycle, The Journal of Systems and Software, 85, 546–561, 2012. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. Software Architecture Fundamentals | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1` | rozdz. 1 |
| 1. Software Architecture Fundamentals | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `Appendix C` | dodatek C |
| 1. Software Architecture Fundamentals | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c2` | rozdz. 2 |
| 1. Software Architecture Fundamentals | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c1-3` | rozdz. 1-3 |
| 1.1. The Senses of “Architecture” | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c2` | rozdz. 2 |
| 1.1. The Senses of “Architecture” | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6.1` | rozdz. 6.1 |
| 1.1. The Senses of “Architecture” | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c6` | rozdz. 6 |
| 1.2. Stakeholders and Concerns | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c3-14` | rozdz. 3-14 |
| 1.2. Stakeholders and Concerns | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c8-9` | rozdz. 8-9 |
| 1.2. Stakeholders and Concerns | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c3` | rozdz. 3 |
| 1.3. Uses of Architecture | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c24` | rozdz. 24 |
| 1.3. Uses of Architecture | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c30` | rozdz. 30 |
| 2. Software Architecture Description | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1.2`, `22` | rozdz. 1.2 |
| 2. Software Architecture Description | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c12-13` | rozdz. 12-13 |
| 2. Software Architecture Description | `[40*]` I. Sommerville, Software Engineering | `c6` | rozdz. 6 |
| 2. Software Architecture Description | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c6-7` | rozdz. 6-7 |
| 2.1. Architecture Views and Viewpoints | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7-9` | rozdz. 7-9 |
| 2.1. Architecture Views and Viewpoints | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c8` | rozdz. 8 |
| 2.1. Architecture Views and Viewpoints | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c3` | rozdz. 3 |
| 2.1. Architecture Views and Viewpoints | `[40*]` I. Sommerville, Software Engineering | `c6.2` | rozdz. 6.2 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c2.12` | rozdz. 2.12 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6`, `15` | rozdz. 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c11` | rozdz. 11 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[40*]` I. Sommerville, Software Engineering | `c6.3` | rozdz. 6.3 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c11` | rozdz. 11 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c22` | rozdz. 22 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c11` | rozdz. 11 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `app` | dodatek |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c6-7` | rozdz. 6-7 |
| 2.4. Architecture as Significant Decisions | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c8` | rozdz. 8 |
| 2.4. Architecture as Significant Decisions | `[40*]` I. Sommerville, Software Engineering | `c6.1` | rozdz. 6.1 |
| 3. Software Architecture Process | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c12-13` | rozdz. 12-13 |
| 3. Software Architecture Process | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c6-7` | rozdz. 6-7 |
| 3. Software Architecture Process | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c4` | rozdz. 4 |
| 3.1. Architecture in Context | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c12-13` | rozdz. 12-13 |
| 3.1. Architecture in Context | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c2` | rozdz. 2 |
| 3.1.1. Relation of Architecture to Design | `[40*]` I. Sommerville, Software Engineering | `c6` | rozdz. 6 |
| 3.1.1. Relation of Architecture to Design | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c2` | rozdz. 2 |
| 3.2. Architectural Design | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c19-23` | rozdz. 19-23 |
| 3.2.1. Architecture Analysis | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c19` | rozdz. 19 |
| 3.2.1. Architecture Analysis | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c8` | rozdz. 8 |
| 3.2.2. Architecture Synthesis | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c20` | rozdz. 20 |
| 3.2.3. Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 |
| 3.2.3. Architecture Evaluation | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c14` | rozdz. 14 |
| 3.3. Architecture Practices, Methods, and Tactics | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c3.4` | rozdz. 3.4 |
| 3.3. Architecture Practices, Methods, and Tactics | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c10` | rozdz. 10 |
| 3.3. Architecture Practices, Methods, and Tactics | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c9-14` | rozdz. 9-14 |
| 3.4. Architecting in the Large | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c12`, `14` | rozdz. 12 |
| 3.4. Architecting in the Large | `[40*]` I. Sommerville, Software Engineering | `c19` | rozdz. 19 |
| 4. Software Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 |
| 4. Software Architecture Evaluation | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c14` | rozdz. 14 |
| 4. Software Architecture Evaluation | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c8` | rozdz. 8 |
| 4.1. “Goodness” in Architecture | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1.3`, `2` | rozdz. 1.3 |
| 4.1. “Goodness” in Architecture | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c17` | rozdz. 17 |
| 4.2. Reasoning about Architectures | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c10` | rozdz. 10 |
| 4.3 Architecture Reviews | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 |
| 4.4 Architecture Metrics | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c23` | rozdz. 23 |

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1. Software Architecture Fundamentals | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1` | rozdz. 1 | 1 |
| 1. Software Architecture Fundamentals | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `appendix C` | dodatek C | 1 |
| 1. Software Architecture Fundamentals | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c2` | rozdz. 2 | 1 |
| 1. Software Architecture Fundamentals | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c1-3` | rozdz. 1-3 | 1 |
| 1.1. The Senses of “Architecture” | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c2` | rozdz. 2 | 1 |
| 1.1. The Senses of “Architecture” | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6.1` | rozdz. 6.1 | 1 |
| 1.1. The Senses of “Architecture” | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c6` | rozdz. 6 | 1 |
| 1.1. The Senses of “Architecture” | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion |  |  | 2 |
| 1.1. The Senses of “Architecture” | `[23]` ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description |  |  | 2 |
| 1.2. Stakeholders and Concerns | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c3-14` | rozdz. 3-14 | 3 |
| 1.2. Stakeholders and Concerns | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c8-9` | rozdz. 8-9 | 3 |
| 1.2. Stakeholders and Concerns | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c3` | rozdz. 3 | 3 |
| 1.2. Stakeholders and Concerns | `[12]` E.W. Dijkstra, “On the role of scientific thought”, 1974, available at https://www. cs.utexas… |  |  | 3 |
| 1.2. Stakeholders and Concerns | `[24]` R. Kazman, S. Haziyev, A. Yakuba, and D.A. Tamburri, Managing Energy Consumption as an Archit… |  |  | 3 |
| 1.3. Uses of Architecture | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c24` | rozdz. 24 | 4 |
| 1.3. Uses of Architecture | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c30` | rozdz. 30 | 4 |
| 1.3. Uses of Architecture | `[11]` M.E. Conway, “How Do Committees Invent?” Datamation, 14(4), 28-31, 1968 |  |  | 4 |
| 1.3. Uses of Architecture | `[28]` Alan MacCormack, John Rusnak & Carliss Baldwin, Exploring the Duality between Product and Org… |  |  | 4 |
| 2. Software Architecture Description | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1.2` | rozdz. 1.2 | 4 |
| 2. Software Architecture Description | `[22]` ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 4 |
| 2. Software Architecture Description | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c12-13` | rozdz. 12-13 | 4 |
| 2. Software Architecture Description | `[40*]` I. Sommerville, Software Engineering | `c6` | rozdz. 6 | 4 |
| 2. Software Architecture Description | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c6-7` | rozdz. 6-7 | 4 |
| 2.1. Architecture Views and Viewpoints | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7-9` | rozdz. 7-9 | 5 |
| 2.1. Architecture Views and Viewpoints | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c8` | rozdz. 8 | 5 |
| 2.1. Architecture Views and Viewpoints | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c3` | rozdz. 3 | 5 |
| 2.1. Architecture Views and Viewpoints | `[40*]` I. Sommerville, Software Engineering | `c6.2` | rozdz. 6.2 | 5 |
| 2.1. Architecture Views and Viewpoints | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… |  |  | 5 |
| 2.1. Architecture Views and Viewpoints | `[23]` ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description |  |  | 5 |
| 2.1. Architecture Views and Viewpoints | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion |  |  | 5 |
| 2.1. Architecture Views and Viewpoints | `[25]` P.B. Kruchten, The “4+1” View Model of Architecture, IEEE Software 12(6) |  |  | 5 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[9]` P. Clements et al., Documenting Software Architecture: Views and Beyond, 2nd edi- tion Addiso… |  |  | 5 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[23]` ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description |  |  | 5 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[39]` M. Shaw and D. Garlan, Software Architecture: Perspectives on an Emerging Discipline |  |  | 6 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[25]` P.B. Kruchten, The “4+1” View Model of Architecture, IEEE Software 12(6) |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c2.12` | rozdz. 2.12 | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6` | rozdz. 6 | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[15]` M. Erder, P. Pureur and E. Woods, Continuous Architecture in Practice: Software Architecture… |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c11` | rozdz. 11 | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[40*]` I. Sommerville, Software Engineering | `c6.3` | rozdz. 6.3 | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c11` | rozdz. 11 | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[7]` F. Buschmann, R. Meunier, H. Rohnert, P. Sommerlad, and M. Stal, Pattern Oriented Software Ar… |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[39]` M. Shaw and D. Garlan, Software Architecture: Perspectives on an Emerging Discipline |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[19]` M. Fowler, D. Rice, M. Foemmel, E.Hieatt, R. Mee and R. Stafford, Patterns of Enterprise Appl… |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[13]` T. Earl, SOA Design Patterns, Prentice-Hall, 2009 |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[37]` C. Richardson, Microservices Patterns, Manning Publications, 2019 |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[17]` E. Fernandez-Buglioni, Security Patterns in Practice: Designing Secure Architectures Using So… |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… |  |  | 6 |
| 2.2. Architecture Patterns, Styles and Reference Architectures | `[23]` ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description |  |  | 6 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c22` | rozdz. 22 | 7 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c11` | rozdz. 11 | 7 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `app` | dodatek | 7 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c6-7` | rozdz. 6-7 | 7 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[36]` R. Prieto-Diaz and J.M. Neighbors, “Module Interconnection Languages”, Journal of Systems and… |  |  | 7 |
| 2.3. Architecture Description Languages and Architecture Frameworks | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations |  |  | 7 |
| 2.4. Architecture as Significant Decisions | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c8` | rozdz. 8 | 7 |
| 2.4. Architecture as Significant Decisions | `[40*]` I. Sommerville, Software Engineering | `c6.1` | rozdz. 6.1 | 7 |
| 2.4. Architecture as Significant Decisions | `[26]` P.B. Kruchten, R.L. Nord, and I.Ozkaya, Managing Technical Debt: Reducing Friction in Softwar… |  |  | 7 |
| 2.4. Architecture as Significant Decisions | `[27]` Z. Li, P. Liang and P. Avgeriou, Architecture viewpoints for doc- umenting architectural tech… |  |  | 8 |
| 3. Software Architecture Process | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c9` | rozdz. 9 | 8 |
| 3. Software Architecture Process | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c6-7` | rozdz. 6-7 | 8 |
| 3. Software Architecture Process | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c4` | rozdz. 4 | 8 |
| 3.1. Architecture in Context | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c12-13` | rozdz. 12-13 | 8 |
| 3.1. Architecture in Context | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c2` | rozdz. 2 | 8 |
| 3.1.1. Relation of Architecture to Design | `[40*]` I. Sommerville, Software Engineering | `c6` | rozdz. 6 | 9 |
| 3.1.1. Relation of Architecture to Design | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c2` | rozdz. 2 | 9 |
| 3.2. Architectural Design | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c19-23` | rozdz. 19-23 | 9 |
| 3.2. Architectural Design | `[20]` C. Hofmeister, P.B. Kruchten, R.L. Nord, H. Obbink, A. Ran, and P. America |  |  | 9 |
| 3.2.1. Architecture Analysis | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c19` | rozdz. 19 | 9 |
| 3.2.1. Architecture Analysis | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c8` | rozdz. 8 | 9 |
| 3.2.1. Architecture Analysis | `[31]` H. Obbink et al., Report on Software Architecture Review and Assessment (SARA) |  |  | 9 |
| 3.2.2. Architecture Synthesis | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c20` | rozdz. 20 | 9 |
| 3.2.3. Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 | 10 |
| 3.2.3. Architecture Evaluation | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c14` | rozdz. 14 | 10 |
| 3.3. Architecture Practices, Methods, and Tactics | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c3.4` | rozdz. 3.4 | 10 |
| 3.3. Architecture Practices, Methods, and Tactics | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c10` | rozdz. 10 | 10 |
| 3.3. Architecture Practices, Methods, and Tactics | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c9-14` | rozdz. 9-14 | 10 |
| 3.4. Architecting in the Large | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting | `c12` | rozdz. 12 | 10 |
| 3.4. Architecting in the Large | `[14]` P. Eeles, and P. Cripps, The Process of Software Architecting, Addison Wesley |  |  | 10 |
| 3.4. Architecting in the Large | `[40*]` I. Sommerville, Software Engineering | `c19` | rozdz. 19 | 10 |
| 3.4. Architecting in the Large | `[29*]` M.W. Maier and E. Rechtin, The Art of Systems Architecting |  |  | 10 |
| 3.4. Architecting in the Large | `[42]` R. Weinreich and G. Buchgeher, Towards supporting the software archi- tecture life cycle |  |  | 10 |
| 4. Software Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 | 10 |
| 4. Software Architecture Evaluation | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c14` | rozdz. 14 | 10 |
| 4. Software Architecture Evaluation | `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations | `c8` | rozdz. 8 | 10 |
| 4. Software Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c1.3` | rozdz. 1.3 | 10 |
| 4. Software Architecture Evaluation | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion |  |  | 10 |
| 4. Software Architecture Evaluation | `[6*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c17` | rozdz. 17 | 10 |
| 4. Software Architecture Evaluation | `[10]` P. Clements, R. Kazman, M. Klein, Evaluating Software Architectures, Addison-Wesley |  |  | 11 |
| 4. Software Architecture Evaluation | `[31]` H. Obbink et al., Report on Software Architecture Review and Assessment (SARA) |  |  | 11 |
| 4.2. Reasoning about Architectures | `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using View… | `c10` | rozdz. 10 | 11 |
| 4.2. Reasoning about Architectures | `[23]` ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description |  |  | 11 |
| 4.2. Reasoning about Architectures | `[3]` L. Bass, J. Ivers, M.H. Klein, and P.Merson, Reasoning Frameworks, CMU/SEI-2005-TR-007 |  |  | 11 |
| 4.3. Architecture Reviews | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c21` | rozdz. 21 | 11 |
| 4.3. Architecture Reviews | `[1]` M. Ali Babar, and I. Gorton, “Software Architecture Review: The State of the Practice” |  |  | 11 |
| 4.3. Architecture Reviews | `[33]` D.L. Parnas and D.M. Weiss, “Active Design Reviews: Principles and Practices” |  |  | 11 |
| 4.3. Architecture Reviews | `[31]` H. Obbink et al., Report on Software Architecture Review and Assessment (SARA) |  |  | 11 |
| 4.4. Architecture Metrics | `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion | `c23` | rozdz. 23 | 11 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[34]` D. Perry, A. Wolf, Foundations for the study of software architecture, ACM SIGSOFT Software Engineering Notes, 17(4), 40–52, 1992
- `[2*]` L. Bass, P. Clements, and R. Kazman, Software Architecture in Practice, 4th edi- tion, 2021.
- `[25]` P.B. Kruchten, The “4+1” View Model of Architecture, IEEE Software 12(6), 1995.
- `[38*]` N. Rozanski and E. Woods, Software Systems Architecture: Working with Stakeholders Using Viewpoints and Perspectives, 2nd edition, Addison- Wesley, 2011.
- `[41*]` R.N. Taylor, N. Medvidović, E. Dashofy, Software Architecture: Foundations, Theory, and Practice, Wiley, 2009
- `[9]` P. Clements et al., Documenting Software Architecture: Views and Beyond, 2nd edi- tion Addison-Wesley, 2011.
- `[5]` S. Brown, Software Architecture for Developers, 2018, http://leanpub.com/ software-architecture-for-developers.
- `[16]` G. Fairbanks, Just Enough Software Architecture: A Risk-Driven Approach, Marshall & Brainerd, 2010.
- `[15]` M. Erder, P. Pureur and E. Woods, Continuous Architecture in Practice: Software Architecture in the Age of Agility and DevOps, Addison-Wesley, 2021.

---

## KA 03 — Software Design

Plik źródłowy: `chapter3/swebok-v4-ch3.pdf` · macierz tematów na stronach PDF: 14, 15

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide, 2 edition, Addison- Wesley, 2005. |
| `[2]` |  | J. Bosch, Design and Use of Software Architectures: Adopting and Evolving a Product-Line Approach, ACM Press, 2000. |
| `[3*]` | ★ | F. Brooks, The Design of Design, Addison-Wesley, 2010. |
| `[4*]` | ★ | D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems, 3 Edition CRC Press, 2021. |
| `[5]` |  | E.W. Dijkstra, On the Role of Scientific Thought. 1974. http://www.cs.utexas.edu/users/EWD/transcriptions/ EWD04xx/EWD447.html. |
| `[6]` |  | M. Galster, D. Weyns, D. Tofan, B. Michalik, and P. Avgeriou, Variability in Software Systems — A Systematic Literature Review, IEEE Transactions on Software Engineering, 40(3), 2014. |
| `[7*]` | ★ | E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software, 1st ed, Addison- Wesley, 1994. |
| `[8]` |  | S. Gregor and D. Jones, The Anatomy of a Design Theory, Association for Information Systems, 2007. |
| `[9]` |  | IEEE Std 7000™-2021, IEEE Standard Model Process for Addressing Ethical Concerns during System Design. |
| `[10]` |  | ISO/IEC/IEEE 12207, Systems and Software Engineering — Software Life Cycle Processes. |
| `[11]` |  | ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, 2nd ed. 2017. |
| `[12]` |  | G. Kiczales et al., Aspect-Oriented Programming, Proc. 11th European Conf. Object-Oriented Programming (ECOOP 97), Springer, 1997. |
| `[13]` |  | T. Kosar, S. Bohra, M. Mernik, Domain-Specific Languages: A Systematic Mapping Study, Information and Software Technology, 71, 77-91, 2016. |
| `[14]` |  | D. Luckham, The Power of Events: an Introduction to Complex Event Processing, Addison-Wesley, 2002. |
| `[15]` |  | G. Mühl, L. Fiege, and P. Pietzuch, Distributed Event-Based Systems, Springer-Verlag, 2006. |
| `[16]` |  | J. Nielsen, Usability Engineering, Morgan Kaufman, 1994. |
| `[17]` |  | D.L. Parnas, On the Criteria To Be Used In Decomposing Systems Into Modules, Communications of the ACM 15(12), 1053–1058, 1972. |
| `[18]` |  | D.L. Parnas and P.C. Clements, A Rational Design Process: How and Why to fake it, IEEE Transactions on Software Engineering 12(2), 251– 257, 1986. |
| `[19]` |  | D.L. Parnas and D.M. Weiss, Active Design Reviews: Principles and Practices, Journal of Systems & Software 7, 259–265, 1987 |
| `[20]` |  | D.T. Ross, J.B. Goodenough, and A.Irvine, Software Engineering: Process, Principles, and Goals, IEEE Computer, May 1975. |
| `[21*]` | ★ | I. Sommerville, Software Engineering, 10 edition, Pearson, 2016. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. Software Design Fundamental | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c1-3` | rozdz. 1-3 |
| 1. Software Design Fundamental | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c1-2` | rozdz. 1-2 |
| 1.1. Design Thinking | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c1-3` | rozdz. 1-3 |
| 1.1. Design Thinking | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c1-2` | rozdz. 1-2 |
| 1.2. Context of Software Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13-14` | rozdz. 13-14 |
| 1.2. Context of Software Design | `[21*]` I. Sommerville, Software Engineering | `c19-20` | rozdz. 19-20 |
| 1.3. Key Issues in Software Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `p69ff` | s. 69, i dalsze |
| 1.3. Key Issues in Software Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c17.1.1` | rozdz. 17.1.1 |
| 1.3. Key Issues in Software Design | `[21*]` I. Sommerville, Software Engineering | `c6-7` | rozdz. 6-7 |
| 1.4. Software Design Principles | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c4.2` | rozdz. 4.2 |
| 2. Software Design Processes | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c3` | rozdz. 3 |
| 2. Software Design Processes | `[21*]` I. Sommerville, Software Engineering | `c2`, `c7` | rozdz. 2; rozdz. 7 |
| 2.1. High-Level Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c5` | rozdz. 5 |
| 2.1. High-Level Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6` | rozdz. 6 |
| 2.2. Detailed Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c14` | rozdz. 14 |
| 3. Software Design Qualities | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c4` | rozdz. 4 |
| 3.1. Concurrency | `[21*]` I. Sommerville, Software Engineering | `c17` | rozdz. 17 |
| 3.2. Control and Event Handling | `[21*]` I. Sommerville, Software Engineering | `c21` | rozdz. 21 |
| 3.3. Data Persistence | `[21*]` I. Sommerville, Software Engineering | `c6`, `c16` | rozdz. 6; rozdz. 16 |
| 3.4. Distribution of Components | `[21*]` I. Sommerville, Software Engineering | `c17` | rozdz. 17 |
| 3.5. Errors and Exception Handling Fault Tolerance | `[21*]` I. Sommerville, Software Engineering | `c11` | rozdz. 11 |
| 3.6. Integration and Interoperability | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c11`, `c14`, `c16` | rozdz. 11; rozdz. 14; rozdz. 16 |
| 3.7. Assurance, Security and Safety | `[21*]` I. Sommerville, Software Engineering | `c10-14` | rozdz. 10-14 |
| 4. Recording Software Designs | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c1-3` | rozdz. 1-3 |
| 4. Recording Software Designs | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7-8` | rozdz. 7-8 |
| 4.1. Model-Based Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7.3` | rozdz. 7.3 |
| 4.1. Model-Based Design | `[21*]` I. Sommerville, Software Engineering | `c5.5` | rozdz. 5.5 |
| 4.2. Structural Design Descriptions | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c4-14` | rozdz. 4-14 |
| 4.2. Structural Design Descriptions | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7`, `c10` | rozdz. 7; rozdz. 10 |
| 4.2. Structural Design Descriptions | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c4` | rozdz. 4 |
| 4.2. Structural Design Descriptions | `[21*]` I. Sommerville, Software Engineering | `c5.3` | rozdz. 5.3 |
| 4.3. Behavioral Design Descriptions | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c15-24` | rozdz. 15-24 |
| 4.3. Behavioral Design Descriptions | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9-10` | rozdz. 9-10 |
| 4.3. Behavioral Design Descriptions | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c5` | rozdz. 5 |
| 4.3. Behavioral Design Descriptions | `[21*]` I. Sommerville, Software Engineering | `c5.4` | rozdz. 5.4 |
| 4.4. Design Patterns and Styles | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c12` | rozdz. 12 |
| 4.4. Design Patterns and Styles | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c15` | rozdz. 15 |
| 4.4. Design Patterns and Styles | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c1-2` | rozdz. 1-2 |
| 4.4. Design Patterns and Styles | `[21*]` I. Sommerville, Software Engineering | `c7.2` | rozdz. 7.2 |
| 4.5. Specialized and Domain- Specific Languages | `[21*]` I. Sommerville, Software Engineering | `c15` | rozdz. 15 |
| 4.6. Design Rationale | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c16` | rozdz. 16 |
| 4.6. Design Rationale | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c12` | rozdz. 12 |
| 4.6. Design Rationale | `[21*]` I. Sommerville, Software Engineering | `c6.1` | rozdz. 6.1 |
| 5. Software Design Strategies and Methods | `[21*]` I. Sommerville, Software Engineering | `c3` | rozdz. 3 |
| 5.1. General Strategies | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13` | rozdz. 13 |
| 5.2. Function-Oriented (or Structured) Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9` | rozdz. 9 |
| 5.3. Data Centered Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9` | rozdz. 9 |
| 5.3. Data Centered Design | `[21*]` I. Sommerville, Software Engineering | `c5.4.1` | rozdz. 5.4.1 |
| 5.4. Object-Oriented Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c10` | rozdz. 10 |
| 5.5 User-Centered Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c9` | rozdz. 9 |
| 5.6. Component-Based Design | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c25`, `c29` | rozdz. 25; rozdz. 29 |
| 5.6. Component-Based Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c11`, `c16` | rozdz. 11; rozdz. 16 |
| 5.6. Component-Based Design | `[21*]` I. Sommerville, Software Engineering | `c16` | rozdz. 16 |
| 5.7. Event-Driven Design | `[21*]` I. Sommerville, Software Engineering | `c5.4.2` | rozdz. 5.4.2 |
| 5.8. Aspect-Oriented Design | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c10` | rozdz. 10 |
| 5.8. Aspect-Oriented Design | `[21*]` I. Sommerville, Software Engineering | `c31` | rozdz. 31 |
| 5.9. Constraint-Based Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c11` | rozdz. 11 |
| 5.10. Domain-Driven Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13.6.2`, `c18.3` | rozdz. 13.6.2; rozdz. 18.3 |
| 5.11. Other Methods | `[21*]` I. Sommerville, Software Engineering | `c18-21` | rozdz. 18-21 |
| 6. Software Design Quality Analysis and Evaluation | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7` | rozdz. 7 |
| 6. Software Design Quality Analysis and Evaluation | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 |
| 6.1. Design Reviews and Audits | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c5.3` | rozdz. 5.3 |
| 6.2. Quality Attributes | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 |
| 6.3. Quality Analysis and Evaluation Techniques | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 |
| 6.4. Measures and Metrics | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c5`, `c17` | rozdz. 5; rozdz. 17 |
| 6.4. Measures and Metrics | `[21*]` I. Sommerville, Software Engineering | `c24.5` | rozdz. 24.5 |
| 6.5. Verification, Validation and Certification | `[21*]` I. Sommerville, Software Engineering | `c7-8` | rozdz. 7-8 |

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[11]` ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 1 |
| 1. Software Design Fundamental | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 |  |  | 2 |
| 1. Software Design Fundamental | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems |  |  | 2 |
| 1.1. Design Thinking | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c1-3` | rozdz. 1-3 | 2 |
| 1.1. Design Thinking | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c1-2` | rozdz. 1-2 | 2 |
| 1.1. Design Thinking | `[20]` D.T. Ross, J.B. Goodenough, and A.Irvine, Software Engineering: Process, Principles |  |  | 2 |
| 1.1. Design Thinking | `[8]` S. Gregor and D. Jones, The Anatomy of a Design Theory, Association for Information Systems |  |  | 2 |
| 1.2. Context of Software Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13-14` | rozdz. 13-14 | 2 |
| 1.2. Context of Software Design | `[21*]` I. Sommerville, Software Engineering | `c19-20` | rozdz. 19-20 | 2 |
| 1.3. Key Issues in Software Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `p69ff` | s. 69, i dalsze | 3 |
| 1.3. Key Issues in Software Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c17.1.1` | rozdz. 17.1.1 | 3 |
| 1.3. Key Issues in Software Design | `[21*]` I. Sommerville, Software Engineering | `c6-7` | rozdz. 6-7 | 3 |
| 5. Software Design Strategies and Methods | `[2]` J. Bosch, Design and Use of Software Architectures: Adopting and Evolving a Product-Line Appr… |  |  | 3 |
| 5. Software Design Strategies and Methods | `[12]` G. Kiczales et al., Aspect-Oriented Programming, Proc. 11th European Conf. Object-Oriented Pr… |  |  | 3 |
| 1.4. Software Design Principles | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c4.2` | rozdz. 4.2 | 3 |
| 1.4. Software Design Principles | `[11]` ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 3 |
| 1.4. Software Design Principles | `[20]` D.T. Ross, J.B. Goodenough, and A.Irvine, Software Engineering: Process, Principles |  |  | 4 |
| 1.4. Software Design Principles | `[5]` E.W. Dijkstra, On the Role of Scientific Thought. 1974. http://www.cs.utexas.edu/users/EWD/tr… |  |  | 4 |
| 1.4. Software Design Principles | `[17]` D.L. Parnas, On the Criteria To Be Used In Decomposing Systems Into Modules |  |  | 4 |
| 1.4. Software Design Principles | `[9]` IEEE Std 7000™-2021, IEEE Standard Model Process for Addressing Ethical Concerns during Syste… |  |  | 5 |
| 2. Software Design Processes | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c3` | rozdz. 3 | 5 |
| 2.1. High-Level Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c5` | rozdz. 5 | 6 |
| 2.1. High-Level Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c6` | rozdz. 6 | 6 |
| 2.2. Detailed Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c14` | rozdz. 14 | 6 |
| 3. Software Design Qualities | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c4` | rozdz. 4 | 6 |
| 3.1. Concurrency | `[21*]` I. Sommerville, Software Engineering | `c17` | rozdz. 17 | 6 |
| 3.2. Control and Event Handling | `[21*]` I. Sommerville, Software Engineering | `c21` | rozdz. 21 | 6 |
| 3.3. Data Persistence | `[21*]` I. Sommerville, Software Engineering | `c6`, `c16` | rozdz. 6; rozdz. 16 | 7 |
| 3.4. Distribution of Components | `[21*]` I. Sommerville, Software Engineering | `c17` | rozdz. 17 | 7 |
| 3.5. Errors and Exception Handling Fault Tolerance | `[21*]` I. Sommerville, Software Engineering | `c11` | rozdz. 11 | 7 |
| 3.6. Integration and Interoperability | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c11`, `c14`, `c16` | rozdz. 11; rozdz. 14; rozdz. 16 | 7 |
| 3.7. Assurance, Security and Safety | `[21*]` I. Sommerville, Software Engineering | `c10-14` | rozdz. 10-14 | 7 |
| 3.7. Assurance, Security and Safety | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software |  |  | 7 |
| 3.7. Assurance, Security and Safety | `[6]` M. Galster, D. Weyns, D. Tofan, B. Michalik, and P. Avgeriou, Variability in Software Systems… |  |  | 7 |
| 4. Recording Software Designs | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide |  |  | 7 |
| 4.1. Model-Based Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7.3` | rozdz. 7.3 | 8 |
| 4.1. Model-Based Design | `[21*]` I. Sommerville, Software Engineering | `c5.5` | rozdz. 5.5 | 8 |
| 4.2. Structural Design Descriptions | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c4-14` | rozdz. 4-14 | 9 |
| 4.2. Structural Design Descriptions | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7`, `c10` | rozdz. 7; rozdz. 10 | 9 |
| 4.2. Structural Design Descriptions | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c4` | rozdz. 4 | 9 |
| 4.2. Structural Design Descriptions | `[21*]` I. Sommerville, Software Engineering | `c5.3` | rozdz. 5.3 | 9 |
| 4.3. Behavioral Design Descriptions | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c15-24` | rozdz. 15-24 | 9 |
| 4.3. Behavioral Design Descriptions | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9-10` | rozdz. 9-10 | 9 |
| 4.3. Behavioral Design Descriptions | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c5` | rozdz. 5 | 9 |
| 4.3. Behavioral Design Descriptions | `[21*]` I. Sommerville, Software Engineering | `c5.4` | rozdz. 5.4 | 9 |
| 4.3. Behavioral Design Descriptions | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems |  |  | 10 |
| 4.4. Design Patterns and Styles | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c12` | rozdz. 12 | 10 |
| 4.4. Design Patterns and Styles | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c15` | rozdz. 15 | 10 |
| 4.4. Design Patterns and Styles | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software | `c1-2` | rozdz. 1-2 | 10 |
| 4.4. Design Patterns and Styles | `[21*]` I. Sommerville, Software Engineering | `c7.2` | rozdz. 7.2 | 10 |
| 4.4. Design Patterns and Styles | `[7*]` E. Gamma et al., Design Patterns: Elements of Reusable Object- Oriented Software |  |  | 10 |
| 4.5. Specialized and Domain- Specific Languages | `[21*]` I. Sommerville, Software Engineering | `c15` | rozdz. 15 | 10 |
| 4.5. Specialized and Domain- Specific Languages | `[21*]` I. Sommerville, Software Engineering |  |  | 10 |
| 4.6. Design Rationale | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c16` | rozdz. 16 | 11 |
| 4.6. Design Rationale | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c12` | rozdz. 12 | 11 |
| 4.6. Design Rationale | `[21*]` I. Sommerville, Software Engineering | `c6.1` | rozdz. 6.1 | 11 |
| 5. Software Design Strategies and Methods | `[21*]` I. Sommerville, Software Engineering | `c3` | rozdz. 3 | 11 |
| 5.1. General Strategies | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13` | rozdz. 13 | 11 |
| 5.2. Function-Oriented (or Structured) Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9` | rozdz. 9 | 11 |
| 5.3. Data Centered Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9` | rozdz. 9 | 11 |
| 5.3. Data Centered Design | `[21*]` I. Sommerville, Software Engineering | `c5.4.1` | rozdz. 5.4.1 | 11 |
| 5.4. Object-Oriented Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c10` | rozdz. 10 | 11 |
| 5.5. User-Centered Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c9` | rozdz. 9 | 12 |
| 5.5. User-Centered Design | `[16]` J. Nielsen, Usability Engineering, Morgan Kaufman, 1994 |  |  | 12 |
| 5.6. Component-Based Design | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c25`, `c29` | rozdz. 25; rozdz. 29 | 12 |
| 5.6. Component-Based Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c11`, `c16` | rozdz. 11; rozdz. 16 | 12 |
| 5.6. Component-Based Design | `[21*]` I. Sommerville, Software Engineering | `c16` | rozdz. 16 | 12 |
| 5.7. Event-Driven Design | `[21*]` I. Sommerville, Software Engineering | `c5.4.2` | rozdz. 5.4.2 | 12 |
| 5.7. Event-Driven Design | `[15]` G. Mühl, L. Fiege, and P. Pietzuch, Distributed Event-Based Systems, Springer-Verlag |  |  | 12 |
| 5.7. Event-Driven Design | `[14]` D. Luckham, The Power of Events: an Introduction to Complex Event Processing |  |  | 12 |
| 5.8. Aspect-Oriented Design | `[1*]` G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide | `c10` | rozdz. 10 | 12 |
| 5.8. Aspect-Oriented Design | `[21*]` I. Sommerville, Software Engineering | `c31` | rozdz. 31 | 12 |
| 5.8. Aspect-Oriented Design | `[12]` G. Kiczales et al., Aspect-Oriented Programming, Proc. 11th European Conf. Object-Oriented Pr… |  |  | 12 |
| 5.9. Constraint-Based Design | `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010 | `c11` | rozdz. 11 | 12 |
| 5.10. Domain-Driven Design | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13.6.2`, `c18.3` | rozdz. 13.6.2; rozdz. 18.3 | 13 |
| 5.11. Other Methods | `[21*]` I. Sommerville, Software Engineering | `c18-c21` | rozdz. 18-21 | 13 |
| 6. Software Design Quality Analysis and Evaluation | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7` | rozdz. 7 | 13 |
| 6. Software Design Quality Analysis and Evaluation | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 | 13 |
| 6.1. Design Reviews and Audits | `[4*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c5.3` | rozdz. 5.3 | 13 |
| 6.2. Quality Attributes | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 | 13 |
| 6.3. Quality Analysis and Evaluation Techniques | `[21*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 | 13 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[3*]` F. Brooks, The Design of Design, Addison-Wesley, 2010.

---

## KA 04 — Software Construction

Plik źródłowy: `chapter4/swebok-v4-ch4.pdf` · macierz tematów na stronach PDF: 15, 16, 17

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | S. McConnell, Code Complete, 2nd edition, Redmond, WA: Microsoft Press, 2004. |
| `[2]` |  | I. Sommerville, Software Engineering, 10th edition, Addison-Wesley, 2016. |
| `[3]` |  | G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security in Technology Organizations, 2nd edition, IT Revolution, 2021. |
| `[4]` |  | H. Heitkötter, S. Hanschke, and T.A. Majchrzak, Evaluating Cross-Platform Development Approaches for Mobile Applications, 2013, in Cordeiro, J., Krempels, K.H. (eds.), Web Information Systems and Technologies. WEBIST 2012. Lecture Notes in Business Information Processing, vol. 140, Springer, Berlin, Heidelberg. |
| `[5]` |  | P. Clements et al., Documenting Software Architectures: Views and Beyond, 2nd edi- tion, Boston: Pearson Education, 2010. |
| `[6]` |  | E. Gamma et al., Design Patterns: Elements of Reusable Object-Oriented Software, 1st edition, Reading, MA: Addison-Wesley Professional, 1994. |
| `[7]` |  | S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture, 1st edition, Boston: Addison-Wesley, 2002. |
| `[8*]` | ★ | L. Null and J. Lobur, The Essentials of Computer Organization and Architecture, 5th ed., Jones and Bartlett Publishers, 2018. |
| `[9]` |  | A. Silberschatz et al., Operating System Concepts, 8th edition, Hoboken, NJ: Wiley, 2008. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Minimizing Complexity | `[1]` S. McConnell, Code Complete | `c2`, `c3`, `c7-c9`, `c24`, `c27`, `c28`, `c31`, `c32`, `c34` | rozdz. 2; rozdz. 3; rozdz. 7-9; rozdz. 24; rozdz. 27; rozdz. 28; rozdz. 31; rozdz. 32; rozdz. 34 |
| 1.2. Anticipating and Embracing Change | `[1]` S. McConnell, Code Complete | `c3-c5`, `c24`, `c31`, `c32`, `c34` | rozdz. 3-5; rozdz. 24; rozdz. 31; rozdz. 32; rozdz. 34 |
| 1.2. Anticipating and Embracing Change | `[2]` I. Sommerville, Software Engineering | `c1`, `c3`, `c9` | rozdz. 1; rozdz. 3; rozdz. 9 |
| 1.2. Anticipating and Embracing Change | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c1` | rozdz. 1 |
| 1.3. Constructing for Verification | `[1]` S. McConnell, Code Complete | `c8`, `c20-c23`, `c31`, `c34` | rozdz. 8; rozdz. 20-23; rozdz. 31; rozdz. 34 |
| 1.4. Reuse | `[2]` I. Sommerville, Software Engineering | `c15` | rozdz. 15 |
| 1.5. Standards in Construction | `[1]` S. McConnell, Code Complete | `c4` | rozdz. 4 |
| 2.1. Construction in Life Cycle Models | `[1]` S. McConnell, Code Complete | `c2`, `c3`, `c27`, `c29` | rozdz. 2; rozdz. 3; rozdz. 27; rozdz. 29 |
| 2.1. Construction in Life Cycle Models | `[2]` I. Sommerville, Software Engineering | `c3`, `c7` | rozdz. 3; rozdz. 7 |
| 2.1. Construction in Life Cycle Models | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c1` | rozdz. 1 |
| 2.2. Construction Planning | `[1]` S. McConnell, Code Complete | `c3`, `c4`, `c21`, `c27-c29` | rozdz. 3; rozdz. 4; rozdz. 21; rozdz. 27-29 |
| 2.3. Construction Measurement | `[1]` S. McConnell, Code Complete | `c25`, `c28` | rozdz. 25; rozdz. 28 |
| 2.4. Managing Dependencies | `[2]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 |
| 3.1. Construction Design | `[1]` S. McConnell, Code Complete | `c3`, `c5`, `c24` | rozdz. 3; rozdz. 5; rozdz. 24 |
| 3.1. Construction Design | `[2]` I. Sommerville, Software Engineering | `c7` | rozdz. 7 |
| 3.2. Construction Languages | `[1]` S. McConnell, Code Complete | `c4` | rozdz. 4 |
| 3.3. Coding | `[1]` S. McConnell, Code Complete | `c5-c19`, `c25-c26` | rozdz. 5-19; rozdz. 25-26 |
| 3.4. Construction Testing | `[1]` S. McConnell, Code Complete | `c22`, `c23` | rozdz. 22; rozdz. 23 |
| 3.4. Construction Testing | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 3.5. Reuse in Construction | `[2]` I. Sommerville, Software Engineering | `c15`, `c16` | rozdz. 15; rozdz. 16 |
| 3.6. Construction Quality | `[1]` S. McConnell, Code Complete | `c8`, `c20-c25` | rozdz. 8; rozdz. 20-25 |
| 3.6. Construction Quality | `[2]` I. Sommerville, Software Engineering | `c8`, `c24` | rozdz. 8; rozdz. 24 |
| 3.7. Integration | `[1]` S. McConnell, Code Complete | `c29` | rozdz. 29 |
| 3.7. Integration | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 3.7. Integration | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c11` | rozdz. 11 |
| 3.8. Cross-Platform Development and Migration | `[4]` H. Heitkötter, S. Hanschke, and T.A. Majchrzak, Evaluating Cross-Platform Development Approac… | `c` |  |
| 4.1. API Design and Use | `[5]` P. Clements et al., Documenting Software Architectures: Views and Beyond | `c7` | rozdz. 7 |
| 4.2. Object-Oriented Runtime Issues | `[1]` S. McConnell, Code Complete | `c6`, `c7` | rozdz. 6; rozdz. 7 |
| 4.3. Parameterization, Templates and Generics | `[6]` E. Gamma et al., Design Patterns: Elements of Reusable Object-Oriented Software | `c1` | rozdz. 1 |
| 4.4. Assertions, Design by Contract and Defensive Programming | `[1]` S. McConnell, Code Complete | `c8`, `c9` | rozdz. 8; rozdz. 9 |
| 4.5. Error Handling, Exception Handling and Fault Tolerance | `[1]` S. McConnell, Code Complete | `c3`, `c8` | rozdz. 3; rozdz. 8 |
| 4.7. State-Based and Table-Driven Construction Techniques | `[1]` S. McConnell, Code Complete | `c18` | rozdz. 18 |
| 4.8. Runtime Configuration and Internationalization | `[1]` S. McConnell, Code Complete | `c3`, `c10` | rozdz. 3; rozdz. 10 |
| 4.9. Grammar-Based Input Processing | `[1]` S. McConnell, Code Complete | `c5` | rozdz. 5 |
| 4.9. Grammar-Based Input Processing | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c8` | rozdz. 8 |
| 4.10. Concurrency Primitives | `[9]` A. Silberschatz et al., Operating System Concepts | `c6` | rozdz. 6 |
| 4.11. Middleware | `[5]` P. Clements et al., Documenting Software Architectures: Views and Beyond | `c1` | rozdz. 1 |
| 4.11. Middleware | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c8` | rozdz. 8 |
| 4.12. Construction Methods for Distributed and Cloud-Based Software | `[2]` I. Sommerville, Software Engineering | `c17`, `c18` | rozdz. 17; rozdz. 18 |
| 4.12. Construction Methods for Distributed and Cloud-Based Software | `[9]` A. Silberschatz et al., Operating System Concepts | `c2` | rozdz. 2 |
| 4.13. Constructing Heterogeneous Systems | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c9` | rozdz. 9 |
| 4.14. Performance Analysis and Tuning | `[1]` S. McConnell, Code Complete | `c25`, `c26` | rozdz. 25; rozdz. 26 |
| 4.15. Platform Standards | `[4]` H. Heitkötter, S. Hanschke, and T.A. Majchrzak, Evaluating Cross-Platform Development Approac… | `c` |  |
| 4.15. Platform Standards | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c10` | rozdz. 10 |
| 4.15. Platform Standards | `[9]` A. Silberschatz et al., Operating System Concepts | `c1` | rozdz. 1 |
| 4.16. Test-First Programming | `[1]` S. McConnell, Code Complete | `c22` | rozdz. 22 |
| 4.16. Test-First Programming | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 4.17. Feedback Loop for Construction | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c3`, `c16` | rozdz. 3; rozdz. 16 |
| 5.1. Development Environments | `[1]` S. McConnell, Code Complete | `c30` | rozdz. 30 |
| 5.2. Visual Programming and Low-Code/Zero- Code Platforms | `[1]` S. McConnell, Code Complete | `c30` | rozdz. 30 |
| 5.3. Unit Testing Tools | `[1]` S. McConnell, Code Complete | `c22` | rozdz. 22 |
| 5.3. Unit Testing Tools | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 5.4. Profiling, Performance Analysis and Slicing Tools | `[1]` S. McConnell, Code Complete | `c25`, `c26` | rozdz. 25; rozdz. 26 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (6)</summary>

- 1. Software Construction Fundamentals
- 2. Managing Construction
- 3. Practical Considerations
- 4. Construction Technologies
- 4.6. Executable Models
- 5. Software Construction Tools

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Minimizing Complexity | `[1]` S. McConnell, Code Complete | `c2`, `c3`, `c7-9`, `c24`, `c27`, `c28`, `c3` | rozdz. 2; rozdz. 3; rozdz. 7-9; rozdz. 24; rozdz. 27; rozdz. 28; rozdz. 3 | 2 |
| 1.1. Minimizing Complexity | `[1]` S. McConnell, Code Complete | `c32`, `c34` | rozdz. 32; rozdz. 34 | 2 |
| 1.2. Anticipating and Embracing Change | `[1]` S. McConnell, Code Complete | `c3-c5`, `c24`, `c31`, `c32`, `c34` | rozdz. 3-5; rozdz. 24; rozdz. 31; rozdz. 32; rozdz. 34 | 2 |
| 1.2. Anticipating and Embracing Change | `[2]` I. Sommerville, Software Engineering | `c1`, `c3`, `c9` | rozdz. 1; rozdz. 3; rozdz. 9 | 2 |
| 1.2. Anticipating and Embracing Change | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c1` | rozdz. 1 | 2 |
| 1.3. Constructing for Verification | `[1]` S. McConnell, Code Complete | `c8`, `c20-c23`, `c31`, `c34` | rozdz. 8; rozdz. 20-23; rozdz. 31; rozdz. 34 | 4 |
| 1.3. Constructing for Verification | `[2]` I. Sommerville, Software Engineering | `c15` | rozdz. 15 | 4 |
| 1.3. Constructing for Verification | `[1]` S. McConnell, Code Complete | `c4` | rozdz. 4 | 4 |
| 2.1. Construction in Life Cycle Models | `[1]` S. McConnell, Code Complete | `c2`, `c3`, `c27`, `c29` | rozdz. 2; rozdz. 3; rozdz. 27; rozdz. 29 | 4 |
| 2.1. Construction in Life Cycle Models | `[2]` I. Sommerville, Software Engineering | `c3`, `c7` | rozdz. 3; rozdz. 7 | 4 |
| 2.1. Construction in Life Cycle Models | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c1` | rozdz. 1 | 4 |
| 2.2. Construction Planning | `[1]` S. McConnell, Code Complete | `c3`, `c4`, `c21`, `c27-c29` | rozdz. 3; rozdz. 4; rozdz. 21; rozdz. 27-29 | 5 |
| 2.3. Construction Measurement | `[1]` S. McConnell, Code Complete | `c25`, `c28` | rozdz. 25; rozdz. 28 | 5 |
| 2.4. Managing Dependencies | `[2]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 | 5 |
| 3.1. Construction Design | `[1]` S. McConnell, Code Complete | `c3`, `c5`, `c24` | rozdz. 3; rozdz. 5; rozdz. 24 | 6 |
| 3.1. Construction Design | `[2]` I. Sommerville, Software Engineering | `c7` | rozdz. 7 | 6 |
| 3.2. Construction Languages | `[1]` S. McConnell, Code Complete | `c4` | rozdz. 4 | 6 |
| 3.3. Coding | `[1]` S. McConnell, Code Complete | `c5-c19`, `c25-c26` | rozdz. 5-19; rozdz. 25-26 | 7 |
| 3.4. Construction Testing | `[1]` S. McConnell, Code Complete | `c22`, `c23` | rozdz. 22; rozdz. 23 | 7 |
| 3.4. Construction Testing | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 7 |
| 3.5. Reuse in Construction | `[2]` I. Sommerville, Software Engineering | `c15`, `c16` | rozdz. 15; rozdz. 16 | 8 |
| 3.6. Construction Quality | `[1]` S. McConnell, Code Complete | `c8`, `c20-c25` | rozdz. 8; rozdz. 20-25 | 8 |
| 3.6. Construction Quality | `[2]` I. Sommerville, Software Engineering | `c8`, `c24` | rozdz. 8; rozdz. 24 | 8 |
| 3.7. Integration | `[1]` S. McConnell, Code Complete | `c29` | rozdz. 29 | 9 |
| 3.7. Integration | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 9 |
| 3.7. Integration | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c11` | rozdz. 11 | 9 |
| 3.8. Cross-Platform Development and Migration | `[4]` H. Heitkötter, S. Hanschke, and T.A. Majchrzak, Evaluating Cross-Platform Development Approac… | `c` |  | 9 |
| 4.1. API Design and Use | `[5]` P. Clements et al., Documenting Software Architectures: Views and Beyond | `c7` | rozdz. 7 | 10 |
| 4.2. Object-Oriented Runtime Issues | `[1]` S. McConnell, Code Complete | `c6`, `c7` | rozdz. 6; rozdz. 7 | 10 |
| 4.3. Parameterization, Templates and Generics | `[6]` E. Gamma et al., Design Patterns: Elements of Reusable Object-Oriented Software | `c1` | rozdz. 1 | 10 |
| 4.4. Assertions, Design by Contract and Defensive Programming | `[1]` S. McConnell, Code Complete | `c8`, `c9` | rozdz. 8; rozdz. 9 | 10 |
| 4.5. Error Handling, Exception Handling and Fault Tolerance | `[1]` S. McConnell, Code Complete | `c8`, `c9` | rozdz. 8; rozdz. 9 | 11 |
| 4.6. Executable Models | `[7]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture |  |  | 11 |
| 4.7. State-Based and Table-Driven Construction Techniques | `[1]` S. McConnell, Code Complete | `c18` | rozdz. 18 | 11 |
| 4.8. Runtime Configuration and Internationalization | `[1]` S. McConnell, Code Complete | `c3`, `c10` | rozdz. 3; rozdz. 10 | 12 |
| 4.9. Grammar-Based Input Processing | `[1]` S. McConnell, Code Complete |  |  | 12 |
| 4.9. Grammar-Based Input Processing | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture |  |  | 12 |
| 4.10. Concurrency Primitives | `[9]` A. Silberschatz et al., Operating System Concepts | `c6` | rozdz. 6 | 12 |
| 4.11. Middleware | `[5]` P. Clements et al., Documenting Software Architectures: Views and Beyond | `c1` | rozdz. 1 | 12 |
| 4.11. Middleware | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c8` | rozdz. 8 | 12 |
| 4.12. Construction Methods for Distributed and Cloud-Based Software | `[2]` I. Sommerville, Software Engineering | `c17`, `c18` | rozdz. 17; rozdz. 18 | 13 |
| 4.12. Construction Methods for Distributed and Cloud-Based Software | `[9]` A. Silberschatz et al., Operating System Concepts | `c2` | rozdz. 2 | 13 |
| 4.13. Constructing Heterogeneous Systems | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c9` | rozdz. 9 | 13 |
| 4.14. Performance Analysis and Tuning | `[1]` S. McConnell, Code Complete | `c25`, `c26` | rozdz. 25; rozdz. 26 | 13 |
| 4.15. Platform Standards | `[4]` H. Heitkötter, S. Hanschke, and T.A. Majchrzak, Evaluating Cross-Platform Development Approac… | `c` |  | 13 |
| 4.15. Platform Standards | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c10` | rozdz. 10 | 13 |
| 4.15. Platform Standards | `[9]` A. Silberschatz et al., Operating System Concepts | `c1` | rozdz. 1 | 13 |
| 4.16. Test-First Programming | `[1]` S. McConnell, Code Complete | `c22` | rozdz. 22 | 14 |
| 4.16. Test-First Programming | `[2]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 14 |
| 4.17. Feedback Loop for Construction | `[3]` G. Kim et al., The DevOps Handbook: How to Create World-Class Agility, Reliability & Security… | `c3`, `c16` | rozdz. 3; rozdz. 16 | 14 |
| 5.1. Development Environments | `[1]` S. McConnell, Code Complete | `c30` | rozdz. 30 | 14 |
| 5.2. Visual Programming and Low-Code/Zero- Code Platforms | `[1]` S. McConnell, Code Complete | `c30` | rozdz. 30 | 14 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture, 5th ed., Jones and Bartlett Publishers, 2018.
- `[9]` A. Silberschatz et al., Operating System Concepts, 8th edition, Hoboken, NJ: Wiley, 2008.

---

## KA 05 — Software Testing

Plik źródłowy: `chapter5/swebok-v4-ch5.pdf` · macierz tematów na stronach PDF: 30, 31, 32, 33

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice, 1st ed: Wiley, 2008. |
| `[2*]` | ★ | I. Sommerville, Software Engineering, 10th ed., Addison-Wesley, 2016. |
| `[3]` |  | E.W. Dijkstra, Notes on Structured Programming, Technological University, Eindhoven, 1970. |
| `[4]` |  | ISO/IEC/IEEE 29119 — System and software engineering — Software testing, ed. 2022. |
| `[5]` |  | “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” 2nd ed. 2017. |
| `[6]` |  | M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. Le Traon, and M. Harman, Chapter Six — Mutation Testing Advances: An Analysis and Survey, Advances in Computers, 112, 2019: 275-378. |
| `[7]` |  | M. Utting, B. Legeard, F. Bouquet, E. Fourneret, F. Peureux, and A. Vernotte, Recent advances in model-based testing, Advances in Computers, 101, 2016, pp. 53-120. |
| `[8]` |  | IEEE Std 1012-2016, IEEE Standard for System, Software, and Hardware Verification, and Validation, ed. 2016. |
| `[9]` |  | ISO/IEC 25010:2011, Systems and software engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) — System and Software Quality Models, ed. 2011. |
| `[10]` |  | ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure systems including application build, package and deployment. |
| `[11]` |  | Software Engineering Competency Model (SWECOM), v1.0, 2014. |
| `[12]` |  | ISO/IEC 20246:2017, “Software and systems engineering — Work product reviews”, 2017. |
| `[13]` |  | V. Riccio, G. Jahangirova, A. Stocco, et al., Testing machine learning based sys- tems: A systematic mapping, Empirical Software Engineering, 25, 2020, pp. 5193-5254. |
| `[14*]` | ★ | C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press, 1st ed., 2018. |
| `[15]` |  | S. Demi, R. Colomo-Palacios, and M. Sánchez-Gordón, Software Engineering Applications Enabled by Blockchain Technology: A Systematic Mapping Study, Applied Sciences, 11(7), 2021, pp. 2960. |
| `[16]` |  | K. Mao, L. Capra, M. Harman, and Y. Jia. A survey of the use of crowd- sourcing in software engineering, Journal of Systems and Software, 126, 2017, pp. 57-84. |
| `[17]` |  | A. Bertolino, G.D. Angelis, M. Gallego, B. García, F. Gortázar, F. Lonetti, and E. Marchetti, A system- atic review on cloud testing, ACM Computing Surveys (CSUR), 52(5), 2019, pp. 1-42. |
| `[18]` |  | R. Achary and P. Raj, Cloud Reliability Engineering: Technologies and Tools, CRC Press, 2021. |
| `[19*]` | ★ | J. Nielsen, Usability Engineering, 1st ed., Boston: Morgan Kaufmann, 1993. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. Software Testing Fundamentals | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1`, `c2` | rozdz. 1; rozdz. 2 |
| 1. Software Testing Fundamentals | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 1. Software Testing Fundamentals | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 1.1. Faults vs. Failures | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s5` | rozdz. 1, sekcja 5 |
| 1.1. Faults vs. Failures | `[2*]` I. Sommerville, Software Engineering | `c1` | rozdz. 1 |
| 1.1. Faults vs. Failures | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c1s3` | rozdz. 1, sekcja 3 |
| 1.2.1. Test Case Creation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s3` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 3 |
| 1.2.1. Test Case Creation | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 1.2.2. Test Selection and Adequacy Criteria | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s14`, `c6s6`, `c12s7` | rozdz. 1, sekcja 14; rozdz. 6, sekcja 6; rozdz. 12, sekcja 7 |
| 1.2.2. Test Selection and Adequacy Criteria | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 1.2.4. Purpose of Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s11`, `c11s4` | rozdz. 13, sekcja 11; rozdz. 11, sekcja 4 |
| 1.2.4. Purpose of Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 1.2.5. Assessment and Certification | `[2*]` I. Sommerville, Software Engineering | `c7`, `c25` | rozdz. 7; rozdz. 25 |
| 1.2.6. Testing for Quality Improvement/Assurance | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16s2` | rozdz. 16, sekcja 2 |
| 1.2.7. The Oracle Problem | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s9`, `c9s7` | rozdz. 1, sekcja 9; rozdz. 9, sekcja 7 |
| 1.2.8. Theoretical and Practical Limitations | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c2s7` | rozdz. 2, sekcja 7 |
| 1.2.9. The Problem of Infeasible Paths | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4s7` | rozdz. 4, sekcja 7 |
| 1.2.10. Testability | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c17s2` | rozdz. 17, sekcja 2 |
| 1.2.12. Scalability | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s7` | rozdz. 8, sekcja 7 |
| 1.2.13. Test Effectiveness | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s1` | rozdz. 1, sekcja 1 |
| 1.2.13. Test Effectiveness | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 |
| 1.2.14. Controllability, Replication and Generalization | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s12` | rozdz. 12, sekcja 12 |
| 2. Test Levels | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s13` | rozdz. 1, sekcja 13 |
| 2. Test Levels | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 |
| 2.1. The Target of the Test | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s13` | rozdz. 1, sekcja 13 |
| 2.1. The Target of the Test | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 |
| 2.1.1. Unit Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3` | rozdz. 3 |
| 2.1.1. Unit Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 2.1.2. Integration Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c7` | rozdz. 7 |
| 2.1.2. Integration Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 2.1.3. System Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8` | rozdz. 8 |
| 2.1.3. System Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 2.1.4. Acceptance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 |
| 2.1.4. Acceptance Testing | `[2*]` I. Sommerville, Software Engineering | `c8s4` | rozdz. 8, sekcja 4 |
| 2.2. Objectives of Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 |
| 2.2.1. Conformance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s4` | rozdz. 10, sekcja 4 |
| 2.2.2. Compliance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s3` | rozdz. 12, sekcja 3 |
| 2.2.3. Installation Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s2` | rozdz. 12, sekcja 2 |
| 2.2.4. Alpha and Beta Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s7`, `c16s6` | rozdz. 13, sekcja 7; rozdz. 16, sekcja 6 |
| 2.2.4. Alpha and Beta Testing | `[2*]` I. Sommerville, Software Engineering | `c8s4` | rozdz. 8, sekcja 4 |
| 2.2.5. Regression Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s11`, `c13s3` | rozdz. 8, sekcja 11; rozdz. 13, sekcja 3 |
| 2.2.6. Prioritization Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s7` | rozdz. 12, sekcja 7 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s7`, `c8s8`, `c14s2`, `c15`, `c17s2` | rozdz. 8, sekcja 7; rozdz. 8, sekcja 8; rozdz. 14, sekcja 2; rozdz. 15; rozdz. 17, sekcja 2 |
| 2.2.7. Non-functional testing | `[2*]` I. Sommerville, Software Engineering | `c8`, `c 11`, `c17` | rozdz. 8; rozdz. 11; rozdz. 17 |
| 2.2.8. Security Testing | `[2*]` I. Sommerville, Software Engineering | `c13` | rozdz. 13 |
| 2.2.9. Privacy Testing | `[2*]` I. Sommerville, Software Engineering | `c13`, `c14` | rozdz. 13; rozdz. 14 |
| 2.2.10. Interface and API Testing | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 |
| 2.2.10. Interface and API Testing | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s12` | rozdz. 7, sekcja 12 |
| 2.2.11. Configuration Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s5` | rozdz. 8, sekcja 5 |
| 2.2.12. Usability and Human-Computer Interaction Testing | `[2*]` I. Sommerville, Software Engineering | `c8s4` | rozdz. 8, sekcja 4 |
| 2.2.12. Usability and Human-Computer Interaction Testing | `[19*]` J. Nielsen, Usability Engineering | `c6` | rozdz. 6 |
| 3. Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s15` | rozdz. 1, sekcja 15 |
| 3.1. Specification-Based Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c6s2` | rozdz. 6, sekcja 2 |
| 3.1.1. Equivalence Partitioning | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s4` | rozdz. 9, sekcja 4 |
| 3.1.2. Boundary Value Analysis | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s5` | rozdz. 9, sekcja 5 |
| 3.1.3. Syntax Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s11` | rozdz. 10, sekcja 11 |
| 3.1.3. Syntax Testing | `[2*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 |
| 3.1.4. Combinatorial Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s3` | rozdz. 9, sekcja 3 |
| 3.1.5. Decision Table | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s6`, `c13s6` | rozdz. 9, sekcja 6; rozdz. 13, sekcja 6 |
| 3.1.6. Cause-Effect Graphing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s6` | rozdz. 1, sekcja 6 |
| 3.1.7. State Transition Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10` | rozdz. 10 |
| 3.1.8. Scenario Testing | `[2*]` I. Sommerville, Software Engineering | `c8s3.2`, `c19s3.1` | rozdz. 8, sekcja 3.2; rozdz. 19, sekcja 3.1 |
| 3.1.9. Random Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s7` | rozdz. 9, sekcja 7 |
| 3.2.1. Control Flow Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4` | rozdz. 4 |
| 3.2.2. Data Flow Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c5` | rozdz. 5 |
| 3.2.3. Reference Models for Structure-Based Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4` | rozdz. 4 |
| 3.3.1. Error Guessing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s8` | rozdz. 9, sekcja 8 |
| 3.4. Fault-Based and Mutation Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s14`, `c3s5` | rozdz. 1, sekcja 14; rozdz. 3, sekcja 5 |
| 3.5. Usage-Based Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15s5` | rozdz. 15, sekcja 5 |
| 3.5.1. Operational Profile | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15s5` | rozdz. 15, sekcja 5 |
| 3.5.1. Operational Profile | `[2*]` I. Sommerville, Software Engineering | `c11` | rozdz. 11 |
| 3.5.2. User Observation Heuristics | `[19*]` J. Nielsen, Usability Engineering | `c5`, `c7` | rozdz. 5; rozdz. 7 |
| 3.6. Techniques Based on the Nature of the Application | `[2*]` I. Sommerville, Software Engineering | `c16`, `c17`, `c18`, `c20`, `c21` | rozdz. 16; rozdz. 17; rozdz. 18; rozdz. 20; rozdz. 21 |
| 3.6. Techniques Based on the Nature of the Application | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4s8` | rozdz. 4, sekcja 8 |
| 3.7. Selecting and Combining Techniques | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s12` | rozdz. 7, sekcja 12 |
| 3.7.1. Combining Functional and Structural | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9` | rozdz. 9 |
| 3.7.2. Deterministic vs. Random | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s6` | rozdz. 9, sekcja 6 |
| 3.8. Techniques Based on Derived Knowledge | `[2*]` I. Sommerville, Software Engineering | `c19`, `c20` | rozdz. 19; rozdz. 20 |
| 3.8. Techniques Based on Derived Knowledge | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 4. Test-Related Measures | `[2*]` I. Sommerville, Software Engineering | `c24s5` | rozdz. 24, sekcja 5 |
| 4. Test-Related Measures | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10` | rozdz. 10 |
| 4.1. Evaluation of the SUT | `[2*]` I. Sommerville, Software Engineering | `c24s5` | rozdz. 24, sekcja 5 |
| 4.1.1. SUT Measurements That Aid in Planning and Designing Tests | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10` | rozdz. 10 |
| 4.1.2. Fault Types, Classification and Statistics | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s4`, `c13s5`, `c13s6` | rozdz. 13, sekcja 4; rozdz. 13, sekcja 5; rozdz. 13, sekcja 6 |
| 4.1.3. Fault Density | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s4` | rozdz. 13, sekcja 4 |
| 4.1.3. Fault Density | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10s1` | rozdz. 10, sekcja 1 |
| 4.1.4. Life Test, Reliability Evaluation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15` | rozdz. 15 |
| 4.1.4. Life Test, Reliability Evaluation | `[2*]` I. Sommerville, Software Engineering | `c11` | rozdz. 11 |
| 4.1.4. Life Test, Reliability Evaluation | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c1s3` | rozdz. 1, sekcja 3 |
| 4.1.5. Reliability Growth Models | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15` | rozdz. 15 |
| 4.1.5. Reliability Growth Models | `[2*]` I. Sommerville, Software Engineering | `c11s5` | rozdz. 11, sekcja 5 |
| 4.2.1. Fault Injection | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c2s5` | rozdz. 2, sekcja 5 |
| 4.2.2. Mutation Score | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3s5` | rozdz. 3, sekcja 5 |
| 4.2.3. Comparison and Relative Effectiveness of Different Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 |
| 5. Test Process | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 5.1.1. Attitudes/Egoless Programming | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16` | rozdz. 16 |
| 5.1.1. Attitudes/Egoless Programming | `[2*]` I. Sommerville, Software Engineering | `c3` | rozdz. 3 |
| 5.1.2. Test Guides and Organizational Process | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1` | rozdz. 12, sekcja 1 |
| 5.1.2. Test Guides and Organizational Process | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 5.1.2. Test Guides and Organizational Process | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s3` | rozdz. 7, sekcja 3 |
| 5.1.3. Test Management and Dynamic Test Processes | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12` | rozdz. 12 |
| 5.1.3. Test Management and Dynamic Test Processes | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s3` | rozdz. 7, sekcja 3 |
| 5.1.4. Test Documentation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s12` | rozdz. 8, sekcja 12 |
| 5.1.4. Test Documentation | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s8` | rozdz. 7, sekcja 8 |
| 5.1.5. Test Team | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16` | rozdz. 16 |
| 5.1.5. Test Team | `[2*]` I. Sommerville, Software Engineering | `c23s5` | rozdz. 23, sekcja 5 |
| 5.1.6. Test Process Measures | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c18s3` | rozdz. 18, sekcja 3 |
| 5.1.6. Test Process Measures | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10` | rozdz. 10 |
| 5.1.8. Test Completion | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s11` | rozdz. 7, sekcja 11 |
| 5.1.9. Test Reusability | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c3` | rozdz. 3 |
| 5.2. Test Sub-Processes and Activities | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s9`, `c1s12` | rozdz. 12, sekcja 9; rozdz. 1, sekcja 12 |
| 5.2.1. Test Planning Process | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s8` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 8 |
| 5.2.2. Test Design and Implementation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s3` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 3 |
| 5.2.3. Test Environment Set-up and Maintenance | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s6` | rozdz. 12, sekcja 6 |
| 5.2.3. Test Environment Set-up and Maintenance | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 |
| 5.2.3. Test Environment Set-up and Maintenance | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c13s2` | rozdz. 13, sekcja 2 |
| 5.2.4. Controlled Experiments and Test Execution | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s7` | rozdz. 12, sekcja 7 |
| 5.2.4. Controlled Experiments and Test Execution | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4s7`, `c5s6` | rozdz. 4, sekcja 7; rozdz. 5, sekcja 6 |
| 5.2.5. Test Incident Reporting | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s4`, `c13s9`, `c13s11` | rozdz. 13, sekcja 4; rozdz. 13, sekcja 9; rozdz. 13, sekcja 11 |
| 5.2.5. Test Incident Reporting | `[2*]` I. Sommerville, Software Engineering | `c8s3` | rozdz. 8, sekcja 3 |
| 5.2.5. Test Incident Reporting | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s8` | rozdz. 7, sekcja 8 |
| 5.3. Staffing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16` | rozdz. 16 |
| 6. Software Testing in the Development Processes and the Application Domains | `[2*]` I. Sommerville, Software Engineering | `c8`, `c15` | rozdz. 8; rozdz. 15 |
| 6. Software Testing in the Development Processes and the Application Domains | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4s8`, `c7` | rozdz. 4, sekcja 8; rozdz. 7 |
| 6.1. Testing Inside Software Development Processes | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 |
| 6.1. Testing Inside Software Development Processes | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 6.1.1. Testing in Traditional Processes | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c18` | rozdz. 18 |
| 6.1.1. Testing in Traditional Processes | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 6.1.2. Testing in Line with Shift- Left Movement | `[2*]` I. Sommerville, Software Engineering | `c3`, `c8s2` | rozdz. 3; rozdz. 8, sekcja 2 |
| 6.2. Testing in the Application Domains | `[2*]` I. Sommerville, Software Engineering | `c15` | rozdz. 15 |
| 6.2. Testing in the Application Domains | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4s8` | rozdz. 4, sekcja 8 |
| 7.1. Testing of Emerging Technologies | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s10` | rozdz. 10, sekcja 10 |
| 7.1. Testing of Emerging Technologies | `[2*]` I. Sommerville, Software Engineering | `c17`, `c18` | rozdz. 17; rozdz. 18 |
| 7.2. Testing Through Emerging Technologies | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3s9` | rozdz. 3, sekcja 9 |
| 8. Software Testing Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s11` | rozdz. 12, sekcja 11 |
| 8. Software Testing Tools | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 8.1. Testing Tool Support and Selection | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s11` | rozdz. 12, sekcja 11 |
| 8.1. Testing Tool Support and Selection | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1`, `c3`, `c4`, `c7`, `c8`, `c9`, `c12` | rozdz. 1; rozdz. 3; rozdz. 4; rozdz. 7; rozdz. 8; rozdz. 9; rozdz. 12 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (15)</summary>

- 1.2. Key Issues
- 1.2.3. Prioritization/Minimization
- 1.2.11. Test Execution and Automation
- 1.2.15. Offline vs. Online Testing
- 1.3. Relationship of Testing to Other Activities
- 3.1.10. Evidence-Based
- 3.1.11. Forcing Exception
- 3.2. Structure-Based Test Techniques
- 3.3. Experience-Based Techniques
- 3.3.2. Exploratory Testing
- 3.3.3. Further Experience-Based Techniques
- 4.2. Evaluation of the Tests Performed
- 5.1. Practical Considerations
- 5.1.7. Test Monitoring and Control
- 7. Testing of and Testing Through Emerging Technologies

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1. Software Testing Fundamentals | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1`, `c2`, `2*`, `c8`, `14*`, `c7` | rozdz. 1; rozdz. 2; rozdz. 8; rozdz. 7 | 3 |
| 1.1. Faults vs. Failures | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s5`, `2*`, `c1`, `14*`, `c1s3` | rozdz. 1, sekcja 5; rozdz. 1; rozdz. 1, sekcja 3 | 3 |
| 1.2.1. Test Case Creation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s3` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 3 | 4 |
| 1.2.1. Test Case Creation | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 4 |
| 1.2.2. Test Selection and Adequacy Criteria | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s14`, `c6s6`, `c12s7` | rozdz. 1, sekcja 14; rozdz. 6, sekcja 6; rozdz. 12, sekcja 7 | 4 |
| 1.2.2. Test Selection and Adequacy Criteria | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 4 |
| 1.2.3. Prioritization/Minimization | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2`, `part 3`, `c5` | część 2; część 3; rozdz. 5 | 4 |
| 1.2.4. Purpose of Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s11`, `c11s4` | rozdz. 13, sekcja 11; rozdz. 11, sekcja 4 | 4 |
| 1.2.4. Purpose of Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 4 |
| 1.2.5. Assessment and Certification | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `c5`, `2*`, `c7`, `c25`, `8` | część 1; rozdz. 5; rozdz. 7; rozdz. 25 | 4 |
| 1.2.6. Testing for Quality Improvement/Assurance | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16s2`, `4`, `part 1`, `c5`, `9` | rozdz. 16, sekcja 2; część 1; rozdz. 5 | 4 |
| 1.2.6. Testing for Quality Improvement/Assurance | `[9]` ISO/IEC 25010:2011, Systems and software engineering — Systems and Software Quality Requireme… |  |  | 4 |
| 1.2.7. The Oracle Problem | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s9`, `c9s7` | rozdz. 1, sekcja 9; rozdz. 9, sekcja 7 | 4 |
| 1.2.8. Theoretical and Practical Limitations | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c2s7` | rozdz. 2, sekcja 7 | 5 |
| 1.2.8. Theoretical and Practical Limitations | `[3]` E.W. Dijkstra, Notes on Structured Programming, Technological University |  |  | 5 |
| 1.2.9. The Problem of Infeasible Paths | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4s7` | rozdz. 4, sekcja 7 | 5 |
| 1.2.10. Testability | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c17s2` | rozdz. 17, sekcja 2 | 5 |
| 1.2.11. Test Execution and Automation | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `c4` | część 1; rozdz. 4 | 5 |
| 1.2.12. Scalability | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s7` | rozdz. 8, sekcja 7 | 5 |
| 1.2.15. Offline vs. Online Testing | `[10]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure system… | `c3` | rozdz. 3 | 6 |
| 2. Test Levels | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s13`, `2*`, `c8s1` | rozdz. 1, sekcja 13; rozdz. 8, sekcja 1 | 6 |
| 2.1. The Target of the Test | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s13` | rozdz. 1, sekcja 13 | 6 |
| 2.1. The Target of the Test | `[2*]` I. Sommerville, Software Engineering | `c8s1` | rozdz. 8, sekcja 1 | 6 |
| 2.1.1. Unit Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3` | rozdz. 3 | 6 |
| 2.1.1. Unit Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 6 |
| 2.1.2. Integration Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c7` | rozdz. 7 | 7 |
| 2.1.2. Integration Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 7 |
| 2.1.3. System Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8` | rozdz. 8 | 7 |
| 2.1.3. System Testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 7 |
| 2.1.4. Acceptance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 | 7 |
| 2.1.4. Acceptance Testing | `[2*]` I. Sommerville, Software Engineering | `c8s4` | rozdz. 8, sekcja 4 | 7 |
| 2.2. Objectives of Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 | 7 |
| 2.2.1. Conformance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s4` | rozdz. 10, sekcja 4 | 7 |
| 2.2.2. Compliance Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s3` | rozdz. 12, sekcja 3 | 8 |
| 2.2.3. Installation Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s2` | rozdz. 12, sekcja 2 | 8 |
| 2.2.4. Alpha and Beta Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s7`, `c16s6` | rozdz. 13, sekcja 7; rozdz. 16, sekcja 6 | 8 |
| 2.2.4. Alpha and Beta Testing | `[2*]` I. Sommerville, Software Engineering | `c8s4` | rozdz. 8, sekcja 4 | 8 |
| 2.2.5. Regression Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s11`, `c13s3`, `4`, `part 1`, `c5` | rozdz. 8, sekcja 11; rozdz. 13, sekcja 3; część 1; rozdz. 5 | 8 |
| 2.2.5. Regression Testing | `[5]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” 2nd ed. 2017 |  |  | 8 |
| 2.2.6. Prioritization Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s7` | rozdz. 12, sekcja 7 | 8 |
| 2.2.7. Non-functional testing | `[2*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 8 |
| 2.2.7. Non-functional testing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1` | część 1 | 8 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s8` | rozdz. 8, sekcja 8 | 9 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c17s2`, `2*`, `c8` | rozdz. 17, sekcja 2; rozdz. 8 | 9 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15`, `2*`, `c11` | rozdz. 15; rozdz. 11 | 9 |
| 2.2.7. Non-functional testing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `10`, `c3` | część 1; rozdz. 3 | 9 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s7`, `2* c17` | rozdz. 8, sekcja 7 | 9 |
| 2.2.7. Non-functional testing | `[17]` A. Bertolino, G.D. Angelis, M. Gallego, B. García, F. Gortázar, F. Lonetti |  |  | 9 |
| 2.2.7. Non-functional testing | `[8]` IEEE Std 1012-2016, IEEE Standard for System, Software, and Hardware Verification | `annex H` | aneks H | 9 |
| 2.2.7. Non-functional testing | `[5]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” 2nd ed. 2017 |  |  | 9 |
| 2.2.7. Non-functional testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c14s2` | rozdz. 14, sekcja 2 | 9 |
| 2.2.8. Security Testing | `[2*]` I. Sommerville, Software Engineering | `c13`, `4`, `part 4`, `annex A` | rozdz. 13; część 4; aneks A | 9 |
| 2.2.9. Privacy Testing | `[2*]` I. Sommerville, Software Engineering | `c13`, `c14` | rozdz. 13; rozdz. 14 | 9 |
| 2.2.10. Interface and API Testing | `[2*]` I. Sommerville, Software Engineering | `c8s1`, `14*`, `c7s12`, `4`, `part 5`, `c4`, `c7` | rozdz. 8, sekcja 1; rozdz. 7, sekcja 12; część 5; rozdz. 4; rozdz. 7 | 10 |
| 2.2.11. Configuration Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s5` | rozdz. 8, sekcja 5 | 10 |
| 3. Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s15`, `4`, `part 4` | rozdz. 1, sekcja 15; część 4 | 10 |
| 3. Test Techniques | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 10 |
| 3.1. Specification-Based Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c6s2`, `4`, `part 4` | rozdz. 6, sekcja 2; część 4 | 10 |
| 3.1.1. Equivalence Partitioning | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s4` | rozdz. 9, sekcja 4 | 10 |
| 3.1.2. Boundary Value Analysis | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s5`, `4`, `part 4` | rozdz. 9, sekcja 5; część 4 | 11 |
| 3.1.3. Syntax Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s11` | rozdz. 10, sekcja 11 | 11 |
| 3.1.3. Syntax Testing | `[2*]` I. Sommerville, Software Engineering | `c5`, `4`, `part 4` | rozdz. 5; część 4 | 11 |
| 3.1.4. Combinatorial Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s3`, `4`, `part 4` | rozdz. 9, sekcja 3; część 4 | 11 |
| 3.1.4. Combinatorial Test Techniques | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 11 |
| 3.1.5. Decision Table | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s6`, `1*`, `c13s6`, `4`, `part 4` | rozdz. 9, sekcja 6; rozdz. 13, sekcja 6; część 4 | 11 |
| 3.1.6. Cause-Effect Graphing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s6`, `4`, `part 3`, `part 4` | rozdz. 1, sekcja 6; część 3; część 4 | 11 |
| 3.1.7. State Transition Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10`, `4`, `part 4` | rozdz. 10; część 4 | 11 |
| 3.1.7. State Transition Testing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 11 |
| 3.1.7. State Transition Testing | `[2*]` I. Sommerville, Software Engineering | `c8s3`, `c19s3`, `4`, `part 4`, `7` | rozdz. 8, sekcja 3; rozdz. 19, sekcja 3; część 4 | 12 |
| 3.1.9. Random Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s7`, `4`, `part 4` | rozdz. 9, sekcja 7; część 4 | 12 |
| 3.1.10. Evidence-Based | `[10]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure system… | `c6s2` | rozdz. 6, sekcja 2 | 12 |
| 3.1.11. Forcing Exception | `[5]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” 2nd ed. 2017 |  |  | 12 |
| 3.2. Structure-Based Test Techniques | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 12 |
| 3.2. Structure-Based Test Techniques | `[12]` ISO/IEC 20246:2017, “Software and systems engineering — Work product reviews” |  |  | 13 |
| 3.2.1. Control Flow Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4`, `4`, `part 4` | rozdz. 4; część 4 | 13 |
| 3.2.2. Data Flow Testing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c5`, `4`, `part 4` | rozdz. 5; część 4 | 13 |
| 3.2.2. Data Flow Testing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 13 |
| 3.2.3. Reference Models for Structure-Based Test Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4` | rozdz. 4 | 13 |
| 3.3. Experience-Based Techniques | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `part 4` | część 1; część 4 | 13 |
| 3.3.1. Error Guessing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s8`, `4`, `part 4` | rozdz. 9, sekcja 8; część 4 | 13 |
| 3.3.2. Exploratory Testing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1` | część 1 | 13 |
| 3.3.3. Further Experience-Based Techniques | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4`, `13` | część 4 | 14 |
| 3.4. Fault-Based and Mutation Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s14`, `1* c3s5`, `5` | rozdz. 1, sekcja 14 | 14 |
| 3.4. Fault-Based and Mutation Techniques | `[6]` M. Papadakis, M. Kintis, J. Zhang, Y. Jia, Y. Le Traon, and M. Harman, Chapter Six — Mutation… |  |  | 15 |
| 3.5. Usage-Based Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15s5` | rozdz. 15, sekcja 5 | 15 |
| 3.5.1. Operational Profile | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15s5` | rozdz. 15, sekcja 5 | 15 |
| 3.5.1. Operational Profile | `[2*]` I. Sommerville, Software Engineering | `c11` | rozdz. 11 | 15 |
| 3.5.2. User Observation Heuristics | `[19*]` J. Nielsen, Usability Engineering | `c5`, `c7`, `4`, `part 4`, `annex A` | rozdz. 5; rozdz. 7; część 4; aneks A | 15 |
| 3.6. Techniques Based on the Nature of the Application | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4`, `part 5` | część 4; część 5 | 15 |
| 3.6. Techniques Based on the Nature of the Application | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 5` | część 5 | 16 |
| 3.7. Selecting and Combining Techniques | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s12`, `10`, `4`, `part 5` | rozdz. 7, sekcja 12; część 5 | 16 |
| 3.7.1. Combining Functional and Structural | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9`, `4`, `part 5` | rozdz. 9; część 5 | 16 |
| 3.7.2. Deterministic vs. Random | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s6` | rozdz. 9, sekcja 6 | 16 |
| 3.8. Techniques Based on Derived Knowledge | `[2*]` I. Sommerville, Software Engineering | `c19`, `c20`, `14*`, `c7` | rozdz. 19; rozdz. 20; rozdz. 7 | 16 |
| 4. Test-Related Measures | `[2*]` I. Sommerville, Software Engineering | `c24s5`, `14*`, `c10`, `4`, `part 4` | rozdz. 24, sekcja 5; rozdz. 10; część 4 | 16 |
| 4. Test-Related Measures | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 16 |
| 4.1. Evaluation of the SUT | `[2*]` I. Sommerville, Software Engineering | `c24s5` | rozdz. 24, sekcja 5 | 17 |
| 4.1.1. SUT Measurements That Aid in Planning and Designing Tests | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10`, `10`, `c6`, `4`, `part 1`, `part 4` | rozdz. 10; rozdz. 6; część 1; część 4 | 17 |
| 4.1.1. SUT Measurements That Aid in Planning and Designing Tests | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4` | część 4 | 17 |
| 4.1.3. Fault Density | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s4`, `14*`, `c10s1` | rozdz. 13, sekcja 4; rozdz. 10, sekcja 1 | 17 |
| 4.1.4. Life Test, Reliability Evaluation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15` | rozdz. 15 | 17 |
| 4.1.4. Life Test, Reliability Evaluation | `[2*]` I. Sommerville, Software Engineering | `c11`, `14*`, `c1s3` | rozdz. 11; rozdz. 1, sekcja 3 | 17 |
| 4.1.4. Life Test, Reliability Evaluation | `[18]` R. Achary and P. Raj, Cloud Reliability Engineering: Technologies and Tools |  |  | 17 |
| 4.1.5. Reliability Growth Models | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c15`, `2* c11s5` | rozdz. 15 | 17 |
| 4.2. Evaluation of the Tests Performed | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 4`, `c6` | część 4; rozdz. 6 | 17 |
| 4.2.1. Fault Injection | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c2s5` | rozdz. 2, sekcja 5 | 18 |
| 4.2.2. Mutation Score | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3s5`, `6` | rozdz. 3, sekcja 5 | 18 |
| 4.2.3. Comparison and Relative Effectiveness of Different Techniques | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7`, `5`, `9` | rozdz. 1, sekcja 7 | 18 |
| 5. Test Process | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `part 2`, `part 3`, `2* c8` | część 1; część 2; część 3 | 18 |
| 5. Test Process | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 18 |
| 5.1. Practical Considerations | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1` | część 1 | 18 |
| 5.1.1. Attitudes/Egoless Programming | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16`, `2*`, `c3` | rozdz. 16; rozdz. 3 | 19 |
| 5.1.2. Test Guides and Organizational Process | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `2* c8`, `4`, `part 2`, `part 3`, `14*`, `c7s3` | rozdz. 12, sekcja 1; część 2; część 3; rozdz. 7, sekcja 3 | 19 |
| 5.1.3. Test Management and Dynamic Test Processes | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12`, `4`, `part 2`, `part 3` | rozdz. 12; część 2; część 3 | 19 |
| 5.1.3. Test Management and Dynamic Test Processes | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s3` | rozdz. 7, sekcja 3 | 19 |
| 5.1.4. Test Documentation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s12`, `14*`, `c7s8`, `4`, `part 3` | rozdz. 8, sekcja 12; rozdz. 7, sekcja 8; część 3 | 19 |
| 5.1.4. Test Documentation | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 3` | część 3 | 19 |
| 5.1.5. Test Team | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16`, `2* c23s5`, `4`, `part 2`, `part 3` | rozdz. 16; część 2; część 3 | 19 |
| 5.1.6. Test Process Measures | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c18s3` | rozdz. 18, sekcja 3 | 20 |
| 5.1.6. Test Process Measures | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c10`, `4`, `part 1`, `part 2`, `part 3` | rozdz. 10; część 1; część 2; część 3 | 20 |
| 5.1.7. Test Monitoring and Control | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 1`, `part 2` | część 1; część 2 | 20 |
| 5.1.7. Test Monitoring and Control | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 20 |
| 5.1.8. Test Completion | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7s11`, `4`, `part 3` | rozdz. 7, sekcja 11; część 3 | 20 |
| 5.1.8. Test Completion | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 20 |
| 5.1.9. Test Reusability | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c3`, `9` | rozdz. 3 | 20 |
| 5.2. Test Sub-Processes and Activities | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s12`, `1*`, `c12s9`, `4`, `part 2` | rozdz. 1, sekcja 12; rozdz. 12, sekcja 9; część 2 | 21 |
| 5.2.1. Test Planning Process | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s8`, `11`, `4`, `part 2` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 8; część 2 | 21 |
| 5.2.1. Test Planning Process | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 21 |
| 5.2.2. Test Design and Implementation | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s1`, `c12s3`, `11` | rozdz. 12, sekcja 1; rozdz. 12, sekcja 3 | 21 |
| 5.2.2. Test Design and Implementation | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 21 |
| 5.2.3. Test Environment Set-up and Maintenance | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s6`, `2* c8s1`, `14* c13s2`, `4`, `part 2`, `11` | rozdz. 12, sekcja 6; część 2 | 21 |
| 5.2.3. Test Environment Set-up and Maintenance | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 21 |
| 5.2.4. Controlled Experiments and Test Execution | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s7`, `14* c4s7`, `14* c5s6`, `4`, `part 2` | rozdz. 12, sekcja 7; część 2 | 21 |
| 5.2.5. Test Incident Reporting | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c13s4`, `c13s9`, `c13s11`, `2*`, `c8s3`, `14*`, `c7s8`, `4`, `part 3`, `12` | rozdz. 13, sekcja 4; rozdz. 13, sekcja 9; rozdz. 13, sekcja 11; rozdz. 8, sekcja 3; rozdz. 7, sekcja 8; część 3 | 22 |
| 5.2.5. Test Incident Reporting | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 2` | część 2 | 22 |
| 5.3. Staffing | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c16`, `4`, `part 3` | rozdz. 16; część 3 | 22 |
| 5.3. Staffing | `[4]` ISO/IEC/IEEE 29119 — System and software engineering — Software testing | `part 3` | część 3 | 22 |
| 6. Software Testing in the Development Processes and the Application Domains | `[2*]` I. Sommerville, Software Engineering | `c8`, `c15`, `14*`, `c4s8`, `c7` | rozdz. 8; rozdz. 15; rozdz. 4, sekcja 8; rozdz. 7 | 22 |
| 6.1. Testing Inside Software Development Processes | `[2*]` I. Sommerville, Software Engineering | `c8`, `14*`, `c7` | rozdz. 8; rozdz. 7 | 23 |
| 6.1.2. Testing in Line with Shift- Left Movement | `[2*]` I. Sommerville, Software Engineering | `c3`, `c8s2`, `4`, `part 1`, `10`, `c3`, `c5` | rozdz. 3; rozdz. 8, sekcja 2; część 1; rozdz. 3; rozdz. 5 | 23 |
| 6.2. Testing in the Application Domains | `[2*]` I. Sommerville, Software Engineering | `c15`, `14*`, `c4s8` | rozdz. 15; rozdz. 4, sekcja 8 | 24 |
| 7.1. Testing of Emerging Technologies | `[13]` V. Riccio, G. Jahangirova, A. Stocco, et al., Testing machine learning based sys- tems: A sys… |  |  | 26 |
| 7.1. Testing of Emerging Technologies | `[15]` S. Demi, R. Colomo-Palacios, and M. Sánchez-Gordón, Software Engineering Applications Enabled… |  |  | 27 |
| 7.1. Testing of Emerging Technologies | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c10s10` | rozdz. 10, sekcja 10 | 27 |
| 7.1. Testing of Emerging Technologies | `[2*]` I. Sommerville, Software Engineering | `c18` | rozdz. 18 | 27 |
| 7.1. Testing of Emerging Technologies | `[2*]` I. Sommerville, Software Engineering | `c17` | rozdz. 17 | 27 |
| 7.2. Testing Through Emerging Technologies | `[13]` V. Riccio, G. Jahangirova, A. Stocco, et al., Testing machine learning based sys- tems: A sys… |  |  | 27 |
| 7.2. Testing Through Emerging Technologies | `[15]` S. Demi, R. Colomo-Palacios, and M. Sánchez-Gordón, Software Engineering Applications Enabled… |  |  | 28 |
| 7.2. Testing Through Emerging Technologies | `[17]` A. Bertolino, G.D. Angelis, M. Gallego, B. García, F. Gortázar, F. Lonetti |  |  | 28 |
| 7.2. Testing Through Emerging Technologies | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3s9` | rozdz. 3, sekcja 9 | 28 |
| 7.2. Testing Through Emerging Technologies | `[16]` K. Mao, L. Capra, M. Harman, and Y. Jia. A survey of the use of crowd- sourcing in software e… |  |  | 28 |
| 8. Software Testing Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s11` | rozdz. 12, sekcja 11 | 28 |
| 8. Software Testing Tools | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 | 28 |
| 8.1. Testing Tool Support and Selection | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s11` | rozdz. 12, sekcja 11 | 29 |
| 8.1. Testing Tool Support and Selection | `[14*]` C.Y. Laporte, and A. April, Software Quality Assurance, IEEE Computer Society Press | `c7` | rozdz. 7 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1`, `c3`, `c4`, `c7`, `c8`, `c9`, `c12` | rozdz. 1; rozdz. 3; rozdz. 4; rozdz. 7; rozdz. 8; rozdz. 9; rozdz. 12 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3s9` | rozdz. 3, sekcja 9 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s11` | rozdz. 12, sekcja 11 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c9s7` | rozdz. 9, sekcja 7 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c4` | rozdz. 4 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c1s7` | rozdz. 1, sekcja 7 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c12s16` | rozdz. 12, sekcja 16 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8` | rozdz. 8 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c3`, `c7s7` | rozdz. 3; rozdz. 7, sekcja 7 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s3`, `c12s11` | rozdz. 8, sekcja 3; rozdz. 12, sekcja 11 | 29 |
| 8.2. Categories of Tools | `[1*]` S. Naik and P. Tripathy, Software Testing and Quality Assurance: Theory and Practice | `c8s3` | rozdz. 8, sekcja 3 | 29 |

---

## KA 06 — Software Engineering Operations

Plik źródłowy: `chapter6/swebok-v4-ch6.pdf` · macierz tematów na stronach PDF: 14, 15

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part 1: Service management systems requirements, ed. IEEE, 2013. |
| `[2*]` | ★ | G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create world-class agility, reliability and security in tech- nology organizations, 2nd ed., IT Revolution Press, 2021. |
| `[3]` |  | ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycle Processes, ed. IEEE, 2017. |
| `[4]` |  | ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable and Secure Systems Including Application Build, Package and Deployment, ed. IEEE, 2022. |
| `[5]` |  | “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” 2nd ed. 2017 |
| `[6]` |  | B. Beyer, C. Jones, J. Petoff, and N.R. Murphy, Site Reliability Engineering —, How Google Runs Production Systems O’Reilly Media, 2016. |
| `[7]` |  | ISO/IEC CD 29110-5-5:2023, Systems and software engineering — Lifecycle profiles for Very Small Entities (VSEs), Part 5-5: Agile/DevOps guidelines. |
| `[8]` |  | J. Humble and D. Farley. Continuous delivery: reliable software releases through build, test, and deployment automation. Pearson Education, 2010. |
| `[9]` |  | J. Turnbull, The Art of Monitoring. James Turnbull, 2016. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Definition of Software Engineering Operations | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c3s3.3` | rozdz. 3, sekcja 3.3 |
| 1.1. Definition of Software Engineering Operations | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12` | rozdz. 6, sekcja 6.4.12 |
| 1.2. Software Engineering Operations Processes | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `s1` | sekcja 1 |
| 1.2. Software Engineering Operations Processes | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12` | rozdz. 6, sekcja 6.4.12 |
| 1.3. Software Installation | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c3`, `c6s6.2` | rozdz. 3; rozdz. 6, sekcja 6.2 |
| 1.3. Software Installation | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c3s3.1` | rozdz. 3, sekcja 3.1 |
| 1.4. Scripting and Automating | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c9` | rozdz. 9 |
| 1.5. Ef﻿fective Testing and Troubleshooting | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c3` | rozdz. 3 |
| 1.6. Performance, Reliability and Load Balancing | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.2` | rozdz. 6, sekcja 6.2 |
| 2.1. Operations Plan and Supplier Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c4s4.1` | rozdz. 4, sekcja 4.1 |
| 2.1. Operations Plan and Supplier Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.1` | rozdz. 6, sekcja 6.1 |
| 2.2. Development and Operational Environments | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c9` | rozdz. 9 |
| 2.3. Software Availability, Continuity and Service Levels | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.3` | rozdz. 6, sekcja 6.3 |
| 2.4. Software Capacity Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.5` | rozdz. 6, sekcja 6.5 |
| 2.5. Software Backup, Disaster Recovery and Failover | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.3.4` | rozdz. 6, sekcja 6.3.4 |
| 2.6. Software and Data Safety, Security, Integrity, Protection and Controls | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.6` | rozdz. 6, sekcja 6.6 |
| 3.1. Operational Testing, Verification and Acceptance | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c10` | rozdz. 10 |
| 3.1. Operational Testing, Verification and Acceptance | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.3.5.3d` | rozdz. 6, sekcja 6.3.5.3d |
| 3.2. Deployment/Release Engineering | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 |
| 3.4. Change Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c9s9.2` | rozdz. 9, sekcja 9.2 |
| 3.5. Problem Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c8s8.3` | rozdz. 8, sekcja 8.3 |
| 4.1. Incident Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c8s8.2` | rozdz. 8, sekcja 8.2 |
| 4.2. Monitor, Measure, Track and Review | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c14-15` | rozdz. 14-15 |
| 4.3. Operations Support | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6`, `c14s5` | rozdz. 6; rozdz. 14, sekcja 5 |
| 4.4. Operations Service Reporting | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.2` | rozdz. 6, sekcja 6.2 |
| 5.1. Incident and Problem Prevention | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c7` | rozdz. 7 |
| 5.2. Operational Risk Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12.3` | rozdz. 6, sekcja 6.4.12.3 |
| 5.3. Automating Software Engineering Operations | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c8` | rozdz. 8 |
| 6. Software Engineering Operations Tools | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c5s5g` | rozdz. 5, sekcja 5g |
| 6. Software Engineering Operations Tools | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 |
| 6.2. Deployment | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 |
| 6.3. Automated Test | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c10` | rozdz. 10 |
| 6.4. Monitoring and Telemetry | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c14-15` | rozdz. 14-15 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (9)</summary>

- 1. Software Engineering Operations Fundamentals
- 2. Software Engineering Operations Planning
- 3. Software Engineering Operations Delivery
- 3.3. Rollback and
- Data Migration
- 4. Software Engineering Operations Control
- 5. Practical Considerations
- 5.4. Software Engineering Operations for Small Organizations
- 6.1. Containers and Virtualization

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 1 |
| (wstęp rozdziału) | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… |  |  | 1 |
| (wstęp rozdziału) | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… |  |  | 1 |
| (wstęp rozdziału) | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… |  |  | 1 |
| (wstęp rozdziału) | `[6]` B. Beyer, C. Jones, J. Petoff, and N.R. Murphy, Site Reliability Engineering — |  |  | 2 |
| 1.1. Definition of Software Engineering Operations | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c3s3.3` | rozdz. 3, sekcja 3.3 | 3 |
| 1.1. Definition of Software Engineering Operations | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12` | rozdz. 6, sekcja 6.4.12 | 3 |
| 1.1. Definition of Software Engineering Operations | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 3 |
| 1.2. Software Engineering Operations Processes | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `s1` | sekcja 1 | 4 |
| 1.2. Software Engineering Operations Processes | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12` | rozdz. 6, sekcja 6.4.12 | 4 |
| 1.2. Software Engineering Operations Processes | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 4 |
| 1.2. Software Engineering Operations Processes | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… |  |  | 4 |
| 1.3. Software Installation | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c3`, `c6s2` | rozdz. 3; rozdz. 6, sekcja 2 | 5 |
| 1.3. Software Installation | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c3s3.1` | rozdz. 3, sekcja 3.1 | 5 |
| 1.4. Scripting and Automating | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c9` | rozdz. 9 | 5 |
| 1.5. Ef﻿fective Testing and Troubleshooting | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c3` | rozdz. 3 | 5 |
| 1.6. Performance, Reliability and Load Balancing | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.2` | rozdz. 6, sekcja 6.2 | 6 |
| 2.1. Operations Plan and Supplier Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c4s4.1` | rozdz. 4, sekcja 4.1 | 6 |
| 2.1. Operations Plan and Supplier Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.1` | rozdz. 6, sekcja 6.1 | 6 |
| 2.1. Operations Plan and Supplier Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12.3a` | rozdz. 6, sekcja 6.4.12.3a | 6 |
| 2.1. Operations Plan and Supplier Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c7s2` | rozdz. 7, sekcja 2 | 6 |
| 2.1. Operations Plan and Supplier Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 7 |
| 2.1. Operations Plan and Supplier Management | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… |  |  | 7 |
| 2.1. Operations Plan and Supplier Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c7s3` | rozdz. 7, sekcja 3 | 7 |
| 2.2. Development and Operational Environments | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c9` | rozdz. 9 | 7 |
| 2.3. Software Availability, Continuity and Service Levels | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.3` | rozdz. 6, sekcja 6.3 | 8 |
| 2.4. Software Capacity Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.5` | rozdz. 6, sekcja 6.5 | 8 |
| 2.6. Software and Data Safety, Security, Integrity, Protection and Controls | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.6` | rozdz. 6, sekcja 6.6 | 9 |
| 3.1. Operational Testing, Verification and Acceptance | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c10` | rozdz. 10 | 9 |
| 3.1. Operational Testing, Verification and Acceptance | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.3.5.3d` | rozdz. 6, sekcja 6.3.5.3d | 9 |
| 3.2. Deployment/Release Engineering | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 | 10 |
| 3.2. Deployment/Release Engineering | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… |  |  | 10 |
| 3.2. Deployment/Release Engineering | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 10 |
| 3.3. Rollback and | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 | 10 |
| 3.3. Rollback and | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.10.3` | rozdz. 6, sekcja 6.4.10.3 | 10 |
| 3.3. Rollback and | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c8s8.3` | rozdz. 8, sekcja 8.3 | 11 |
| 4.1. Incident Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c8s8.2` | rozdz. 8, sekcja 8.2 | 11 |
| 4.1. Incident Management | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c9s9.2` | rozdz. 9, sekcja 9.2 | 11 |
| 4.1. Incident Management | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c14-15` | rozdz. 14-15 | 11 |
| 4.4. Operations Service Reporting | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6`, `c14s5` | rozdz. 6; rozdz. 14, sekcja 5 | 12 |
| 4.4. Operations Service Reporting | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… |  |  | 12 |
| 4.4. Operations Service Reporting | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… |  |  | 12 |
| 4.4. Operations Service Reporting | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… |  |  | 12 |
| 4.4. Operations Service Reporting | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c6s6.2` | rozdz. 6, sekcja 6.2 | 12 |
| 5.1. Incident and Problem Prevention | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c7` | rozdz. 7 | 12 |
| 5.2. Operational Risk Management | `[3]` ISO/IEC/IEEE IEEE standard, 12207:2017, Systems and software engineering — Software Life Cycl… | `c6s6.4.12.3c4` | rozdz. 6, sekcja 6.4.12.3, rozdz. 4 | 12 |
| 5.2. Operational Risk Management | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… |  |  | 12 |
| 5.3. Automating Software Engineering Operations | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c8` | rozdz. 8 | 12 |
| 5.4. Software Engineering Operations for Small Organizations | `[7]` ISO/IEC CD 29110-5-5:2023, Systems and software engineering — Lifecycle profiles for Very Sma… |  |  | 13 |
| 6. Software Engineering Operations Tools | `[1]` IEEE standard, ISO/IEC/IEEE 20000- 1:2013, Information technology — Service management — Part… | `c5s5g` | rozdz. 5, sekcja 5g | 13 |
| 6. Software Engineering Operations Tools | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 | 13 |
| 6. Software Engineering Operations Tools | `[8]` J. Humble and D. Farley. Continuous delivery: reliable software releases through build, test |  |  | 13 |
| 6.1. Containers and Virtualization | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… | `c6s6.4.12` | rozdz. 6, sekcja 6.4.12 | 13 |
| 6.2. Deployment | `[2*]` G. Kim, J. Humble, J. Debois, J. The DevOps Willis, and N. Forsgren, Handbook: How to create… | `c12` | rozdz. 12 | 13 |
| 6.2. Deployment | `[4]` ISO/IEC/IEEE IEEE standard, 32675:2022, Information Technology — DevOps: Building Reliable an… | `c5s5.1` | rozdz. 5, sekcja 5.1 | 13 |

---

## KA 07 — Software Maintenance

Plik źródłowy: `chapter7/swebok-v4-ch7.pdf` · macierz tematów na stronach PDF: 16, 17

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Maintenance, third ed. |
| `[2*]` | ★ | P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice, 2nd ed. River Edge, NJ: World Scientific Publishing, 2003. |
| `[3]` |  | A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement. Wiley- IEEE Computer Society Press, 2008. |
| `[4]` |  | C. Seybold and R. Keller, Aligning Software Maintenance to the Offshore Reality, 12th European Conference on Software Maintenance and Reengineering. April 1-4, 2008, Athens, Greece, DOI:10.1109/ CSMR.2008.4493298. |
| `[5]` |  | IEEE Standard for DevOps: Building Reliable and Secure Systems Including Application Build, Package and Deployment, IEEE Std 2675-2021, Apr. 2021. |
| `[6]` |  | W. Titus, T. Manshreck, and H. Wright. Software engineering at Google: Lessons learned from programming over time. O’Reilly Media, 2020. |
| `[7]` |  | A. Abran and H. Nguyenkim, Measurement of the maintenance pro- cess from a demand-based perspec- tive, Journal of Software Maintenance: Research and Practice, Vol. 5 Issue 2: 63-90, 1993. |
| `[8]` |  | M.M. Lehman, “Laws of software evolution revisited.” European work- shop on software process technology. Berlin, Heidelberg: Springer Berlin Heidelberg, 1996. |
| `[9]` |  | J. Humble and D. Fairley, Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation, Addison-Wesley, 2010. |
| `[10]` |  | ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes, 2017. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Definitions and Terminology | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.2`, `c2s2.2` | rozdz. 1, sekcja 1.2; rozdz. 2, sekcja 2.2 |
| 1.2. Nature of Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.3` | rozdz. 1, sekcja 1.3 |
| 1.3. Need for Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.5` | rozdz. 1, sekcja 1.5 |
| 1.4. Majority of Maintenance Costs | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c4s4.3`, `c5s5.2` | rozdz. 4, sekcja 4.3; rozdz. 5, sekcja 5.2 |
| 1.5. Evolution of Software | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c3s3.5` | rozdz. 3, sekcja 3.5 |
| 1.6. Categories of Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.8`, `c3s3.3` | rozdz. 1, sekcja 1.8; rozdz. 3, sekcja 3.3 |
| 2.1.1. Limited Understanding | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6s6.9` | rozdz. 6, sekcja 6.9 |
| 2.1.2. Testing | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c9`, `c13s13.4.4` | rozdz. 9; rozdz. 13, sekcja 13.4.4 |
| 2.1.3. Impact Analysis | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c13s13.3` | rozdz. 13, sekcja 13.3 |
| 2.1.4. Maintainability | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.5.5` | rozdz. 12, sekcja 12.5.5 |
| 2.2.1. Alignment with Organizational Objectives | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c2s2.3.1.2`, `c3s3.4` | rozdz. 2, sekcja 2.3.1.2; rozdz. 3, sekcja 3.4 |
| 2.2.2. Staffing | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c2s2.3.1.5`, `c10s10.4` | rozdz. 2, sekcja 2.3.1.5; rozdz. 10, sekcja 10.4 |
| 2.2.3. Process | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c5` | rozdz. 5 |
| 2.2.5. Organizational Aspects of Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c10` | rozdz. 10 |
| 2.3.1. Technical Debt Cost Estimation | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.5` | rozdz. 12, sekcja 12.5 |
| 2.3.2. Maintenance Costs Estimation | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.5.6` | rozdz. 12, sekcja 12.5.6 |
| 2.4. Software Maintenance Measurement | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12` | rozdz. 12 |
| 3.1. Software Maintenance Processes | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c5` | rozdz. 5 |
| 3.2. Software Maintenance Activities and Tasks | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6`, `c7` | rozdz. 6; rozdz. 7 |
| 3.2.1. Supporting and Monitoring Activities | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c3s3.4` | rozdz. 3, sekcja 3.4 |
| 3.2.2. Planning Activities | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c10` | rozdz. 10 |
| 3.2.3. Software Configuration Management | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c11s11.3` | rozdz. 11, sekcja 11.3 |
| 3.2.4. Software Quality | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c13s13.4` | rozdz. 13, sekcja 13.4 |
| 4.1. Program Comprehension | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6`, `c14s14.5` | rozdz. 6; rozdz. 14, sekcja 14.5 |
| 4.2. Software Reengineering | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c7` | rozdz. 7 |
| 4.3. Reverse Engineering | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c7`, `c14s14.5` | rozdz. 7; rozdz. 14, sekcja 14.5 |
| 5. Software Maintenance Tools | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c14` | rozdz. 14 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (10)</summary>

- 1. Software Maintenance Fundamentals
- 2. Key Issues in Software Maintenance
- 2.1. Technical Issues
- 2.2. Management Issues
- 2.2.4. Supplier Management
- 2.3. Maintenance Costs
- 3. Software Maintenance Process
- 4. Software Maintenance Techniques
- 4.4. Continuous Integration, Delivery, Testing and Deployment
- 4.5. Visualizing Maintenance

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Definitions and Terminology | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s3.1` | sekcja 3.1 | 2 |
| 1.1. Definitions and Terminology | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.2`, `c2s2` | rozdz. 1, sekcja 1.2; rozdz. 2, sekcja 2 | 2 |
| 1.1. Definitions and Terminology | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice |  |  | 2 |
| 1.1. Definitions and Terminology | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 2 |
| 1.2. Nature of Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.3` | rozdz. 1, sekcja 1.3 | 2 |
| 1.3. Need for Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.5` | rozdz. 1, sekcja 1.5 | 3 |
| 1.4. Majority of Maintenance Costs | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c4s4.3`, `c5s5.2` | rozdz. 4, sekcja 4.3; rozdz. 5, sekcja 5.2 | 3 |
| 1.4. Majority of Maintenance Costs | `[3]` A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement… |  |  | 3 |
| 1.4. Majority of Maintenance Costs | `[7]` A. Abran and H. Nguyenkim, Measurement of the maintenance pro- cess from a demand-based persp… |  |  | 3 |
| 1.5. Evolution of Software | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c3s3.5` | rozdz. 3, sekcja 3.5 | 3 |
| 1.5. Evolution of Software | `[8]` M.M. Lehman, “Laws of software evolution revisited.” European work- shop on software process… |  |  | 3 |
| 1.6. Categories of Software Maintenance | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s3.1.8` | sekcja 3.1.8 | 4 |
| 1.6. Categories of Software Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c1s1.8`, `c3s3.3` | rozdz. 1, sekcja 1.8; rozdz. 3, sekcja 3.3 | 4 |
| 1.6. Categories of Software Maintenance | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 4 |
| 2.1.1. Limited Understanding | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6s6.9` | rozdz. 6, sekcja 6.9 | 5 |
| 2.1.2. Testing | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.2` | sekcja 6.2 | 5 |
| 2.1.2. Testing | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c9`, `c13s13.4.4` | rozdz. 9; rozdz. 13, sekcja 13.4.4 | 5 |
| 2.1.3. Impact Analysis | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s5.1.6` | sekcja 5.1.6 | 6 |
| 2.1.3. Impact Analysis | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c13s13.3` | rozdz. 13, sekcja 13.3 | 6 |
| 2.1.3. Impact Analysis | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 6 |
| 2.1.4. Maintainability | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s8.8` | sekcja 8.8 | 6 |
| 2.1.4. Maintainability | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.5.5` | rozdz. 12, sekcja 12.5.5 | 6 |
| 2.1.4. Maintainability | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 6 |
| 2.2.1. Alignment with Organizational Objectives | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s9.1.8` | sekcja 9.1.8 | 7 |
| 2.2.1. Alignment with Organizational Objectives | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c2s2.3.1.2`, `c3s3.4` | rozdz. 2, sekcja 2.3.1.2; rozdz. 3, sekcja 3.4 | 7 |
| 2.2.2. Staffing | `[1*]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.4.13.3c` | sekcja 6.4.13.3c | 7 |
| 2.2.2. Staffing | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c2s2.3.1.5`, `c10s10.4` | rozdz. 2, sekcja 2.3.1.5; rozdz. 10, sekcja 10.4 | 7 |
| 2.2.3. Process | `[1*]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6` | sekcja 6 | 8 |
| 2.2.3. Process | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c5` | rozdz. 5 | 8 |
| 2.2.4. Supplier Management | `[1*]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.2`, `s8.3`, `s8.8.2` | sekcja 6.1.2; sekcja 8.3; sekcja 8.8.2 | 8 |
| 2.2.4. Supplier Management | `[3]` A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement… |  |  | 8 |
| 2.2.5. Organizational Aspects of Maintenance | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s9.1.8` | sekcja 9.1.8 | 8 |
| 2.2.5. Organizational Aspects of Maintenance | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c10` | rozdz. 10 | 8 |
| 2.2.5. Organizational Aspects of Maintenance | `[3]` A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement… |  |  | 9 |
| 2.2.5. Organizational Aspects of Maintenance | `[7]` A. Abran and H. Nguyenkim, Measurement of the maintenance pro- cess from a demand-based persp… |  |  | 9 |
| 2.3.1. Technical Debt Cost Estimation | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.7`, `s8.8.3.6` | sekcja 6.1.7; sekcja 8.8.3.6 | 9 |
| 2.3.1. Technical Debt Cost Estimation | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12.12.5` | rozdz. 12.12.5 | 9 |
| 2.3.2. Maintenance Costs Estimation | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.2.2`, `s9.1.4`, `s9.1.9-10` | sekcja 6.2.2; sekcja 9.1.4; sekcja 9.1.9-10 | 9 |
| 2.3.2. Maintenance Costs Estimation | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.5.6` | rozdz. 12, sekcja 12.5.6 | 9 |
| 2.3.2. Maintenance Costs Estimation | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `c6s1.4` | rozdz. 6, sekcja 1.4 | 9 |
| 2.3.2. Maintenance Costs Estimation | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `c7s2.4` | rozdz. 7, sekcja 2.4 | 9 |
| 2.4. Software Maintenance Measurement | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.7` | sekcja 6.1.7 | 10 |
| 2.4. Software Maintenance Measurement | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12` | rozdz. 12 | 10 |
| 2.4. Software Maintenance Measurement | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c12s12.3.1` | rozdz. 12, sekcja 12.3.1 | 10 |
| 2.4. Software Maintenance Measurement | `[7]` A. Abran and H. Nguyenkim, Measurement of the maintenance pro- cess from a demand-based persp… |  |  | 11 |
| 3. Software Maintenance Process | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 11 |
| 3.1. Software Maintenance Processes | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s5.2` | sekcja 5.2 | 11 |
| 3.1. Software Maintenance Processes | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c5` | rozdz. 5 | 11 |
| 3.1. Software Maintenance Processes | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 11 |
| 3.1. Software Maintenance Processes | `[10]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes, 2017 |  |  | 11 |
| 3.1. Software Maintenance Processes | `[3]` A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement… |  |  | 11 |
| 3.2. Software Maintenance Activities and Tasks | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1` | sekcja 6.1 | 11 |
| 3.2. Software Maintenance Activities and Tasks | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6`, `c7` | rozdz. 6; rozdz. 7 | 11 |
| 3.2.1. Supporting and Monitoring Activities | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c3s3.4` | rozdz. 3, sekcja 3.4 | 12 |
| 3.2.2. Planning Activities | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.3`, `s8.7.2` | sekcja 6.1.3; sekcja 8.7.2 | 12 |
| 3.2.2. Planning Activities | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c10` | rozdz. 10 | 12 |
| 3.2.2. Planning Activities | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… |  |  | 13 |
| 3.2.2. Planning Activities | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.3c`, `s6.4.13.3d4` | sekcja 6.1.3c | 13 |
| 3.2.2. Planning Activities | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c11s11.3` | rozdz. 11, sekcja 11.3 | 13 |
| 3.2.4. Software Quality | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.1.6`, `s8.7.2` | sekcja 6.1.6; sekcja 8.7.2 | 13 |
| 3.2.4. Software Quality | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c13s13.4` | rozdz. 13, sekcja 13.4 | 13 |
| 4.1. Program Comprehension | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c6`, `c14s14.5` | rozdz. 6; rozdz. 14, sekcja 14.5 | 13 |
| 4.2. Software Reengineering | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c7` | rozdz. 7 | 13 |
| 4.3. Reverse Engineering | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c7`, `c14s14.5` | rozdz. 7; rozdz. 14, sekcja 14.5 | 14 |
| 4.4. Continuous Integration, Delivery, Testing and Deployment | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `s6.4.13.3 Note 1` |  | 14 |
| 4.4. Continuous Integration, Delivery, Testing and Deployment | `[9]` J. Humble and D. Fairley, Continuous Delivery: Reliable Software Releases through Build |  |  | 14 |
| 4.4. Continuous Integration, Delivery, Testing and Deployment | `[6]` W. Titus, T. Manshreck, and H. Wright. Software engineering at Google: Lessons learned from p… | `c23`, `c24` | rozdz. 23; rozdz. 24 | 14 |
| 5. Software Maintenance Tools | `[1]` IEEE Std, ISO/IEC/IEEE 14764:2022, Software Engineering — Software Life Cycle Processes — Mai… | `c6s4` | rozdz. 6, sekcja 4 | 15 |
| 5. Software Maintenance Tools | `[2*]` P. Grubb and A.A. Takang, Software Maintenance: Concepts and Practice | `c14` | rozdz. 14 | 15 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[3]` A. April and A. Abran, Software Maintenance Management: Evaluation and Continuous Improvement. Wiley- IEEE Computer Society Press, 2008.
- `[5]` IEEE Standard for DevOps: Building Reliable and Secure Systems Including Application Build, Package and Deployment, IEEE Std 2675-2021, Apr. 2021.

---

## KA 08 — Software Configuration Management

Plik źródłowy: `chapter8/swebok-v4-ch8.pdf` · macierz tematów na stronach PDF: 15, 16

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” 2nd ed. 2017. |
| `[2]` |  | IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software Engineering, 2012. |
| `[3*]` | ★ | A.M.J. Hass. Configuration Management Principles and Practices, 1st ed. Boston: Addison-Wesley, 2003. |
| `[4*]` | ★ | I. Sommerville, Software Engineering, 10th ed. Global ed. Pearson, 2016. |
| `[5]` |  | J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide, 1st ed. Hoboken, NJ: Wiley-IEEE Computer Society Press, 2006. |
| `[6]` |  | S.P. Berczuk and B. Appleton, Software Configuration Management Patterns: Effective Teamwork, Practical Integration : Addison-Wesley Professional, 2003. |
| `[7]` |  | CMMI for development, Version 2.0, CMMI Institute, 2018. |
| `[8]` |  | B. Aiello and L.A. Sachs, Configuration management best practices: Practical methods that work in the real world (1st edition), 2011. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Organizational Context for SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `Introduction` | wprowadzenie |
| 1.1. Organizational Context for SCM | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 |
| 1.2. Constraints and Guidance for the SCM Process | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c2`, `c5` | rozdz. 2; rozdz. 5 |
| 1.3. Planning for SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 |
| 1.3. Planning for SCM | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 |
| 1.3.1. SCM Organization and Responsibilities | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c10-11` | rozdz. 10-11 |
| 1.3.1. SCM Organization and Responsibilities | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 |
| 1.3.2. SCM Resources and Schedules | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 |
| 1.3.3. Tool Selection and Implementation | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c26s2`, `s6` | rozdz. 26, sekcja 2; sekcja 6 |
| 1.3.4. Vendor/Subcontractor Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c13s9-c14s2` |  |
| 1.3.5. Interface Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23s4` | rozdz. 23, sekcja 4 |
| 1.4. SCM Plan | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 |
| 1.5. Surveillance of Software Configuration Management | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s3` | rozdz. 11, sekcja 3 |
| 1.5.1. SCM Measures and Measurement | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9s2`, `c25s2-s3` | rozdz. 9, sekcja 2; rozdz. 25, sekcja 2-3 |
| 1.5.2. In-Process Audits of SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s1` | rozdz. 1, sekcja 1 |
| 2.1. Identifying Items to Be Controlled | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s2` | rozdz. 1, sekcja 2 |
| 2.1.2. Software Configuration Item | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 |
| 2.2. Configuration Item Identifiers and Attributes | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 |
| 2.5. Relationships Scheme Definition | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c7s4` | rozdz. 7, sekcja 4 |
| 2.6. Software Libraries | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s3` | rozdz. 1, sekcja 3 |
| 3. Software Configuration Change Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8` | rozdz. 8 |
| 3. Software Configuration Change Control | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s1` | rozdz. 11, sekcja 1 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 3.1.1. Software Configuration Control Board | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s1` | rozdz. 11, sekcja 1 |
| 3.1.1. Software Configuration Control Board | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 3.1.2. Software Change Request Process | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s4`, `c8s4` | rozdz. 1, sekcja 4; rozdz. 8, sekcja 4 |
| 3.1.2. Software Change Request Process | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 3.1.3. Software Change Request Forms Definition | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8s4` | rozdz. 8, sekcja 4 |
| 3.1.3. Software Change Request Forms Definition | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 3.2. Implementing Software Changes | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 |
| 4. Software Configuration Status Accounting | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 |
| 4.2. Software Configuration Status Reporting | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s5`, `c9s1` | rozdz. 1, sekcja 5; rozdz. 9, sekcja 1 |
| 6. Software Release Management and Delivery | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8s2` | rozdz. 8, sekcja 2 |
| 6. Software Release Management and Delivery | `[4*]` I. Sommerville, Software Engineering | `c25s4` | rozdz. 25, sekcja 4 |
| 6.1. Software Building | `[4*]` I. Sommerville, Software Engineering | `c25s2` | rozdz. 25, sekcja 2 |
| 6.2. Software Release Management | `[4*]` I. Sommerville, Software Engineering | `c25s2` | rozdz. 25, sekcja 2 |
| 7. Software Configuration Management Tools | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c26s1` | rozdz. 26, sekcja 1 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (11)</summary>

- 1. Management of the SCM Process
- 2. Software Configuration Identification
- 2.1.1. Software Configuration
- 2.3. Baseline Identification
- 2.4. Baseline Attributes
- 3.3. Deviations and Waivers
- 4.1. Software Configuration Status Information
- 5. Software Configuration Auditing
- 5.1. Software Functional Configuration Audit
- 5.2. Software Physical Configuration Audit
- 5.3. In-Process Audits of a Software Baseline

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 1 |
| 1. Management of the SCM Process | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c6`, `c7` | rozdz. 6; rozdz. 7 | 2 |
| 1.1. Organizational Context for SCM | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c6`, `ann. D` | rozdz. 6; aneks D | 2 |
| 1.1. Organizational Context for SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `Introduction` | wprowadzenie | 2 |
| 1.1. Organizational Context for SCM | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 | 2 |
| 1.2. Constraints and Guidance for the SCM Process | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c6`, `ann. D`, `ann. E` | rozdz. 6; aneks D; aneks E | 3 |
| 1.2. Constraints and Guidance for the SCM Process | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c2`, `c5` | rozdz. 2; rozdz. 5 | 3 |
| 1.2. Constraints and Guidance for the SCM Process | `[5]` J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide | `c19s2.2` | rozdz. 19, sekcja 2.2 | 3 |
| 1.3. Planning for SCM | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c6`, `ann. D`, `ann. E` | rozdz. 6; aneks D; aneks E | 3 |
| 1.3. Planning for SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 | 3 |
| 1.3. Planning for SCM | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 | 3 |
| 1.3. Planning for SCM | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 3 |
| 1.3.1. SCM Organization and Responsibilities | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `ann. Ds5-6` | aneks D, sekcja 5-6 | 4 |
| 1.3.1. SCM Organization and Responsibilities | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c10-11` | rozdz. 10-11 | 4 |
| 1.3.1. SCM Organization and Responsibilities | `[4*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 | 4 |
| 1.3.2. SCM Resources and Schedules | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `ann. Ds8` | aneks D, sekcja 8 | 4 |
| 1.3.2. SCM Resources and Schedules | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 | 4 |
| 1.3.3. Tool Selection and Implementation | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c26s2`, `c26s6` | rozdz. 26, sekcja 2; rozdz. 26, sekcja 6 | 4 |
| 1.3.4. Vendor/Subcontractor Control | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c13` | rozdz. 13 | 5 |
| 1.3.4. Vendor/Subcontractor Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c13s9-c14s2` |  | 5 |
| 1.3.5. Interface Control | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c12` | rozdz. 12 | 5 |
| 1.3.5. Interface Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23s4` | rozdz. 23, sekcja 4 | 5 |
| 1.4. SCM Plan | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `ann. D` | aneks D | 5 |
| 1.4. SCM Plan | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c23` | rozdz. 23 | 5 |
| 1.4. SCM Plan | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… |  |  | 5 |
| 1.4. SCM Plan | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s3` | rozdz. 11, sekcja 3 | 5 |
| 1.5.1. SCM Measures and Measurement | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9s2`, `c25s2-s3` | rozdz. 9, sekcja 2; rozdz. 25, sekcja 2-3 | 6 |
| 1.5.2. In-Process Audits of SCM | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s1` | rozdz. 1, sekcja 1 | 6 |
| 2. Software Configuration Identification | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8` | rozdz. 8 | 6 |
| 2.1. Identifying Items to Be Controlled | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.2` | rozdz. 8, sekcja 2.2 | 6 |
| 2.1.2. Software Configuration Item | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.1` | rozdz. 8, sekcja 2.1 | 6 |
| 2.1.2. Software Configuration Item | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 | 6 |
| 2.1.2. Software Configuration Item | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 6 |
| 2.2. Configuration Item Identifiers and Attributes | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.3`, `c8s2.4` | rozdz. 8, sekcja 2.3; rozdz. 8, sekcja 2.4 | 7 |
| 2.2. Configuration Item Identifiers and Attributes | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 | 7 |
| 2.3. Baseline Identification | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.5.4`, `c8s2.5.5`, `c8s2.5.6` | rozdz. 8, sekcja 2.5.4; rozdz. 8, sekcja 2.5.5; rozdz. 8, sekcja 2.5.6 | 7 |
| 2.4. Baseline Attributes | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.5.4` | rozdz. 8, sekcja 2.5.4 | 7 |
| 2.5. Relationships Scheme Definition | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c7s4` | rozdz. 7, sekcja 4 | 7 |
| 2.6. Software Libraries | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c8s2.5` | rozdz. 8, sekcja 2.5 | 8 |
| 2.6. Software Libraries | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s3` | rozdz. 1, sekcja 3 | 8 |
| 3. Software Configuration Change Control | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c9` | rozdz. 9 | 9 |
| 3. Software Configuration Change Control | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8` | rozdz. 8 | 9 |
| 3. Software Configuration Change Control | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 9 |
| 3. Software Configuration Change Control | `[5]` J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide | `c11.s3.3` |  | 9 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c9s2.4` | rozdz. 9, sekcja 2.4 | 9 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s1` | rozdz. 11, sekcja 1 | 9 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 9 |
| 3.1. Requesting, Evaluating and Approving Software Changes | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 9 |
| 3.1.1. Software Configuration Control Board | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c9s2.2` | rozdz. 9, sekcja 2.2 | 10 |
| 3.1.1. Software Configuration Control Board | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c11s1` | rozdz. 11, sekcja 1 | 10 |
| 3.1.1. Software Configuration Control Board | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 10 |
| 3.1.2. Software Change Request Process | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s4`, `c8s4` | rozdz. 1, sekcja 4; rozdz. 8, sekcja 4 | 10 |
| 3.1.2. Software Change Request Process | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 10 |
| 3.1.3. Software Change Request Forms Definition | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c9s2.3`, `c9s2.5` | rozdz. 9, sekcja 2.3; rozdz. 9, sekcja 2.5 | 10 |
| 3.1.3. Software Change Request Forms Definition | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8s4` | rozdz. 8, sekcja 4 | 10 |
| 3.1.3. Software Change Request Forms Definition | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 10 |
| 3.2. Implementing Software Changes | `[4*]` I. Sommerville, Software Engineering | `c25s3` | rozdz. 25, sekcja 3 | 10 |
| 3.3. Deviations and Waivers | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary | `c3` | rozdz. 3 | 11 |
| 4. Software Configuration Status Accounting | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c10` | rozdz. 10 | 11 |
| 4. Software Configuration Status Accounting | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c9` | rozdz. 9 | 11 |
| 4. Software Configuration Status Accounting | `[5]` J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide | `c11s3.4` | rozdz. 11, sekcja 3.4 | 11 |
| 4.1. Software Configuration Status Information | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c10s2.1` | rozdz. 10, sekcja 2.1 | 11 |
| 4.2. Software Configuration Status Reporting | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c10s2.4` | rozdz. 10, sekcja 2.4 | 11 |
| 4.2. Software Configuration Status Reporting | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c1s5`, `c9s1` | rozdz. 1, sekcja 5; rozdz. 9, sekcja 1 | 11 |
| 5. Software Configuration Auditing | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c11` | rozdz. 11 | 12 |
| 5. Software Configuration Auditing | `[5]` J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide | `c11s3.5` | rozdz. 11, sekcja 3.5 | 12 |
| 5. Software Configuration Auditing | `[1]` ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary |  |  | 12 |
| 5.1. Software Functional Configuration Audit | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c11s2.1` | rozdz. 11, sekcja 2.1 | 12 |
| 5.2. Software Physical Configuration Audit | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c11s2.2` | rozdz. 11, sekcja 2.2 | 12 |
| 5.3. In-Process Audits of a Software Baseline | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c11s2.3` | rozdz. 11, sekcja 2.3 | 12 |
| 6. Software Release Management and Delivery | `[2]` IEEE. IEEE Standard 828- 2012, Standard for Configuration Management in Systems and Software… | `c14` | rozdz. 14 | 13 |
| 6. Software Release Management and Delivery | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c8s2` | rozdz. 8, sekcja 2 | 13 |
| 6. Software Release Management and Delivery | `[4*]` I. Sommerville, Software Engineering | `c25s4` | rozdz. 25, sekcja 4 | 13 |
| 6.1. Software Building | `[4*]` I. Sommerville, Software Engineering | `c25s2` | rozdz. 25, sekcja 2 | 13 |
| 6.2. Software Release Management | `[4*]` I. Sommerville, Software Engineering | `c25s2` | rozdz. 25, sekcja 2 | 13 |
| 7. Software Configuration Management Tools | `[3*]` A.M.J. Hass. Configuration Management Principles and Practices | `c26s1` | rozdz. 26, sekcja 1 | 14 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[6]` S.P. Berczuk and B. Appleton, Software Configuration Management Patterns: Effective Teamwork, Practical Integration : Addison-Wesley Professional, 2003.
- `[7]` CMMI for development, Version 2.0, CMMI Institute, 2018.
- `[8]` B. Aiello and L.A. Sachs, Configuration management best practices: Practical methods that work in the real world (1st edition), 2011.

---

## KA 09 — Software Engineering Management

Plik źródłowy: `chapter9/swebok-v4-ch9.pdf` · macierz tematów na stronach PDF: 17, 18

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide), 6th ed., Newton Square, PA: Project Management Institute, 2017. |
| `[2]` |  | Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition, Project Management Institute, 2013. |
| `[3*]` | ★ | R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Society Press, 2009. |
| `[4*]` | ★ | I. Sommerville, Software Engineering, 10th ed., New York: Addison- Wesley, 2016. |
| `[5*]` | ★ | B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston: Addison- Wesley, 2003. |
| `[6]` |  | IEEE, IEEE Standard Adoption of ISO/ IEC 15939: 2007 Systems and Software Engineering Measurement Process, ed: IEEE, 2017. |
| `[7*]` | ★ | J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers, Addison-Wesley Professional, 2001. |
| `[8]` |  | J. McDonald, Managing the Development of Software-Intensive Systems. Hoboken, NJ: John Wiley and Sons, Inc., 2010. |
| `[9]` |  | Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework Parts 1-3: Concepts, Definitions, Principles, and Measures, Version 2.1, 15 April 2021. |
| `[10]` |  | S. Sheard, M. Bouyaud, M. Osaisai, J. Siviy, and K. Nidiffer, “Book Club” Guides a Working Group to Create INCOSE System-Software Interface Products, INSIGHT, Volume 24, Issue 2, 2021. |
| `[11]` |  | K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance, Special Report, CMU/SEI-2018-SR-025, Software Solutions and CERT Divisions, Software Engineering Institute/ Carnegie Mellon University, August 2018. |
| `[12]` |  | R.E. Fairley, Systems Engineering of Software-Enabled Systems, ISBN 978-1- 119-53501-0, 2019. |
| `[13]` |  | Defense Innovation Board, Software Is Never Done: Refactoring the Acquisition Code for Competitive Advantage Defense, v3.3, March 12, 2019. |
| `[14]` |  | “DevOps: Building Reliable and Secure Systems Including Application Build, Package, and Deployment,” IEEE Standard, 2675-2021, 2021. |
| `[15]` |  | M. Chemuturi and T. Cagley, Mastering Software Project Management: Best Practices, Tools and Techniques, J. Ross Publishing, July 2010. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Determination and Negotiation of Requirements | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3` | rozdz. 3 |
| 1.2. Feasibility Analysis | `[4*]` I. Sommerville, Software Engineering | `c4` | rozdz. 4 |
| 1.3. Process for the Review and Revision of Requirements | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3` | rozdz. 3 |
| 2.1. Process Planning | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c2`, `c3`, `c4`, `c5` | rozdz. 2; rozdz. 3; rozdz. 4; rozdz. 5 |
| 2.1. Process Planning | `[5*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston:… | `c1` | rozdz. 1 |
| 2.2. Determine Deliverables | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c4`, `c5`, `c6` | rozdz. 4; rozdz. 5; rozdz. 6 |
| 2.3. Effort, Schedule and Cost Estimation | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c6` | rozdz. 6 |
| 2.4. Resource Allocation | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c5`, `c10`, `c11` | rozdz. 5; rozdz. 10; rozdz. 11 |
| 2.5. Risk Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c9` | rozdz. 9 |
| 2.5. Risk Management | `[5*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston:… | `c5` | rozdz. 5 |
| 2.6. Quality Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c4` | rozdz. 4 |
| 2.6. Quality Management | `[4*]` I. Sommerville, Software Engineering | `c24` | rozdz. 24 |
| 2.7. Plan Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c4` | rozdz. 4 |
| 3.1. Implementation of Plans | `[4*]` I. Sommerville, Software Engineering | `c2` | rozdz. 2 |
| 3.2. Software Acquisition and Supplier Contract Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3`, `c4` | rozdz. 3; rozdz. 4 |
| 3.3. Implementation of Measurement Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c7` | rozdz. 7 |
| 3.4. Monitor Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c8` | rozdz. 8 |
| 3.5. Control Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c7`, `c8` | rozdz. 7; rozdz. 8 |
| 3.6. Reporting | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c11` | rozdz. 11 |
| 4.2. Reviewing and Evaluating Performance | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c8`, `c10` | rozdz. 8; rozdz. 10 |
| 6.1. Establish and Sustain Measurement Commitment | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 |
| 6.2. Plan the Measurement Process | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 |
| 6.3. Perform the Measurement Process | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 |
| 6.4. Evaluate Measurement | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 |
| 7. Software Engineering Management Tools | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c5`, `c6`, `c7` | rozdz. 5; rozdz. 6; rozdz. 7 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (9)</summary>

- 1. Initiation and Scope Definition
- 2. Software Project Planning
- 3. Software Project Enactment
- 4. Review and Evaluation
- 4.1. Determining Satisfaction of Requirements
- 5. Closure
- 5.1. Determining Closure
- 5.2. Closure Activities
- 6. Software Engineering Measurement

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… |  |  | 1 |
| (wstęp rozdziału) | `[12]` R.E. Fairley, Systems Engineering of Software-Enabled Systems, ISBN 978-1- 119-53501-0 |  |  | 1 |
| (wstęp rozdziału) | `[10]` S. Sheard, M. Bouyaud, M. Osaisai, J. Siviy, and K. Nidiffer, “Book Club” Guides a Working Gr… |  |  | 1 |
| (wstęp rozdziału) | `[13]` Defense Innovation Board, Software Is Never Done: Refactoring the Acquisition Code for Compet… |  |  | 1 |
| (wstęp rozdziału) | `[5*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston:… |  |  | 2 |
| (wstęp rozdziału) | `[1]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) |  |  | 3 |
| (wstęp rozdziału) | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 3 |
| (wstęp rozdziału) | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c7`, `c8` | rozdz. 7; rozdz. 8 | 4 |
| (wstęp rozdziału) | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 5 |
| (wstęp rozdziału) | `[14]` “DevOps: Building Reliable and Secure Systems Including Application Build, Package |  |  | 5 |
| (wstęp rozdziału) | `[15]` M. Chemuturi and T. Cagley, Mastering Software Project Management: Best Practices |  |  | 5 |
| 1.1. Determination and Negotiation of Requirements | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3` | rozdz. 3 | 6 |
| 1.2. Feasibility Analysis | `[4*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 | 6 |
| 1.2. Feasibility Analysis | `[1]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) |  |  | 7 |
| 1.3. Process for the Review and Revision of Requirements | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3` | rozdz. 3 | 7 |
| 2. Software Project Planning | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 7 |
| 2.1. Process Planning | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3`, `c4`, `c5` | rozdz. 3; rozdz. 4; rozdz. 5 | 8 |
| 2.1. Process Planning | `[5*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston:… | `c1` | rozdz. 1 | 8 |
| 2.1. Process Planning | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 8 |
| 2.1. Process Planning | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 8 |
| 2.1. Process Planning | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c2` | rozdz. 2 | 8 |
| 2.2. Determine Deliverables | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c4`, `c5`, `c6` | rozdz. 4; rozdz. 5; rozdz. 6 | 8 |
| 2.3. Effort, Schedule and Cost Estimation | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… |  |  | 8 |
| 2.3. Effort, Schedule and Cost Estimation | `[10]` S. Sheard, M. Bouyaud, M. Osaisai, J. Siviy, and K. Nidiffer, “Book Club” Guides a Working Gr… |  |  | 8 |
| 2.3. Effort, Schedule and Cost Estimation | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 8 |
| 2.3. Effort, Schedule and Cost Estimation | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 8 |
| 2.3. Effort, Schedule and Cost Estimation | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c5`, `c10`, `c11` | rozdz. 5; rozdz. 10; rozdz. 11 | 9 |
| 2.4. Resource Allocation | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c9` | rozdz. 9 | 9 |
| 2.4. Resource Allocation | `[5*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Boston:… | `c5` | rozdz. 5 | 9 |
| 2.5. Risk Management | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 9 |
| 2.5. Risk Management | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 9 |
| 2.6. Quality Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c4` | rozdz. 4 | 9 |
| 2.6. Quality Management | `[4*]` I. Sommerville, Software Engineering | `c2` | rozdz. 2 | 9 |
| 2.6. Quality Management | `[1]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) |  |  | 10 |
| 2.6. Quality Management | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 10 |
| 2.6. Quality Management | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition | `9.11` |  | 10 |
| 2.6. Quality Management | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 10 |
| 2.7. Plan Management | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 10 |
| 3.1. Implementation of Plans | `[4*]` I. Sommerville, Software Engineering | `c2` | rozdz. 2 | 11 |
| 3.2. Software Acquisition and Supplier Contract Management | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c3`, `c4` | rozdz. 3; rozdz. 4 | 11 |
| 3.2. Software Acquisition and Supplier Contract Management | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition |  |  | 12 |
| 3.3. Implementation of Measurement Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c7` | rozdz. 7 | 12 |
| 3.3. Implementation of Measurement Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c8` | rozdz. 8 | 12 |
| 3.4. Monitor Process | `[11]` K. Nidiffer, C. Woody, and T.A. Chick, Program Manager’s Guidebook for Software Assurance |  |  | 12 |
| 3.4. Monitor Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c7`, `c8` | rozdz. 7; rozdz. 8 | 12 |
| 3.5. Control Process | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c11` | rozdz. 11 | 13 |
| 4.1. Determining Satisfaction of Requirements | `[4*]` I. Sommerville, Software Engineering | `c8` | rozdz. 8 | 13 |
| 4.2. Reviewing and Evaluating Performance | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c8`, `c10` | rozdz. 8; rozdz. 10 | 13 |
| 5. Closure | `[1]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) | `s3.7`, `s4.6` | sekcja 3.7; sekcja 4.6 | 13 |
| 5.2. Closure Activities | `[2]` Software Extension to the Project Management Body of Knowledge (PMBOK® Guide), Fifth Edition | `s3.7`, `s4.8` | sekcja 3.7; sekcja 4.8 | 14 |
| 6. Software Engineering Measurement | `[6]` IEEE, IEEE Standard Adoption of ISO/ IEC 15939: 2007 Systems and Software Engineering Measure… |  |  | 14 |
| 6. Software Engineering Measurement | `[9]` Practical Software and Systems Measurement Continuous Iterative Development Measurement Frame… |  |  | 14 |
| 6.1. Establish and Sustain Measurement Commitment | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 | 14 |
| 6.2. Plan the Measurement Process | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 | 15 |
| 6.3. Perform the Measurement Process | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 | 15 |
| 6.4. Evaluate Measurement | `[7*]` J. McGarry et al., Practical Software Measurement: Objective Information for Decision Makers | `c1`, `c2` | rozdz. 1; rozdz. 2 | 16 |
| 7. Software Engineering Management Tools | `[3*]` R. E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley IEEE Computer Socie… | `c5`, `c6`, `c7` | rozdz. 5; rozdz. 6; rozdz. 7 | 16 |

---

## KA 10 — Software Engineering Process

Plik źródłowy: `chapter10/swebok-v4-ch10.pdf` · macierz tematów na stronach PDF: 10, 11

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes. |
| `[2]` |  | “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” Edition 2, 2017. |
| `[3*]` | ★ | I. Sommerville, Software Engineering. 10th ed. 2016. |
| `[4*]` | ★ | C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press, 1st ed., 2018. |
| `[5]` |  | Project Management Institute, S oftware Extension to the PMBOK® Guide — Fifth Edition, 2013. |
| `[6]` |  | ISO/IEC 33001:2015 Information technology — Process assessment — Concepts and terminology. |
| `[7]` |  | ISO/IEC 25000:2014 Systems and software engineering — Systems and software product quality requirements and evaluation (SQuaRE) — Guide to SQuaRE. |
| `[8*]` | ★ | D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Addison-Wesley Professional, 2021. |
| `[9*]` | ★ | J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media, 2nd ed. 2021. |
| `[10*]` | ★ | Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Alliance. 2017. |
| `[11]` |  | ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure systems including application build, package and deployment. |
| `[12]` |  | ISO/IEC/IEEE 24774:2021 Systems and software engineering — Life cycle management — Specification for pro- cess description. |
| `[13]` |  | Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) — Sixth Edition. |
| `[14]` |  | ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering — Life cycle management — Part 1: Guidelines for life cycle management. |
| `[15]` |  | W.A. Shewhart and W.E. Deming, Statistical Method from the Viewpoint of Quality Control. Dover, New York, 1986. |
| `[16]` |  | “The Agile Manifesto.” https:// agilemanifesto.org. [Accessed March 5, 2022]. |
| `[17]` |  | S. McConnell, More Effective Agile: A Roadmap for Software Leaders, 2019. |
| `[18]` |  | “Subway Map to Agile Practices.” Agile Alliance. https://www.agilealliance.org /agile101/subway-map-to-agile -practices/ [Accessed March 5, 2022]. |
| `[19]` |  | J. Eckstein and J. Buck, Company-wide Agility with Beyond Budgeting, Open Space & Sociocracy: Survive & Thrive on Disruption, 2021. |
| `[20]` |  | ISO/IEC TR 29110-5-3:2018 Systems and software engineering — Lifecycle profiles for very small entities (VSEs) — Part 5-3: Service delivery guidelines. |
| `[21]` |  | N. Fenton and J. Bieman, Software Metrics, 3rd ed. CRC Press, 2014. |
| `[22]` |  | CMMI Institute — CMMI V2.0. https://cmmiinstitute.com/cmmi. [Accessed 5 March 2022]. |
| `[23]` |  | ISO/IEC/IEEE 24748-3:2020. Part 3: Guidelines for the application of ISO/ IEC/IEEE 12207 (software life cycle processes). |
| `[24]` |  | D.R. Kiran, Total Quality Management. Elsevier, 2017. |
| `[25]` |  | J. Rumbaugh, G. Booch, I. Jacobson. The Unified Software Development Process, 1999 |
| `[26]` |  | P. Kruchten. The Rational Unified Process: An Introduction. 3rd Ed. 2004. |
| `[27]` |  | The Eclipse Foundation https://www. eclipse.org/org/foundation/ [Accessed 25 April 2024]. |
| `[28]` |  | T. Dingsøyr, Postmortem reviews: purpose and approaches in software engineering, Information and Software Technology, vol. 47, Issue 5, 2005, Pages 293-303. |
| `[29]` |  | ISO/IEC 29110-1-1:2024 Systems and software engineering - Lifecycle pro- files for very small entities (VSEs) Part 1-1: Overview. |
| `[30]` |  | ISO/IEC/IEEE 31320-1:2012 Information technology — Modeling LanguagesPart 1: Syntax and Semantics for IDEF0 |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1 Introduction | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 |
| 1.1 Introduction | Others: `[13]` Project Management Institute, A Guide to the Project Manageme… |  |  |
| 1.2 Software Engineering Process Definition | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 |
| 1.2 Software Engineering Process Definition | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V…, `[7]` ISO/IEC 25000:2014 Systems and software engineering — Systems…, `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering…, `[20]` ISO/IEC TR 29110-5-3:2018 Systems and software engineering —… |  |  |
| 2.1 Life cycle definition, process categories and terminology | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5-6` | rozdz. 5-6 |
| 2.1 Life cycle definition, process categories and terminology | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 |
| 2.1 Life cycle definition, process categories and terminology | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c1-3` | rozdz. 1-3 |
| 2.1 Life cycle definition, process categories and terminology | Others: `[13]` Project Management Institute, A Guide to the Project Manageme… |  |  |
| 2.2 Rationale for life cycles | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 |
| 2.2 Rationale for life cycles | Others: `[12]` ISO/IEC/IEEE 24774:2021 Systems and software engineering — Li… |  |  |
| 2.3 The concept of process models and life cycles models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 |
| 2.3 The concept of process models and life cycles models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c2` | rozdz. 2 |
| 2.3 The concept of process models and life cycles models | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V… |  |  |
| 2.4 Some paradigms for development life cycle models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2-3` | rozdz. 2-3 |
| 2.4 Some paradigms for development life cycle models | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 |
| 2.4 Some paradigms for development life cycle models | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media | `c1` | rozdz. 1 |
| 2.4 Some paradigms for development life cycle models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c1` | rozdz. 1 |
| 2.4 Some paradigms for development life cycle models | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V…, `[11]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Bui…, `[13]` Project Management Institute, A Guide to the Project Manageme… |  |  |
| 2.5 Development life cycle models and their engineering dimension | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 |
| 2.5 Development life cycle models and their engineering dimension | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 |
| 2.5 Development life cycle models and their engineering dimension | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media | `c1` | rozdz. 1 |
| 2.5 Development life cycle models and their engineering dimension | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c1` | rozdz. 1 |
| 2.5 Development life cycle models and their engineering dimension | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V…, `[11]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Bui…, `[16]` “The Agile Manifesto.” https:// agilemanifesto.org. [Accessed…, `[17]` S. McConnell, More Effective Agile: A Roadmap for Software Le…, `[18]` “Subway Map to Agile Practices.” Agile Alliance. https://www.…, `[19]` J. Eckstein and J. Buck, Company-wide Agility with Beyond Bud…, `[25]` J. Rumbaugh, G. Booch, I. Jacobson. The Unified Software Deve…, `[26]` P. Kruchten. The Rational Unified Process: An Introduction. 3…, `[27]` The Eclipse Foundation https://www. eclipse.org/org/foundatio… |  |  |
| 2.6 The management of SLCPs | Others: `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering… |  |  |
| 2.7 Software engineering process management | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 |
| 2.7 Software engineering process management | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V… |  |  |
| 2.8 Software life cycle adaptation | Others: `[5]` Project Management Institute, S oftware Extension to the PMBO…, `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering…, `[23]` ISO/IEC/IEEE 24748-3:2020. Part 3: Guidelines for the applica…, `[29]` ISO/IEC 29110-1-1:2024 Systems and software engineering - Lif… |  |  |
| 2.10 Software process infrastructure, tools, methods | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 |
| 2.10 Software process infrastructure, tools, methods | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 |
| 2.10 Software process infrastructure, tools, methods | Others: `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — V… |  |  |
| 2.11 Software engineering process monitoring | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5-6` | rozdz. 5-6 |
| 2.11 Software engineering process monitoring | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 |
| 2.11 Software engineering process monitoring | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4-10` | rozdz. 4-10 |
| 2.11 Software engineering process monitoring | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 |
| 3. Software Process Assessment and Improvement | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4-10` | rozdz. 4-10 |
| 3.1 Overview of software process assessment and improvement | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4` | rozdz. 4 |
| 3.1 Overview of software process assessment and improvement | Others: `[15]` W.A. Shewhart and W.E. Deming, Statistical Method from the Vi…, `[24]` D.R. Kiran, Total Quality Management. Elsevier |  |  |
| 3.2 Goal-question metric (GQM) | Others: `[21]` N. Fenton and J. Bieman, Software Metrics |  |  |
| 3.3 Framework-based methods | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4-10` | rozdz. 4-10 |
| 3.3 Framework-based methods | Others: `[6]` ISO/IEC 33001:2015 Information technology — Process assessmen…, `[22]` CMMI Institute — CMMI V2.0. https://cmmiinstitute.com/cmmi. [… |  |  |
| 3.4 Process Assessment and improvement in Agile | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media | `c11` | rozdz. 11 |
| 3.4 Process Assessment and improvement in Agile | Others: `[28]` T. Dingsøyr, Postmortem reviews: purpose and approaches in so… |  |  |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (3)</summary>

- 1. Software Engineering Process Fundamentals
- 2. Life Cycles
- 2.9 Practical considerations

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Introduction | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 | 1 |
| 1.1. Introduction | `[13]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Gui… |  |  | 1 |
| 1.1. Introduction | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes |  |  | 2 |
| 1.2. Software Engineering Process Definition | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 | 3 |
| 1.2. Software Engineering Process Definition | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 3 |
| 1.2. Software Engineering Process Definition | `[7]` ISO/IEC 25000:2014 Systems and software engineering — Systems and software product quality re… |  |  | 3 |
| 1.2. Software Engineering Process Definition | `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering — Life cycle management — Part… |  |  | 3 |
| 1.2. Software Engineering Process Definition | `[20]` ISO/IEC TR 29110-5-3:2018 Systems and software engineering — Lifecycle profiles for very smal… |  |  | 3 |
| 1.2. Software Engineering Process Definition | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes |  |  | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5-6` | rozdz. 5-6 | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c1-3` | rozdz. 1-3 | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[13]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Gui… |  |  | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes |  |  | 3 |
| 2.1. Life cycle definition, process categories and terminology | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 3 |
| 2.2. Rationale for life cycles | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 | 4 |
| 2.2. Rationale for life cycles | `[12]` ISO/IEC/IEEE 24774:2021 Systems and software engineering — Life cycle management — Specificat… |  |  | 4 |
| 2.2. Rationale for life cycles | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 4 |
| 2.3. The concept of process models and life cycles models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 | 5 |
| 2.3. The concept of process models and life cycles models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c2` | rozdz. 2 | 5 |
| 2.3. The concept of process models and life cycles models | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 5 |
| 2.3. The concept of process models and life cycles models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 |  |  | 5 |
| 2.3. The concept of process models and life cycles models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2-3` | rozdz. 2-3 | 5 |
| 2.4. Some paradigms for development life cycle models | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 | 5 |
| 2.4. Some paradigms for development life cycle models | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media | `c1` | rozdz. 1 | 5 |
| 2.4. Some paradigms for development life cycle models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c1` | rozdz. 1 | 5 |
| 2.4. Some paradigms for development life cycle models | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[11]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure system… |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[12]` ISO/IEC/IEEE 24774:2021 Systems and software engineering — Life cycle management — Specificat… |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[13]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Gui… |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media |  |  | 5 |
| 2.4. Some paradigms for development life cycle models | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… |  |  | 5 |
| 2.5. Development life cycle models and their engineering dimension | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media | `c1` | rozdz. 1 | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… | `c1` | rozdz. 1 | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[11]` ISO/IEC/IEEE 32675:2022 Information technology — DevOps — Building reliable and secure system… |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[16]` “The Agile Manifesto.” https:// agilemanifesto.org. [Accessed March 5, 2022] |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[17]` S. McConnell, More Effective Agile: A Roadmap for Software Leaders, 2019 |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[18]` “Subway Map to Agile Practices.” Agile Alliance. https://www.agilealliance.org /agile101/subw… |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[19]` J. Eckstein and J. Buck, Company-wide Agility with Beyond Budgeting, Open Space & Sociocracy:… |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[25]` J. Rumbaugh, G. Booch, I. Jacobson. The Unified Software Development Process |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[26]` P. Kruchten. The Rational Unified Process: An Introduction. 3rd Ed. 2004 |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[27]` The Eclipse Foundation https://www. eclipse.org/org/foundation/ [Accessed 25 April 2024] |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[9*]` J. Shore and S. Warden, The Art of Agile Development, O’Reilly Media |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[10*]` Project Management Institute, Agile Practice Guide. Project Management Institute and Agile Al… |  |  | 6 |
| 2.5. Development life cycle models and their engineering dimension | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 7 |
| 2.5. Development life cycle models and their engineering dimension | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press |  |  | 7 |
| 2.6. The management of SLCPs | `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering — Life cycle management — Part… |  |  | 7 |
| 2.7. Software engineering process management | `[1*]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5` | rozdz. 5 | 8 |
| 2.7. Software engineering process management | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 8 |
| 2.7. Software engineering process management | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes |  |  | 8 |
| 2.8. Software life cycle adaptation | `[5]` Project Management Institute, S oftware Extension to the PMBOK® Guide — Fifth Edition |  |  | 8 |
| 2.8. Software life cycle adaptation | `[14]` ISO/IEC/IEEE 24748-1:2018(E) Systems and software engineering — Life cycle management — Part… |  |  | 8 |
| 2.8. Software life cycle adaptation | `[23]` ISO/IEC/IEEE 24748-3:2020. Part 3: Guidelines for the application of ISO/ IEC/IEEE 12207 (sof… |  |  | 8 |
| 2.8. Software life cycle adaptation | `[29]` ISO/IEC 29110-1-1:2024 Systems and software engineering - Lifecycle pro- files for very small… |  |  | 8 |
| 2.9. Practical considerations | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 | 8 |
| 2.9. Practical considerations | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 8 |
| 2.10. Software process infrastructure, tools, methods | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 | 9 |
| 2.10. Software process infrastructure, tools, methods | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… | `c2-3` | rozdz. 2-3 | 9 |
| 2.10. Software process infrastructure, tools, methods | `[2]` “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, ” Edition 2 |  |  | 9 |
| 2.10. Software process infrastructure, tools, methods | `[30]` ISO/IEC/IEEE 31320-1:2012 Information technology — Modeling LanguagesPart 1: Syntax and Seman… |  |  | 9 |
| 2.10. Software process infrastructure, tools, methods | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 |  |  | 9 |
| 2.10. Software process infrastructure, tools, methods | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 9 |
| 2.11. Software engineering process monitoring | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes | `c5-6` | rozdz. 5-6 | 9 |
| 2.11. Software engineering process monitoring | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 | `c2` | rozdz. 2 | 9 |
| 2.11. Software engineering process monitoring | `[1]` ISO/IEC/IEEE 12207:2017 Systems and software engineering — Software life cycle processes |  |  | 9 |
| 2.11. Software engineering process monitoring | `[3*]` I. Sommerville, Software Engineering. 10th ed. 2016 |  |  | 9 |
| 2.11. Software engineering process monitoring | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press |  |  | 9 |
| 2.11. Software engineering process monitoring | `[8*]` D. Farley, Modern Software Engineering: Doing What Works to Build Better Software Faster. Add… |  |  | 9 |
| 3.1. Overview of software process assessment and improvement | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press | `c4` | rozdz. 4 | 9 |
| 3.1. Overview of software process assessment and improvement | `[15]` W.A. Shewhart and W.E. Deming, Statistical Method from the Viewpoint of Quality Control. Dover |  |  | 9 |
| 3.1. Overview of software process assessment and improvement | `[24]` D.R. Kiran, Total Quality Management. Elsevier, 2017 |  |  | 9 |
| 3.1. Overview of software process assessment and improvement | `[4*]` C. Y. Laporte and A. April, Software Quality Assurance, IEEE Computer Society Press |  |  | 9 |

---

## KA 11 — Software Engineering Models and Methods

Plik źródłowy: `chapter11/swebok-v4-ch11.pdf` · macierz tematów na stronach PDF: 11, 12

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems, 3rd Edition, CRC Press, 2021. |
| `[2*]` | ★ | S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture, 1st ed. Addison-Wesley, 2002. |
| `[3*]` | ★ | I. Sommerville, Software Engineering, 10th ed. Addison-Wesley, 2016. |
| `[4*]` | ★ | M. Page-Jones, Fundamentals of Object- Oriented Design in UML, 1st ed. Addison-Wesley, 1999. |
| `[5*]` | ★ | J.M. Wing, “A Specifier’s Introduction to Formal Methods,” Computer, vol. 23, pp. 8, 10-23, 1990. |
| `[6*]` | ★ | J.G. Brookshear, Computer Science: An Overview, 10th ed. Addison- Wesley, 2008. |
| `[7*]` | ★ | B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Addison-Wesley, 2003. |
| `[8]` |  | B. Selic and S. Gerard, Modeling and Analysis of Real-Time and Embedded Systems with UML and MARTE: Developing Cyber-Physical Systems, Morgan Kaufmann, 2013. |
| `[9]` |  | M. Brambilla, J. Cabot, and M. Wimmer, Model-Driven Software Engineering in Practice, Morgan & Claypool Publishers, 2017. |
| `[10]` |  | D. Jackson, Software Abstractions, revised edition, The MIT Press, 2016. |
| `[11]` |  | R. Aarenstrup, Managing Model-Based Design, CreateSpace Independent Publishing Platform, 2015. |
| `[12]` |  | C. Larman, Applying UML and Patterns: An Introduction to Object- oriented Analysis and Design and Iterative Development, Prentice Hall PTR, 2005. |
| `[13]` |  | M. Poppendieck and T. Poppendieck, Lean Software Development: An Agile Toolkit, Addison-Wesley Professional, 2003. |
| `[14]` |  | T. Ohno, Toyota Production System: Beyond Large-Scale Production, Taylor & Francis Distribution, 2021. |
| `[15]` |  | D.J. Anderson, Kanban: Successful Evolutionary Change for Your Technology Business, Blue Hole Press; 2010. |
| `[16]` |  | J. Goodpasture, Project management the agile way: Making it work in the enter- prise, J. Ross Publishing, 2010. |
| `[17]` |  | ISO/IEC 19505-1:2012, Information technology — Object Management Group Unified Modeling Language (OMG UML) — Part 1: Infrastructure. |
| `[18]` |  | ISO/IEC/IEEE 32675:2022, Information technology — DevOps — Building reliable and secure systems including application build, package and deployment. |
| `[19]` |  | G. Kiczales, J. Lamping, A. Mendhekar, C. Maeda, C. Lopes, J. M. Loingtier, and J. Irwin, Aspect-oriented pro- gramming, ECOOP’97, LNCS, Vol. 1241, 1997. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Modeling Principles | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c3s3`, `c3s5`, `c4s2`, `c7s1`, `c7s2` | rozdz. 3, sekcja 3; rozdz. 3, sekcja 5; rozdz. 4, sekcja 2; rozdz. 7, sekcja 1; rozdz. 7, sekcja 2 |
| 1.1. Modeling Principles | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c2s2` | rozdz. 2, sekcja 2 |
| 1.1. Modeling Principles | `[3*]` I. Sommerville, Software Engineering | `c5s0` | rozdz. 5, sekcja 0 |
| 1.2. Properties and Expression of Models | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7s2`, `c7s3` | rozdz. 7, sekcja 2; rozdz. 7, sekcja 3 |
| 1.2. Properties and Expression of Models | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6p3`, `c5s0p3` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6, s. 3; rozdz. 5, sekcja 0, s. 3 |
| 1.3. Syntax, Semantics and Pragmatics | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c2s2.2.2p6` | rozdz. 2, sekcja 2.2.2, s. 6 |
| 1.3. Syntax, Semantics and Pragmatics | `[3*]` I. Sommerville, Software Engineering | `c5s0` | rozdz. 5, sekcja 0 |
| 1.4. Preconditions, Postconditions and Invariants | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c4s4` | rozdz. 4, sekcja 4 |
| 1.4. Preconditions, Postconditions and Invariants | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c10s4p2`, `c10s5p2p4` | rozdz. 10, sekcja 4, s. 2; rozdz. 10, sekcja 5, s. 2, s. 4 |
| 2.1. Structural Modeling | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9s5`, `c10s5` | rozdz. 9, sekcja 5; rozdz. 10, sekcja 5 |
| 2.1. Structural Modeling | `[3*]` I. Sommerville, Software Engineering | `c8s1`, `c5s3` | rozdz. 8, sekcja 1; rozdz. 5, sekcja 3 |
| 2.1. Structural Modeling | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c4` | rozdz. 4 |
| 2.2. Behavioral Modeling | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c9s3`, `c10s6` | rozdz. 9, sekcja 3; rozdz. 10, sekcja 6 |
| 2.2. Behavioral Modeling | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c9s2` | rozdz. 9, sekcja 2 |
| 2.2. Behavioral Modeling | `[3*]` I. Sommerville, Software Engineering | `c5s4` | rozdz. 5, sekcja 4 |
| 3.1. Analyzing for Completeness | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6 |
| 3.1. Analyzing for Completeness | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 |
| 3.2. Analyzing for Consistency | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6 |
| 3.2. Analyzing for Consistency | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 |
| 3.3. Analyzing for Correctness | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 |
| 3.4. Traceability | `[3*]` I. Sommerville, Software Engineering | `c4s7.1`, `c4s7.2` | rozdz. 4, sekcja 7.1; rozdz. 4, sekcja 7.2 |
| 3.5. Interaction Analysis | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c10`, `c11` | rozdz. 10; rozdz. 11 |
| 3.5. Interaction Analysis | `[3*]` I. Sommerville, Software Engineering | `c29s1.1`, `c29s5` | rozdz. 29, sekcja 1.1; rozdz. 29, sekcja 5 |
| 3.5. Interaction Analysis | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c5` | rozdz. 5 |
| 4.1. Heuristic Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13` | rozdz. 13 |
| 4.1. Heuristic Methods | `[3*]` I. Sommerville, Software Engineering | `c2s2.2`, `c7s1`, `c5s4.1` | rozdz. 2, sekcja 2.2; rozdz. 7, sekcja 1; rozdz. 5, sekcja 4.1 |
| 4.2. Formal Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c18s2` | rozdz. 18, sekcja 2 |
| 4.2. Formal Methods | `[3*]` I. Sommerville, Software Engineering | `c27` | rozdz. 27 |
| 4.2. Formal Methods | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-24` | s. 8-24 |
| 4.3. Prototyping Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c14s1`, `c14s2`, `c14s3` | rozdz. 14, sekcja 1; rozdz. 14, sekcja 2; rozdz. 14, sekcja 3 |
| 4.3. Prototyping Methods | `[3*]` I. Sommerville, Software Engineering | `c2s3.1` | rozdz. 2, sekcja 3.1 |
| 4.3. Prototyping Methods | `[6*]` J.G. Brookshear, Computer Science: An Overview | `c7s3p5` | rozdz. 7, sekcja 3, s. 5 |
| 4.4. Agile Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c14s5`, `c14s6` | rozdz. 14, sekcja 5; rozdz. 14, sekcja 6 |
| 4.4. Agile Methods | `[3*]` I. Sommerville, Software Engineering | `c3` | rozdz. 3 |
| 4.4. Agile Methods | `[6*]` J.G. Brookshear, Computer Science: An Overview | `c7s3p7` | rozdz. 7, sekcja 3, s. 7 |
| 4.4. Agile Methods | `[7*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Addison-… | `c6`, `app. A` | rozdz. 6; dodatek A |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (4)</summary>

- 1. Modeling
- 2. Types of Models
- 3. Analysis of Models
- 4. Software Engineering Methods

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Modeling Principles | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c2s2`, `c5s1`, `c5s2` | rozdz. 2, sekcja 2; rozdz. 5, sekcja 1; rozdz. 5, sekcja 2 | 2 |
| 1.1. Modeling Principles | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c2s2` | rozdz. 2, sekcja 2 | 2 |
| 1.1. Modeling Principles | `[3*]` I. Sommerville, Software Engineering | `c5s0` | rozdz. 5, sekcja 0 | 2 |
| 1.2. Properties and Expression of Models | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c5s2`, `c5s3` | rozdz. 5, sekcja 2; rozdz. 5, sekcja 3 | 3 |
| 1.2. Properties and Expression of Models | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6p3`, `c5s0p3` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6, s. 3; rozdz. 5, sekcja 0, s. 3 | 3 |
| 1.3. Syntax, Semantics and Pragmatics | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c2s2.2.2p6` | rozdz. 2, sekcja 2.2.2, s. 6 | 3 |
| 1.3. Syntax, Semantics and Pragmatics | `[3*]` I. Sommerville, Software Engineering | `c5s0` | rozdz. 5, sekcja 0 | 3 |
| 1.4. Preconditions, Postconditions and Invariants | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c4s4` | rozdz. 4, sekcja 4 | 4 |
| 1.4. Preconditions, Postconditions and Invariants | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c10s4p2`, `c10s5p2p4` | rozdz. 10, sekcja 4, s. 2; rozdz. 10, sekcja 5, s. 2, s. 4 | 4 |
| 2.1. Structural Modeling | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7s2.2`, `c7s2.5`, `c7s3.1`, `c7s3.2` | rozdz. 7, sekcja 2.2; rozdz. 7, sekcja 2.5; rozdz. 7, sekcja 3.1; rozdz. 7, sekcja 3.2 | 5 |
| 2.1. Structural Modeling | `[3*]` I. Sommerville, Software Engineering | `c5s3`, `c8s1` | rozdz. 5, sekcja 3; rozdz. 8, sekcja 1 | 5 |
| 2.1. Structural Modeling | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c4` | rozdz. 4 | 5 |
| 2.1. Structural Modeling | `[17]` ISO/IEC 19505-1:2012, Information technology — Object Management Group Unified Modeling Langu… |  |  | 5 |
| 2.2. Behavioral Modeling | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c7s2.1`, `c7s2.3`, `c7s2.4` | rozdz. 7, sekcja 2.1; rozdz. 7, sekcja 2.3; rozdz. 7, sekcja 2.4 | 5 |
| 2.2. Behavioral Modeling | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c9s2` | rozdz. 9, sekcja 2 | 5 |
| 2.2. Behavioral Modeling | `[3*]` I. Sommerville, Software Engineering | `c5s4` | rozdz. 5, sekcja 4 | 5 |
| 2.2. Behavioral Modeling | `[8]` B. Selic and S. Gerard, Modeling and Analysis of Real-Time and Embedded Systems with UML and… | `c1s5.4` | rozdz. 1, sekcja 5.4 | 5 |
| 3.1. Analyzing for Completeness | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6 | 6 |
| 3.1. Analyzing for Completeness | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 | 6 |
| 3.2. Analyzing for Consistency | `[3*]` I. Sommerville, Software Engineering | `c4s1.1p7`, `c4s6` | rozdz. 4, sekcja 1.1, s. 7; rozdz. 4, sekcja 6 | 6 |
| 3.2. Analyzing for Consistency | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 | 6 |
| 3.3. Analyzing for Correctness | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-11` | s. 8-11 | 6 |
| 3.3. Analyzing for Correctness | `[3*]` I. Sommerville, Software Engineering | `c4s7.1`, `c4s7.2` | rozdz. 4, sekcja 7.1; rozdz. 4, sekcja 7.2 | 6 |
| 3.3. Analyzing for Correctness | `[2*]` S.J. Mellor and M.J. Balcer, Executable UML: A Foundation for Model-Driven Architecture | `c10`, `c11` | rozdz. 10; rozdz. 11 | 6 |
| 3.3. Analyzing for Correctness | `[3*]` I. Sommerville, Software Engineering | `c29s1.1`, `c29s5` | rozdz. 29, sekcja 1.1; rozdz. 29, sekcja 5 | 6 |
| 3.3. Analyzing for Correctness | `[4*]` M. Page-Jones, Fundamentals of Object- Oriented Design in UML | `c5` | rozdz. 5 | 6 |
| 4.1. Heuristic Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c13`, `c15`, `c16` | rozdz. 13; rozdz. 15; rozdz. 16 | 7 |
| 4.1. Heuristic Methods | `[3*]` I. Sommerville, Software Engineering | `c2s2.2`, `c7s1`, `c5` | rozdz. 2, sekcja 2.2; rozdz. 7, sekcja 1; rozdz. 5 | 7 |
| 4.1. Heuristic Methods | `[8]` B. Selic and S. Gerard, Modeling and Analysis of Real-Time and Embedded Systems with UML and… | `pp.xiii-xvii 9`, `c2s2` | rozdz. 2, sekcja 2 | 7 |
| 4.1. Heuristic Methods | `[11]` R. Aarenstrup, Managing Model-Based Design, CreateSpace Independent Publishing Platform | `c1` | rozdz. 1 | 7 |
| 4.1. Heuristic Methods | `[12]` C. Larman, Applying UML and Patterns: An Introduction to Object- oriented Analysis and Design… | `c1s1` | rozdz. 1, sekcja 1 | 7 |
| 4.1. Heuristic Methods | `[19]` G. Kiczales, J. Lamping, A. Mendhekar, C. Maeda, C. Lopes, J. M. Loingtier | `pp.220-242` | s. 220-242 | 7 |
| 4.2. Formal Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c18` | rozdz. 18 | 8 |
| 4.2. Formal Methods | `[3*]` I. Sommerville, Software Engineering | `c27` | rozdz. 27 | 8 |
| 4.2. Formal Methods | `[5*]` J.M. Wing, “A Specifier’s Introduction to Formal Methods, ” Computer | `pp8-24` | s. 8-24 | 8 |
| 4.2. Formal Methods | `[10]` D. Jackson, Software Abstractions, revised edition, The MIT Press, 2016 | `pp.xi-xiv` |  | 8 |
| 4.3. Prototyping Methods | `[1*]` D. Budgen, Software Design: Creating Solutions for Ill-Structured Problems | `c12s2` | rozdz. 12, sekcja 2 | 9 |
| 4.3. Prototyping Methods | `[3*]` I. Sommerville, Software Engineering | `c2s3.1` | rozdz. 2, sekcja 3.1 | 9 |
| 4.3. Prototyping Methods | `[6*]` J.G. Brookshear, Computer Science: An Overview | `c7s3p5` | rozdz. 7, sekcja 3, s. 5 | 9 |
| 4.4. Agile Methods | `[3*]` I. Sommerville, Software Engineering | `c3` | rozdz. 3 | 9 |
| 4.4. Agile Methods | `[6*]` J.G. Brookshear, Computer Science: An Overview | `c7s3p7` | rozdz. 7, sekcja 3, s. 7 | 9 |
| 4.4. Agile Methods | `[7*]` B. Boehm and R. Turner, Balancing Agility and Discipline: A Guide for the Perplexed. Addison-… | `c6`, `App. A` | rozdz. 6; dodatek A | 9 |
| 4.4. Agile Methods | `[13]` M. Poppendieck and T. Poppendieck, Lean Software Development: An Agile Toolkit |  |  | 9 |
| 4.4. Agile Methods | `[14]` T. Ohno, Toyota Production System: Beyond Large-Scale Production, Taylor & Francis Distribution |  |  | 9 |
| 4.4. Agile Methods | `[15]` D.J. Anderson, Kanban: Successful Evolutionary Change for Your Technology Business |  |  | 9 |
| 4.4. Agile Methods | `[16]` J. Goodpasture, Project management the agile way: Making it work in the enter- prise |  |  | 9 |
| 4.4. Agile Methods | `[18]` ISO/IEC/IEEE 32675:2022, Information technology — DevOps — Building reliable and secure syste… |  |  | 9 |

---

## KA 12 — Software Quality

Plik źródłowy: `chapter12/swebok-v4-ch12.pdf` · macierz tematów na stronach PDF: 15, 16

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018. |
| `[2]` |  | P.B. Crosby, Quality Is Free, McGraw- Hill, 1979. |
| `[3]` |  | W. Humphrey, Managing the Software Process, Addison-Wesley, 1989. |
| `[4]` |  | “ISO/IEC 25010:2011 Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE) — Systems and Software Quality Models,” 2011. |
| `[5*]` | ★ | IEEE CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practices, “Software Engineering Code of Ethics and Professional Practice https://www.computer.org/education/code-of -ethics. |
| `[6]` |  | IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014. |
| `[7*]` | ★ | I. Sommerville, Software Engineering, 10th ed., Addison-Wesley, 2016. |
| `[8]` |  | RTCA, “DO-178C, Software Considerations in Airborne Systems and Equipment Certification,” 2012. Also known as ED-12C in EUROCAE. |
| `[9]` |  | ISO/IEC 15026-1:2019 Systems and Software Engineering — Systems and Software Assurance — Part 1: Concepts and Vocabulary, 2019. |
| `[10]` |  | “ISO 9001:2015 Quality Management Systems — Requirements,” 2015. |
| `[11]` |  | IEEE Std. 1012:2016, “Standard for System and Software Verification and Validation,” 2016. |
| `[12]` |  | ISO/IEC 20246:2017, “Software and systems engineering — Work product reviews,” 2017. |
| `[13*]` | ★ | K.E. Wiegers, Software Requirements, 3rd ed., Microsoft Press, 2013. |
| `[14]` |  | ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, 2017. |
| `[15]` |  | N. Leveson, Safeware: System Safety and Computers, Addison-Wesley Professional, 1995. |
| `[16]` |  | T. Gilb and D. Graham, Software Inspection, Addison-Wesley Professional, 1993. |
| `[17*]` | ★ | K.E. Wiegers, Peer Reviews in Software: A Practical Guide, Addison- Wesley Professional, 2001. |
| `[18]` |  | BS EN 50128:2011+A2:2020, “Standard for Railway Applications –Communications, Signaling and Processing Systems – Software for Railway Control and Protection Systems,” British-Adopted European Standard, 10 August 2020. |
| `[19]` |  | K. Iberle, They don’t care about quality, proceedings of STAR East, Orlando, United States, 2013, available at https://kiberle.com/publications/. |
| `[20]` |  | D. Wallace, L.M. Ippolito, and B.B. Cuthill, Reference Information for the Software Verification and Validation Process, National Institute of Standards and Technology (NIST), U.D. Department of Commerce, Special Publication 500-234, 1996. |
| `[21]` |  | IEC 60300-1:2014, “Dependability Management — Part 1: Guidance for Management and Application,” 2014. |
| `[22]` |  | D. Leffingwell, SAFe 4.5 Reference Guide: Scaled Agile Framework For Lean Enterprises, 2nd ed., Addison- Wesley, 2018. |
| `[23]` |  | ISO/IEC TS 33061:2021, “Information technology — Process assessment — Process Assessment Model for Software Life Cycle Processes,” 2021. |
| `[24]` |  | IEEE 15288.2:2014, “IEEE Standard for Technical Reviews and Audits on Defense Programs,” 2014. |
| `[25]` |  | A guide to the Project management Body of Knowledge, 7th edition, PMI, 2021. |
| `[26]` |  | ISO/IEC/IEEE 90003:2018, “Guidelines for the application of ISO 9001:2015 to computer soft- ware”, 2018. |
| `[27]` |  | COBIT, “Control Objectives for Information Technology”, version 2019, ISACA and the IT Governance Institute. |
| `[28]` |  | BABOK, “A guide to the Business Analysis Body of Knowledge”, version 3, International Institute of Business Analysis, 04-2015. |
| `[29]` |  | CMMI, “Capability Maturity Model Integration”, version 10, ISACA, 2023. |
| `[30]` |  | TOGAF, “Open Group Architecture Framework”, version 10, 2022. |
| `[31]` |  | ISO/IEC 27001:2022, “Information security, cybersecurity, and privacy protection — Information secu- rity — management systems — Requirements”, 2022. |
| `[32]` |  | Humphrey, W.,.PSP: A Self- Improvement Process for Software Engineers, Addison-Wesley Professional, 2005. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Software Engineering Culture and Ethics | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `C1s6`, `C2s3` | rozdz. 1, sekcja 6; rozdz. 2, sekcja 3 |
| 1.1. Software Engineering Culture and Ethics | `[5*]` IEEE CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practices, “Soft… | `X` | cała pozycja dotyczy tematu |
| 1.2. Value and Cost of Quality | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c2s2` | rozdz. 2, sekcja 2 |
| 1.3. Standards, Models and Certifications | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c4` | rozdz. 4 |
| 1.3. Standards, Models and Certifications | `[7*]` I. Sommerville, Software Engineering | `c24s2` | rozdz. 24, sekcja 2 |
| 1.4. Software Dependability and Integrity Levels | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c4s8 c7s2-3` | rozdz. 4, sekcja 8, rozdz. 7, sekcja 2-3 |
| 1.4. Software Dependability and Integrity Levels | `[7*]` I. Sommerville, Software Engineering | `C10` | rozdz. 10 |
| 2.1. Software Quality Improvement | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `C9s9` | rozdz. 9, sekcja 9 |
| 2.3. Evaluate Quality Management | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `C10` | rozdz. 10 |
| 2.3. Evaluate Quality Management | `[7*]` I. Sommerville, Software Engineering | `c24s5` | rozdz. 24, sekcja 5 |
| 2.4. Perform Corrective and Preventive Actions | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c1s3` | rozdz. 1, sekcja 3 |
| 3.1. Prepare for Quality Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c1s5`, `c4s6` | rozdz. 1, sekcja 5; rozdz. 4, sekcja 6 |
| 3.1. Prepare for Quality Assurance | `[13*]` K.E. Wiegers, Software Requirements | `c14` | rozdz. 14 |
| 3.2. Perform Process Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c3s2-3 c8`, `c9`, `c4s6.1.3` | rozdz. 3, sekcja 2-3, rozdz. 8; rozdz. 9; rozdz. 4, sekcja 6.1.3 |
| 3.2. Perform Process Assurance | `[7*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 |
| 3.3. Perform Product Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c3s2-3 c5`, `c7`, `c4s6.1.2` | rozdz. 3, sekcja 2-3, rozdz. 5; rozdz. 7; rozdz. 4, sekcja 6.1.2 |
| 3.3. Perform Product Assurance | `[7*]` I. Sommerville, Software Engineering | `c4s1.2` | rozdz. 4, sekcja 1.2 |
| 3.4. Verification & Validation and Tests | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c5`, `c6`, `c7` | rozdz. 5; rozdz. 6; rozdz. 7 |
| 3.4. Verification & Validation and Tests | `[7*]` I. Sommerville, Software Engineering | `c10s10.5` | rozdz. 10, sekcja 10.5 |
| 4. Software Quality Tools | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c3s2.3`, `c7s8.1`, `c7s11` | rozdz. 3, sekcja 2.3; rozdz. 7, sekcja 8.1; rozdz. 7, sekcja 11 |
| 4. Software Quality Tools | `[5*]` IEEE CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practices, “Soft… | `X` | cała pozycja dotyczy tematu |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (4)</summary>

- 1. Software Quality Fundamentals
- 2. Software Quality Management Process
- 2.2. Plan Quality Management
- 3. Software Quality Assurance Process

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[2]` P.B. Crosby, Quality Is Free, McGraw- Hill, 1979 |  |  | 1 |
| (wstęp rozdziału) | `[3]` W. Humphrey, Managing the Software Process, Addison-Wesley, 1989 |  |  | 1 |
| (wstęp rozdziału) | `[4]` “ISO/IEC 25010:2011 Systems and Software Engineering — Systems and Software Quality Requireme… |  |  | 1 |
| (wstęp rozdziału) | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 1 |
| 1. Software Quality Fundamentals | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 3 |
| 1. Software Quality Fundamentals | `[14]` ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, 2017 |  |  | 3 |
| 1.1. Software Engineering Culture and Ethics | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c1s1.6`, `c2s3` | rozdz. 1, sekcja 1.6; rozdz. 2, sekcja 3 | 3 |
| 1.1. Software Engineering Culture and Ethics | `[5*]` IEEE CS/ACM Joint Task Force on Software Engineering Ethics and Professional Practices, “Soft… |  |  | 3 |
| 1.1. Software Engineering Culture and Ethics | `[19]` K. Iberle, They don’t care about quality, proceedings of STAR East, Orlando |  |  | 3 |
| 1.2. Value and Cost of Quality | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c2s2` | rozdz. 2, sekcja 2 | 4 |
| 1.3. Standards, Models and Certifications | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c4` | rozdz. 4 | 4 |
| 1.3. Standards, Models and Certifications | `[7*]` I. Sommerville, Software Engineering | `c24s2` | rozdz. 24, sekcja 2 | 4 |
| 1.3. Standards, Models and Certifications | `[19]` K. Iberle, They don’t care about quality, proceedings of STAR East, Orlando |  |  | 4 |
| 1.3. Standards, Models and Certifications | `[27]` COBIT, “Control Objectives for Information Technology”, version 2019, ISACA and the IT Govern… |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[25]` A guide to the Project management Body of Knowledge |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[28]` BABOK, “A guide to the Business Analysis Body of Knowledge”, version 3, International Institu… |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[29]` CMMI, “Capability Maturity Model Integration”, version 10, ISACA, 2023 |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[30]` TOGAF, “Open Group Architecture Framework”, version 10, 2022 |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[10]` “ISO 9001:2015 Quality Management Systems — Requirements, ” 2015 |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[31]` ISO/IEC 27001:2022, “Information security, cybersecurity, and privacy protection — Informatio… |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[32]` Humphrey, W., .PSP: A Self- Improvement Process for Software Engineers, Addison-Wesley Profes… |  |  | 5 |
| 1.3. Standards, Models and Certifications | `[22]` D. Leffingwell, SAFe 4.5 Reference Guide: Scaled Agile Framework For Lean Enterprises |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c4s8`, `c7s3.3` | rozdz. 4, sekcja 8; rozdz. 7, sekcja 3.3 | 5 |
| 1.4. Software Dependability and Integrity Levels | `[11]` IEEE Std. 1012:2016, “Standard for System and Software Verification and Validation |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[8]` RTCA, “DO-178C, Software Considerations in Airborne Systems and Equipment Certification |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[18]` BS EN 50128:2011+A2:2020, “Standard for Railway Applications –Communications |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[15]` N. Leveson, Safeware: System Safety and Computers, Addison-Wesley Professional |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[16]` T. Gilb and D. Graham, Software Inspection, Addison-Wesley Professional, 1993 |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[9]` ISO/IEC 15026-1:2019 Systems and Software Engineering — Systems and Software Assurance — Part… |  |  | 5 |
| 1.4. Software Dependability and Integrity Levels | `[7*]` I. Sommerville, Software Engineering | `c10` | rozdz. 10 | 5 |
| 1.4. Software Dependability and Integrity Levels | `[21]` IEC 60300-1:2014, “Dependability Management — Part 1: Guidance for Management and Application |  |  | 6 |
| 1.4. Software Dependability and Integrity Levels | `[7*]` I. Sommerville, Software Engineering | `c10.5` | rozdz. 10.5 | 6 |
| 1.4. Software Dependability and Integrity Levels | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c4s8`, `c7s3.2` | rozdz. 4, sekcja 8; rozdz. 7, sekcja 3.2 | 6 |
| 1.4. Software Dependability and Integrity Levels | `[26]` ISO/IEC/IEEE 90003:2018, “Guidelines for the application of ISO 9001:2015 to computer soft- w… |  |  | 6 |
| 2. Software Quality Management Process | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 6 |
| 2. Software Quality Management Process | `[26]` ISO/IEC/IEEE 90003:2018, “Guidelines for the application of ISO 9001:2015 to computer soft- w… |  |  | 6 |
| 2.1. Software Quality Improvement | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c9`, `c9s9` | rozdz. 9; rozdz. 9, sekcja 9 | 7 |
| 2.1. Software Quality Improvement | `[2]` P.B. Crosby, Quality Is Free, McGraw- Hill, 1979 |  |  | 7 |
| 2.1. Software Quality Improvement | `[3]` W. Humphrey, Managing the Software Process, Addison-Wesley, 1989 |  |  | 7 |
| 2.1. Software Quality Improvement | `[32]` Humphrey, W., .PSP: A Self- Improvement Process for Software Engineers, Addison-Wesley Profes… |  |  | 7 |
| 2.2. Plan Quality Management | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c13` | rozdz. 13 | 7 |
| 2.3. Evaluate Quality Management | `[23]` ISO/IEC TS 33061:2021, “Information technology — Process assessment — Process Assessment Mode… |  |  | 8 |
| 2.3. Evaluate Quality Management | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 8 |
| 2.3. Evaluate Quality Management | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c10` | rozdz. 10 | 8 |
| 2.3. Evaluate Quality Management | `[7*]` I. Sommerville, Software Engineering | `24s5` |  | 8 |
| 2.4. Perform Corrective and Preventive Actions | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c1s3` | rozdz. 1, sekcja 3 | 9 |
| 3.1. Prepare for Quality Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c1s5`, `c4s6` | rozdz. 1, sekcja 5; rozdz. 4, sekcja 6 | 9 |
| 3.1. Prepare for Quality Assurance | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 9 |
| 3.2. Perform Process Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c3s2-3`, `c4s6.1.3`, `c8`, `c9` | rozdz. 3, sekcja 2-3; rozdz. 4, sekcja 6.1.3; rozdz. 8; rozdz. 9 | 10 |
| 3.2. Perform Process Assurance | `[7*]` I. Sommerville, Software Engineering | `c25` | rozdz. 25 | 10 |
| 3.2. Perform Process Assurance | `[2]` P.B. Crosby, Quality Is Free, McGraw- Hill, 1979 |  |  | 10 |
| 3.2. Perform Process Assurance | `[3]` W. Humphrey, Managing the Software Process, Addison-Wesley, 1989 |  |  | 10 |
| 3.2. Perform Process Assurance | `[10]` “ISO 9001:2015 Quality Management Systems — Requirements, ” 2015 |  |  | 10 |
| 3.2. Perform Process Assurance | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 10 |
| 3.3. Perform Product Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `s3.2-s3.3` | sekcja 3.2-3.3 | 11 |
| 3.3. Perform Product Assurance | `[7*]` I. Sommerville, Software Engineering | `c4`, `s6.1.2` | rozdz. 4; sekcja 6.1.2 | 11 |
| 3.3. Perform Product Assurance | `[4]` “ISO/IEC 25010:2011 Systems and Software Engineering — Systems and Software Quality Requireme… |  |  | 11 |
| 3.3. Perform Product Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c7` | rozdz. 7 | 12 |
| 3.3. Perform Product Assurance | `[11]` IEEE Std. 1012:2016, “Standard for System and Software Verification and Validation |  |  | 12 |
| 3.3. Perform Product Assurance | `[14]` ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary, 2017 |  |  | 12 |
| 3.3. Perform Product Assurance | `[20]` D. Wallace, L.M. Ippolito, and B.B. Cuthill, Reference Information for the Software Verificat… |  |  | 12 |
| 3.3. Perform Product Assurance | `[7*]` I. Sommerville, Software Engineering | `c10s5` | rozdz. 10, sekcja 5 | 13 |
| 3.3. Perform Product Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c7s10` | rozdz. 7, sekcja 10 | 13 |
| 3.3. Perform Product Assurance | `[25]` A guide to the Project management Body of Knowledge |  |  | 13 |
| 3.3. Perform Product Assurance | `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014 |  |  | 13 |
| 3.3. Perform Product Assurance | `[1*]` C.Y. Laporte and A. April, Software Quality Assurance, IEEE Press, 2018 | `c5`, `c6` | rozdz. 5; rozdz. 6 | 13 |
| 3.3. Perform Product Assurance | `[23]` ISO/IEC TS 33061:2021, “Information technology — Process assessment — Process Assessment Mode… | `s4`, `s5` | sekcja 4; sekcja 5 | 13 |
| 3.3. Perform Product Assurance | `[17*]` K.E. Wiegers, Peer Reviews in Software: A Practical Guide, Addison- Wesley Professional |  |  | 13 |
| 3.3. Perform Product Assurance | `[12]` ISO/IEC 20246:2017, “Software and systems engineering — Work product reviews |  |  | 14 |
| 3.3. Perform Product Assurance | `[24]` IEEE 15288.2:2014, “IEEE Standard for Technical Reviews and Audits on Defense Programs |  |  | 14 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[6]` IEEE 730 Standard for Software Quality Assurance Processes, IEEE, 2014.
- `[11]` IEEE Std. 1012:2016, “Standard for System and Software Verification and Validation,” 2016.
- `[12]` ISO/IEC 20246:2017, “Software and systems engineering — Work product reviews,” 2017.
- `[15]` N. Leveson, Safeware: System Safety and Computers, Addison-Wesley Professional, 1995.
- `[16]` T. Gilb and D. Graham, Software Inspection, Addison-Wesley Professional, 1993.
- `[17*]` K.E. Wiegers, Peer Reviews in Software: A Practical Guide, Addison- Wesley Professional, 2001.

---

## KA 13 — Software Security

Plik źródłowy: `chapter13/swebok-v4-ch13.pdf` · macierz tematów na stronach PDF: 7

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineering: A Guide for Project Managers, Addison-Wesley Professional, 2008. |
| `[2]` |  | G. McGraw, Software Security: Building Security In, Addison-Wesley Professional, 2006. |
| `[3*]` | ★ | M. Bishop, Computer Security, 2nd Edition, Addison-Wesley Professional, 2019. |
| `[4]` |  | L. Bell, M. Brunton-Spall, R. Smith, and J. Bird, Agile Application Security, O’Reilly, 2017. |
| `[5]` |  | T. Hsiang-Chih Hsu, Hands-On Security in DevOps: Ensure continuous security, deployment, and delivery with DevSecOps, Packt Publishing, 2018. |
| `[6]` |  | T. Hsiang-Chih Hsu, Practical Security Automation and Testing: Tools and techniques for automated security scan- ning and testing in DevSecOps, Packt Publishing, 2019. |
| `[7]` |  | G. Wilson, DevSecOps: A leader’s guide to producing secure software without com- promising flow, feedback and continuous improvement, Rethink Press, 2020. |
| `[8]` |  | L. Rice, Container Security: Fundamental Technology Concepts That Protect Containerized Applications, O’Reilly & Associates Inc., 2020. |
| `[9]` |  | ISO/IEC/JTC1 SC27 Standards: Trustworthiness, Cryptography, Data security, Cryptography, Security eval- uation and testing, Security control, Identity management and privacy technologies. |
| `[10]` |  | ISO/IEC 25010:2023 Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model. |
| `[11]` |  | ISO/IEC 27000:2018 Information technology — Security techniques — Information security management sys- tems — Overview and vocabulary. |
| `[12]` |  | ISO/IEC 27032:2012 Information technology — Security techniques — Guidelines for cybersecurity. |
| `[13]` |  | ISO/IEC 19770-1:2017 Information technology — IT asset management — Part 1: IT asset management systems — Requirements. |
| `[14]` |  | ISO/IEC 21827:2008 Information technology — Security techniques — Systems Security Engineering — Capability Maturity Model (SSE-CMM). |
| `[15]` |  | ISO/IEC 27001:2022 Information security, cybersecurity and privacy pro- tection — Information security man- agement systems — Requirements. |
| `[16]` |  | M. Howard and S. Lipner, The Security Development Lifecycle, Microsoft Press, 2006. |
| `[17]` |  | F. Swiderski and W. Snyder, Threat Modeling: Design for Security, Wiley, 2014. |
| `[18]` |  | D. Firesmith, “Security use cases,” Journal of Object Technology, Vol. 2, No. 1, pp. 53-64, 2003. |
| `[19]` |  | E. Fernandez-Buglioni, Security Patterns in Practice: Designing Secure Architectures Using Software Patterns, Wiley, 2013. |
| `[20]` |  | C. Nagappan, R. Lai, and R. Steel, Core Security Patterns: Best Practices and Strategies for J2EE, Web Services, and Identity Management, Prentice Hall, 2005. |
| `[21]` |  | M. Schumacher, E. Fernandez- Buglioni, D. Hybertson, F. Buschmann, and P. Sommerlad, Security Patterns: Integrating Security and Systems Engineering, Wiley, 2006. |
| `[22]` |  | R.C. Seacord, The CERT C Secure Coding Standard, Addison-Wesley Professional, 2008. |
| `[23]` |  | R.C. Seacord, Secure Coding in C and C++, Addison-Wesley Professional, 2013. |
| `[24]` |  | D. Long, F. Mohindra, D. Seacord, R.C. Sutherland, and D.F. Svoboda, The CERT Oracle Secure Coding Standard for Java, 2011. |
| `[25]` |  | J. Erickson, Hacking: The Art of Exploitation, 2nd Edition, No Starch Press, 2008. |
| `[26]` |  | K. Scarfone, M. Souppaya, A. Cody, and A. Orebaugh, Technical Guide to Information Security Testing and Assessment, NIST SP800-115, 2008. |
| `[27]` |  | PCI Security Standards Council, PCI DSS: Payment Card Industry Data Security Standard, Version 3.2, 2017. |
| `[28]` |  | MITRE, “Common Vulnerabilities and Exposures (CVE),” https://www.cve.org/. |
| `[29]` |  | MITRE, “Common Weakness Enumeration (CWE),” https://cwe. mitre.org/. |
| `[30]` |  | MITRE, “Common Attack Pattern Enumeration and Classification (CAPEC),” https://capec.mitre.org/. |
| `[31*]` | ★ | C. Dotson, Practical Cloud Security, O’Reilly, 2019. |
| `[32]` |  | “Internet of Things Security Best Practices,” IEEE, 2017, https:// standards.ieee.org/wp-content/uploads /import/documents/other/whitepaper -internet-of-things-2017-dh-v1.pdf. |
| `[33]` |  | “IoT 2020: Smart and secure IoT plat- form,” IEC, 2016, https://www.iec.ch /basecamp/iot-2020-smart-and-secure -iot-platform. |
| `[34]` |  | ISO/IEC 15408-1:2022 Information security, cybersecurity and privacy pro- tection — Evaluation criteria for IT security — Part 1: Introduction and general model. |
| `[35]` |  | ISO/IEC 18045:2008 Information technology — Security techniques — Methodology for IT security evaluation. |
| `[36]` |  | DoD Enterprise DevSecOps, https://dodcio.defense.gov/Portals/0 /Documents/Library/DoD%20 Enterprise%20DevSecOps%20 Fundamentals%20v2.5.pdf. |
| `[37]` |  | C. Easttom, Computer Security Fundamentals, 4th Edition, Pearson IT Certification, 2019. |
| `[38]` |  | Y. Diogenes and E. Ozkaya, Cybersecurity — Attack and Defense Strategies, Second Edition, Packt Publishing, 2019. |
| `[39]` |  | C. Chio and D. Freeman, Machine Learning and Security: Protecting Systems with Data and Algorithms, O’Reilly, 2018. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.3. Cybersecurity | `[3*]` M. Bishop, Computer Security | `c23` | rozdz. 23 |
| 2. Security Management and Organization | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c7` | rozdz. 7 |
| 2.1. Capability Maturity Model | `[3*]` M. Bishop, Computer Security | `c22` | rozdz. 22 |
| 3.1. Security Engineering and Secure Development Life Cycle | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c1` | rozdz. 1 |
| 3.2. Common Criteria for Information Technology Security Evaluation | `[3*]` M. Bishop, Computer Security | `c22`, `c25` | rozdz. 22; rozdz. 25 |
| 4. Security Engineering for Software Systems | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c1`, `c3` | rozdz. 1; rozdz. 3 |
| 4. Security Engineering for Software Systems | `[3*]` M. Bishop, Computer Security | `c1`, `c3` | rozdz. 1; rozdz. 3 |
| 4.1. Security Requirements | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c3` | rozdz. 3 |
| 4.1. Security Requirements | `[3*]` M. Bishop, Computer Security | `c20`, `c31` | rozdz. 20; rozdz. 31 |
| 4.2. Security Design | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c4` | rozdz. 4 |
| 4.2. Security Design | `[3*]` M. Bishop, Computer Security | `c20`, `c31` | rozdz. 20; rozdz. 31 |
| 4.3. Security Patterns | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c4` | rozdz. 4 |
| 4.4. Construction for Security | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c5` | rozdz. 5 |
| 4.4. Construction for Security | `[3*]` M. Bishop, Computer Security | `c20`, `c31` | rozdz. 20; rozdz. 31 |
| 4 .5. Security Testing | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c5` | rozdz. 5 |
| 4 .5. Security Testing | `[3*]` M. Bishop, Computer Security | `c24`, `c31` | rozdz. 24; rozdz. 31 |
| 4.6. Vulnerability Management | `[3*]` M. Bishop, Computer Security | `c24` | rozdz. 24 |
| 5.1. Security Vulnerability Checking Tools | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c6` | rozdz. 6 |
| 5.2. Penetration Testing Tools | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c4` | rozdz. 4 |
| 5.2. Penetration Testing Tools | `[3*]` M. Bishop, Computer Security | `c31` | rozdz. 31 |
| 6.1. Security for Container and Cloud | `[31*]` C. Dotson, Practical Cloud Security, O’Reilly, 2019 | `c1-c3` | rozdz. 1-3 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (10)</summary>

- 1. Software Security Fundamentals
- 1.1. Software Security
- 1.2. Information Security
- 2.2. Information Security Management System
- 2.3. Agile Practice for Software Security
- 3. Software Security Engineering and Processes
- 5. Software Security Tools
- 6. Domain-Specific Software Security
- 6.2. Security for IoT Software
- 6.3. Security for Machine Learning-Based Application

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1. Software Security Fundamentals | `[37]` C. Easttom, Computer Security Fundamentals |  |  | 1 |
| 1. Software Security Fundamentals | `[9]` ISO/IEC/JTC1 SC27 Standards: Trustworthiness, Cryptography, Data security |  |  | 1 |
| 1.1. Software Security | `[10]` ISO/IEC 25010:2023 Systems and software engineering — Systems and software Quality Requiremen… |  |  | 1 |
| 1.2. Information Security | `[11]` ISO/IEC 27000:2018 Information technology — Security techniques — Information security manage… |  |  | 1 |
| 1.3. Cybersecurity | `[12]` ISO/IEC 27032:2012 Information technology — Security techniques — Guidelines for cybersecurity |  |  | 2 |
| 1.3. Cybersecurity | `[38]` Y. Diogenes and E. Ozkaya, Cybersecurity — Attack and Defense Strategies |  |  | 2 |
| 2. Security Management and Organization | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c7` | rozdz. 7 | 2 |
| 2. Security Management and Organization | `[13]` ISO/IEC 19770-1:2017 Information technology — IT asset management — Part 1: IT asset manageme… |  |  | 2 |
| 2. Security Management and Organization | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… |  |  | 2 |
| 2.1. Capability Maturity Model | `[3*]` M. Bishop, Computer Security | `c22` | rozdz. 22 | 2 |
| 2.1. Capability Maturity Model | `[14]` ISO/IEC 21827:2008 Information technology — Security techniques — Systems Security Engineerin… |  |  | 2 |
| 2.2. Information Security Management System | `[15]` ISO/IEC 27001:2022 Information security, cybersecurity and privacy pro- tection — Information… |  |  | 2 |
| 2.3. Agile Practice for Software Security | `[4]` L. Bell, M. Brunton-Spall, R. Smith, and J. Bird, Agile Application Security | `c15`, `c16` | rozdz. 15; rozdz. 16 | 3 |
| 2.3. Agile Practice for Software Security | `[4]` L. Bell, M. Brunton-Spall, R. Smith, and J. Bird, Agile Application Security |  |  | 3 |
| 3.1. Security Engineering and Secure Development Life Cycle | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c1` | rozdz. 1 | 3 |
| 3.1. Security Engineering and Secure Development Life Cycle | `[16]` M. Howard and S. Lipner, The Security Development Lifecycle, Microsoft Press |  |  | 3 |
| 3.1. Security Engineering and Secure Development Life Cycle | `[36]` DoD Enterprise DevSecOps, https://dodcio.defense.gov/Portals/0 /Documents/Library/DoD%20 Ente… |  |  | 3 |
| 3.2. Common Criteria for Information Technology Security Evaluation | `[3*]` M. Bishop, Computer Security | `c22`, `c25` | rozdz. 22; rozdz. 25 | 3 |
| 3.2. Common Criteria for Information Technology Security Evaluation | `[34]` ISO/IEC 15408-1:2022 Information security, cybersecurity and privacy pro- tection — Evaluatio… |  |  | 3 |
| 3.2. Common Criteria for Information Technology Security Evaluation | `[35]` ISO/IEC 18045:2008 Information technology — Security techniques — Methodology for IT security… |  |  | 3 |
| 4. Security Engineering for Software Systems | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c1`, `c3` | rozdz. 1; rozdz. 3 | 3 |
| 4. Security Engineering for Software Systems | `[3*]` M. Bishop, Computer Security | `c1`, `c3` | rozdz. 1; rozdz. 3 | 3 |
| 4.1. Security Requirements | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c3` | rozdz. 3 | 3 |
| 4.1. Security Requirements | `[2]` G. McGraw, Software Security: Building Security In, Addison-Wesley Professional | `c2` | rozdz. 2 | 3 |
| 4.1. Security Requirements | `[3*]` M. Bishop, Computer Security | `c20`, `c30` | rozdz. 20; rozdz. 30 | 3 |
| 4.1. Security Requirements | `[18]` D. Firesmith, “Security use cases, ” Journal of Object Technology |  |  | 3 |
| 4.2. Security Design | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c4` | rozdz. 4 | 4 |
| 4.2. Security Design | `[2]` G. McGraw, Software Security: Building Security In, Addison-Wesley Professional | `c5` | rozdz. 5 | 4 |
| 4.2. Security Design | `[3*]` M. Bishop, Computer Security | `c20`, `c31` | rozdz. 20; rozdz. 31 | 4 |
| 4.2. Security Design | `[17]` F. Swiderski and W. Snyder, Threat Modeling: Design for Security, Wiley, 2014 |  |  | 4 |
| 4.3. Security Patterns | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c4` | rozdz. 4 | 4 |
| 4.3. Security Patterns | `[19]` E. Fernandez-Buglioni, Security Patterns in Practice: Designing Secure Architectures Using So… |  |  | 4 |
| 4.3. Security Patterns | `[20]` C. Nagappan, R. Lai, and R. Steel, Core Security Patterns: Best Practices and Strategies for… |  |  | 4 |
| 4.3. Security Patterns | `[21]` M. Schumacher, E. Fernandez- Buglioni, D. Hybertson, F. Buschmann, and P. Sommerlad |  |  | 4 |
| 4.4. Construction for Security | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c5` | rozdz. 5 | 4 |
| 4.4. Construction for Security | `[3*]` M. Bishop, Computer Security | `c20`, `c31` | rozdz. 20; rozdz. 31 | 4 |
| 4.4. Construction for Security | `[22]` R.C. Seacord, The CERT C Secure Coding Standard, Addison-Wesley Professional |  |  | 4 |
| 4.4. Construction for Security | `[23]` R.C. Seacord, Secure Coding in C and C++, Addison-Wesley Professional, 2013 |  |  | 4 |
| 4.4. Construction for Security | `[24]` D. Long, F. Mohindra, D. Seacord, R.C. Sutherland, and D.F. Svoboda, The CERT Oracle Secure C… |  |  | 4 |
| 4.4. Construction for Security | `[2]` G. McGraw, Software Security: Building Security In, Addison-Wesley Professional | `c7` | rozdz. 7 | 5 |
| 4.4. Construction for Security | `[3*]` M. Bishop, Computer Security | `c24`, `c31` | rozdz. 24; rozdz. 31 | 5 |
| 4.4. Construction for Security | `[26]` K. Scarfone, M. Souppaya, A. Cody, and A. Orebaugh, Technical Guide to Information Security T… |  |  | 5 |
| 4.4. Construction for Security | `[27]` PCI Security Standards Council, PCI DSS: Payment Card Industry Data Security Standard |  |  | 5 |
| 4.6. Vulnerability Management | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c5` | rozdz. 5 | 5 |
| 4.6. Vulnerability Management | `[3*]` M. Bishop, Computer Security | `c24` | rozdz. 24 | 5 |
| 4.6. Vulnerability Management | `[28]` MITRE, “Common Vulnerabilities and Exposures (CVE), ” https://www.cve.org/ |  |  | 5 |
| 4.6. Vulnerability Management | `[29]` MITRE, “Common Weakness Enumeration (CWE), ” https://cwe. mitre.org/ |  |  | 5 |
| 4.6. Vulnerability Management | `[30]` MITRE, “Common Attack Pattern Enumeration and Classification (CAPEC), ” https://capec.mitre.org/ |  |  | 5 |
| 4.6. Vulnerability Management | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… |  |  | 5 |
| 5.1. Security Vulnerability Checking Tools | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… | `c6` | rozdz. 6 | 5 |
| 5.1. Security Vulnerability Checking Tools | `[25]` J. Erickson, Hacking: The Art of Exploitation |  |  | 5 |
| 5.1. Security Vulnerability Checking Tools | `[1*]` J.H. Allen, S.J. Barnum, R.J. Ellison, G. McGraw, and N.R. Mead, Software Security Engineerin… |  |  | 6 |
| 5.2. Penetration Testing Tools | `[2]` G. McGraw, Software Security: Building Security In, Addison-Wesley Professional | `c4` | rozdz. 4 | 6 |
| 5.2. Penetration Testing Tools | `[2]` G. McGraw, Software Security: Building Security In, Addison-Wesley Professional |  |  | 6 |
| 6.1. Security for Container and Cloud | `[31*]` C. Dotson, Practical Cloud Security, O’Reilly, 2019 | `c1-c3` | rozdz. 1-3 | 6 |
| 6.1. Security for Container and Cloud | `[31*]` C. Dotson, Practical Cloud Security, O’Reilly, 2019 |  |  | 6 |
| 6.2. Security for IoT Software | `[32]` “Internet of Things Security Best Practices, ” IEEE, 2017, https:// standards.ieee.org/wp-con… |  |  | 6 |
| 6.2. Security for IoT Software | `[33]` “IoT 2020: Smart and secure IoT plat- form, ” IEC, 2016, https://www.iec.ch /basecamp/iot-202… |  |  | 6 |
| 6.3. Security for Machine Learning-Based Application | `[39]` C. Chio and D. Freeman, Machine Learning and Security: Protecting Systems with Data and Algor… | `c8` | rozdz. 8 | 6 |
| 6.3. Security for Machine Learning-Based Application | `[39]` C. Chio and D. Freeman, Machine Learning and Security: Protecting Systems with Data and Algor… |  |  | 6 |

---

## KA 14 — Software Engineering Professional Practice

Plik źródłowy: `chapter14/swebok-v4-ch14.pdf` · macierz tematów na stronach PDF: 13, 14

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | F. Bott et al., Professional Issues in Software Engineering, 3rd ed., Taylor & Francis, 2000. |
| `[2]` |  | Appendix B of this Guide. |
| `[3*]` | ★ | G. Voland, Engineering by Design, 2nd ed., Prentice-Hall, 2003. |
| `[4*]` | ★ | I. Sommerville, Software Engineering, 10th ed., Addison-Wesley, 2016. |
| `[5*]` | ★ | S. McConnell, Code Complete, 2nd ed., Microsoft Press, 2004. |
| `[6]` |  | 25 Years Washington Accord, IEC, 2014. |
| `[12]` |  | IFIP Code of Ethics and Professional Conduct, 2021. |
| `[13*]` | ★ | S. Tockey, Return on Software: Maximizing the Return on Your Software Investment, Addison-Wesley, 2004. |
| `[14*]` | ★ | R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press, 2009. |
| `[15]` |  | G. M. Weinberg, The Psychology of Computer Programming: Silver Anniversary Edition, Dorset House, 1998. |
| `[16]` |  | Kinney and Lange, P.A., Intellectual Property Law for Business Lawyers, Thomson West, 2013. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c1s5`, `c1s10` | rozdz. 1, sekcja 5; rozdz. 1, sekcja 10 |
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[4*]` I. Sommerville, Software Engineering | `c12s10` | rozdz. 12, sekcja 10 |
| 1.2. Codes of Ethics and Professional Conduct | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c1s7-s9`, `c10s2`, `App` | rozdz. 1, sekcja 7-9; rozdz. 10, sekcja 2; dodatek |
| 1.2. Codes of Ethics and Professional Conduct | `[4*]` I. Sommerville, Software Engineering | `c1s2` | rozdz. 1, sekcja 2 |
| 1.3. Nature and Role of Professional Societies | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c2s3` | rozdz. 2, sekcja 3 |
| 1.3. Nature and Role of Professional Societies | `[4*]` I. Sommerville, Software Engineering | `c1s2` | rozdz. 1, sekcja 2 |
| 1.3. Nature and Role of Professional Societies | `[5*]` S. McConnell, Code Complete | `c35s1` | rozdz. 35, sekcja 1 |
| 1.4. Nature and Role of Software Engineering Standards | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c10s2` | rozdz. 10, sekcja 2 |
| 1.4. Nature and Role of Software Engineering Standards | `[4*]` I. Sommerville, Software Engineering | `*` | cała pozycja dotyczy tematu |
| 1.4. Nature and Role of Software Engineering Standards | `[5*]` S. McConnell, Code Complete | `c32s6` | rozdz. 32, sekcja 6 |
| 1.5. Economic Impact of Software | `[3*]` G. Voland, Engineering by Design | `c1s1`, `c10s8` | rozdz. 1, sekcja 1; rozdz. 10, sekcja 8 |
| 1.5. Economic Impact of Software | `[4*]` I. Sommerville, Software Engineering | `c1s1` | rozdz. 1, sekcja 1 |
| 1.5. Economic Impact of Software | `[13*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `*` | cała pozycja dotyczy tematu |
| 1.6. Employment Contracts | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c6`, `c7` | rozdz. 6; rozdz. 7 |
| 1.6. Employment Contracts | `[4*]` I. Sommerville, Software Engineering | `*` | cała pozycja dotyczy tematu |
| 1.7. Legal Issues | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c6`, `c11` | rozdz. 6; rozdz. 11 |
| 1.7. Legal Issues | `[3*]` G. Voland, Engineering by Design | `c5s3- s4` | rozdz. 5, sekcja 3-4 |
| 1.7. Legal Issues | `[4*]` I. Sommerville, Software Engineering | `c12s3`, `c13s2` | rozdz. 12, sekcja 3; rozdz. 13, sekcja 2 |
| 1.8. Documentation | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c10s5` | rozdz. 10, sekcja 5 |
| 1.8. Documentation | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 |
| 1.8. Documentation | `[4*]` I. Sommerville, Software Engineering | `*` | cała pozycja dotyczy tematu |
| 1.8. Documentation | `[5*]` S. McConnell, Code Complete | `c32` | rozdz. 32 |
| 1.9. Trade-Off Analysis | `[3*]` G. Voland, Engineering by Design | `c1s2`, `c10` | rozdz. 1, sekcja 2; rozdz. 10 |
| 1.9. Trade-Off Analysis | `[4*]` I. Sommerville, Software Engineering | `c7s2`, `c13s4` | rozdz. 7, sekcja 2; rozdz. 13, sekcja 4 |
| 1.9. Trade-Off Analysis | `[13*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c9s5-10` | rozdz. 9, sekcja 5-10 |
| 2.1. Dynamics of Working in Teams/Groups | `[3*]` G. Voland, Engineering by Design | `c1s6` | rozdz. 1, sekcja 6 |
| 2.1. Dynamics of Working in Teams/Groups | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c1s3-5`, `c10` | rozdz. 1, sekcja 3-5; rozdz. 10 |
| 2.2. Individual Cognition | `[3*]` G. Voland, Engineering by Design | `c1s6` | rozdz. 1, sekcja 6 |
| 2.2. Individual Cognition | `[5*]` S. McConnell, Code Complete | `c33` | rozdz. 33 |
| 2.3. Dealing with Problem Complexity | `[3*]` G. Voland, Engineering by Design | `c3s2` | rozdz. 3, sekcja 2 |
| 2.3. Dealing with Problem Complexity | `[4*]` I. Sommerville, Software Engineering | `c1s1`, `c20s1-s5` | rozdz. 1, sekcja 1; rozdz. 20, sekcja 1-5 |
| 2.4. Interacting with Stakeholders | `[4*]` I. Sommerville, Software Engineering | `*` | cała pozycja dotyczy tematu |
| 2.5. Dealing with Uncertainty and Ambiguity | `[4*]` I. Sommerville, Software Engineering | `c4s1`, `c4s4`, `c11s5c24s5` | rozdz. 4, sekcja 1; rozdz. 4, sekcja 4; rozdz. 11, sekcja 5, rozdz. 24, sekcja 5 |
| 2.5. Dealing with Uncertainty and Ambiguity | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c9s4` | rozdz. 9, sekcja 4 |
| 2.6. Dealing with Equity, Diversity, and Inclusivity | `[4*]` I. Sommerville, Software Engineering | `*` | cała pozycja dotyczy tematu |
| 2.6. Dealing with Equity, Diversity, and Inclusivity | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s7` | rozdz. 10, sekcja 7 |
| 3.1. Reading, Understanding, and Summarizing | `[4*]` I. Sommerville, Software Engineering | `c4s5` | rozdz. 4, sekcja 5 |
| 3.1. Reading, Understanding, and Summarizing | `[5*]` S. McConnell, Code Complete | `c33s3` | rozdz. 33, sekcja 3 |
| 3.2. Writing | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 |
| 3.2. Writing | `[4*]` I. Sommerville, Software Engineering | `c4s2-s3` | rozdz. 4, sekcja 2-3 |
| 3.3. Team and Group Communication | `[3*]` G. Voland, Engineering by Design | `c1s6` | rozdz. 1, sekcja 6 |
| 3.3. Team and Group Communication | `[4*]` I. Sommerville, Software Engineering | `c22s3` | rozdz. 22, sekcja 3 |
| 3.3. Team and Group Communication | `[5*]` S. McConnell, Code Complete | `c27s1` | rozdz. 27, sekcja 1 |
| 3.3. Team and Group Communication | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s4` | rozdz. 10, sekcja 4 |
| 3.4. Presentation Skills | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 |
| 3.4. Presentation Skills | `[4*]` I. Sommerville, Software Engineering | `c22` | rozdz. 22 |
| 3.4. Presentation Skills | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s7-s8` | rozdz. 10, sekcja 7-8 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (3)</summary>

- 1. Professionalism
- 2. Group Dynamics and Psychology
- 3. Communication Skills

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `cls4-s5`, `cls10` |  | 2 |
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[2]` Appendix B of this Guide |  |  | 2 |
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[4*]` I. Sommerville, Software Engineering | `c12s10` | rozdz. 12, sekcja 10 | 2 |
| 1.1. Accreditation, Certification and Qualification, and Licensing | `[6]` 25 Years Washington Accord, IEC, 2014 |  |  | 2 |
| 1.2. Codes of Ethics and Professional Conduct | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `cls7-s9`, `c10s2`, `Appendix` | rozdz. 10, sekcja 2; dodatek | 3 |
| 1.2. Codes of Ethics and Professional Conduct | `[3*]` G. Voland, Engineering by Design | `c8` | rozdz. 8 | 3 |
| 1.2. Codes of Ethics and Professional Conduct | `[4*]` I. Sommerville, Software Engineering | `cls2` |  | 3 |
| 1.2. Codes of Ethics and Professional Conduct | `[5*]` S. McConnell, Code Complete | `c33` | rozdz. 33 | 3 |
| 1.2. Codes of Ethics and Professional Conduct | `[13*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment |  |  | 3 |
| 1.3. Nature and Role of Professional Societies | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c2s3` | rozdz. 2, sekcja 3 | 4 |
| 1.3. Nature and Role of Professional Societies | `[4*]` I. Sommerville, Software Engineering | `c1s2` | rozdz. 1, sekcja 2 | 4 |
| 1.3. Nature and Role of Professional Societies | `[5*]` S. McConnell, Code Complete | `c35s1` | rozdz. 35, sekcja 1 | 4 |
| 1.4. Nature and Role of Software Engineering Standards | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c10s2` | rozdz. 10, sekcja 2 | 4 |
| 1.4. Nature and Role of Software Engineering Standards | `[2]` Appendix B of this Guide |  |  | 4 |
| 1.4. Nature and Role of Software Engineering Standards | `[4*]` I. Sommerville, Software Engineering |  |  | 4 |
| 1.4. Nature and Role of Software Engineering Standards | `[5*]` S. McConnell, Code Complete | `c32s6` | rozdz. 32, sekcja 6 | 4 |
| 1.5. Economic Impact of Software | `[3*]` G. Voland, Engineering by Design | `c1s1`, `c10s8` | rozdz. 1, sekcja 1; rozdz. 10, sekcja 8 | 5 |
| 1.5. Economic Impact of Software | `[4*]` I. Sommerville, Software Engineering | `c1s1` | rozdz. 1, sekcja 1 | 5 |
| 1.5. Economic Impact of Software | `[13*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment |  |  | 5 |
| 1.6. Employment Contracts | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c6`, `c7` | rozdz. 6; rozdz. 7 | 5 |
| 1.6. Employment Contracts | `[12]` IFIP Code of Ethics and Professional Conduct, 2021 |  |  | 5 |
| 1.7. Legal Issues | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c6`, `c11` | rozdz. 6; rozdz. 11 | 6 |
| 1.7. Legal Issues | `[2]` Appendix B of this Guide |  |  | 6 |
| 1.7. Legal Issues | `[3*]` G. Voland, Engineering by Design | `c5s3-c5s4` |  | 6 |
| 1.7. Legal Issues | `[4*]` I. Sommerville, Software Engineering | `c12s3`, `c13s2` | rozdz. 12, sekcja 3; rozdz. 13, sekcja 2 | 6 |
| 1.8. Documentation | `[1*]` F. Bott et al., Professional Issues in Software Engineering | `c10s5.8` | rozdz. 10, sekcja 5.8 | 8 |
| 1.8. Documentation | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 | 8 |
| 1.8. Documentation | `[4*]` I. Sommerville, Software Engineering |  |  | 8 |
| 1.8. Documentation | `[5*]` S. McConnell, Code Complete | `c32` | rozdz. 32 | 8 |
| 1.9. Trade-Off Analysis | `[3*]` G. Voland, Engineering by Design | `c1s2`, `c10` | rozdz. 1, sekcja 2; rozdz. 10 | 9 |
| 1.9. Trade-Off Analysis | `[4*]` I. Sommerville, Software Engineering | `c7s2`, `c13s4` | rozdz. 7, sekcja 2; rozdz. 13, sekcja 4 | 9 |
| 1.9. Trade-Off Analysis | `[13*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c9s5.10` | rozdz. 9, sekcja 5.10 | 9 |
| 2.1. Dynamics of Working in Teams/Groups | `[3*]` G. Voland, Engineering by Design | `c1s6` | rozdz. 1, sekcja 6 | 9 |
| 2.1. Dynamics of Working in Teams/Groups | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c1s3.5`, `c10` | rozdz. 1, sekcja 3.5; rozdz. 10 | 9 |
| 2.2. Individual Cognition | `[3*]` G. Voland, Engineering by Design | `c1s6.5` | rozdz. 1, sekcja 6.5 | 10 |
| 2.2. Individual Cognition | `[5*]` S. McConnell, Code Complete | `c33` | rozdz. 33 | 10 |
| 2.3. Dealing with Problem Complexity | `[3*]` G. Voland, Engineering by Design | `c3s2` | rozdz. 3, sekcja 2 | 10 |
| 2.3. Dealing with Problem Complexity | `[4*]` I. Sommerville, Software Engineering | `c1s1`, `c20s1-s5` | rozdz. 1, sekcja 1; rozdz. 20, sekcja 1-5 | 10 |
| 2.3. Dealing with Problem Complexity | `[5*]` S. McConnell, Code Complete | `c33` | rozdz. 33 | 10 |
| 2.4. Interacting with Stakeholders | `[4*]` I. Sommerville, Software Engineering |  |  | 10 |
| 2.5. Dealing with Uncertainty and Ambiguity | `[4*]` I. Sommerville, Software Engineering | `c4s1`, `c4s4`, `c11s5`, `c24s5` | rozdz. 4, sekcja 1; rozdz. 4, sekcja 4; rozdz. 11, sekcja 5; rozdz. 24, sekcja 5 | 11 |
| 2.5. Dealing with Uncertainty and Ambiguity | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c9s4` | rozdz. 9, sekcja 4 | 11 |
| 2.6. Dealing with Equity, Diversity, and Inclusivity | `[4*]` I. Sommerville, Software Engineering |  |  | 11 |
| 2.6. Dealing with Equity, Diversity, and Inclusivity | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s7` | rozdz. 10, sekcja 7 | 11 |
| 3.1. Reading, Understanding, and Summarizing | `[4*]` I. Sommerville, Software Engineering | `c4s5` | rozdz. 4, sekcja 5 | 12 |
| 3.1. Reading, Understanding, and Summarizing | `[5*]` S. McConnell, Code Complete | `c33s3` | rozdz. 33, sekcja 3 | 12 |
| 3.2. Writing | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 | 12 |
| 3.2. Writing | `[4*]` I. Sommerville, Software Engineering | `c4s2-s3` | rozdz. 4, sekcja 2-3 | 12 |
| 3.3. Team and Group Communication | `[3*]` G. Voland, Engineering by Design | `c1s6.8` | rozdz. 1, sekcja 6.8 | 12 |
| 3.3. Team and Group Communication | `[4*]` I. Sommerville, Software Engineering | `c22s3` | rozdz. 22, sekcja 3 | 12 |
| 3.3. Team and Group Communication | `[5*]` S. McConnell, Code Complete | `c27s1` | rozdz. 27, sekcja 1 | 12 |
| 3.3. Team and Group Communication | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s4` | rozdz. 10, sekcja 4 | 12 |
| 3.4. Presentation Skills | `[3*]` G. Voland, Engineering by Design | `c1s5` | rozdz. 1, sekcja 5 | 12 |
| 3.4. Presentation Skills | `[4*]` I. Sommerville, Software Engineering | `c22` | rozdz. 22 | 12 |
| 3.4. Presentation Skills | `[14*]` R. E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c10s7-c10s8` |  | 12 |

---

## KA 15 — Software Engineering Economics

Plik źródłowy: `chapter15/swebok-v4-ch15.pdf` · macierz tematów na stronach PDF: 20, 21, 22

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | E. DeGarmo et al., Engineering Economy, 9th ed., Prentice Hall, 1993. |
| `[2]` |  | P. Rodriguez, C. Urquhart, and E. Mendes. “A Theory of Value for Value- based Feature Selection in Software Engineering,” IEEE Transactions on Software Engineering, 1, 2020. |
| `[3*]` | ★ | S. Tockey, Return on Software: Maximizing the Return on Your Software Investment, Addison-Wesley, 2005. |
| `[4]` |  | International Valuation Standards (IVS), Norwich: Page Bros, 2019. |
| `[5]` |  | K. Voigt, O. Buliga, and K. Michl, Business Model Pioneers: How Innovators Successfully Implement New Business Models, Springer, 2017. |
| `[6]` |  | M.-I. Sanchez-Segura, G.-L. Dugarte- Peña, A. Amescua-Seco, and F. Medina-Domínguez, “Exploring How The Intangible Side of an Organization Impacts its Business Model,” Kybernetes, Vol. 50 No. 10, pp. 2790-2822. 2021. https://doi.org /10.1108/K-05-2020-0302. |
| `[7]` |  | ISO/IEC/IEEE 12207-2:2020 – Systems and software engineering — Software life cycle processes — Part 2: Relation and mapping between ISO/ IEC/IEEE 12207:2017 and ISO/IEC 12207:2008, IEEE, 2020, pp. 1-278. |
| `[8*]` | ★ | ISO/IEC/IEEE 15288:2023 – Systems and Software Engineering – System Life Cycle Processes, IEEE. |
| `[9]` |  | T. Brown and B. Katz, Change by Design: How Design Thinking Transforms Organizations and Inspires Innovation, Revised and updated ed., Harper Collins, 2019. |
| `[10*]` | ★ | I. Sommerville, Software Engineering, 10th ed., Addison-Wesley, 2016. |
| `[11]` |  | T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering, and Software Engineering Using Planguage, Elsevier Butterworth-Heinemann, 2005. |
| `[12]` |  | R. Kazman, M. Klein, and P. Clements, “ATAMSM: Method for Architecture Evaluation,” CMU/SEI- 2000-TR-004, Software Engineering Institute, August 2000. |
| `[13]` |  | M.I. Sanchez-Segura, A. Ruiz- Robles, F. Medina-Domínguez, and G.L. Dugarte-Peña. “Strategic Characterization of Process Assets Based on Asset Quality and Business Impact,” Industrial Management and Data Systems, 117(8), 1720-1734. https://doi. org/10.1108/IMDS-10-2016-0422, 2017. |
| `[14]` |  | M.I. Sanchez-Segura, A. Ruiz Robles, F.Medina-Domínguez. “Uncovering Hidden Process Assets: A Case Study.” Information Systems Frontiers, https://www.springerprofessional.de/ en/uncovering-hidden-process-assets-a -case-study/11724394, 2016. |
| `[15]` |  | A. Osterwalder, Y. Pigneur, G. Bernarda, A. Smith, and T. Papadakos, Value Proposition Design, Wiley, 2015. |
| `[16]` |  | D. Gotterbarn, K. Miller, and S. Rogerson, “Software Engineering Code of Ethics,” Commun. ACM 40, 11, 110-118, doi: 10.1145/265684.265699, 1997. |
| `[17]` |  | S. McConnell, Software Estimation: Demystifying the Black Art, 1st ed., Microsoft Press, 2009. |
| `[18]` |  | R.D. Stutzke, Estimating Software- Intensive Systems Projects, Products, and Processes, 1st ed., Addison-Wesley, 2005. |
| `[19]` |  | M. Ben-Eli, Understanding Systems. Systems Innovation, https://netzerocities. app/_content/files/knowledge/3148/ understanding_systems_thinking___ systems_modelling_the_sustainability_ lab_2019__1_.pdf, 2019. |
| `[20]` |  | J. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World, McGraw-Hill, 2000. |
| `[21]` |  | S. Pereira, G. Medina, et al., “System Thinking and Business Model Canvas for Collaborative Business Models Design,” IFIP Advances in Information and Communication Technology, Vol. 488, pp. 461-468, 2016. |
| `[22*]` | ★ | R.E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press, 2009. |
| `[23]` |  | Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide), 7th ed., Project Management Institute, 2021. |
| `[24]` |  | Project Management Institute, PMI Lexicon of Project Management Term, 2012. |
| `[25]` |  | Project Management Institute and IEEE Computer Society, Software Extension to the PMBOK® Guide Fifth Edition, Project Management Institute, 2013. |
| `[26]` |  | B.W. Boehm, Software Engineering Economics, Prentice-Hall, 1981. |
| `[27]` |  | C. Ebert and R. Dumke, Software Measurement, Springer, 2007. |
| `[28]` |  | D.J. Reifer, Making the Software Business Case: Improvement by the Numbers, Addison-Wesley, 2002. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1.1. Proposals | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c3pp23-24` | rozdz. 3, s. 23-24 |
| 1.2. Cash Flow | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c3pp24-32` | rozdz. 3, s. 24-32 |
| 1.3. Time-Value of Money | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c5-6` | rozdz. 5-6 |
| 1.4. Equivalence | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c7` | rozdz. 7 |
| 1.5. Bases for Comparison | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c8` | rozdz. 8 |
| 1.6. Alternatives | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c9` | rozdz. 9 |
| 2.1. Process Overview | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp35-36` | rozdz. 4, s. 35-36 |
| 2.2. Understand the Real Problem | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp37-39` | rozdz. 4, s. 37-39 |
| 2.3. Identify All Reasonable Technically Feasible Solutions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp40-41` | rozdz. 4, s. 40-41 |
| 2.4. Define the Selection Criteria | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp39-40`, `c26pp441-442` | rozdz. 4, s. 39-40; rozdz. 26, s. 441-442 |
| 2.5. Evaluate Each Alternative Against the Selection Criteria | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp41-42` | rozdz. 4, s. 41-42 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4p42`, `c26pp447-458` | rozdz. 4, s. 42; rozdz. 26, s. 447-458 |
| 2.7. Monitor the Performance of the Selected Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp42-43` | rozdz. 4, s. 42-43 |
| 3.1. Minimum Acceptable Rate of Return | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c10pp141-143` | rozdz. 10, s. 141-143 |
| 3.2. Economic Life | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c11pp160-164` | rozdz. 11, s. 160-164 |
| 3.3. Planning Horizon | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c11` | rozdz. 11 |
| 3.4. Replacement Decisions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c12pp171-178 c9` | rozdz. 12, s. 171-178, rozdz. 9 |
| 3.5. Retirement Decisions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c12pp178-181 c9` | rozdz. 12, s. 178-181, rozdz. 9 |
| 3.6. Advanced For-Profit Decision Considerations | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c13-17` | rozdz. 13-17 |
| 4.1. Benefit-Cost Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c18pp303-311` | rozdz. 18, s. 303-311 |
| 4.2. Cost-Effectiveness Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c18pp311-314` | rozdz. 18, s. 311-314 |
| 5.1. Break-Even Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c19` | rozdz. 19 |
| 5.2. Optimization Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c20` | rozdz. 20 |
| 6.1. Compensatory Techniques | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c26pp449-458` | rozdz. 26, s. 449-458 |
| 6.2. Non-Compensatory Techniques | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c26pp447-449` | rozdz. 26, s. 447-449 |
| 8.1. Expert Judgment | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp367-369` | rozdz. 22, s. 367-369 |
| 8.2. Analogy | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp369-371` | rozdz. 22, s. 369-371 |
| 8.3. Decomposition | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp371-374` | rozdz. 22, s. 371-374 |
| 8.4. Parametric | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp374-377` | rozdz. 22, s. 374-377 |
| 8.5. Multiple Estimates | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp377-379` | rozdz. 22, s. 377-379 |
| 10.1. Accounting | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c15pp234-245` | rozdz. 15, s. 234-245 |
| 10.2. Cost and Costing | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c15pp245-259` | rozdz. 15, s. 245-259 |
| 10.5. Efficiency and Effectiveness | `[10*]` I. Sommerville, Software Engineering | `c22pp422-23` | rozdz. 22, s. 422-23 |
| 10.6. Productivity | `[10*]` I. Sommerville, Software Engineering | `c23pp689` | rozdz. 23, s. 689 |
| 10.8. Project | `[22*]` R.E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c2s2.4` | rozdz. 2, sekcja 2.4 |
| 10.13. Price and Pricing | `[10*]` I. Sommerville, Software Engineering | `c23s23.1` | rozdz. 23, sekcja 23.1 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (30)</summary>

- 1. Software Engineering Economics Fundamentals
- 1.7. Intangible Assets
- 1.8. Business Model
- 2. The Engineering Decision- Making Process
- 3. For-Profit Decision-Making
- 4. Nonprofit Decision-Making
- 5. Present Economy Decision-Making
- 6. Multiple-Attribute Decision-Making
- 7. Identifying and Characterizing Intangible Assets
- 7.1. Identify Processes and Define Business Goals
- 7.2. Identify Intangible Assets Linked with Business Goals
- 7.3. Identify Software Products That Support Intangible Assets
- 7.4. Define and Measure Indicators
- 7.5. Intangible Asset Characterization
- 7.6. Link Specific Intangible Assets with the Business Model
- 7.7. Decision-Making
- 8. Estimation
- 9. Practical Considerations
- 9.1. Business Case
- 9.2. Multiple-Currency Analysis
- 9.3. Systems Thinking
- 10. Related Concepts
- 10.3. Finance
- 10.4. Controlling
- 10.7. Product or Service
- 10.9. Program
- 10.10. Portfolio
- 10.11. Product Life Cycle
- 10.12. Project Life Cycle
- 10.14. Prioritization

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[1]` E. DeGarmo et al., Engineering Economy |  |  | 1 |
| (wstęp rozdziału) | `[2]` P. Rodriguez, C. Urquhart, and E. Mendes. “A Theory of Value for Value- based Feature Selecti… |  |  | 2 |
| 1.1. Proposals | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c3pp23-24` | rozdz. 3, s. 23-24 | 3 |
| 1.2. Cash Flow | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c3pp24-32` | rozdz. 3, s. 24-32 | 3 |
| 1.3. Time-Value of Money | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c5-6` | rozdz. 5-6 | 3 |
| 1.4. Equivalence | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c7` | rozdz. 7 | 4 |
| 1.5. Bases for Comparison | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c8` | rozdz. 8 | 4 |
| 1.6. Alternatives | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c9` | rozdz. 9 | 4 |
| 1.7. Intangible Assets | `[4]` International Valuation Standards (IVS), Norwich: Page Bros, 2019 |  |  | 4 |
| 1.8. Business Model | `[5]` K. Voigt, O. Buliga, and K. Michl, Business Model Pioneers: How Innovators Successfully Imple… |  |  | 5 |
| 1.8. Business Model | `[6]` M.-I. Sanchez-Segura, G.-L. Dugarte- Peña, A. Amescua-Seco, and F. Medina-Domínguez |  |  | 5 |
| 2.1. Process Overview | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp35-36` | rozdz. 4, s. 35-36 | 5 |
| 2.1. Process Overview | `[7]` ISO/IEC/IEEE 12207-2:2020 – Systems and software engineering — Software life cycle processes… |  |  | 5 |
| 2.1. Process Overview | `[8*]` ISO/IEC/IEEE 15288:2023 – Systems and Software Engineering – System Life Cycle Processes, IEEE |  |  | 5 |
| 2.2. Understand the Real Problem | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp37-39` | rozdz. 4, s. 37-39 | 5 |
| 2.2. Understand the Real Problem | `[9]` T. Brown and B. Katz, Change by Design: How Design Thinking Transforms Organizations and Insp… |  |  | 5 |
| 2.3. Identify All Reasonable Technically Feasible Solutions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp40-41` | rozdz. 4, s. 40-41 | 6 |
| 2.4. Define the Selection Criteria | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp39-40`, `c26pp441-442` | rozdz. 4, s. 39-40; rozdz. 26, s. 441-442 | 6 |
| 2.5. Evaluate Each Alternative Against the Selection Criteria | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp41-42` | rozdz. 4, s. 41-42 | 6 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4p42`, `c26pp447-458` | rozdz. 4, s. 42; rozdz. 26, s. 447-458 | 6 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c21pp344- 356` | rozdz. 21, s. 344-356 | 7 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c23` | rozdz. 23 | 7 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c24` | rozdz. 24 | 7 |
| 2.6. Select the Preferred Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c25` | rozdz. 25 | 7 |
| 2.7. Monitor the Performance of the Selected Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4pp42-43` | rozdz. 4, s. 42-43 | 7 |
| 2.7. Monitor the Performance of the Selected Alternative | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c21pp356- 358` | rozdz. 21, s. 356-358 | 7 |
| 3.1. Minimum Acceptable Rate of Return | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c10pp141-143` | rozdz. 10, s. 141-143 | 7 |
| 3.2. Economic Life | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c11pp160-164` | rozdz. 11, s. 160-164 | 7 |
| 3.3. Planning Horizon | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c11` | rozdz. 11 | 8 |
| 3.4. Replacement Decisions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c12pp171-178` | rozdz. 12, s. 171-178 | 8 |
| 3.4. Replacement Decisions | `[8*]` ISO/IEC/IEEE 15288:2023 – Systems and Software Engineering – System Life Cycle Processes, IEEE | `c9` | rozdz. 9 | 8 |
| 3.5. Retirement Decisions | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c12pp178-181` | rozdz. 12, s. 178-181 | 9 |
| 3.5. Retirement Decisions | `[8*]` ISO/IEC/IEEE 15288:2023 – Systems and Software Engineering – System Life Cycle Processes, IEEE | `c9` | rozdz. 9 | 9 |
| 3.6. Advanced For-Profit Decision Considerations | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c13-17` | rozdz. 13-17 | 9 |
| 4.1. Benefit-Cost Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c18pp303-311` | rozdz. 18, s. 303-311 | 9 |
| 4.2. Cost-Effectiveness Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c18pp311-314` | rozdz. 18, s. 311-314 | 9 |
| 5.1. Break-Even Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c19` | rozdz. 19 | 9 |
| 5.2. Optimization Analysis | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c20` | rozdz. 20 | 9 |
| 6. Multiple-Attribute Decision-Making | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c26` | rozdz. 26 | 10 |
| 6.1. Compensatory Techniques | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c26pp449-458` | rozdz. 26, s. 449-458 | 10 |
| 6.1. Compensatory Techniques | `[11]` T. Gilb, Competitive Engineering: A Handbook for Systems Engineering, Requirements Engineering |  |  | 10 |
| 6.1. Compensatory Techniques | `[12]` R. Kazman, M. Klein, and P. Clements, “ATAMSM: Method for Architecture Evaluation |  |  | 10 |
| 6.2. Non-Compensatory Techniques | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c26pp447-449` | rozdz. 26, s. 447-449 | 10 |
| 7. Identifying and Characterizing Intangible Assets | `[13]` M.I. Sanchez-Segura, A. Ruiz- Robles, F. Medina-Domínguez, and G.L. Dugarte-Peña. “Strategic… |  |  | 10 |
| 7.2. Identify Intangible Assets Linked with Business Goals | `[14]` M.I. Sanchez-Segura, A. Ruiz Robles, F.Medina-Domínguez. “Uncovering Hidden Process Assets: A… |  |  | 11 |
| 7.2. Identify Intangible Assets Linked with Business Goals | `[6]` M.-I. Sanchez-Segura, G.-L. Dugarte- Peña, A. Amescua-Seco, and F. Medina-Domínguez |  |  | 11 |
| 7.3. Identify Software Products That Support Intangible Assets | `[13]` M.I. Sanchez-Segura, A. Ruiz- Robles, F. Medina-Domínguez, and G.L. Dugarte-Peña. “Strategic… |  |  | 11 |
| 7.6. Link Specific Intangible Assets with the Business Model | `[6]` M.-I. Sanchez-Segura, G.-L. Dugarte- Peña, A. Amescua-Seco, and F. Medina-Domínguez |  |  | 13 |
| 8. Estimation | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c21-26` | rozdz. 21-26 | 13 |
| 8. Estimation | `[16]` D. Gotterbarn, K. Miller, and S. Rogerson, “Software Engineering Code of Ethics |  |  | 14 |
| 8. Estimation | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c21pp358-361` | rozdz. 21, s. 358-361 | 14 |
| 8. Estimation | `[17]` S. McConnell, Software Estimation: Demystifying the Black Art |  |  | 14 |
| 8. Estimation | `[18]` R.D. Stutzke, Estimating Software- Intensive Systems Projects, Products, and Processes |  |  | 14 |
| 8. Estimation | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment |  |  | 14 |
| 8.1. Expert Judgment | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp367-369` | rozdz. 22, s. 367-369 | 14 |
| 8.2. Analogy | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp369-371` | rozdz. 22, s. 369-371 | 15 |
| 8.3. Decomposition | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp371-374` | rozdz. 22, s. 371-374 | 15 |
| 8.4. Parametric | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp374-377` | rozdz. 22, s. 374-377 | 15 |
| 8.5. Multiple Estimates | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c22pp377-379` | rozdz. 22, s. 377-379 | 15 |
| 9.3. Systems Thinking | `[19]` M. Ben-Eli, Understanding Systems. Systems Innovation, https://netzerocities. app/_content/fi… |  |  | 16 |
| 9.3. Systems Thinking | `[20]` J. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World |  |  | 16 |
| 9.3. Systems Thinking | `[21]` S. Pereira, G. Medina, et al., “System Thinking and Business Model Canvas for Collaborative B… |  |  | 16 |
| 10.1. Accounting | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c15pp234-245` | rozdz. 15, s. 234-245 | 16 |
| 10.2. Cost and Costing | `[3*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c15pp245-259` | rozdz. 15, s. 245-259 | 16 |
| 10.5. Efficiency and Effectiveness | `[10*]` I. Sommerville, Software Engineering | `c22pp422-23` | rozdz. 22, s. 422-23 | 17 |
| 10.6. Productivity | `[10*]` I. Sommerville, Software Engineering | `c23pp689` | rozdz. 23, s. 689 | 18 |
| 10.6. Productivity | `[23]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) |  |  | 18 |
| 10.8. Project | `[22*]` R.E. Fairley, Managing and Leading Software Projects, Wiley-IEEE Computer Society Press | `c2s2.4` | rozdz. 2, sekcja 2.4 | 18 |
| 10.8. Project | `[24]` Project Management Institute, PMI Lexicon of Project Management Term, 2012 |  |  | 18 |
| 10.9. Program | `[24]` Project Management Institute, PMI Lexicon of Project Management Term, 2012 |  |  | 18 |
| 10.10. Portfolio | `[24]` Project Management Institute, PMI Lexicon of Project Management Term, 2012 |  |  | 18 |
| 10.12. Project Life Cycle | `[23]` Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK® Guide) |  |  | 19 |
| 10.12. Project Life Cycle | `[20*]` J. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World | `c2` | rozdz. 2 | 19 |
| 10.12. Project Life Cycle | `[25]` Project Management Institute and IEEE Computer Society, Software Extension to the PMBOK® Guid… |  |  | 19 |
| 10.13. Price and Pricing | `[10*]` I. Sommerville, Software Engineering | `c23s23.1` | rozdz. 23, sekcja 23.1 | 19 |

---

## KA 16 — Computing Foundations

Plik źródłowy: `chapter16/swebok-v4-ch16.pdf` · macierz tematów na stronach PDF: 28, 29, 30, 31

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | Joint Task Force on Computing Curricula, IEEE Computer Society and Association for Computing Machinery, Software Engineering 2014: Curriculum Guidelines for Undergraduate Degree Programs in Software Engineering, 2014; http://sites.computer.org/ccse/ SE2004Volume.pdf. |
| `[2*]` | ★ | G. Voland, Engineering by Design, 2nd ed., Prentice Hall, 2003. |
| `[3*]` | ★ | S. McConnell, Code Complete, 2nd ed., Microsoft Press, 2004. |
| `[4*]` | ★ | J.G. Brookshear, Computer Science: An Overview, 12th ed., Addison- Wesley, 2017. |
| `[5*]` | ★ | E. Horowitz et al., Computer Algorithms, 2nd ed., Silicon Press, 2007. |
| `[6*]` | ★ | I. Sommerville, Software Engineering, 10th ed., Addison-Wesley, 2016. |
| `[7]` |  | ISO/IEC/IEEE, “ISO/IEC/IEEE 24765:2017 Systems and Software Engineering — Vocabulary,” 2nd ed. 2017. |
| `[8*]` | ★ | L. Null and J. Lobur, The Essentials of Computer Organization and Architecture, 5th ed., Jones and Bartlett Publishers, 2018. |
| `[9*]` | ★ | J. Nielsen, Usability Engineering, Morgan Kaufmann, 1994. |
| `[10]` |  | ISO 9241-420:2011 Ergonomics of Human-System Interaction, ISO, 2011. |
| `[11*]` | ★ | M. Bishop, Computer Security: Art and Science, 2 ed, Addison-Wesley, 2018. |
| `[12]` |  | R.C. Seacord, The CERT C Secure Coding Standard, Addison-Wesley Professional, 2016. |
| `[13]` |  | R. Fagin, “ A Normal Form for Relational Databases that is based on Domains and Keys, ” ACM Transactions on Database Systems, Vol. 6, No. 3, ACM, September 1981 |
| `[14]` |  | I. Goodfellow, Y. Bengio, A. Courville, Deep Learning (Adaptive Computation and Machine Learning series) Illustrated Edition, 2018. |
| `[15]` |  | S. Shafiq, A. Mashkoor, C. Mayr- Dorn, A. Egyed, “A Literature Review of Using Machine Learning in Software Development Life Cycle Stages,” IEEE Access, Volume 9, IEEE, October 2021. |
| `[16]` |  | S. Martínez-Fernández, J. Bogner, X.Franch, M. Oriol, J. Siebert, A. Trendowicz, A. M. Vollmer, “Software Engineering for AI-Based Systems: A Survey,” ACM Transactions on Software Engineering and Methodology, Vol. 31, No. 2, ACM, April 2022. |
| `[17*]` | ★ | H. Washizaki, F. Khomh, Y. G. Gueheneuc, H. Takeuchi, N. Natori, T. Doi, S. Okuda, “Software Engineering Design Patterns for Machine Learning Applications,” Computer, Vol. 55, No. 3, IEEE Computer Society, March 2022. |
| `[18*]` | ★ | Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algorithms,” Fourth Edition, 2022. |
| `[19*]` | ★ | Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems,” 4e, 2016. |
| `[20]` |  | https://ieeexplore.ieee.org/document /9779481 |
| `[21]` |  | Neal Ford, Mark Richards, Pramod Sadalage and Zhamak Dehgh, Software Architecture: The Hard Parts, O Reilly, First Edition – 2021 |
| `[22]` |  | Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design, Implementation and Management, 6th Edition – Pearson |
| `[23]` |  | Michael J. Hernandez, Database Design For Mere Mortals, 4th Edition, Addison-Wesley |
| `[24]` |  | James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach, 7th Edition, Pearson |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. Basic Concept of a System or Solution | `[6*]` I. Sommerville, Software Engineering | `C10` | rozdz. 10 |
| 2.1 Computer Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.1` | rozdz. 1.1 |
| 2.2 Types of Computer Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.14`, `C5` | rozdz. 4.14; rozdz. 5 |
| 2.2.1 Von Neumann Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.9` | rozdz. 1.9 |
| 2.2.2 Harward Architecture | Articles and Journals: `[20]` https://ieeexplore.ieee.org/document /9779481 |  |  |
| 2.2.3 Instruction Set Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.8.3` | rozdz. 4.8.3 |
| 2.2.4 Flynn’s Architecture or Taxonomy | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C9.3` | rozdz. 9.3 |
| 2.2.5 System Architecture | `[6*]` I. Sommerville, Software Engineering | `C6` | rozdz. 6 |
| 2.2.5 System Architecture | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6` | rozdz. 6 |
| 2.3 Micro Architecture or Computer Organization | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4` | rozdz. 4 |
| 2.3.1 Arithmetic Logic Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.2` | rozdz. 1.2 |
| 2.3.2 Memory Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C6` | rozdz. 6 |
| 2.3.3 Input / Output Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C7` | rozdz. 7 |
| 2.3.4 Control Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.2` | rozdz. 4.2 |
| 3. Data Structures and Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `c10`, `Part V` | rozdz. 10; część V |
| 3. Data Structures and Algorithms | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C2` | rozdz. 2 |
| 3.1 Types of Data Structures | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `c10` | rozdz. 10 |
| 3.1 Types of Data Structures | `[5*]` E. Horowitz et al., Computer Algorithms | `S2.1-2.6` | sekcja 2.1-2.6 |
| 3.2 Operations on Data Structures | `[5*]` E. Horowitz et al., Computer Algorithms | `S2.1-2.6` | sekcja 2.1-2.6 |
| 3.3 Algorithms and Attributes of Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `c26`, `c27` | rozdz. 26; rozdz. 27 |
| 3.4 Algorithm Complexity | `[5*]` E. Horowitz et al., Computer Algorithms | `s1.1-1.3`, `s3.3-3.6`, `s4.1-4.8`, `s5.1-5.7`, `s6.1-6.3`, `7.6`, `s11.1`, `s12.1` | sekcja 1.1-1.3; sekcja 3.3-3.6; sekcja 4.1-4.8; sekcja 5.1-5.7; sekcja 6.1-6.3; sekcja 11.1; sekcja 12.1 |
| 3.5 Measurement of Complexity | `[5*]` E. Horowitz et al., Computer Algorithms | `s1.1-s3.3- 3.6`, `s4.1-4.8`, `s5.1-5.7`, `s6.1-6.3`, `s7.1-7.6`, `s11.1`, `s12.1` | sekcja 4.1-4.8; sekcja 5.1-5.7; sekcja 6.1-6.3; sekcja 7.1-7.6; sekcja 11.1; sekcja 12.1 |
| 3.6 Designing Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `Part IV`, `Part VII` | część IV; część VII |
| 3.7 Sorting Techniques | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `c6`, `c7`, `c8`, `c9` | rozdz. 6; rozdz. 7; rozdz. 8; rozdz. 9 |
| 3.8 Searching Techniques | `[5*]` E. Horowitz et al., Computer Algorithms | `C6` | rozdz. 6 |
| 3.9 Hashing | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `c11.2` | rozdz. 11.2 |
| 4. Programming Fundamentals and Languages | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6` | rozdz. 6 |
| 4.1 Programming Language Types | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C8.4.4` | rozdz. 8.4.4 |
| 4.2 Programming Syntax, Semantics, Type Systems | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C8.4.4` | rozdz. 8.4.4 |
| 4.3 Subprograms and Coroutines | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.3` | rozdz. 6.3 |
| 4.4 Object- Oriented Programming | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.5` | rozdz. 6.5 |
| 4.5 Distributed Programming and Parallel Programming | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.6` | rozdz. 6.6 |
| 4.6 Debugging | `[6*]` I. Sommerville, Software Engineering | `C2.2.2` | rozdz. 2.2.2 |
| 4.7 Standards and Guidelines | `[3*]` S. McConnell, Code Complete | `C28.5`, `C31.5` | rozdz. 28.5; rozdz. 31.5 |
| 5.1 Processor Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `c2`, `c8` | rozdz. 2; rozdz. 8 |
| 5.2 Memory Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `c3` | rozdz. 3 |
| 5.3 Device Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `c5` | rozdz. 5 |
| 5.4 Information Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `c4` | rozdz. 4 |
| 5.5 Network Management | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 |
| 6.1 Schema | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C2.1.4` | rozdz. 2.1.4 |
| 6.2 Data Models and Storage Models | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C2.3` | rozdz. 2.3 |
| 6.3 Database Management Systems | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C1.3` | rozdz. 1.3 |
| 6.4 Relational Database Management Systems and Normalization | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C4` | rozdz. 4 |
| 6.5 Structured Query Language | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C6`, `C7`, `C8` | rozdz. 6; rozdz. 7; rozdz. 8 |
| 6.6 Data Mining and Data Warehousing | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C34` | rozdz. 34 |
| 6.7 Database Backup and Recovery | `[22]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C22` | rozdz. 22 |
| 7. Computer Networks and Communications | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 |
| 7. Computer Networks and Communications | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1` | rozdz. 1 |
| 7.1 Types of Computer Networks | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 |
| 7.1 Types of Computer Networks | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.2.1` | rozdz. 1.2.1 |
| 7.2 Layered Architecture of Networks | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 |
| 7.3 Open Systems Interconnection Model | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 |
| 7.4 Encapsulation and Decapsulation | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5.2` | rozdz. 1.5.2 |
| 7.5 Application Layer Protocols | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C2` | rozdz. 2 |
| 7.6 Design Techniques for Reliable and Efficient Network | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 |
| 7.7 Internet Protocol Suite | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C3` | rozdz. 3 |
| 7.8 Wireless and Mobile Networks | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C7` | rozdz. 7 |
| 7.9 Security and Vulnerabilities | `[24]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C8` | rozdz. 8 |
| 8.1 User Human Factors | `[3*]` S. McConnell, Code Complete | `c8` | rozdz. 8 |
| 8.2. Developer Human Factors | `[3*]` S. McConnell, Code Complete | `c31- c32` | rozdz. 31-32 |
| 9. Artificial Intelligence and Machine Learning | `[17*]` H. Washizaki, F. Khomh, Y. G. Gueheneuc, H. Takeuchi, N. Natori, T. Doi, S. Okuda | `C1` | rozdz. 1 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (10)</summary>

- 2. Computer Architecture and Organization
- 5. Operating Systems
- 6. Database Management
- 8. User and Developer Human Factors
- 9.1 Reasoning
- 9.2 Learning
- 9.3 Models
- 9.4 Perception and Problem-Solving
- 9.5 Natural Language Processing
- 9.6 AI and Software Engineering

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1. Basic Concept of a System or Solution | `[6*]` I. Sommerville, Software Engineering | `C10` | rozdz. 10 | 2 |
| 2. Computer Architecture and Organization | `[6*]` I. Sommerville, Software Engineering | `C6` | rozdz. 6 | 3 |
| 2.1. Computer Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.1` | rozdz. 1.1 | 3 |
| 2.2. Types of Computer Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.14`, `C5` | rozdz. 4.14; rozdz. 5 | 3 |
| 2.2.1. Von Neumann Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.9` | rozdz. 1.9 | 3 |
| 2.2.1. Von Neumann Architecture | `[20*]` https://ieeexplore.ieee.org/document /9779481 |  |  | 4 |
| 2.2.3. Instruction Set Architecture | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.8.3` | rozdz. 4.8.3 | 4 |
| 2.2.4. Flynn’s Architecture or Taxonomy | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C9.3` | rozdz. 9.3 | 5 |
| 2.2.5. System Architecture | `[6*]` I. Sommerville, Software Engineering | `C6` | rozdz. 6 | 5 |
| 2.3. Micro Architecture or Computer Organization | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4` | rozdz. 4 | 5 |
| 2.3.1. Arithmetic Logic Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C1.2` | rozdz. 1.2 | 5 |
| 2.3.2. Memory Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C6` | rozdz. 6 | 6 |
| 2.3.3. Input / Output Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C7` | rozdz. 7 | 6 |
| 2.3.4. Control Unit | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C4.2` | rozdz. 4.2 | 6 |
| 3. Data Structures and Algorithms | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C2` | rozdz. 2 | 6 |
| 3. Data Structures and Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `C10 Part V` | rozdz. 10, część V | 6 |
| 3.1. Types of Data Structures | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `C10` | rozdz. 10 | 6 |
| 3.1. Types of Data Structures | `[5*]` E. Horowitz et al., Computer Algorithms | `C2.1 - 2.6` | rozdz. 2.1-2.6 | 6 |
| 3.2. Operations on Data Structures | `[5*]` E. Horowitz et al., Computer Algorithms | `C2.1 - 2.6` | rozdz. 2.1-2.6 | 7 |
| 3.3. Algorithms and Attributes of Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `C26`, `C27` | rozdz. 26; rozdz. 27 | 7 |
| 3.4. Algorithm Complexity | `[5*]` E. Horowitz et al., Computer Algorithms | `S1`, `S3`, `S4`, `S5`, `S6`, `S7`, `S11`, `S12` | sekcja 1; sekcja 3; sekcja 4; sekcja 5; sekcja 6; sekcja 7; sekcja 11; sekcja 12 | 8 |
| 3.5. Measurement of Complexity | `[5*]` E. Horowitz et al., Computer Algorithms | `S1.1`, `S3`, `S4`, `S5`, `S6`, `S11.1`, `S12.1` | sekcja 1.1; sekcja 3; sekcja 4; sekcja 5; sekcja 6; sekcja 11.1; sekcja 12.1 | 8 |
| 3.6. Designing Algorithms | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `Part IV`, `Part VI` | część IV; część VI | 8 |
| 3.7. Sorting Techniques | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `C6-C9` | rozdz. 6-9 | 9 |
| 3.8. Searching Techniques | `[5*]` E. Horowitz et al., Computer Algorithms | `C6` | rozdz. 6 | 10 |
| 3.9. Hashing | `[18*]` Thomas H Cormen, Charles E Leiserson, Ronald L Rivest, Clifford Stein, “Introduction to Algor… | `C11.2` | rozdz. 11.2 | 10 |
| 4. Programming Fundamentals and Languages | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6` | rozdz. 6 | 10 |
| 4.1. Programming Language Types | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C8.4.4` | rozdz. 8.4.4 | 10 |
| 4.2. Programming Syntax, Semantics, Type Systems | `[8*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `C8.4.4` | rozdz. 8.4.4 | 11 |
| 4.3. Subprograms and Coroutines | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.3` | rozdz. 6.3 | 11 |
| 4.4. Object- Oriented Programming | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.5` | rozdz. 6.5 | 12 |
| 4.5. Distributed Programming and Parallel Programming | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C6.6` | rozdz. 6.6 | 13 |
| 4.6. Debugging | `[6*]` I. Sommerville, Software Engineering | `C2.2.2` | rozdz. 2.2.2 | 13 |
| 4.7. Standards and Guidelines | `[3*]` S. McConnell, Code Complete | `C28.5`, `C31.5` | rozdz. 28.5; rozdz. 31.5 | 13 |
| 5. Operating Systems | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 |  |  | 15 |
| 5.1. Processor Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `C2`, `C8` | rozdz. 2; rozdz. 8 | 15 |
| 5.2. Memory Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `C3` | rozdz. 3 | 16 |
| 5.3. Device Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `C5` | rozdz. 5 | 16 |
| 5.4. Information Management | `[19*]` Andrew W Tanenbaum, Herbert Bos, “Modern Operating Systems, ” 4e, 2016 | `C4` | rozdz. 4 | 16 |
| 5.5. Network Management | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 | 16 |
| 6.1. Schema | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C2.1.4` | rozdz. 2.1.4 | 17 |
| 6.2. Data Models and Storage Models | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C2.3` | rozdz. 2.3 | 17 |
| 6.3. Database Management Systems | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C1.3` | rozdz. 1.3 | 18 |
| 6.4. Relational Database Management Systems and Normalization | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C4` | rozdz. 4 | 18 |
| 6.4. Relational Database Management Systems and Normalization | `[13]` R. Fagin, “ A Normal Form for Relational Databases that is based on Domains and Keys |  |  | 19 |
| 6.5. Structured Query Language | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C6`, `C7`, `C8` | rozdz. 6; rozdz. 7; rozdz. 8 | 19 |
| 6.6. Data Mining and Data Warehousing | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C34` | rozdz. 34 | 19 |
| 6.7. Database Backup and Recovery | `[22*]` Thomas Connolly, Carolyn Begg, Database Systems - A Practical Approach to Design | `C22` | rozdz. 22 | 20 |
| 7. Computer Networks and Communications | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 | 20 |
| 7. Computer Networks and Communications | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1` | rozdz. 1 | 20 |
| 7.1. Types of Computer Networks | `[4*]` J.G. Brookshear, Computer Science: An Overview | `C4.1` | rozdz. 4.1 | 20 |
| 7.1. Types of Computer Networks | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.2.1` | rozdz. 1.2.1 | 20 |
| 7.2. Layered Architecture of Networks | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 | 21 |
| 7.3. Open Systems Interconnection Model | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 | 21 |
| 7.4. Encapsulation and Decapsulation | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5.2` | rozdz. 1.5.2 | 22 |
| 7.5. Application Layer Protocols | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C2` | rozdz. 2 | 22 |
| 7.6. Design Techniques for Reliable and Efficient Network | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C1.5` | rozdz. 1.5 | 22 |
| 7.7. Internet Protocol Suite | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C3` | rozdz. 3 | 23 |
| 7.9. Security and Vulnerabilities | `[24*]` James F Kurose, Keith W Ross, Computer Networking - A Top-Down Approach | `C9` | rozdz. 9 | 23 |
| 8.1. User Human Factors | `[3*]` S. McConnell, Code Complete | `C8` | rozdz. 8 | 24 |
| 8.2. Developer Human Factors | `[3*]` S. McConnell, Code Complete | `C31 - C32` | rozdz. 31-32 | 24 |
| 9. Artificial Intelligence and Machine Learning | `[17*]` H. Washizaki, F. Khomh, Y. G. Gueheneuc, H. Takeuchi, N. Natori, T. Doi, S. Okuda |  |  | 25 |
| 9.6. AI and Software Engineering | `[15]` S. Shafiq, A. Mashkoor, C. Mayr- Dorn, A. Egyed, “A Literature Review of Using Machine Learni… |  |  | 27 |
| 9.6. AI and Software Engineering | `[16]` S. Martínez-Fernández, J. Bogner, X.Franch, M. Oriol, J. Siebert, A. Trendowicz |  |  | 27 |

---

## KA 17 — Mathematical Foundations

Plik źródłowy: `chapter17/swebok-v4-ch17.pdf` · macierz tematów na stronach PDF: 22

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1*]` | ★ | K. Rosen, Discrete Mathematics and Its Applications, 8th ed., McGraw-Hill, 2018. |
| `[2*]` | ★ | E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing, 7th ed., Addison Wesley, 2020. |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. Basic Logic | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c1` | rozdz. 1 |
| 2. Proof Techniques | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c1` | rozdz. 1 |
| 3. Set, Relation, Function | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c2` | rozdz. 2 |
| 4. Graph and Tree | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c10`, `c11` | rozdz. 10; rozdz. 11 |
| 5. Finite State Machine | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c13` | rozdz. 13 |
| 6. Grammar | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c13` | rozdz. 13 |
| 7. Number Theory | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c4` | rozdz. 4 |
| 8. Basics of Counting | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c6` | rozdz. 6 |
| 9. Discrete Probability | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c7` | rozdz. 7 |
| 10. Numerical Precision, Accuracy and Error | `[2*]` E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing | `c1` | rozdz. 1 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (2)</summary>

- 11. Algebraic Structures
- 12. Calculus

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| 1. Basic Logic | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c1` | rozdz. 1 | 1 |
| 2. Proof Techniques | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c1` | rozdz. 1 | 3 |
| 3. Set, Relation, Function | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c2` | rozdz. 2 | 5 |
| 4. Graph and Tree | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c10`, `c11` | rozdz. 10; rozdz. 11 | 8 |
| 4. Graph and Tree | `[1*]` K. Rosen, Discrete Mathematics and Its Applications |  |  | 11 |
| 5. Finite State Machine | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c13` | rozdz. 13 | 12 |
| 6. Grammar | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c13` | rozdz. 13 | 13 |
| 7. Number Theory | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c4` | rozdz. 4 | 14 |
| 8. Basics of Counting | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c6` | rozdz. 6 | 16 |
| 9. Discrete Probability | `[1*]` K. Rosen, Discrete Mathematics and Its Applications | `c7` | rozdz. 7 | 17 |
| 10. Numerical Precision, Accuracy and Error | `[2*]` E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing | `c1` | rozdz. 1 | 18 |

---

## KA 18 — Engineering Foundations

Plik źródłowy: `chapter18/swebok-v4-ch18.pdf` · macierz tematów na stronach PDF: 18, 19

### Bibliografia rozdziału (`REFERENCES`)

| Nr | Rekomendowana | Pozycja |
|---|---|---|
| `[1]` |  | ISO/IEC/IEEE 24765:2017, Systems and Software Engineering — Vocabulary. |
| `[2*]` | ★ | S. Tockey, Return on Software: Maximizing the Return on Your Software Investment, 1st ed., Addison- Wesley, 2004. |
| `[3*]` | ★ | G. Voland, Engineering by Design, 2nd ed., Prentice Hall, 2003. |
| `[4]` |  | “2021 Accreditation Criteria and Procedures,” Canadian Engineering Accreditation Board, Engineers Canada, 2021. |
| `[5]` |  | E.A. Commission, “Criteria for Accrediting Engineering Programs, 2022-2023,” ABET, 2021. |
| `[6*]` | ★ | S. McConnell, Code Complete, 2nd ed., Microsoft Press, 2004. |
| `[7]` |  | Edsger W. Dijkstra, “The Humble Programmer,” Communications of the ACM, vol. 15, issue 10, October 1972. |
| `[8*]` | ★ | D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers, 7th ed. Hoboken, NJ: Wiley, 2018. |
| `[9*]` | ★ | L. Null and J. Lobur, The Essentials of Computer Organization and Architecture, 5th ed. Sudbury, MA: Jones and Bartlett Publishers, 2018. |
| `[10*]` | ★ | E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing, 7th ed. Belmont, CA: Brooks/Cole, 2020. |
| `[11*]` | ★ | I. Sommerville, Software Engineering, 10th ed. New York: Addison- Wesley, 2016. |
| `[12*]` | ★ | R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Society Press, 2009. |
| `[13*]` | ★ | S.H. Kan, Metrics and Models in Software Quality Engineering, 2nd ed. Boston: Addison-Wesley, 2002. |
| `[14]` |  | J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide, 1st ed. Hoboken, NJ: Wiley-IEEE Computer Society Press, 2006. |
| `[15]` |  | K. Ishikawa, Introduction to Quality Control, Productivity Press, 1990. |
| `[16]` |  | D. Gano, Apollo Root Cause Analysis, 3rd ed., Apollonian Publications, 2007. |
| `[17]` |  | E. Goldratt, It’s Not Luck, North River Press, 1994. |
| `[18]` |  | A. Abran, Software Metrics and Software Metrology : Wiley-IEEE Computer Society Press, 2010. |
| `[19]` |  | W.G. Vincenti, What Engineers Know and How They Know It. Johns Hopkins University Press, 1993. |
| `[20]` |  | Elisa Yumi Nakagawa, Pablo Oliveira Antonio, Frank Schnicke, Thomas Kuhn, Peter Liggesmeyer, Continuous Systems and Software Engineering for Industry 4.0: A disruptive view, Elsevier, Volume 135, July 2021, 106562 (https: //www.sciencedirect.com/science /article/abs/pii/S0950584921000458.) |

### Macierz: podrozdział → literatura → miejsce w źródle

| Podrozdział SWEBOK | Pozycja | Lokalizacja (oryginał) | Gdzie szukać |
|---|---|---|---|
| 1. The Engineering Process | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4` | rozdz. 4 |
| 2. Engineering Design | `[3*]` G. Voland, Engineering by Design | `c1s2-4` | rozdz. 1, sekcja 2-4 |
| 2.2. Design as a Problem- Solving Activity | `[3*]` G. Voland, Engineering by Design | `c1s4`, `c2s1`, `c3s3` | rozdz. 1, sekcja 4; rozdz. 2, sekcja 1; rozdz. 3, sekcja 3 |
| 2.2. Design as a Problem- Solving Activity | `[6*]` S. McConnell, Code Complete | `c5s1` | rozdz. 5, sekcja 1 |
| 3. Abstraction and Encapsulation | `[6*]` S. McConnell, Code Complete | `c5s2-4` | rozdz. 5, sekcja 2-4 |
| 4. Empirical Methods and Experimental Techniques | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c1` | rozdz. 1 |
| 5. Statistical Analysis | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c9s1`, `c2s1` | rozdz. 9, sekcja 1; rozdz. 2, sekcja 1 |
| 5. Statistical Analysis | `[9*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c11s3` | rozdz. 11, sekcja 3 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c3s5`, `c3s8`, `c4s5`, `c7s1`, `c7s3`, `c8s1`, `c9s1` | rozdz. 3, sekcja 5; rozdz. 3, sekcja 8; rozdz. 4, sekcja 5; rozdz. 7, sekcja 1; rozdz. 7, sekcja 3; rozdz. 8, sekcja 1; rozdz. 9, sekcja 1 |
| 5.2. Correlation and Regression | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c11s2`, `c11s8` | rozdz. 11, sekcja 2; rozdz. 11, sekcja 8 |
| 6. Modeling, Simulation and Prototyping | `[3*]` G. Voland, Engineering by Design | `c6` | rozdz. 6 |
| 6. Modeling, Simulation and Prototyping | `[10*]` E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing | `c10s3` | rozdz. 10, sekcja 3 |
| 6. Modeling, Simulation and Prototyping | `[11*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 |
| 6.3. Prototyping | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c2s8` | rozdz. 2, sekcja 8 |
| 7. Measurement | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `pp 442- 447` | s. 442-447 |
| 7. Measurement | `[3*]` G. Voland, Engineering by Design | `c4s4` | rozdz. 4, sekcja 4 |
| 7. Measurement | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c7s5` | rozdz. 7, sekcja 5 |
| 7. Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s1-2` | rozdz. 3, sekcja 1-2 |
| 7.1. Levels (Scales) of Measurement | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `p442- 447` | s. 442-447 |
| 7.1. Levels (Scales) of Measurement | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c7s5` | rozdz. 7, sekcja 5 |
| 7.1. Levels (Scales) of Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s2` | rozdz. 3, sekcja 2 |
| 7.3. Direct and Derived Measures | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c7s5` | rozdz. 7, sekcja 5 |
| 7.4. Reliability and Validity | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s4-5` | rozdz. 3, sekcja 4-5 |
| 7.5. Assessing Reliability | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s5` | rozdz. 3, sekcja 5 |
| 8. Standards | `[3*]` G. Voland, Engineering by Design | `c9s3.2` | rozdz. 9, sekcja 3.2 |
| 9. Root Cause Analysis | `[3*]` G. Voland, Engineering by Design | `c9s3-5` | rozdz. 9, sekcja 3-5 |
| 9. Root Cause Analysis | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c5`, `c3s7`, `c9s8` | rozdz. 5; rozdz. 3, sekcja 7; rozdz. 9, sekcja 8 |
| 9.1. Root Cause Analysis Techniques | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4` | rozdz. 4 |

<details><summary>Podrozdziały bez wskazania literatury w macierzy (14)</summary>

- 2.1. Engineering Design in Engineering Education
- 3.1. Levels of Abstraction
- 3.2. Encapsulation
- 3.3. Hierarchy
- 3.4. Alternate Abstractions
- 4.1. Designed Experiment
- 4.2. Observational Study
- 4.3. Retrospective Study
- 6.1. Modeling
- 6.2. Simulation
- 7.2. Implications of Measurement Theory for Programming Languages
- 7.6. Goal-Question- Metric Paradigm: Why Measure?
- 9.2. Root Cause-Based Improvement
- 10. Industry 4.0 and Software Engineering

</details>

### Cytowania w treści rozdziału

| Podrozdział (kontekst) | Pozycja | Lokalizacja (oryginał) | Gdzie szukać | Strona PDF |
|---|---|---|---|---|
| (wstęp rozdziału) | `[1]` ISO/IEC/IEEE 24765:2017, Systems and Software Engineering — Vocabulary |  |  | 1 |
| 1. The Engineering Process | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4` | rozdz. 4 | 1 |
| 2. Engineering Design | `[3*]` G. Voland, Engineering by Design | `c1s2-s4` | rozdz. 1, sekcja 2-4 | 2 |
| 2.1. Engineering Design in Engineering Education | `[4]` “2021 Accreditation Criteria and Procedures, ” Canadian Engineering Accreditation Board | `p7` | s. 7 | 3 |
| 2.1. Engineering Design in Engineering Education | `[5]` E.A. Commission, “Criteria for Accrediting Engineering Programs, 2022-2023 | `p7` | s. 7 | 3 |
| 2.2. Design as a Problem- Solving Activity | `[3*]` G. Voland, Engineering by Design | `c1s4`, `c2s1`, `c3s3` | rozdz. 1, sekcja 4; rozdz. 2, sekcja 1; rozdz. 3, sekcja 3 | 3 |
| 2.2. Design as a Problem- Solving Activity | `[6*]` S. McConnell, Code Complete | `c5s1` | rozdz. 5, sekcja 1 | 3 |
| 3. Abstraction and Encapsulation | `[6*]` S. McConnell, Code Complete | `c5s2-4` | rozdz. 5, sekcja 2-4 | 3 |
| 3. Abstraction and Encapsulation | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment |  |  | 4 |
| 3. Abstraction and Encapsulation | `[7]` Edsger W. Dijkstra, “The Humble Programmer, ” Communications of the ACM |  |  | 4 |
| 4. Empirical Methods and Experimental Techniques | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c1` | rozdz. 1 | 4 |
| 5. Statistical Analysis | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c9s1`, `c2s1` | rozdz. 9, sekcja 1; rozdz. 2, sekcja 1 | 5 |
| 5. Statistical Analysis | `[9*]` L. Null and J. Lobur, The Essentials of Computer Organization and Architecture | `c11s3` | rozdz. 11, sekcja 3 | 5 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c3s5` | rozdz. 3, sekcja 5 | 6 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c3s8` | rozdz. 3, sekcja 8 | 6 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c4s5` | rozdz. 4, sekcja 5 | 6 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c7s1`, `c7s3` | rozdz. 7, sekcja 1; rozdz. 7, sekcja 3 | 7 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c7s3`, `c8s1` | rozdz. 7, sekcja 3; rozdz. 8, sekcja 1 | 7 |
| 5.1. Unit of Analysis (Sampling Units), Population and Sample | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c9s1` | rozdz. 9, sekcja 1 | 7 |
| 5.2. Correlation and Regression | `[8*]` D.C. Montgomery and G.C. Runger, Applied Statistics and Probability for Engineers | `c11s2`, `c11s8` | rozdz. 11, sekcja 2; rozdz. 11, sekcja 8 | 8 |
| 6. Modeling, Simulation and Prototyping | `[3*]` G. Voland, Engineering by Design | `c6` | rozdz. 6 | 8 |
| 6. Modeling, Simulation and Prototyping | `[10*]` E.W. Cheney and D.R. Kincaid, Numerical Mathematics and Computing | `c10s3` | rozdz. 10, sekcja 3 | 8 |
| 6. Modeling, Simulation and Prototyping | `[11*]` I. Sommerville, Software Engineering | `c5` | rozdz. 5 | 8 |
| 6.3. Prototyping | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c2s8` | rozdz. 2, sekcja 8 | 9 |
| 7. Measurement | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `pp442-447` | s. 442-447 | 10 |
| 7. Measurement | `[3*]` G. Voland, Engineering by Design | `c4s4` | rozdz. 4, sekcja 4 | 10 |
| 7. Measurement | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c7s5` | rozdz. 7, sekcja 5 | 10 |
| 7. Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s1-2` | rozdz. 3, sekcja 1-2 | 10 |
| 7. Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `p273` | s. 273 | 10 |
| 7.1. Levels (Scales) of Measurement | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `pp442-447` | s. 442-447 | 10 |
| 7.1. Levels (Scales) of Measurement | `[12*]` R.E. Fairley, Managing and Leading Software Projects. Hoboken, NJ: Wiley- IEEE Computer Socie… | `c7s5` | rozdz. 7, sekcja 5 | 10 |
| 7.1. Levels (Scales) of Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s2` | rozdz. 3, sekcja 2 | 10 |
| 7.1. Levels (Scales) of Measurement | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `p274` | s. 274 | 11 |
| 7.3. Direct and Derived Measures | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c7s5` | rozdz. 7, sekcja 5 | 13 |
| 7.4. Reliability and Validity | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s4-5` | rozdz. 3, sekcja 4-5 | 14 |
| 7.5. Assessing Reliability | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c3s5` | rozdz. 3, sekcja 5 | 14 |
| 8. Standards | `[3*]` G. Voland, Engineering by Design | `c9s3.2` | rozdz. 9, sekcja 3.2 | 15 |
| 8. Standards | `[14]` J.W. Moore, The Road Map to Software Engineering: A Standards-Based Guide | `p8` | s. 8 | 15 |
| 9. Root Cause Analysis | `[3*]` G. Voland, Engineering by Design | `c9s3-5` | rozdz. 9, sekcja 3-5 | 16 |
| 9. Root Cause Analysis | `[13*]` S.H. Kan, Metrics and Models in Software Quality Engineering | `c5`, `c3s7`, `c9s8` | rozdz. 5; rozdz. 3, sekcja 7; rozdz. 9, sekcja 8 | 16 |
| 9.1. Root Cause Analysis Techniques | `[2*]` S. Tockey, Return on Software: Maximizing the Return on Your Software Investment | `c4` | rozdz. 4 | 16 |
| 9.1. Root Cause Analysis Techniques | `[15]` K. Ishikawa, Introduction to Quality Control, Productivity Press, 1990 |  |  | 16 |
| 9.1. Root Cause Analysis Techniques | `[16]` D. Gano, Apollo Root Cause Analysis |  |  | 16 |
| 9.1. Root Cause Analysis Techniques | `[17]` E. Goldratt, It’s Not Luck, North River Press, 1994 |  |  | 17 |

### Dalsze lektury (`FURTHER READINGS`)

Pozycje polecane przez SWEBOK jako lektura uzupełniająca do całego obszaru (bez przypisania do konkretnego podrozdziału):

- `[18]` A. Abran, Software Metrics and Software Metrology : Wiley-IEEE Computer Society Press, 2010.
- `[19]` W.G. Vincenti, What Engineers Know and How They Know It. Johns Hopkins University Press, 1993.

