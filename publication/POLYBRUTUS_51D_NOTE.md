# Polybrutus 51D: Exact 56-point Euclidean metric and a forty-fivefold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible case study**
**AI disclosure:** OpenAI ChatGPT (Astra) materially assisted independent rational programs, mathematical checks, manuscript and publication; AI is not the scientific author.

## Abstract

We construct an exact synthetic Euclidean labelled squared-distance metric on 56 norm-one points through a conservative perpendicular unit-point extension of the immutable Polybrutus D50 data [1]. All 1485 predecessor labelled distances remain unchanged; 55 new squared distances each equal 2R², giving 1540 unordered labelled pairs. The centered Euclidean Gram is positive semidefinite with exact rank 51, establishing minimal affine dimension 51 for this particular metric. Separately, a stipulated ideal scalar-unit-mass weighted complete graph with w_ij=1/d_ij² has exact Laplacian eigenvalue 28 with multiplicity 45 and 55/2 with multiplicity 4. Two independent exact rational implementations exhaustively check every label, source provenance, centered rank, and model spectral nullities. The mode values are dimensionless and not experimentally measured frequencies.

## 1. Direct scientific predecessor and immutable data provenance

The one immediate predecessor is St-Pierre's Polybrutus D50 [1], DOI 10.5281/zenodo.24429826, Git tag Topbrutus/polybrutus-d50@v0.1.0 at peeled scientific commit e94150cdafe611ef3522fc77de76bf931a64b749. Its complete original frozen scientific source ZIP is embedded byte-identically as prior/d50/frozen_scientific_tag_v0.1.0.zip, 2785666 bytes, 31 entries, CRC PASS, SHA-256 0130c197acd8ef08a6a5b4a0d530c40deb9b2bf907f989f2d9cb19204491b1c4, including all previously nested immutable source ZIPs. Original D50 certificate prior/d50/results/certificate_d50.json is copied unchanged, SHA-256 e371670c9f5b5acc74780b8d61146b449cdbca234bf6cf0e55e2fb7230fc85d3. Both independent checkers authenticate source SHA, CRC and original parent certificate bytes.

Embed each old unit point p_i, i=1,...,55, by q_i=(p_i,0), and adjoin one new perpendicular unit point q_56. Every original labelled squared distance is preserved because zero embedding does not change pairwise distances. Every new squared distance is ||q_56-q_i||²=2R²; hence C(56,2)=1540=1485+55 exact unordered labelled pairs. This is a constructive synthetic Euclidean extension, not evidence for physical spacetime dimensions.

## 2. Gram construction, exact rank and exhaustive audit

An exact rational Gram G is the orthogonal sum of seven canonical unit points of rank 3, an independent regular centered five-unit-simplex of rank 4 (off-diagonal inner products -1/4), and 44 mutually orthogonal independent unit axes. G=XXᵀ is therefore positive semidefinite with diagonal one and exact rank 3+4+44=51. Put D_ij=2-2G_ij for i≠j with zero diagonal, and H=I-11ᵀ/56. Then B=-(HDH)/2=HGH is PSD with exact rank 51. The inherited canonical antipodal pair guarantees the origin is in the affine hull, giving minimum affine Euclidean realization dimension 51 (52 storage coordinates).

For unit radius the exhaustive normalized squared-distance histogram k=4d²/R² is 4:6, 7:2, 8:1509, 9:3, 10:10, 12:6, 13:2, 16:2 (1540 unordered pairs). The exact total squared-distance sum is 12367/4. Each of the 1485 predecessor pairs is compared by its labels with the original authenticated frozen D50 certificate, not simply matched by a histogram.

## 3. Separately selected ideal complete weighted graph

Take scalar unit masses at each unit point and stipulate symmetric dimensionless weights w_ij=1/d_ij². Each new edge joining the added unit point has weight 1/2. The Laplacian is the symmetric uniform join L51=[[L50+I55/2,-1_55/2],[-1_55ᵀ/2,55/2]]. The characteristic-polynomial recurrence is chi56(z)=z(z-28)chi55(z-1/2)/(z-1/2), with closed form chi56(z)=z(z-28)^45(z-55/2)^4*f6(z-49/2), f6(z)=chiP7(z)/z for the fixed seven-point factor. Exact rational Laplacian nullity computations confirm eigenvalue 28 multiplicity 45 and 55/2 multiplicity 4.

These ideal graph eigenmodes do not denote acoustic frequencies, particle properties, observed resonances or additional physical spacetime dimensions. Extra physical assumptions and experimental evidence would be required for such claims.

## 4. Independent verification, counterexamples and historical caveat

src/verify_d51.py constructs rational Gram G and all 1540 labelled squared-distance values with SymPy, audits the original ZIP and certificate SHA/CRC, checks rank of centered Gram and Laplacian exact eigenspaces. tests/independent_d51.py reconstructs all 1540 labelled distances using separately defined fractions.Fraction rules without importing the primary Gram constructor; it verifies 1485 original labels, centered Gram rank, and ideal Laplacian nullities. Both programs independently regenerate precisely the same deterministic results/certificate_d51.json and its SHA-256.

Four adversarial primary controls detect modified labelled pair, duplicate final vertex, a norm-one but nonperpendicular tilted point, and pair-label permutation that preserves the histogram but violates label conservation. The independent checker additionally tests a damaged label and a histogram-preserving relabelling.

An original old D47 certificate refers incorrectly to its own D46 parent Git commit in a textual metadata field; the discrepancy was disclosed in D48 and remains preserved inside nested historical archives. D51 authenticates only its immediate D50 scientific parent against actual frozen tag and original certificate; no ancestor files are silently rewritten.

## 5. Reproduction, metadata and scope

Exact code uses Python 3.12 and sympy==1.14.0. Orthogonal unit-point extension and weighted graph joins are established mathematical operations. This publication checks one freely specified exact Euclidean metric and one freely selected ideal graph; it does not claim an independently peer-reviewed novel theorem, experimental observations, new particles, physical extra dimensions or measured frequencies.

The Zenodo record must include current dimension keyword fifty-one, ideal eigenmode multiplicity forty-fivefold, structured isDerivedFrom to D50 DOI 10.5281/zenodo.24429826 and a separate bibliography citing D50 [1] and historical D7 [2]. All public metadata and three original artifacts must be verified via Zenodo API after publication.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 50D: Exact 55-Point Euclidean Metric and Forty-Fourfold Ideal Graph Mode. Zenodo. DOI: 10.5281/zenodo.24429826. https://doi.org/10.5281/zenodo.24429826

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo. DOI: 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Polybrutus D50 complete original frozen scientific tag v0.1.0. GitHub https://github.com/Topbrutus/polybrutus-d50/tree/v0.1.0; actual commit e94150cdafe611ef3522fc77de76bf931a64b749. Full ZIP embedded as original.
