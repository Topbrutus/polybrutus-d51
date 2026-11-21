# Polybrutus 51D - exact 56-point Euclidean metric and forty-fivefold ideal graph mode

**Human scientific author:** Gabriel St-Pierre, independent researcher.
**AI assistance:** OpenAI ChatGPT (Astra) materially assisted mathematical checks, two independent programs, manuscript and release; AI is not a scientific author.

## Official public Polybrutus D51 DOI and verification

- **DOI:** [10.5281/zenodo.24430047](https://doi.org/10.5281/zenodo.24430047), [public Zenodo record](https://zenodo.org/records/24430047).
- **Immutable scientific source tag:** [v0.1.0](https://github.com/Topbrutus/polybrutus-d51/tree/v0.1.0) at peeled scientific commit \`d523aada12f90486482fee9f7406be364ea38b36\`.
- **Main scientific GitHub CI:** https://github.com/Topbrutus/polybrutus-d51/actions/runs/44959395398 — success on the source-equivalent earlier main commit (prior to adding VALIDATION.md).
- **Scientific frozen tag CI:** https://github.com/Topbrutus/polybrutus-d51/actions/runs/44959443447 — success on the exact scientific tag commit.
- **Zenodo original artifacts:** source ZIP, scientific manuscript PDF, deterministic exact JSON certificate; all names, MD5 and byte sizes verified via Zenodo public API against original local SHA256.
- **Current bibliography:** nine fifty-one / forty-fivefold keywords, structured isDerivedFrom DOI D50 10.5281/zenodo.24429826, separate textual references D50 and historical D7 10.5281/zenodo.24407952.
- **Durable Memoria checkpoint:** https://github.com/Topbrutus/topbrutus_one/blob/main/memoria/checkpoints/POLYBRUTUS_D51_PUBLICATION_2026-11-21.md .

## Reproducible exact rational mathematical construction

- **56** norm-one vertices; **1540 / 1540** exact unordered labelled squared-distance pairs.
- All **1485 / 1485** frozen Polybrutus D50 predecessor labelled distances preserved, **55** new squared distances precisely **2R²**.
- Gram G and centered Gram B are PSD and of exact rank **51**, proving minimal affine Euclidean dimension 51 for this one synthetic metric, represented in 52 storage coordinates.
- Exact unit-radius histogram \`k=4d²/R²\`: 4:6, 7:2, 8:1509, 9:3, 10:10, 12:6, 13:2, 16:2. Exact sum of squared distances at R=1: **12367/4**.
- A separate stipulated ideal scalar-unit-mass graph with weights \`w_ij=1/d_ij²\` has Laplacian eigenvalue **28 (multiplicity 45)** and **55/2 (multiplicity 4)**. No measured hertz follows.
- Two independent programs and four adversarial negative controls, with preserved source ancestry and deterministic exact certificate.

Run:

    python -m pip install sympy==1.14.0
    python src/verify_d51.py
    python tests/independent_d51.py
    python src/check_zenodo_metadata.py

CI repeats both checkers and verifies deterministic certificate and bibliography.

## Original immutable source parent and bibliography

Direct scientific parent is [Polybrutus D50 v0.1.0](https://github.com/Topbrutus/polybrutus-d50/tree/v0.1.0), commit \`e94150cdafe611ef3522fc77de76bf931a64b749\`, DOI [10.5281/zenodo.24429826](https://doi.org/10.5281/zenodo.24429826). The full authentic original parent ZIP (including nested older source archives) SHA-256 \`0130c197acd8ef08a6a5b4a0d530c40deb9b2bf907f989f2d9cb19204491b1c4\`, and its original certificate SHA-256 \`e371670c9f5b5acc74780b8d61146b449cdbca234bf6cf0e55e2fb7230fc85d3\`, are embedded *unchanged* in \`prior/d50\` and authenticated in both programs.

Zenodo current-dimension keywords must include \`fifty-one\` and \`forty-fivefold\`, structured \`isDerivedFrom\` to D50 DOI, and a separate two-reference bibliography D50 and historical D7 DOI 10.5281/zenodo.24407952.

[Specification](SPECIFICATION_D51.md) | [proof](PREUVE_D51.md) | [provenance](PROVENANCE.md) | [references](REFERENCES.md) | [scientific PDF](publication/POLYBRUTUS_51D_NOTE.pdf).

**Scientific limits:** Only a synthetic exact Euclidean labelled metric and a separately selected dimensionless ideal weighted complete graph are demonstrated. There is no experimental measurement, evidence for physical extra dimensions, particles, novel universal theorem, or independent human peer review.
**Licenses:** MIT source code, CC BY 4.0 manuscript.
